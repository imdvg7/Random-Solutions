!pip install tk
!pip install zipfile36
from tkinter import filedialog
import   os
from zipfile import ZipFile

def get_xml_data(apk):
    zip_file = 'test.zip'
    os.rename(apk,zip_file)
    from zipfile import ZipFile
    with ZipFile(zip_file, 'r') as z:
        z.extract('AndroidManifest.xml')
    
    #enoding = 'unicode_escape'
    with open('AndroidManifest.xml', 'r', encoding='unicode_escape') as f:
        lines = f.read()
    return lines

def openFile(apk):
    data = get_xml_data(apk)
    return data

 
apk = filedialog.askopenfilename()
metadata = openFile(apk)
print(f'Android Manifest File : {data}')
#Try to run this file in folder where apk is stored
