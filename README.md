# Experimento de CQRS y cola de mensajes para el enmascaramiento de errores
## Proposito
Se busca demostrar el enmascaramiento de errores de los microservicios de finanzas aplicando tacticas de CQRS durante la elaboración de un reporte de finanzas.

## Resultados obtenidos
Se evidenció que todos los mensajes enviados por el servicio de comandos durante el tiempo que el de consultas estuvo caído fueron leídos correctamente una vez se integro el servicio de nuevo, replicando toda la información correctamente.

# Como correr el proyecto
## Prerequisitos
- Docker
- Python >= 3.8
- Make

## Correr la infrastructura con docker
En la carpeta base correr `make start`, este levantará los siguientes servicios:
- Finanzas consultas - Rest
- Finanzas comandos - Rest
- Redis
- Locust

## Detener la infrastructura con docker
En la carpeta base correr `make stop`, se detendran y removeran los contenedores

## Finanzas comandos REST
### POST /consumos
#### Body
```
{
    "pacienteId": 1,
    "monto": 5000,
    "realizadoEl": "2021-09-13"
}
```

### Response 200
```
"{\"pacienteId\": \"1\", \"realizadoEl\": \"2021-09-13\", \"id\": 4, \"monto\": 5000.0}"
```

## Finanzas consultas REST
### POST /reporte
#### Params
```
/reporte?fechaInicio=2021-09-01&fechaFin=2021-09-30
```

### Response 200
```
{
    "fechaInicio": "2021-09-01",
    "fechaFin": "2021-09-30",
    "ingresos": 8736.82,
    "impuestos": 1310.52,
    "gananciaNeta": 7426.29
}
```

