from flask import Blueprint
pypivot = Blueprint('pypivot', '__name__')
from . import routes