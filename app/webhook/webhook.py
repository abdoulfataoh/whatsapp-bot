# coding: utf-8

from crypt import methods
from typing import Dict
from flask import Flask
from flask import request

from app import tasks


app = Flask(__name__)

@app.route('/health/', methods=['GET', 'POST'])
def health() -> Dict[str, str]:
    result = tasks.health()
    return result


@app.route('/webhook/', methods=['POST'])
def webhook() -> None:
    body = request.json
    print(body)
