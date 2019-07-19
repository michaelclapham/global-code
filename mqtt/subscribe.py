import paho.mqtt.subscribe as subscribe

topics = ['#']

m = subscribe.simple(topics, hostname="localhost",port=4000, retained=False, msg_count=2)
for a in m:
    print(a.topic)
    print(a.payload)
