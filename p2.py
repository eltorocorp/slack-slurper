#reading a text file, for this open the file first
file = open("sample.txt",'r')
#reading a line in a file
for line in file:
    separateLine = line.split()
    print(separateLine)
    

