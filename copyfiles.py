import os, shutil
path = "./108MP"
datanames = os.listdir(path)
for i in datanames:
	if(i[13:17] == "1600"):
		shutil.copy(path + "/" + i, "./demo/108mp1600")
		print(i)

