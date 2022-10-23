from app import app
from app import utils
from flask import request, jsonify
import _pickle as cPickle
from google.cloud import storage
from xgboost import XGBClassifier


@app.post('/')
def predecir():
    dataset = request.get_json()
    ubicaciones_recursos = utils.ubicaciones_recursos

    storage_client = storage.Client.from_service_account_json("credentials.json")
    bucket = storage_client.bucket('bbva-hackaton-bigminds')
    model_blob = bucket.blob(ubicaciones_recursos["alg_rep"])

    try:
        dataset = utils.json_to_dataframe(dataset["users"])
    except:
        return jsonify (codigo  = '30',
                        mensaje = 'Error al convertir a dataframe'), 404

    try:
        dataset_preprocesado = utils.preprocesar(dataset, ubicaciones_recursos)
    except OSError as e:
        return jsonify (codigo  = '30',
                        mensaje = f'Error al abrir recurso: {e}'), 404
    
    with model_blob.open("rb") as model_file:
        model = cPickle.load(model_file)

    y = model.predict(dataset_preprocesado)

    return jsonify(output = len(y))