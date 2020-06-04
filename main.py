import os
from shutil import copyfile

dir_path = os.getcwd()
inFolder = os.path.join(dir_path, "in")
outFolder = os.path.join(dir_path, "out")

trimSize = 122

footer = [124, 60, 45, 45, 83, 110, 105, 112, 32, 97, 98, 111, 118, 101, 32, 104,
          101, 114, 101, 32, 116, 111, 32, 99, 114, 101, 97, 116, 101, 32, 97, 32,
          114, 97, 119, 32, 115, 97, 118, 32, 98, 121, 32, 101, 120, 99, 108, 117,
          100, 105, 110, 103, 32, 116, 104, 105, 115, 32, 68, 101, 83, 109, 117, 77,
          69, 32, 115, 97, 118, 101, 100, 97, 116, 97, 32, 102, 111, 111, 116, 101,
          114, 58, 1, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0,
          0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 124, 45, 68, 69, 83, 77,
          85, 77, 69, 32, 83, 65, 86, 69, 45, 124]

for root, dirs, files in os.walk(inFolder, topdown=False):
    for name in files:
        if name.endswith(".dsv"):
            savExt = ".sav"
            inFilename = os.path.join(inFolder, name)
            outFilename = os.path.join(outFolder, name[:-4] + savExt)
            fileSize = os.stat(inFilename).st_size
            readTo = fileSize - trimSize
            with open(inFilename, 'rb') as inFile:
                with open(outFilename, 'wb') as outFile:
                    outFile.write(inFile.read()[:readTo])
            print("dsv->sav: Converted '" + name + "' to '" + name[:-4] + savExt + "'")
        if name.endswith(".sav"):
            dsvExt = ".dsv"
            inFilename = os.path.join(inFolder, name)
            outFilename = os.path.join(outFolder, name[:-4] + dsvExt)
            binary = bytearray(footer)
            with open(inFilename, 'rb') as inFile:
                with open(outFilename, 'wb') as outFile:
                    contents = inFile.read()
                    outFile.write(contents)
                    outFile.write(binary)
            print("sav->dsv: Converted '" + name + "' to '" + name[:-4] + dsvExt + "'")

