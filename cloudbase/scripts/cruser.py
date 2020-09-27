import shutil, os, errno
def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)
os.chdir("..")
print(os.getcwd())
name = input("Enter name:\n")
path = "cbusers/"
fullpath = path + name
copy("scripts/user", fullpath)
input("Press ENTER to exit")