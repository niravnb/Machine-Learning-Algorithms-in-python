def main():
    f= open("guru99.txt","w+")
    #f=open("guru99.txt","a+")
    for i in range(10):
         f.write("This is line %d\r\n" % (i+1))
    f.close()
    #Open the file back and read the contents
    f=open("guru99.txt", "r")
    if f.mode == 'r':
      contents =f.read()
       print (contents)
    # or, readlines reads the individual line into a list
    fl =f.readlines()
    for x in fl:
    print(x)



f = open("demofile.txt", "r")
for x in f:
  print(x)

f = open("demofile.txt", "r")
print(f.readline())
f.close()


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())


# Python code to illustrate split() function 
with open("file.text", "r") as file: 
    data = file.readlines() 
    for line in data: 
        word = line.split() 
        print word 


# To open a text file, use:
# fh = open("hello.txt", "r")

# To read a text file, use:
# fh = open("hello.txt","r")
# print fh.read()

# To read one line at a time, use:
# fh = open("hello".txt", "r")
# print fh.readline()

# To read a list of lines use:
# fh = open("hello.txt.", "r")
# print fh.readlines()

# To write to a file, use:
# fh = open("hello.txt","w")
# write("Hello World")
# fh.close()

# To write to a file, use:
# fh = open("hello.txt", "w")
# lines_of_text = ["a line of text", "another line of text", "a third line"]
# fh.writelines(lines_of_text)
# fh.close()

# To append to file, use:
# fh = open("Hello.txt", "a")
# write("Hello World again")
# fh.close()

# To close a file, use
# fh = open("hello.txt", "r")
# print fh.read()
# fh.close()








if __name__== "__main__":
  main()