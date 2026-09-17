FROM python:3.12-slim

WORKDIR /myapp

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY project ./project

EXPOSE 8000

CMD ["uvicorn", "project.main:app", "--host", "0.0.0.0", "--port", "8000"]