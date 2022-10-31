#update with writeback
import shelve
s = shelve.open('student.db',writeback=True)
s['key1']['Course'] = "MCA Distance Education"
s.close()
print("Updated with Course as MCA Distance Education")
