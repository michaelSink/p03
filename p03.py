import Stack03
import sys
import os.path

def main():

    try:
        inFile = open(inFileName, "r")
    except:
        sys.exit("Cannot open input file: " + inFileName)

    try:
        outFile = open(outFileName, "w")
    except:
        sys.exit("Cannot open output file: " + outFile)

    map = {"(" : ")", "{" : "}", "[" : "]"}

    fileContents = []
    for line in inFile.readlines():
        fileContents.append(line.strip())

    fileContentStack = Stack03.Stack();

    for content in fileContents:
        for char in content:
            if char in map:
                fileContentStack.push(char)
            elif char in map.values():
                if(fileContentStack.isEmpty() or map[fileContentStack.pop()] != char):
                    fileContentStack.push(char)
                    break
        if(fileContentStack.isEmpty()):
            outFile.write(content + " is balanced\n");
        else:
            outFile.write(content + " is not balanced\n");
            fileContentStack.clear()

    inFile.close()
    outFile.close()

if __name__ == "__main__":

    argc = len(sys.argv)

    if(argc == 1):
        inFileName = input("Enter the input file name: ");
        outFileName = input("Enter the output file name: ");
    elif(argc == 2):
        inFileName = sys.argv[1]
        outFileName = input("Enter the output file name: ");
    elif(argc == 3):
        inFileName = sys.argv[1]
        outFileName = sys.argv[2]
    else:
        sys.exit("Invlaid arguments");

    main();