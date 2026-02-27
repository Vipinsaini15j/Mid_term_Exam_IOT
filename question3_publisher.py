# Name: Vipin Saini
# Subject: Internet of Things
# roll No : 24IMAI007
#question 3:

# subscriber ( MQTT client)

import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "security/face_alert"

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Received Alert: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

print("Monitoring System Started...")
client.loop_forever()