FROM python:3.12

WORKDIR /app

COPY requirements.txt /

COPY config.yaml /

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY src /app/src/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]