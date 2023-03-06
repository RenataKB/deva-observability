# Observabilidade

Projeto final para o módulo de Observabilidade do programa Deva.

Os arquivos são para a criação de um aplicativo em Python / Flask e um cliente para simular acessos, gerando métricas e logs.
Foco em criar dashboards com as principais ferramentas de Observabilidade.

## Instruções

Crie as imagens que serão utilizadas para o app e para o client.

```
docker image build -t ada-deva-observabitity -f Dockerfile .
```

```
docker image build -t ada-app-client -f Dockerfile-client .
```

Suba o docker compose
```
docker compose up -d
```

## Imagens

Gráficos criado no Grafana:
![Grafana 1](/screenshots/screenshot-1.jpg)
![Grafana 2](/screenshots/screenshot-2.jpg)
![Grafana 3](/screenshots/screenshot-3.jpg)
![Grafana 4](/screenshots/screenshot-4.jpg)
![Grafana 5](/screenshots/screenshot-5.jpg)

Dados do Graylog:
![Graylog 1](/screenshots/screenshot-6.jpg)
![Graylog 2](/screenshots/screenshot-7.jpg)