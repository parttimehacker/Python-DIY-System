''' Test Bed for Diyhas System Status class '''

import time
import socket

import paho.mqtt.client as mqtt

import diysystem

HOSTNAME = socket.gethostname()

def on_connect(mq_client, userdata, flags, rc_code):
    """ Subscribing in on_connect() means that if we lose the connection and
        reconnect then subscriptions will be renewed.
    """
    print "Connected to MQTT Server!"
    print "client:   "+str(mq_client)
    print "userdata: "+str(userdata)
    print "flags:    "+str(flags)
    print "rc:       "+str(rc_code)

def on_message(mq_client, userdata, msg):
    """ dispatch to the appropriate MQTT topic handler
    """
    print "On Message from Publish"
    print "client:   "+str(mq_client)
    print "userdata: "+str(userdata)
    print "topic:    "+msg.topic+" payload: "+msg.payload

if __name__ == '__main__':
    CLIENT = mqtt.Client()
    CLIENT.on_connect = on_connect
    CLIENT.on_message = on_message
    CLIENT.connect("192.168.1.133", 1883, 60)
    CLIENT.loop_start()

    SYSTEM = diysystem.DiySystem(CLIENT, HOSTNAME, 10)

    print "ready"

    while True:
        try:
            time.sleep(10.0)
            print "running"
        except KeyboardInterrupt:
            # here you put any code you want to run before the program
            # exits when you press CTRL+C
            print "User exit with control-c"
            print "Shutting down"
            SYSTEM.shutdown()
            time.sleep(1)
            exit()

