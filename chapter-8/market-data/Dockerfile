FROM python:3.6
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["gunicorn", "-c", "config.py", "app:app", "--bind", "0.0.0.0:8080"]
EXPOSE 8000
