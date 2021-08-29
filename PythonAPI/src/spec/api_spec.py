from src.spec.messages import *

health = {200: {"model": None, "description": health_success},
          400: {"model": None, "description": error_400},
          500: {"model": None, "description": error_500}
          }

server_transmission = {202: {"model": None, "description": server_transmission_success},
                         400: {"model": None, "description": error_400},
                         422: {"model": None, "description": "Possíveis erros de atributos"},
                         500: {"model": None, "description": error_500}}