from flask import Flask
from flasgger import Swagger

from api.routes import init_routes

app = Flask(__name__)
Swagger(app)
init_routes(app)

app.run()
