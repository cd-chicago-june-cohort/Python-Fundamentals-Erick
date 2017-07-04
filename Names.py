students = [
     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#Names
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

def names(arr):
    for i in arr:
        for k in i:
            print(i.get("first_name") + ' ' + i.get("last_name"))
            break

# names(students)
        
def names_but_better(arr):
    for key, val in arr.items():
        print key
        counter = 1
        for key in val:
            print(str(counter) + ' - ' + key["first_name"].upper() + ' ' + key["last_name"].upper() + ' - ' + str(len(key["first_name"] + key["last_name"])))
            counter += 1

names_but_better(users)