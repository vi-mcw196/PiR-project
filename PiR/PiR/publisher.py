import paho.mqtt.client as mqtt  # importing mqtt library
import time
import psutil

BROKER_HOST = "io.adafruit.com"
PORT = 1883
TOPIC = "JavaPG/feeds/rpi-rfid"
ADAFRUIT_USER = "JavaPG"
ADAFRUIT_KEY = "aio_FqvQ51I2XkJCChPfNRnCY3IqE9SV"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("Connected OK")
    else:
        print("Bad connection Returned code=", rc)


mqtt.Client.connected_flag = False

client = mqtt.Client("Publisher1")
client.on_connect = on_connect

print("Connecting to broker ", BROKER_HOST)
client.username_pw_set(ADAFRUIT_USER, password=ADAFRUIT_KEY)
client.connect(BROKER_HOST, port=PORT)
client.loop_start()

while not client.connected_flag:
    print("Waiting for connection")
    time.sleep(1)

try:
    while True:
        cpu = psutil.cpu_percent()
        print("CPU", cpu)
        client.publish(TOPIC, cpu, 0, True)
        time.sleep(5)
except KeyboardInterrupt:
    print('Stoping CPU publisher')

client.loop_stop()
client.disconnect()
