import requests
import json
import os
import re
import time

API_key = '<ここにAPI_keyを入力>'
def post_text(text):
    url_items = 'https://www.googleapis.com/language/translate/v2'
    item_data = {
        'target': 'ja',
        'source': 'en',
        'q':text
    }
    response = requests.post('https://www.googleapis.com/language/translate/v2?key={}'.format(API_key), data=item_data)
    return response.text
    
def jsonConversion(jsonStr):
    data = json.loads(jsonStr)
    print(data["data"]["translations"][0]["translatedText"])
    return data["data"]["translations"][0]["translatedText"]
    
def split_text(text):
    sen_list = text.split('.')
    
    to_google_sen = ""
    from_google = ""
    

    for index, sen in enumerate(sen_list[:-1]):
        to_google_sen += sen + '. '
        if len(to_google_sen)>1000:
            from_google += jsonConversion(post_text(to_google_sen)) +'\n'
            time.sleep(1)
            
            to_google_sen = ""
        if index == len(sen_list):
            from_google += jsonConversion(post_text(to_google_sen))
            time.sleep(1)
    return from_google
        

if __name__ == '__main__':
	for file_name in os.listdir("eng_txt"):
		print("source: " + file_name)
		with open("eng_txt/"+file_name) as f:
		    s = f.read()
		    new_text = split_text(s)
		    path_w = "jpn_txt/" + file_name
		    with open(path_w, mode='w') as f:
			    f.write(new_text)
