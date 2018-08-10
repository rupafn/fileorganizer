#OS module in Python provides a way of using operating system dependent functionality.
#walk yeild two list for each directory it visits, splitting into files and dirs
import sys
from os import walk
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
    files = [f for f in os.listdir(path) if os.path.isfile(f)]
    for name in files:
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



if __name__ == "__main__":
    path = sys.argv[1]
    runOrganizer(path)
