"""f = open('myData', 'r')

#print(f.read())
print(f.readline())
"""

#f = open('myDataTest', 'w')


#f = open('myDataTest', 'a') #a for append
#f.write("\ndummy file")

#To read all the content from file myData and write the data to the file myDataTest
"""f = open('myData', 'r')
f1 = open('myDataTest', 'w')

for data in f:
    f1.write(data)"""

#To copy an image
f = open('temp.jpg', 'rb')
f1 = open('temp1.jpg', 'wb')
for i in f:
    f1.write(i)
