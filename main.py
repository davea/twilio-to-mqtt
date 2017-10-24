#!/usr/bin/env python3

from flask import Flask, request
import paho.mqtt.publish as publish
from os import environ

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def publish_to_mqtt():
    message = request.values.get('Body', None)
    if not message:
        return "No message found"
    topic = environ.get('MQTT_TOPIC')
    broker = environ.get('MQTT_BROKER')
    if not topic or not broker:
        return "Invalid MQTT configuration"
    publish.multiple([{'topic': topic, 'payload': message}], hostname=broker)
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
