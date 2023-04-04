from flask_restful import Api
from flaskAPI import flaskAppInstance
from .Task import Task

restServer = Api(flaskAppInstance)
restServer.add_resource(Task, "/api/v1.0/task")
