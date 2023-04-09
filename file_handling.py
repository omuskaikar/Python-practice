count = 0
number = int(input("enter the number:"))
while number > 10:
    number = number // 6
    count = count + 1
print(count)


f = open("om.txt", "w+")
f.write("om is the best")
f.close()
f = open("om.txt", "r")
for line in f:
    output = line.title()
print(output)


letter = input("enter letter:")
f = open("om.txt", "r")
m = f.read()
c = m.count(letter)
print(c)


f = open("om.txt", "w")
f.write("hatttttt")
f.close()
f = open("om.txt", "r")
for line in f:
    print(line)
f.close()
f = open("om.txt", "a")
f.write("\naditya is also good")
f.close()
f = open("om.txt", "r")
for line in f:
    print(line)


f = open("om.txt", "r")
for line in f:
    print(line)


fn1 = input("enter the name of first file:")
fn2 = input("enter the name of 2nd file:")
f1 = open(fn1, "r")
f2 = open(fn2, "w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()
f2 = f2 = open(fn2, "r")
for line in f2:
    print(line)


f = open("om.txt", "w")
n = int(input("enter the no. of students:"))
while n > 0:
    a_id = input("enter student id:")
    name = input("enter student name:")
    n = n - 1
    f.write("name:" + name + "  id:  " + a_id + "\n")
f.close()
f = open("om.txt", "r")
for line in f:
    print(line)
