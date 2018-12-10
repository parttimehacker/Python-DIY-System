diysystem
=========

A class to collect four Raspberry PI server metrics and the publish to a MQTT messager broker. The class collects CPU, memory, and disk utilization. It also computes server up time since last reboot. It was developed as part of my Do It Yourself Home Automation System.

Usage
-----
        
        import diysystem
        
        SYSTEM = diysystem.DiySystem(CLIENT, HOST_NAME, INTERVAL_SECONDS)
        
- CLIENT is an MQTT client
- HOST_NAME is the server host name string
- INTERVAL_SECONDS is the frame rate of the metrics collection and publish cycle

Installation
------------

        git clone https://github.com/parttimehacker/Python-DIY-System.git
        cd Python-DIY-System
        python setup.py install

Requirements

       import datetime
       import time
       from threading import Thread
       import logging
       import psutil

Licence
-------

MIT

Authors
-------

`diysystem` was written by `Dave Wilson <parttimehacker@gmail.com>`_.
