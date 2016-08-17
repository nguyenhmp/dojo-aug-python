class Bike(object): #creating a new class called bike with the miles, price, max_speed as attributes/properties
    def __init__(self, price, max_speed): #def__init__ intializes the object and self creates the object. price and max speed are other parameters.
        self.price = price #attribues 
        self.max_speed = max_speed
        self.miles = 0


    def displayInfo(self): #methods being created for instances 
        print 'Price is: $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed) + 'mph'
        print 'Total miles: ' + str(self.miles) + ' miles'
        return self 
    def drive(self):
        print 'Driving'
        self.miles += 10
        return self 
    def reverse(self):
        print 'Reversing'
        # prevent negative miles
        if self.miles >= 5:
            self.miles -= 5
        return self 
# create instances and run methods
bike1 = Bike(99.99, 12) #parameters are price and max speed 
bike1.drive().drive().drive().reverse().displayInfo();

bike2 = Bike(129.99, 20)
bike2.drive().drive().reverse().reverse().displayInfo();


bike3 = Bike(69.99, 15)
bike3.reverse().reverse().reverse().displayInfo();
