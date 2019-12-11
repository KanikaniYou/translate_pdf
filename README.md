# translate_pdf
Translate text in PDF files(EN to JP) and output as text files.
# Requirement

* python3.6.8
* requests
* urllib3
* pdfminer
 
# Installation
 
```bash
pip install pdfminer.six
```
 
# Usage
 
Get API Key from Google Cloud.
https://cloud.google.com/translate/docs/

```bash
git clone https://github.com/KanikaniYou/translate_pdf
cd translate_pdf

#Place the PDF files you want to translate in pdf_source.

python pdf_to_txt.py

#Delete unnecessary parts in the text file if you need.

python let_translatable.py
python translate_en_jp.py

```
