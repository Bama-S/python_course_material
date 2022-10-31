#reverse the numbers in the list
def revslice(listn):
    print ("Original list before reverse: ", listn)
    #use slicing operation
    revlist = listn[::-1]
    print ("List after reverse using slice operation: ", revlist)

def revbuiltin(listn):
    print ("Original list before reverse: ", listn)
    #use built in function
    listn.reverse()
    print ("List after reverse using builtin: ", listn)

nlist = [2,3,4,5,6,100]
revslice(nlist)
revbuiltin(nlist)
