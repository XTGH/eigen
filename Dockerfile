FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN [ "python", "-c", "import nltk; nltk.download('popular')" ]
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
