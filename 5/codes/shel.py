import shelve

s = shelve.open('student.db')
s['key1'] = {'Roll number':202111520, 'Name':"Geiko",'Course':"MCA"}
s.close()
print("Stored as a persistent data")
