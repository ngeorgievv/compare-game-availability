FROM python:3.9

WORKDIR /app

RUN pip install flask

RUN pip install werkzeug

COPY . .

EXPOSE 8002

CMD ["python", "compare_ttl.py"]