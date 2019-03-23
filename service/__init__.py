from flask import Blueprint

bp = Blueprint('service', __name__)

from cssa.service import routes, infoRequest