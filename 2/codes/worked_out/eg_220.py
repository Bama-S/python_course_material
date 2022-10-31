#Sort by value
from collections import Counter
dict1 = {"a":499,"b":299,"c":399,"d":199,"e":99}
X = Counter(dict1)
print ("The dictionary is ")
print (dict1)

print ("The sorted values are ")
print (X.most_common())
