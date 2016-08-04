class Underscore(object):
    def map(self, list, callback):
        newList = []
        for item in list:
            newList.append(callback(item)) 
        return newList
        
    def reduce(self, list, callback, memo):
        for item in list:
            memo = callback(item,memo)
        return memo
      
    def find(self, list, callback):
        for item in list:
            if callback(item) == True:
                return item
        return None

    def filter(self, list, callback):
        for item in list:
            if callback(item) == False:
                list.remove(item)
        return list

    def reject(self, list, callback):
        for item in list:
            if callback(item) == True:
                list.remove(item)
        return list


# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
#print evens

newMapThing = _.map([1,2,3], lambda x: x*3)
#print newMapThing

reducedValue = _.reduce([1,2,3], lambda x,y: x + y, 0)
#print 

found = _.find([1,2,3,4,5,6],  lambda x: x % 2 == 0)
#print found

odds = _.reject([1,2,3,4,5,6], lambda x: x % 2 == 0)
print odds









