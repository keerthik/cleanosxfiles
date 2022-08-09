# -*- coding: utf-8 -*-

"""
###############################################################################
Be careful to not delete your system files!
Do NOT use this on a boot drive or a Mac system drive.
###############################################################################

original: https://github.com/Pantuflip/DeleteTempFiles
Modified by: Keerthik O
e-mail: razazapata@rzgcontrol.com

Program to delete filesList
._.DS_Store
.DS_Store
._*
looking inside every subfolder
"""
import os, sys

def deleteFile(pathFile):
    if os.path.exists(pathFile):
        os.remove(pathFile) # Este comando borra y despues de borrado no se pueden recuperar los archivos
        print(f"{pathfile} was deleted.")
    else:
        print(f" ¡¡¡¡¡¡¡ {pathFile} could not be deleted !!!!!!!")


def listSubFoldersOptimize(MainFolder):
    mi_List = []
    for root, dirs, files in os.walk(MainFolder, topdown=True, onerror=None, followlinks=False):
        for dir in dirs:
            mi_List.append("{}\{}".format(root,dir))
    return mi_List


def listFiles(MainFolder):
    result = []
    try:
        for f in os.listdir(MainFolder):
            if os.path.isfile(os.path.join(MainFolder, f)):
                result.extend([f])
    except Exception as error:
        print ("Skipping " + MainFolder + " because " + error.strerror)
    return result
    # return [MainFolder+"/"+f for f in os.listdir(MainFolder) if os.path.isfile(os.path.join(MainFolder, f))]


def printList(lista):
    for data in lista:
        print(data)


def listFileFilter(lista):
    newList = []
    for filepath in lista:
        filename = filepath.split("/")[-1]
        if filename[0]=="." and filename[1]=="_":
            newList.append(filepath)
        elif filename == ".DS_Store":
            newList.append(filepath)
    return newList


### -----------  MAIN PROGRAM -----------------------------------
def run():
    filesWithRoot = {}
    # Test D:\CursoPlatzi
    # findPath = "C:\CursoPlatzi"
    findPath = input("Drive path to clean up (eg, D:\\)   \n?> ")
    while os.path.exists(findPath) is False:  # validation
        findPath = input("Drive path to search: example (D:\\)   \n?> ")
    folders = listSubFoldersOptimize(findPath)
    folders.insert(0, findPath)

    for folder in folders:
        filesWithRoot[folder] = listFileFilter(listFiles(folder))
        # if len (filesWithRoot[folder]) > 0:
        #   print ("Within " + folder + ":")
        #   print (filesWithRoot[folder])

    filesListToDelete = [f"{key}\\{path}" for key in filesWithRoot for path in filesWithRoot[key]]
    printList(filesListToDelete)
    respuesta_Usuario = input("\n\nType 's' to delete above files.\nEnter anything else to cancel\n?> ")

    if respuesta_Usuario.lower() == "s":
        for pathFile in filesListToDelete:
            deleteFile(pathFile)
    else:
        quit()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    run()
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~