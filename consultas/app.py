from consultas import create_app
from flask_restful import Api, Resource
from .modelos import db, Consumo, ConsumoSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

consumo_schema = ConsumoSchema()

class VistaReporte(Resource):

    def get(self, fechaInicio, fechaFin):

        consumos = Consumo.query.filter(
            Consumo.realizadoEl >= fechaInicio).filter(Consumo.realizadoEl <= fechaFin)
        ingresos = 0.0
        impuestos = 0.0
        for actual in consumos:
            ingresos += actual.monto
        impuestos = ingresos*0.15
        gananciaNeta = ingresos - impuestos
        reporte = {"fechaInicio":fechaInicio, "fechaFin":fechaFin,"ingresos":ingresos,"impuestos":impuestos,"gananciaNeta":gananciaNeta}
        return reporte
    
api = Api(app)
api.add_resource(VistaReporte, '/reporte')
