import shutil, os , re

print("{0:>45}".format("RENAME ALL FILES DOWNLOADED FROM YOUTUBE\n"))

location = ""


def take_user_input():
    global location
    """A FUNCTION THAT ASKS THE USER TO PROVIDE A DIRECTORY TO
    WORK WITH"""
    while True:
        filelocationation = input("Do you want to use the current directory?(y/n): \n")
        if filelocationation.lower() == "y":
            location = os.getcwd()
            break
        elif filelocationation.lower() == "n":
            #convert the path into an absolute path
            user_path = os.path.abspath(input("Please enter a path to be used: \n"))
            #check whether the path exists and is a directory 
            if os.path.exists(user_path) and os.path.isdir(user_path):
                location = user_path
                break
        else:
            print ("Please Enter y/n \n")

take_user_input()

def rename_files():
    global location
    """A FUNCTION FOR RENAMING ALL YOUTUBE FILES DOWNLOADED FROM Y2MATE.COM
      """
      #a regular expression to match files downloaded from y2mate.com
    filepattern = re.compile(r"(y2mate.com - )(.*?)$", re.DOTALL)
    #list all files in the provided location
    ytfiles = os.listdir(location)
#loop through all files in the directory
    for y2mate in ytfiles:
        #search for files with the pattern in the regular expression
        y2 = filepattern.search(y2mate)
        if y2 == None:
            continue
        #store both parts of the filename in variables 
        importantpart = y2.group(1)
        filenme = y2.group(2)
        #join the two filenames with the directory path
        oldfilename = os.path.join(location ,y2mate)
        newfilename = os.path.join(location, filenme)
        print('Renaming "%s" to "%s"....' %(oldfilename, newfilename))
        #use the shutil module to rename the files
        shutil.move(oldfilename , newfilename)

rename_files()










