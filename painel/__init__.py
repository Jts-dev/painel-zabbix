
from flask import Flask , jsonify
from flask_cors import CORS
from api_zabbix import login_no_zabbix , pesquisa_item_por_key_texto

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/item_por_key', methods=["GET"])

def item_por_key(): 


    zapi=login_no_zabbix()


    pesquisa_item_por_key_texto(zapi  )

    return jsonify( pesquisa_item_por_key_texto(zapi  ))
