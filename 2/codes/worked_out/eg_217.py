#Count the frequency of word in a sentence. Use dictionary with key as word
#occurrence as value

sen = str(input("Enter the sentence: "))
word = sen.split()
freq = {}
for w in word:
    freq[w] = freq.get(w,0)+1
print ("Frequency of words in the sentence: ")
print (freq)
