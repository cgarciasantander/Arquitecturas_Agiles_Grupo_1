from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Consumo(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    pacienteId = db.Column(db.String(128))
    monto = db.Column(db.Float)
    realizadoEl = db.Column(db.Date)

class ConsumoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Consumo
        load_instance=True