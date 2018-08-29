#########################################
# Project   : ARFF to CSV converter     #
# Created   : 10/01/17 11:08:06         #
# Author    : haloboy777                #
# Licence   : MIT                       #
#########################################

# Importing library
import os

# Getting all the arff files from the current directory
files = [arff for arff in os.listdir('.') if arff.endswith(".arff")]

def shrink(attr):
    '''
    This function shrinks the attribute name into a single line
    : param attr: the string attribute to be shrinked

    : return: the string shrinked
    '''
    if(len(attr) > 1):
        return attr[0] + shrink(attr[1:])
    else:
        return attr[0]

# Function for converting arff list to csv list
def toCsv(content, file_name=None):
    data = False
    header = ""
    newContent = []
    for line in content:
        if not data:
            if "@attribute" in line:
                attri = line.split()
                if(len(attri) > 3):
                    attri = shrink(attri[1:-1])
                columnName = attri[attri.index("@attribute")+1]
                header = header + columnName + ";"
            elif "@data" in line:
                data = True
                header = header[:-1]
                header += '\n'
                newContent.append(header)
        else:
            newContent.append(line)
            
    if(file_name != None):
        with open(file_name+".csv", "w") as output_file:
            output_file.writelines(newContent)
    
    return newContent

# Main loop for reading and writing files
def main():
    for file in files:
        with open(file , "r") as inFile:
            content = inFile.readlines()
            name,ext = os.path.splitext(inFile.name)
            new = toCsv(content)
            with open(name+".csv", "w") as outFile:
                outFile.writelines(new)

if __name__ == '__main__':
    main()