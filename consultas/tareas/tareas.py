from ..app import db
from ..modelos import Consumo, ConsumoSchema
from celery import Celery
from celery.signals import task_postrun
from datetime import datetime
import os

redis_host = os.environ.get('REDIS_HOST')
celery_app = Celery('tasks', broker = redis_host)

consumo_schema = ConsumoSchema()

@celery_app.task(name='tabla.registrar')
def registrar_consumo(consumo_json):
    print(consumo_json)
    consumo = Consumo(
        pacienteId=consumo_json['pacienteId'],
        monto=consumo_json['monto'],
        realizadoEl=datetime.fromisoformat(consumo_json['realizadoEl'])
        )
    db.session.add(consumo)
    db.session.commit()

@task_postrun.connect()
def close_session(*args, **kwargs):
    db.session.remove()
