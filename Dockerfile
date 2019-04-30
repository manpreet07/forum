FROM python:3

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app

RUN pip install -r requirements.txt

COPY . /opt/app

ADD forum.py /

CMD [ "python", "./forum.py" ]