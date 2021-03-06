import paho.mqtt.client as mqtt
import json

ACCESS_TOKEN = ""
MQTT_BROKER = "mqtt-server01.local"
MQTT_PORT = 1883

client = None


def mqtt_setup():
    global client
    client = mqtt.Client()
    if ACCESS_TOKEN:
        client.username_pw_set(ACCESS_TOKEN)

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    return client


def publish_sensor_data(path, sensor_data):
    global client
    client.publish(path, json.dumps(sensor_data), qos=1)

