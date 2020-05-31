FROM python:3-slim

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD app/ .

EXPOSE 5000

CMD [ "python", "./server.py" ]