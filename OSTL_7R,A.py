file=open('my_file.txt','a+')
n=input("Enter the string :")
if n=="!" or n=="@":
    file.close()
else:
    file.write(n+'\n')
file=open(r'my_file.txt')
print(file.read())
file.close()

n1 = input("Enter file to be read from: ")
n2 = input("Enter file to be appended to: ")
fin = open(n1, "r")
data2 = fin.read()
fin.close()
fout = open(n2, "a")
fout.write(data2)
fout.close()

def countWords(fileName):
    numwords = 0
    numchars = 0
    numlines = 0

    with open(fileName, 'r') as file:
        for line in file:
            wordlist = line.split()
            numlines += 1
            numwords += len(wordlist)
            numchars += len(line)

    print ("Words: ", numwords)
    print ("Lines: ", numlines)
    print ("Characters: ", numchars)

if __name__ == '__main__':
    countWords('my_file.txt')

import os
for dirpath,dirnames,filenames in os.walk('.'):
    print("Current Directory path",dirpath)
    print("Current directory names:",dirnames)
    print("Files present in dir :",filenames)


