from python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["urvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]