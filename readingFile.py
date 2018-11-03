##readingFile = open("MeuNome.txt","r").read()
##
##split = readingFile.split("\n")
##
##print(split)
##
##for chunk in split:
##    if(chunk == ""):
##        continue
##    print(chunk)

read = open("MeuNome.txt","r").readlines()
for chunk in read:
    if(chunk == ""):
        continue
    print(chunk)

