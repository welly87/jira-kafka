import flask
from flask import request
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': '35.197.152.28:9092'})

app = flask.Flask(__name__)

@app.route('/jira-events', methods=['POST'])
def home():
    # print(request.headers)
    p.produce('jira-events', request.get_json().encode('utf-8'))
    p.flush()


@app.route('/jira', methods=['GET'])
def check():
    return "JIRA"

app.run(host='0.0.0.0')
