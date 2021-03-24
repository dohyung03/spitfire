from google_trans_new import google_translator
import sys
import os
query = sys.argv[1:-1]
query = ' '.join(query)
file_name = sys.argv[-1]
print(query) 
translator = google_translator()  
translate_text = translator.translate(query, lang_src='ko', lang_tgt='en')  
print(translate_text)
os.system(f"howdoi {translate_text} > {file_name}")