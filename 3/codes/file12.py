#copy the text content from url to a file
import urllib.request

url = "http://textfiles.com/food/aphrodis.txt"
text = urllib.request.urlopen(url)
data = text.read()
#print (text)
file = open('urltext','w+')
file.write(str(data))
file.close()
print ("The content is written")
