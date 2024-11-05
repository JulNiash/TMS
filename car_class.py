class Car:

    def __init__(self, mark, modl, yer):
        self.__marka = mark
        self.__model = modl
        self.__year = yer
        self.__speed = 0
    
    @property
    def marka(self):
        return self.__marka

    @property
    def model(self):
        return self.__model
    
    @property
    def year(self):
        return self.__year
    
    @property
    def speed(self):
        return self.__speed
    
    @marka.setter
    def marka(self, value):
        self.__marka = value

    @year.setter
    def year(self, value):
        self.__year = value

    @model.setter
    def model(self, value):
        self.__model = value

    @speed.setter
    def speed(self, value):
        self.__speed = value
        print("car's speed is", self.__speed)

    def up_speed(self):
        self.__speed += 5
        print("car's speed is", self.__speed)

    def low_speed(self):
        if self.__speed >= 5:
            self.__speed -= 5
            print("car's speed is", self.__speed)
        else:
            print("you move with", self.__speed, "km/h, you can stop only")
    
    def stop(self):
        self.__speed = 0
        print("car's speed is", self.__speed)

    
Tesla = Car("Tesla", "X", 2021)
print(Tesla.marka, Tesla.model, Tesla.year, Tesla.speed)
Tesla.marka = "Lada"
Tesla.model = "Vesta"
Tesla.year = 2022
Tesla.up_speed()
Tesla.up_speed()
Tesla.low_speed()
Tesla.stop()
