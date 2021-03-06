#OS module in Python provides a way of using operating system dependent functionality.

import sys
import os

def organize(dirpath, name, filefolder):
    source = dirpath + "/"+name
    dest = dirpath + "/"+ filefolder + "/" + name
    os.rename(source, dest)


#read each filenames
#split on dot (.)
#get the last string
#create a folder if not exist on the string
# put this file into that folder
def runOrganizer(path):

    mypath = path
    files = [f for f in os.listdir(mypath) if os.path.isfile(mypath+'/'+f)]
    for name in files:
        try:
            str = name.split('.')
            arrlen = len(str)
            filefolder = str[arrlen-1]
            pathexist = os.path.exists(mypath+'/'+filefolder)
            if not pathexist:
                newpath = mypath + '/' + filefolder
                os.mkdir(newpath)
                organize(mypath,name,filefolder)

            else:
                organize(mypath,name,filefolder)
        except:
            print("Cannot create folder for this file: ", name)



if __name__ == "__main__":
    path = sys.argv[1]
    runOrganizer(path)
