FROM python:3.10-alpine
COPY requirements.txt /requirements.txt
RUN python -m venv /opt/venv
RUN pip install --upgrade pip
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -r /requirements.txt
COPY dataUpdater.py /app/main.py
COPY db.py /app/db.py
COPY DBtables/ /app/DBtables
COPY .env.server /app/.env
WORKDIR /app
CMD python3 main.py