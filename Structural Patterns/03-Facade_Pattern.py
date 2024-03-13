'''

This can be used for IOT Applications

'''
class sensor(object):
    def sensor_on(self):
        print("The sensor is ON")

    def sensor_off(self):
        print("The sensor is OFF")

class smoke(object):
    def smoke_on(self):
        print("The smoke is ON")
    
    def smoke_off(self):
        print("The smoke is OFF")

class lights(object):
    def lights_on(self):
        print("Lights are ON")
    
    def lights_off(self):
        print("Lights are OFF")

class Facade(object):
    
    def __init__(self) -> None:
        self.__sen = sensor()
        self.__smo = smoke()
        self.__lig = lights()
    
    def Emergency(self):
        self.__sen.sensor_on()
        self.__smo.smoke_on()
        self.__lig.lights_on()
    
    def NOTEmergency(self):
        self.__sen.sensor_off()
        self.__smo.smoke_off()
        self.__lig.lights_off()

def read_sensor():
    return 19

if __name__ == "__main__":
    F = Facade()
    sensor = read_sensor()
    
    if sensor > 20:
        F.Emergency()
    else:
        F.NOTEmergency()
