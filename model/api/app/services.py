from app import app
from app import utils
from flask import request, jsonify
import _pickle as cPickle
from google.cloud import storage
import pandas as pd


@app.get('/')
def index():
  return "Running..."

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

    df_preds = dataset[["FULLNAME", "PHONE_NUMBER"]].copy()
    
    y = model.predict(dataset_preprocesado)
    y_probs = model.predict_proba(dataset_preprocesado)

    df_preds = pd.concat([df_preds, pd.DataFrame(y, columns=["PREDICTIONS"]), pd.DataFrame(y_probs[:,:-1], columns=["PROBABILITY"])], axis = 1)
    json_preds = df_preds.to_dict('records')

    response = jsonify(output = json_preds)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response