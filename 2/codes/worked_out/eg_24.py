#interchange first and last element in the list

def interchange(listn):
    #find the length of the list
    num = len(listn)
    #print before interchange
    print ("Original list before interchange: ", listn)
    first_element = listn[0]
    last_element = listn[-1]
    #interchange the elements
    listn[0] = last_element
    listn[-1] = first_element
    print ("List after interchange: ", listn)

nlist = [2,3,4,5,6,100]
interchange(nlist)
