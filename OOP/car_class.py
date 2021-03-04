class Car:
    annual_discount = 0.9
    def __init__(self, manufacturer, model, price, mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price
        self.mileage = mileage
        
    def drive(self):
        self.mileage += 1
    
    def apply_discount(self):
        self.price = self.price * self.annual_discount
        
    @classmethod
    def set_discount(cls, new_discount):
        cls.annual_discount = new_discount
        
        

car_1 = Car("Toyota", "Prius", 1000, 0)
car_2 = Car("Kia", "Ceed", 1500, 800)

Car.set_discount(0.5)
print(car_1.model, car_1.price)
car_1.apply_discount()
print(f'{car_1.model, car_1.price} after applying discount')



#print(car_2.mileage)