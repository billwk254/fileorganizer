import shutil, os , re
filepattern = re.compile(r"(y2mate.com - )(.*?)$", re.DOTALL)


filelocation = input("Do you want to use the current directory?(y/n): ")
if filelocation.lower() == "y":
    loc = os.getcwd()
elif filelocation.lower() == "n":
    user = input("Please enter a path to be used: ")
    loc = os.path.abspath(user)
else:
    print ("Please Enter y/n ")

ytfiles = os.listdir(loc)


for y2mate in ytfiles:
    y2 = filepattern.search(y2mate)
    if y2 == None:
        continue
    importantpart = y2.group(1)
    filenme = y2.group(2)
    oldfilename = os.path.join(loc ,y2mate)
    newfilename = os.path.join(loc, filenme)
    print('Renaming "%s" to "%s"....' %(oldfilename, newfilename))
    shutil.move(oldfilename , newfilename)












