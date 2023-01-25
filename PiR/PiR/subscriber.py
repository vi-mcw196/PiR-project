import paho.mqtt.client as mqtt
from datetime import datetime

BROKER_HOST = "io.adafruit.com"
PORT = 1883
SUBSCRIBE_TOPIC = "JavaPG/feeds/rpi-rfid"
PUBLISHER_TOPIC = "JavaPG/feeds/rpi-led"
ADAFRUIT_USER = "JavaPG"
ADAFRUIT_KEY = "aio_FqvQ51I2XkJCChPfNRnCY3IqE9SV"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print("Connected OK")
        client.subscribe(SUBSCRIBE_TOPIC, qos=0)

    else:
        print("Bad connection Returned code=", rc)


def on_message(client, userdata, msg):
    now = datetime.now().time()
    payload = msg.payload.decode("utf-8")
    list_dostepnosci = ['25118719434160']
    if payload != 'bad':
        if payload in list_dostepnosci:
            client.publish(PUBLISHER_TOPIC, "good", 0, True)
        else:
            client.publish(PUBLISHER_TOPIC, "bad", 0, True)
    print("Msg received {}, topic: {} value: {}".format(now, msg.topic, payload))


mqtt.Client.connected_flag = False

client = mqtt.Client("SubscriberTEST")
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to broker ", BROKER_HOST)
client.username_pw_set(ADAFRUIT_USER, password=ADAFRUIT_KEY)
client.connect(BROKER_HOST, port=PORT, keepalive=60)

client.loop_forever()
