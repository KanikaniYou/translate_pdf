import sys

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

import os
import re

def find_textboxes_recursively(layout_obj):
	if isinstance(layout_obj, LTTextBox):
		return [layout_obj]

	if isinstance(layout_obj, LTContainer):
		boxes = []
		for child in layout_obj:
			boxes.extend(find_textboxes_recursively(child))
		return boxes
	return[]
	
def pdf_read_controller(filepath):
	try:
		text_in_pdf = ""
			
		with open(filepath, 'rb') as f:

			for page in PDFPage.get_pages(f):
				interpreter.process_page(page)
				layout = device.get_result()
		
				boxes = find_textboxes_recursively(layout)
				boxes.sort(key=lambda b:(-b.y1, b.x0))
				
				text_in_page = ""
				for box in boxes:
					text_in_box = ""
					
					text_in_box += box.get_text().strip().strip(" ")
					
					text_in_box.rstrip("\n")
					text_in_box = re.sub(r'  ', " ", text_in_box)
		
					text_in_page += text_in_box
				text_in_pdf += text_in_page
					
		# print(text_in_pdf)
		return(text_in_pdf)
		
	except:
		print("error: " + filepath)
		return("no-text")


def make_txtfile(folder_path,file_name,text='error'):
	if text != "no-text":
		with open(folder_path+"/"+file_name, mode='w') as f:
			f.write(text)
	

laparams = LAParams(detect_vertical=True)
resource_manager = PDFResourceManager()
device = PDFPageAggregator(resource_manager, laparams=laparams)
interpreter = PDFPageInterpreter(resource_manager, device)

if __name__ == '__main__':
	for file_name in os.listdir("pdf_source"):
		if file_name.endswith(".pdf"):
			print(file_name)

			text_in_page = pdf_read_controller("pdf_source/" + file_name)
			
			make_txtfile("eng_txt_split",file_name.rstrip("pdf")+"txt",text_in_page)

		

