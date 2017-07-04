#Making a Tuple list form a Dictionary
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict_tuples(arr):
    tuples = []
    for key, val in arr.items():
        tuples.append(tuple((key, val)))
    print tuples

dict_tuples(my_dict)
