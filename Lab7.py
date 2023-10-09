#WAP to Demonstrate dictionaries in Python....
dict1={1:'Python',2:'Java',3:'Ruby',4:'Scala'}
#copy() method
dict2=dict1.copy()
print(dict2)
#clear() method
dict1.clear() #deletes all the key-value pairs from dictionary
print("After clearing dict:",dict1)
#get() method
print(dict2.get(2))
#items() method
print(dict2.items())
#keys() method
print(dict2.keys())
#pop() method
dict2.pop(2)
print(dict2)
#popitem() method
dict2.popitem()
print(dict2)
#value() method
print(dict2.values())