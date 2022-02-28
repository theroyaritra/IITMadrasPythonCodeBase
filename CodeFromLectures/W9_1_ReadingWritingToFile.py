
f=open('myText.txt','w') #'w' stands for write. So, thus we open a text file named myText in writing mode.
f.write("Aritra Roy is a good man, from West Bengal, India.")
f.write("\n He is a student in the IITM B.Sc. degree course in Programming and Data Science")
f.write("\n He is also persuing B.E. in Civil Engineering from BMSCE, Bangalore")
f.write("\n He plans to complete both the degrees by August, 2024")
f.write("\n He is a good singer and a good guitarist as well, though currently little out of practice.")
f.close()

x=open("myText.txt",'r') #'r' stands for read. So, thus we open a text file named myText in reading mode.
s=x.read()
print(s)
print(type(s))
x.close()