import os
import re
import time
if __name__ == '__main__':
	for file_name in os.listdir("eng_txt_split"):
		if file_name.endswith(".txt"):
			print(file_name)
			text = ""
			with open("eng_txt_split/"+file_name) as f:
				l = f.readlines()
				for line in l:
					text += str(line).rstrip('\n')
				
			path_w = "eng_txt/" + file_name
			with open(path_w, mode='w') as f:
				f.write(text)
