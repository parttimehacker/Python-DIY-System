'''
    Diyhas System Status class
'''

import datetime
import time
from threading import Thread
import logging

import psutil

class DiySystem(object,):
    ''' Check and publish process status information '''

    def __init__(self, client, host, interval):
        ''' server system status monitor thread with MQTT reporting
        '''
        self.client = client
        self.host = host
        self.interval = interval
        self.boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        self.running_since = self.boot_time.strftime("%d. %B %Y")
        self.logger = logging.getLogger()
        handler = logging.FileHandler('%s.log' % host, 'w')
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
        self.thread = Thread(target=self.system_status_thread)
        self.thread.start()

    def get_cpu(self,):
        ''' publish cpu use as a percentage
        '''
        topic = "diyhas/"+self.host+"/cpu"
        value = psutil.cpu_percent(interval=1)
        info = "{0:.1f}".format(value)
        self.logger.debug("cpu; "+str(info))
        self.client.publish(topic, str(info), 0, True)

    def get_memory(self,):
        ''' publish memory use as a percentage
        '''
        topic = "diyhas/"+self.host+"/memory"
        value = psutil.virtual_memory()[2]
        info = "{0:.1f}".format(value)
        self.logger.debug("memory; "+str(info))
        self.client.publish(topic, str(info), 0, True)

    def get_disk(self,):
        ''' publish disk space used as a percentage
        '''
        topic = "diyhas/"+self.host+"/disk"
        value = psutil.disk_usage('/')[3]
        info = "{0:.1f}".format(value)
        self.logger.debug("disk; "+str(info))
        self.client.publish(topic, str(info), 0, True)

    def get_up_time(self,):
        ''' publish up time in days, hours, minutes and seconds
        '''
        topic = "diyhas/"+self.host+"/uptime"
        seconds = int(time.time()) - int(psutil.boot_time())
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        up_time = [days, hours, minutes, seconds]
        up_time_info = ":".join(str(v) for v in up_time)
        self.logger.debug("uptime; "+up_time_info)
        self.client.publish(topic, up_time_info, 0, True)

    def check_system_status(self,):
        ''' collect and publish four system status values
        '''
        self.get_cpu()
        self.get_memory()
        self.get_disk()
        self.get_up_time()

    def system_status_thread(self,):
        ''' check server status on user defined interval
        '''
        while True:
            time.sleep(self.interval)
            self.check_system_status()

    def shutdown(self,):
        ''' shutdown the diysystem thread
        '''
        self.thread.exit()


if __name__ == '__main__':
    exit()
