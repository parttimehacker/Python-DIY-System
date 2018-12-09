diysystem
=========

Do It Yourself Raspberry Pi server status monitoring class. 

Usage
-----

import DiyhasSystem
...

SYSTEM = DiyhasSystem.DiyhasSystem(CLIENT, HOSTNAME, INTERVAL)

# CLIENT is the MQTT client
# HOSTNAME is the Raspberry Pi host name
# INTERVAL is the time interval to collect and publish status in seconds

Installation
------------

       git clone https://github.com/parttimehacker/Python-DIY-System.git
       python setup.py install

Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`diysystem` was written by `Dave Wilson <parttimehacker@gmail.com>`_.
