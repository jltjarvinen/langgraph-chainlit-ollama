FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY .chainlit/config.toml /app/.chainlit/config.toml
COPY .chainlit/public /app/public

CMD ["chainlit", "run", "main.py", "--host", "0.0.0.0", "--port", "8000", "--headless"]

