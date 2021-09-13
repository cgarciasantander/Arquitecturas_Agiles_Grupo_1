from consultas.modelos.modelos import ConsumoSchema
from comandos import create_app
from .modelos import db, Consumo
from flask_restful import Resource, Api
from datetime import datetime
from flask import Flask, request
import json
from celery import Celery
import os

redis_host = os.environ.get('REDIS_HOST')
celery_app = Celery('tasks', broker = redis_host)

app = create_app('default')
app_context = app.app_context()
app_context.push()
api = Api(app)

db.init_app(app)
db.create_all()

@celery_app.task(name='tabla.registrar')
def registrar_consumo(consumo_json):
    print(consumo_json)
    pass

consumo_schema = ConsumoSchema()

class VistaConsumo(Resource):

    def post(self):
       nuevo_consumo = Consumo(
           pacienteId=request.json['pacienteId'], 
           monto=request.json['monto'], 
           realizadoEl=datetime.fromisoformat(request.json['realizadoEl'])
        )
       id_consumo = nuevo_consumo.id
       db.session.add(nuevo_consumo)
       db.session.commit()
       consumo= consumo_schema.dump(nuevo_consumo)
       args = (consumo,)
       registrar_consumo.apply_async(args)
       return json.dumps(consumo)

api.add_resource(VistaConsumo, '/consumos')