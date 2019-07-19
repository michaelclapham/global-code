import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    while True:
        message = input('Your message: ')
        client.publish('glblcd/sam', message)

client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 4000, 60)
client.loop_forever()
