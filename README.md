diysystem
=========

Do It Yourself Raspberry Pi server status monitoring class

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

Compatibility
-------------

Licence
-------

MIT

Authors
-------

`diysystem` was written by `Dave Wilson <parttimehacker@gmail.com>`_.
