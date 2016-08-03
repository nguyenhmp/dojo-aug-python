from underscore import _

print _.map([1,2,3], lambda x : x**2)           # [1,4,9]
print _.reduce([2,4,6], lambda x : x*-1)        # -12
print _.find([1,3,6,8,9], lambda x : x%4==0)    # 8
print _.filter([1,3,6,8,9], lambda x: x%5==0)   # None
print _.reject([1,3,6,8,9], lambda x: x%3==0)   # [1,8]
