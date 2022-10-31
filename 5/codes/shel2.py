import shelve
t = shelve.open('student.db')
print(t['key1'])
t.close()
