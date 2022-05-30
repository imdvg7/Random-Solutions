!pip install zipfile36
from zipfile import ZipFile

path_of_your_zip_file = ''
from zipfile import ZipFile
with ZipFile(path_of_your_zip_file, 'r') as z:
  z.extract()
  
#If you want to extract specific file from zip pass it as argment like -
#with ZipFile(path_of_your_zip_file, 'r') as z:
# z.extract('file_you_want_to_extract.extension')
