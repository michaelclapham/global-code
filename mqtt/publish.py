import paho.mqtt.publish as publish

publish.single("ucc/michael", "bzzzz, I like mosquitto", hostname="broker.hivemq.com", port=1883)
