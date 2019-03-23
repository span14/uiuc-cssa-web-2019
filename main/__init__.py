from flask import Blueprint

bp = Blueprint('main', __name__)

from cssa.main import routes