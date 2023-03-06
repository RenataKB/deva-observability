FROM python:3.10.5-slim-buster
COPY requirements.txt /requirements.txt
COPY templates /templates
COPY static /static
COPY app.py /app.py
RUN pip3 install -r requirements.txt
CMD ["python", "app.py"]