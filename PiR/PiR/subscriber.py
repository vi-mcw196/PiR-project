import paho.mqtt.client as mqtt  # importing mqtt library
from datetime import datetime

BROKER_HOST = "io.adafruit.com"  # variable for mqtt broker address
PORT = 1883  # mqtt broker port
TOPIC = "JavaPG/feeds/rpi-cpu"  # topic to publish cpu
ADAFRUIT_USER = "JavaPG"
ADAFRUIT_KEY = "aio_bBTw41wA1QduVSprc7nDrLQALlZj"


def on_connect(client, userdata, flags, rc):  # function called on connected
    if rc == 0:
        client.connected_flag = True  # set flag
        print("Connected OK")
        client.subscribe(TOPIC, qos=0)

    else:
        print("Bad connection Returned code=", rc)


# The callback for when a message is received from the server.
def on_message(client, userdata, msg):
    now = datetime.now().time()
    payload = msg.payload.decode("utf-8")
    print("Msg received {}, topic: {} value: {}".format(now, msg.topic, payload))


mqtt.Client.connected_flag = False

client = mqtt.Client("Subscriber1")  # creating client object
client.on_connect = on_connect  # defining function o handler on connected
client.on_message = on_message

print("Connecting to broker ", BROKER_HOST)
client.username_pw_set(ADAFRUIT_USER, password=ADAFRUIT_KEY)
client.connect(BROKER_HOST, port=PORT, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()
