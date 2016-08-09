class Underscore(object):
    def map(self, arr, function):
        x = []
        for i in arr:
            if function(i):
                x.append(i*3)
        return x
    def reduce(self, arr, function, memo):
          for i in arr: 
            memo = function(i, memo)
          return memo
    def find(self, arr, function):
        for i in arr:
            if function(i):
                return i
        return "undefined"     
    def filter(self, arr, function):
        x = []
        for i in arr: 
            if function(i): 
                x.append(i)
        return x 
    def reject(self, arr, function):
        x = []
        for i in arr: 
            if not function(i): 
                x.append(i)
        return x 
     
        
# you just created a library with 5 methods!
# let's create an instance of our class
underscore1 = Underscore() # yes we are setting our instance to a variable that is an underscore
# evens = underscore1.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
# mappings = underscore1.map([1, 2, 3, 4, 5, 6], lambda x: x * 3)
# print mappings
# reducing = underscore1.reduce([1, 2, 3, 4, 5, 6], (lambda x, y: x + y), 0)
# print reducing 
# finds = underscore1.find([1, 2, 3, 3, 3, 3], lambda x: x % 2 == 0)
# print finds
rejecting = underscore1.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print rejecting

