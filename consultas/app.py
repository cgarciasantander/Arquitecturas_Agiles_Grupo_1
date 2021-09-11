from consultas import create_app
from flask_restful import Api, Resource
from .modelos import db, Consumo

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

consumo= Consumo()

class VistaReporte(Resource):

    def get(self, fechaInicio, fechaFin):
        consumos = consumo.query.filter_by()
        #Falta hallar los consumos que esten dentro de las fechas y calcular los ingresos, impuestos y ganancia.
        # Retornar el json con el reporte
    
api = Api(app)
api. add_resource(VistaReporte, '/reporte')