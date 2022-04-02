import os
import shutil


MAX_FILE_FOR_DIR = 100
originBaseDir = "./WhatsApp"
destinationBaseDir = "./WhatsApp-Split"


audioExt = {"mp3","opus", "m4a"}
photoExt = {"jpg","thumb","heic"}
videoExt = {"mp4"}
docExt = {"doc","txt","xls","pptx","docx","pdf","ppt","xlsx"}
stickersExt = {"wastickers"}
othersExt = {"pkpass","db","rar","sql","zip"}



audioDirNumber = 0
audioFileNumber = 0
audioDirBase = destinationBaseDir + "/Audio" 
audioDirActual = audioDirBase + "/Dir-" + str(audioDirNumber)

photoDirNumber = 0
photoFileNumber = 0
photoDirBase = destinationBaseDir + "/Photo"
photoDirActual = photoDirBase + "/Dir-" + str(photoDirNumber)

videoDirNumber = 0
videoFileNumber = 0
videoDirBase = destinationBaseDir + "/Video"
videoDirActual = videoDirBase + "/Dir-" + str(videoDirNumber)

docDirNumber = 0
docFileNumber = 0
docDirBase = destinationBaseDir + "/Doc"
docDirActual = docDirBase + "/Dir-" + str(docDirNumber)

stickersDirNumber = 0
stickersFileNumber = 0
stickersDirBase = destinationBaseDir + "/Stickers"
stickersDirActual = stickersDirBase + "/Dir-" + str(stickersDirNumber)

othersDirNumber = 0
othersFileNumber = 0
othersDirBase = destinationBaseDir + "/Others"
othersDirActual = othersDirBase + "/Dir-" + str(othersDirNumber)





def copyFile(file,destPath):
	shutil.copyfile(file, destPath)

def makeAndCheckDir(dirPath):
	if not os.path.exists(dirPath):
		os.mkdir(dirPath)


#making dir
if not os.path.exists(destinationBaseDir):
	os.mkdir(destinationBaseDir) 

if not os.path.exists(audioDirBase):
	os.mkdir(audioDirBase)
if not os.path.exists(audioDirActual):
	os.mkdir(audioDirActual)

if not os.path.exists(videoDirBase):
	os.mkdir(videoDirBase)
if not os.path.exists(videoDirActual):
	os.mkdir(videoDirActual)

if not os.path.exists(photoDirBase):
	os.mkdir(photoDirBase)
if not os.path.exists(photoDirActual):
	os.mkdir(photoDirActual)

if not os.path.exists(docDirBase):
	os.mkdir(docDirBase)
if not os.path.exists(docDirActual):
	os.mkdir(docDirActual)

if not os.path.exists(stickersDirBase):
	os.mkdir(stickersDirBase)
if not os.path.exists(stickersDirActual):
	os.mkdir(stickersDirActual)

if not os.path.exists(othersDirBase):
	os.mkdir(othersDirBase)
if not os.path.exists(othersDirActual):
	os.mkdir(othersDirActual)



files = os.listdir(originBaseDir)

i = -1
for file in files:
	i += 1
	fileExt = str(file).split(".")[1]

	if fileExt in docExt:
		print("DOC " + str(i))
		copyFile(originBaseDir+"/"+file,docDirActual+"/"+file)

		docFileNumber += 1
		if docFileNumber == MAX_FILE_FOR_DIR:
			docFileNumber = 0
			docDirNumber += 1
			docDirActual = docDirBase + "/Dir-" + str(docDirNumber)
			makeAndCheckDir(docDirActual)

	elif fileExt in photoExt:
		print("PHOTO "+ str(i))
		copyFile(originBaseDir+"/"+file,photoDirActual+"/"+file)

		photoFileNumber += 1
		if photoFileNumber == MAX_FILE_FOR_DIR:
			photoFileNumber = 0
			photoDirNumber += 1
			photoDirActual = photoDirBase + "/Dir-" + str(photoDirNumber)
			makeAndCheckDir(photoDirActual)

	elif fileExt in videoExt:
		print("VIDEO "+ str(i))
		copyFile(originBaseDir+"/"+file,videoDirActual+"/"+file)

		videoFileNumber += 1
		if videoFileNumber == MAX_FILE_FOR_DIR:
			videoFileNumber = 0
			videoDirNumber += 1
			videoDirActual = videoDirBase + "/Dir-" + str(videoDirNumber)
			makeAndCheckDir(videoDirActual)

	elif fileExt in audioExt:
		print("AUDIO "+ str(i))
		copyFile(originBaseDir+"/"+file,audioDirActual+"/"+file)

		audioFileNumber += 1
		if audioFileNumber == MAX_FILE_FOR_DIR:
			audioFileNumber = 0
			audioDirNumber += 1
			audioDirActual = audioDirBase + "/Dir-" + str(audioDirNumber)
			makeAndCheckDir(audioDirActual)

	elif fileExt in othersExt:
		print("OTHERS "+ str(i))
		copyFile(originBaseDir+"/"+file,othersDirActual+"/"+file)

		othersFileNumber += 1
		if othersFileNumber == MAX_FILE_FOR_DIR:
			othersFileNumber = 0
			othersDirNumber += 1
			othersDirActual = othersDirBase + "/Dir-" + str(othersDirNumber)
			makeAndCheckDir(othersDirActual)

	elif fileExt in stickersExt:
		print("STICKERS "+ str(i))
		copyFile(originBaseDir+"/"+file,stickersDirActual+"/"+file)

		stickersFileNumber += 1
		if stickersFileNumber == MAX_FILE_FOR_DIR:
			stickersFileNumber = 0
			stickersDirNumber += 1
			stickersDirActual = stickersDirBase + "/Dir-" + str(stickersDirNumber)
			makeAndCheckDir(stickersDirActual)




















