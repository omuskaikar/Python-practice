#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(50)
y=np.random.randn(50)
plt.scatter(x,y,facecolor="none",edgecolor="b")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# In[2]:


math_marsk=[88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range,math_marsk,label="math_marsk",color="r")
plt.scatter(marks_range,science_marks,label="science_marks",color="g")
plt.legend()
plt.show()


# In[3]:


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
for d in (dic1,dic2,dic3):
    dic1.update(d)
dic1


# In[4]:


dic1={1:2,2:3,3:4}
key=3
if key in dic1:
    print("key exists")
else:
    print("doesnt exist")


# In[5]:


dic1={}
for i in range (1,6):
    dic1[i]=i*i
print(dic1)


# In[6]:



del dic1[4]
print( dic1)


# In[7]:


key=[1,2,3,4,5]
values=[2,3,4,5,6]
dic1=dict(zip(key,values))
dic1


# In[8]:


Sample_Data=[{"V":"S001"},
             {"V": "S002"}, 
             {"VI": "S001"}, 
             {"VI": "S005"}, 
             {"VII":"S005"}, 
             {"V":"S009"},
             {"VIII":"S007"}]
ans=set(val for dic in Sample_Data for val in dic.values())
ans


# In[9]:


string="apple"
for i in range(len(string)):
    dic1[i+1]=string[i]
print(dic1)


# In[10]:


sentence=input("enter the sentence:")
for i in sentence:
    if (i==" "):
        print("-",end="")
    else:
        print(i,end="")


# In[ ]:


import random
a=[]
for i in range (10):
    a.append(random.randrange(100,200))
print("list is:",a)
print(min(a))


# In[ ]:


countries={"INDIA":"INR",
           "USA":"USD",
           "DUBAI":"DHIRAM",
           "QATAR":" DINAR",
           "ENGLAND":"POUNDS"}
print(countries["INDIA"])


# In[ ]:


number=-12+5j
print(type(number))
print("real part is:",number.real)
print("imaginary part is:",number-number.real)
print("conjugate is ",number.conjugate())
print("absolute is:",abs(number))


# In[ ]:


string="hello"
string=string.replace("hello","help")
print(string)


# In[ ]:


a=[]
for i in range(0,10):
      a.append(random.randrange(100,200))
print(a)
print(min(a))


# In[ ]:


string="lemon"
string=string[-1]+string[1:-1]+string[:1]
print(string)


# In[ ]:


string="prerajulisation"
subs="om"
if subs in string:
    print("yes")
else:
    print("no")


# In[ ]:


sentence="let's all agree that DBMS sucks"
sentence=sentence.replace(" ","-")
print(sentence)


# In[ ]:


string="malayalam"
reverse=""
for i in range (len(string)-1,-1,-1):
    reverse=reverse+string[i]
if (string==reverse):
    print("palindrome")
else:
    print("not palindrome")


# In[ ]:


sentence=input("enter the sentence:")
sentence=sentence.title()
sentence


# In[ ]:


string=input("enter the string:")
count=0
char=input("enter the char:")
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print(count)


# In[ ]:


dic1={"om":"uskaikar","aditya":"sonavane"}
dic2={"mihir":"randhive"}
dic1.update(dic2)
dic1


# In[ ]:


sentence=input("enter the sentence:")
vowel=0
consonant=0
digit=0
spchar=0
for i in range (len(sentence)):
    ch=sentence[i]
    ch=ch.lower()
    if(ch=='a' or ch=='e'or ch=='i'or ch=='o'or ch=='u'):
        vowel=vowel+1
    elif(ch>='a'and ch<='z'):
        consonant=consonant+1
    elif(ch>='0'and ch<='9'):
        digit=digit+1
    else:
        spchar=spchar+1
print(f"vowel:{vowel}")
print(f"consonant:{consonant}")
print(f"digits:{digit}")
print(f"special characters:{spchar}")


# In[ ]:


a=np.full((3,3),1)
a


# In[ ]:



if [1,1,1] in a.tolist():
    print("yes")
else:
    print("no")


# In[ ]:


a=np.array([[3,3,3],[1,3,1],[1,8,9]])
b=np.array([[1,0,0],[0,1,0],[0,0,1]])
c=a+b
d=np.dot(a,b)
print (c)
print(d)


# In[ ]:


a=a.flatten()
print(np.bincount(a).argmax())


# In[ ]:


a=np.array([[1,2],[3,4]])
print(a)
print(a.flatten())
a=a.reshape(1,4)
print(a)


# In[ ]:


a=np.array([[1,1,1],[2,2,2],[3,3,3]])
print(a)
for i in range(3):
    sum=0
    for j in range(3):
        sum=sum+a[j][i]
    print(sum,end=" ")


# In[ ]:


a=np.array([1,1,1,1,1,1,1,1,1,1,1,1])
print(np.mean(a))
print(np.var(a))
print(np.std(a))


# In[ ]:


a=np.array(['python','is','easy'])
x=np.char.join(" ",a)
print(x)


# In[ ]:


a=np.array([1,2,3])
b=np.array([2,3,5])
x=np.arange(1,11)
y=x*x
plt.title("line graph")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,color="r")
plt.show()


# In[ ]:



def reverse(number):
    revnum=0
    while(number>0):
        digit=number%10
        revnum=revnum*10+digit
        number=number//10
    return revnum
print(reverse(int(input("enter the number:"))))


# In[ ]:


n=int(input("enter the number:"))
for i in range(n):
    list1=[]
    for j in range(i):
        print(i,end=" ")
        if(i<j):
            print("+",end=" ")
        list1.append(i)
    print("=",sum(list1))
print()
    


# In[ ]:


limit=int(input("Enter upper limit:"))
c=0
m=2
while(c<limit):
    for n in range(1,m+1):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if(c>limit):
            break
        if(a==0 or b==0 or c==0):
            break
        print(a,b,c)
    m=m+1


# In[ ]:


limit=int(input("enter upper limit:"))
c=0
m=2
while(c<limit):
    for n in range(1,m+1):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if(c>limit):
            break
        if(a==0 or b==0 or c==0):
            break
        print(a,b,c)
    m=m+1


# In[ ]:


for i in range(0,7):
    for j in range(0,i):
        print(i,end="")
    print()


# In[ ]:


l1=[1,2,3]
l2=[2,3,4]
dic=dict(zip(l1,l2))
dic


# In[ ]:


count=0
number=int(input("enter the number:"))
while(number>10):
    number=number//6
    count=count+1
print(count)


# In[ ]:


f=open("om.txt","w+")
f.write("om is the best")
f.close()
f=open("om.txt","r")
for line in f:
        output=line.title()
print(output)


# In[ ]:


letter = input("enter letter:")
f=open("om.txt","r")
m=f.read()
c=m.count(letter)
print(c)


# In[ ]:


f=open("om.txt","w")
f.write("hatttttt")
f.close()
f=open("om.txt","r")
for line in f:
    print(line)
f.close()
f=open("om.txt","a")
f.write("\naditya is also good")
f.close()
f=open("om.txt","r")
for line in f:
    print(line)


# In[ ]:


f=open("om.txt","r")
for line in f:
    print(line)


# In[ ]:


fn1=input("enter the name of first file:")
fn2=input("enter the name of 2nd file:")
f1=open(fn1,"r")
f2=open(fn2,"w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()
f2=f2=open(fn2,"r")
for line in f2:
    print(line)


# In[140]:


f=open("om.txt","w")
n= int (input("enter the no. of students:"))
while(n>0):
    a_id=input("enter student id:")
    name=input("enter student name:")
    n=n-1
    f.write("name:"+name+"  id:  "+a_id+"\n")
f.close()
f=open("om.txt","r")
for line in f:
    print(line)


# In[145]:



a=np.array([1,3,56,7,1,2,4])
c=np.sort(a)
print(c)
for i in c:
    


# In[ ]:


print("Enter the Name of Source File: ")
sFile = input()
print("Enter the Name of Target File: ")
tFile = input()

fileHandle = open(sFile, "r")
texts = fileHandle.readlines()
fileHandle.close()

fileHandle = open(tFile, "w")
for s in texts:
    fileHandle.write(s)
fileHandle.close()

print("\nFile Copied Successfully!")


# In[ ]:


f=open("om.txt","r")
while 1:
    char=f.read(1)
    if not char:
        break
    print(char)
f.close()


# In[ ]:


def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0
    f=open(fname, 'r') 
    for line in f:
            num_lines += 1
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif (letter == ' '):
                    num_spaces += 1
                    word = 'Y'
                for i in letter:
                    if(i !=" " and i !="\n"):
                        num_charc += 1
    print("Number of words in text file: ",num_words)
    print("Number of lines in text file: ",num_lines)
    print('Number of characters in text file: ',num_charc)
    print('Number of spaces in text file: ',num_spaces)
if __name__ == '__main__':
    fname = 'om.txt'
    try:
        counter(fname)
    except:
        print('File not found')


# In[ ]:


class Invalid_Marks(Exception):
    def __str__(self):
        return "the marks entered are above 100"
marks=int(input("enter the marks:"))
if(marks>100):
    raise Invalid_Marks
else:
    print("valid marks")


# In[ ]:


class zeroerr(Exception):
    def __str__(self):
        return "the value of b*d is 0"
a=int(input("enter value for a:"))
b=int(input("enter value for b:"))
c=int(input("enter value for c:"))
d=int(input("enter value for d:"))
if(b or d==0):
    raise zeroerr
else:
    value=((a+d)+(b*c))/(b*d)
    print(f"the value of given expression is:{value}")


# In[ ]:


age=int(input("enter the age:"))
class chotu(Exception):
    def __str__(self):
        return "chotu hai tu"
if(age<18):
    raise chotu
else:
    print("valid age")


# In[ ]:


string=input('enter a string up to 15 char:')
while len(string)>15:
    string=input('enter a string upto 15 char:')
for i in range(0,len(string)):
    print(string[i],i)


# In[ ]:


if __name__ == '__main__':
    fname = 'File1.txt'
    try:
        counter(fname)
    except:
        print('File not found')


# In[ ]:


class TypeError(Exception):
    def __str__(self):
        return "wrong datatype"
a=15
b="om"
if(type(b)!= str ):
    raise TypeError
else:
    print("valid")
    


# In[9]:


class complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def add_comp(self,c1,c2):
        temp=complex(0,0)
        temp.real=c1.real+c2.real
        temp.imaginary=c1.imaginary+c2.imaginary
        return temp
c1=complex(0,0)
c2=complex(0,0)
c1.real=int(input("enter real part"))
c1.imaginary=int(input("enter img. part"))
c2.real=int(input("enter real part"))
c2.imaginary=int(input("enter img. part"))
c3=complex(0,0)
c3=c3.add_comp(c1,c2)
print("sum is:",c3.real,"+i",(c3.imaginary))


# In[49]:


class triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def peri(self):
        return  a+b+c
a=int(input("enter value for a:"))
b=int(input("enter value for b:"))
c=int(input("enter value for c:"))
object=triangle(a,b,c)
print("perimeter is:",object.peri())


# In[55]:


class lists:
    def __init__(self,a):
        self.a=a
    def append(self,value):
        self.value=value
        a.append(value)
        return a
    def remove(self,value):
        self.value=value
        a.remove(value)
        return a
    def display(self):
        print(a)
object=lists(a)
a=[1,2,3,4]
object.append(int(input("enter value to append:")))
print(a)
object.remove(int(input("enter value to remove:")))
print(a)
object.display()


# In[1]:


class calculator:
      def multiply(self,a,b):
        self.a=a
        self.b=b
        return a*b
      def addition(self,a,b):
        self.a=a
        self.b=b
        return a+b
a=int(input("enter value of a"))
b=int(input("enter value of b"))

object1=calculator()
choice=1
print("1 for addition")
print("2 for multiplication")
choice=int(input("enter"))
if(choice==1):
    print(object1.addition(a,b))
elif(choice==2):
    print(object1.multiply(a,b))
else:
    print("invalid choice")


# In[20]:


class rev:
    def __init__(self,string):
        self.string=string
    def reverse(self,string):
        string=string.split()
        for i in range (len(string)):
            reversestr=string[i]
            reversestr=reversestr[::-1]
            print(reversestr,end=" ")
string=(input("enter the string:"))
obj=rev(string)
obj.reverse(string)


# In[22]:


a="hello"
print(a.title())


# In[30]:


class vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage
    def display(self):
        print(self.maxspeed)
        print(self.mileage)
class bus(vehicle):
    pass

maxspeed=int(input("enter the speed:"))
mileage=int(input("enter the mileage:"))
obj=bus(maxspeed,mileage)
obj.display()


# In[38]:


l=[0, 2, 3, 4, 6, 7, 9, 0]
l1=[]
count=0
for i in range(len(l)):
    if (l[i]!=0):
        l1.append(l[i])
    else:
        count=count+1
for i in range(count):
    l1.append(0)
print(l1)


# In[40]:


import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


# In[113]:


df=pd.DataFrame(exam_data,index=labels)


# In[44]:


df.head(3)


# In[49]:


df1=df[['name','score']]
df1


# In[59]:


df1=df.loc['a':'e',['name','score']]


# In[61]:


df.iloc[:7,[1,3]]


# In[66]:


df[df['attempts']>2]


# In[68]:


print("no. of coulmns is:",len(df.columns))
print("no. of rows are:",len(df))


# In[79]:


df1=df[df['score']>15]
df1=df1[df1['score']<=20]
df1


# In[82]:


df1=df[df['attempts']<2] 
df2=df1[df1['score']>15]
df2


# In[84]:


df.loc['k']=['om',20.0,2,'yes']


# In[85]:


df


# In[88]:


df.drop('k',inplace=True)
df


# In[90]:


df.sort_values(by=['name','score'],ascending=[False,True])


# In[110]:


a=df.head(10)
a


# In[114]:


df['qualify']= df['qualify'].map({'yes':True,'no':False})


# In[115]:


df


# In[116]:


df.at['d','score']=10.2


# In[117]:


df


# In[123]:


df.isnull()
df.dropna()


# In[125]:


df.duplicated()


# In[139]:


l1=[0,10,20,40,60,80]
l2=[10,30,40,50,70]
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)


# In[ ]:




