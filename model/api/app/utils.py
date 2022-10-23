from app import app
from types import DynamicClassAttribute
from functools import wraps
from flask import request, jsonify
import numpy as np
import jwt
import _pickle as cPickle
import pandas as pd
import json
from google.cloud import storage


ubicaciones_recursos = {
  "alg_rep": "alg_rep.pkl",
  "nor_num": "nor_num.pkl",
  "cod_cat": "cod_cat.pkl",
  "imp_num": "imp_num.json",
  "imp_cat": "imp_cat.json",
  "ftr_nor": "ftr_nor.pkl",
  "ftr_cod": "ftr_cod.pkl"
}


def imputar(dataset, recurso):
    for columna in dataset.columns.tolist():
        valor_imp = recurso[columna]
        dataset[columna].replace(np.nan, valor_imp, inplace = True)

    return dataset



def codificar(dataset_cat, encoder, features):
    dataset_cat = dataset_cat.reindex(columns=features)
    d = encoder.transform(dataset_cat)
    dataset_cat_cod = pd.DataFrame(d.toarray(), columns=encoder.get_feature_names_out())

    return dataset_cat_cod



def normalizar(dataset_num, scaler, features):
    dataset_num = dataset_num.reindex(columns=features)
    d = scaler.transform(dataset_num)
    dataset_num_nor = pd.DataFrame(d, columns=dataset_num.columns)

    return dataset_num_nor


def json_to_dataframe(dataset_json):
    dataset = pd.DataFrame.from_dict(dataset_json)

    return dataset


def cargar_recursos(ubicaciones_recursos):
    storage_client = storage.Client.from_service_account_json("credentials.json")
    bucket = storage_client.bucket('bbva-hackaton-bigminds')
    
    scaler_blob = bucket.blob(ubicaciones_recursos["nor_num"])
    encoder_blob = bucket.blob(ubicaciones_recursos["cod_cat"])
    imputer_num_blob = bucket.blob(ubicaciones_recursos["imp_num"])
    imputer_cat_blob = bucket.blob(ubicaciones_recursos["imp_cat"])
    features_nor_blob = bucket.blob(ubicaciones_recursos["ftr_nor"])
    features_cod_blob = bucket.blob(ubicaciones_recursos["ftr_cod"])

    try:
        with scaler_blob.open("rb") as scaler_file:
            scaler = cPickle.load(scaler_file)
        with encoder_blob.open("rb") as encoder_file:
            encoder = cPickle.load(encoder_file)
        with imputer_num_blob.open("rb") as imputer_num_file:
            imputer_num = json.load(imputer_num_file)
        with imputer_cat_blob.open("rb") as imputer_cat_file:
            imputer_cat = json.load(imputer_cat_file)
        with features_nor_blob.open("rb") as features_nor_file:
            features_nor = cPickle.load(features_nor_file)
        with features_cod_blob.open("rb") as features_cod_file:
            features_cod = cPickle.load(features_cod_file)
    except OSError:
        raise

    return scaler, encoder, imputer_num, imputer_cat, features_nor, features_cod



def preprocesar(dataset, ubicaciones_recursos):
    try:
        scaler, encoder, imputer_num, imputer_cat, features_nor, features_cod = cargar_recursos(ubicaciones_recursos)
    except OSError:
        raise
    
    dataset_num = dataset[features_nor]
    dataset_cat = dataset[features_cod]

    dataset_num_imp = imputar(dataset_num, imputer_num)
    dataset_cat_imp = imputar(dataset_cat, imputer_cat)

    dataset_num_nor = normalizar(dataset_num_imp, scaler, features_nor)
    dataset_cat_cod = codificar(dataset_cat_imp, encoder, features_cod)

    dataset_preprocesado = pd.concat([dataset_num_nor, dataset_cat_cod], axis = 1)

    return dataset_preprocesado