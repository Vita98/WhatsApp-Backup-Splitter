import os
import shutil
import argparse

from fileExt import *



def main(args):
	print(args.all)
	print(args.audio)
	print(args.MAX_FILE_FOR_DIR)



def argParse():
	parser = argparse.ArgumentParser(description='Split the WhatsApp Media backup made by the Syncios Free Mode.')
	parser.add_argument('origin', type=str, help='Path of the folder with the backup')
	parser.add_argument('destination', type=str, help='Path of the destination folder')

	parser.add_argument('-A','--all', action='store_true',help='Split all the file type')
	parser.add_argument('-M','--max', dest="MAX_FILE_FOR_DIR", type=int, default=100, help='Max number of file for each directory. (Default:100)')
	
	parser.add_argument('-p','--photo', action='store_true',help='Split photos')
	parser.add_argument('-a','--audio', action='store_true',help='Split audio')
	parser.add_argument('-v','--video', action='store_true',help='Split videos')
	parser.add_argument('-d','--doc', action='store_true',help='Split documents')
	parser.add_argument('-s','--sticker', action='store_true',help='Split stickers')
	parser.add_argument('-o','--other', action='store_true',help='Split other files')	
	
	args = parser.parse_args()
	main(args)

if __name__ == "__main__":
	argParse()