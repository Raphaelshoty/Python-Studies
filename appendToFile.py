textToBeAeppended = "30 years old"

saveFile = open("MeuNome.txt","a")
saveFile.write("\n"+textToBeAeppended)
saveFile.close()
