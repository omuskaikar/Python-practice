def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0
    f = open(fname, "r")
    for line in f:
        num_lines += 1
        word = "Y"
        for letter in line:
            if letter != " " and word == "Y":
                num_words += 1
                word = "N"
            elif letter == " ":
                num_spaces += 1
                word = "Y"
            for i in letter:
                if i != " " and i != "\n":
                    num_charc += 1
    print("Number of words in text file: ", num_words)
    print("Number of lines in text file: ", num_lines)
    print("Number of characters in text file: ", num_charc)
    print("Number of spaces in text file: ", num_spaces)


if __name__ == "__main__":
    fname = "om.txt"
    try:
        counter(fname)
    except:
        print("File not found")


class Invalid_Marks(Exception):
    def __str__(self):
        return "the marks entered are above 100"


marks = int(input("enter the marks:"))
if marks > 100:
    raise Invalid_Marks
else:
    print("valid marks")


class zeroerr(Exception):
    def __str__(self):
        return "the value of b*d is 0"


a = int(input("enter value for a:"))
b = int(input("enter value for b:"))
c = int(input("enter value for c:"))
d = int(input("enter value for d:"))
if b or d == 0:
    raise zeroerr
else:
    value = ((a + d) + (b * c)) / (b * d)
    print(f"the value of given expression is:{value}")


age = int(input("enter the age:"))


class chotu(Exception):
    def __str__(self):
        return "chotu hai tu"


if age < 18:
    raise chotu
else:
    print("valid age")


if __name__ == "__main__":
    fname = "File1.txt"
    try:
        counter(fname)
    except:
        print("File not found")


class TypeError(Exception):
    def __str__(self):
        return "wrong datatype"


a = 15
b = "om"
if type(b) != str:
    raise TypeError
else:
    print("valid")
