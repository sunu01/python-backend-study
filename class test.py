class Car():
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def drive(self):
        print(f"{self.brand}이 시속 {self.speed}km로 달립니다.")



car2 = Car("벤츠", 100)


car2.drive()


class ElectricCar(Car):
    def __init__(self, brand, speed, battery_capacity):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
    
    def drive(self):
        print(f"{self.brand}이 시속 {self.speed}km로 조용히 달립니다.배터리용량:{self.battery_capacity}kwh")


car1 = ElectricCar("제네시스", 120, 200)
car1.drive()