#   Loop

from dirsync import sync
import os, shutil, glob

l = 1

os.chdir("..")
print(os.getcwd())



while (l==1):
    #   This section syncs shared folders and share folders, names and stuff
    path = os.listdir("/cbusers/*")
    dst = os.listdir("/cbusers/share")
    dst2 = os.listdir("/cbuser/shared")
    print(path + dst + dst2)
    if ((path == dst) == 0):
        print("Currently unsynced. Syncing " + path + dst)
        shutil.copytree(path, dst)
    else:
        print("Currently synced")
    if ((path == dst2) == 0):
        print("Currently unsynced. Syncing " + path + dst2)
        shutil.copytree(path, dst2)
    #   This section syncs folders
    
    