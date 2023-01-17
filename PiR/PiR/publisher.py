import paho.mqtt.client as mqtt  # importing mqtt library
import time
import psutil

BROKER_HOST = "io.adafruit.com"  # variable for mqtt broker address
PORT = 1883  # mqtt broker port
TOPIC = "JavaPG/feeds/rpi-cpu"  # topic to publish cpu
ADAFRUIT_USER = "JavaPG"
ADAFRUIT_KEY = "aio_ZpSW58DN5RUr8yHYjxyHYDij1mAI"


def on_connect(client, userdata, flags, rc):  # function called on connected
    if rc == 0:
        client.connected_flag = True  # set flag
        print("Connected OK")
    else:
        print("Bad connection Returned code=", rc)


mqtt.Client.connected_flag = False

client = mqtt.Client("Publisher1")  # creating client object
client.on_connect = on_connect  # defining function o handler on connected

print("Connecting to broker ", BROKER_HOST)
client.username_pw_set(ADAFRUIT_USER, password=ADAFRUIT_KEY)
client.connect(BROKER_HOST, port=PORT)  # starting connection
client.loop_start()  # starting mqtt client internal loop

while not client.connected_flag:  # wait until connected to broker
    print("Waiting for connection")
    time.sleep(1)

try:
    while True:  # main reading loop
        cpu = psutil.cpu_percent()
        print("CPU", cpu)
        client.publish(TOPIC, cpu, 0, True)  # publish current cpu load
        time.sleep(5)
except KeyboardInterrupt:
    print('Stoping CPU publisher')

client.loop_stop()  # stop internal mqtt loop
client.disconnect()  # disconnect broker
