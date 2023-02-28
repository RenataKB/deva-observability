import http.client
import random
import time
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
import prometheus_client as prom
import logging

# configure the logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


app = Flask(__name__)
metrics = PrometheusMetrics(app)
quantidade_usuarios_online = prom.Gauge("quantidade_usuarios_online", "Número de usuarios online no momento")


def parametros_endpoint():
    time.sleep(random.randint(1,10))
    quantidade_usuarios_online.set(random.randint(1,100))


@app.route('/renda-fixa')
# @metrics.counter('efetivacao_renda_fixa', 'Numero de papeis de renda fixa efetivados', labels={'tipo': 'RENDA FIXA'})
def renda_fixa():
    app.logger.info("Acessando Renda Fixa!")
    parametros_endpoint()
    if random.randint(0, 1):
        return http.client.BAD_REQUEST
    return render_template('lista.html', titulo="Renda Fixa")


@app.route('/renda-variavel')
def renda_variavel():
    parametros_endpoint()
    return render_template('lista.html', titulo="Renda Variável")


@app.route('/fii')
def fii():
    parametros_endpoint()
    return render_template('lista.html', titulo="Fundo de Investimento Imobiliário")


@app.route('/cripto')
def cripto():
    parametros_endpoint()
    return render_template('lista.html', titulo="Cripto")


if __name__ == "__main__":
    app.run(host="0.0.0.0") #, port=5001 #se quiser mudar a porta