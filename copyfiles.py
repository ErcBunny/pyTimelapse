import os, shutil
path = "C:/Users/Yueqian/Pictures/timelapse/108MP"
datanames = os.listdir(path)
for i in datanames:
	if(i[13:17] == "1600"):
		shutil.copy(path + "/" + i, "C:/Users/Yueqian/Pictures/timelapse/demo/108mp1600")
		print(i)

