#print unique values in a dictionary
dict1 = {"a":199,"b":299,"c":399,"d":199,"e":299}
print ("The dictionary is ")
print (dict1)

values = []
for key,value in dict1.items():
    values = values + [dict1[key]]
print ("The values from dictionary are ", values)
unique_values = set(values)
print ("The unique values are ", unique_values)
