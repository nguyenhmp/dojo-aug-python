class Underscore(object):
    def map(self,list,callback):
        newlist = []
        for x in list:
            newlist.append(callback(x))
        return newlist
    def reduce(self,list,callback,memo):
        for x in list:
            memo = callback(memo,x)
        return memo
    def find(self,list,callback):
        for x in list:
            if callback(x)==True:
                return x
        return None
    def filter(self,list,callback):
        for x in list:
            if callback(x)==False:
                list.remove(x)
        return list
    def reject(self,list,callback):
        for x in list:
            if callback(x)==True:
                list.remove(x)
        return list

        
_ = Underscore() 
evens = _.filter([1, 2, 3, 4, 5, 6,], lambda x: x % 2 == 0)
print evens
maps = _.map([1, 2, 3], lambda x: x * 3)
print maps
add_all = _.reduce([1,2,3], lambda x,memo: x+memo, 0)
print add_all
odd = _.find([1,2,3,4], lambda x: x % 2 != 0)
print odd
not_even = _.reject([1, 2, 3, 4, 5, 6,], lambda x: x % 2 == 0)
print not_even
