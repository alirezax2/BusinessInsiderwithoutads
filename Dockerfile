FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

EXPOSE 8080

# CMD ["panel", "serve", "/app/main.py", "--address", "0.0.0.0", "--port", "8080", "--allow-websocket-origin", "sophiamyang-panel-example.hf.space"]
CMD ["panel", "serve", "/app/main.py", "--port", "8080"]
