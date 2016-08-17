# Part 1
students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
] 

for value in students:
	print value["first_name"] + ' ' + value["last_name"]
	#(SECOND MANUAL WAY)
# print students[0]['first_name'] , students[0]['last_name']
	


#Part 2
users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key, data in users.items():
	counter = 0
	for value in data:
		counter = counter +1
		full_name = value["first_name"] + " " + value["last_name"]
		full_name_upper = full_name.upper()
		name_count = len(value["first_name"]) + len(value["last_name"])
		
		print counter, '-',full_name_upper, name_count


# for value in users.values():
# 	print value[0]['first_name'], value[0]['last_name']

# for value in users.items:
# 	print value['first_name']
# 	print value["first_name"] + ' ' + value["last_name"]








