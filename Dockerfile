FROM python:3

ADD . /forum

WORKDIR /forum

RUN pip install -r requirements.txt

COPY forum.py .

CMD ["python", "./forum.py"]