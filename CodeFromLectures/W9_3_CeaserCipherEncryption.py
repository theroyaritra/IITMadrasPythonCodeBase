#We shift all the letters by 3 units in this example of ceaser cipher encryption. All the other numbers, printables etc. remain the same in the encrypted file.
import string
def create_ceaser_dict1(): #Creating disctionary for ceaser cipher encryption process
    l=string.ascii_letters
    l=list(l)
    d={'Ã':'Ã','ƒ':'ƒ','Â':'Â','Å':'Å','â':'â','ª':'ª'}
    for i in range(len(l)):
        d[l[i]]=l[(i+3)%26]
    return d
def create_ceaser_dict2(): #Creating dictionary for ceaser cipher decryption process
    l=string.ascii_letters
    l=list(l)
    d={'Ã':'Ã','ƒ':'ƒ','Â':'Â','Å':'Å','â':'â','ª':'ª'}
    for i in range(len(l)):
        d[l[i]]=l[(i-3)%26]
    return d
#Ceaser Cipher Encryption of the big story to a new file:-
f=open("BigStory_TextFile.txt","r")
n=open("BigStoryEncrypted.txt","w")
s=f.read(1)
while(s!=''):
    if(s.isalpha()):
        x=create_ceaser_dict1()[s]
        n.write(x)
    else:
        n.write(s)
    s=f.read(1)
f.close()
n.close()
#Decrypting the encrypted file to a new file to find original big story:-
m=open("BigStoryEncrypted.txt",'r')
z=open("BigStory_Decrypted.txt","w")
p=m.read(1)
while(p!=''):
    if(p.isalpha()):
        x=create_ceaser_dict2()[p]
        z.write(x)
    else:
        z.write(p)
    p=m.read(1)
m.close()
z.close()