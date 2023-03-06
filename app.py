import http.client
import random
import time
from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
import prometheus_client as prom
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


app = Flask(__name__)
metrics = PrometheusMetrics(app)
quantidade_usuarios_online = prom.Gauge(
    "quantidade_usuarios_online", "Número de usuarios online no momento"
)


def parametros_endpoint():
    time.sleep(random.randint(1, 10))
    quantidade_usuarios_online.set(random.randint(1, 100))


# Deixei apenas no renda-fixa e no cripto, para nao gerar tanto erro
def pagina_ou_erro(nome_pag):
    app.logger.info(f"Acessando {nome_pag}!")
    if random.choice([True, False]):
        app.logger.error(
            "%s %s %s %s",
            request.remote_addr,
            request.method,
            request.scheme,
            request.full_path,
        )
        http.client.BAD_REQUEST
        return render_template("mensagem_erro.html"), 500
    app.logger.info(
        "%s %s %s %s",
        request.remote_addr,
        request.method,
        request.scheme,
        request.full_path,
    )
    return render_template("lista.html", titulo=nome_pag)


@app.route("/")
def index():
    app.logger.info(
        "%s %s %s %s",
        request.remote_addr,
        request.method,
        request.scheme,
        request.full_path,
    )
    return render_template("index.html")


@app.route("/renda-fixa")
def renda_fixa():
    parametros_endpoint()
    return pagina_ou_erro("Renda Fixa")


@app.route("/renda-variavel")
def renda_variavel():
    parametros_endpoint()
    app.logger.info(
        "%s %s %s %s",
        request.remote_addr,
        request.method,
        request.scheme,
        request.full_path,
    )
    return render_template("lista.html", titulo="Renda Variável")


@app.route("/fii")
def fii():
    parametros_endpoint()
    app.logger.info(
        "%s %s %s %s",
        request.remote_addr,
        request.method,
        request.scheme,
        request.full_path,
    )
    return render_template("lista.html", titulo="Fundo de Investimento Imobiliário")


@app.route("/cripto")
def cripto():
    parametros_endpoint()
    return pagina_ou_erro("Cripto")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
