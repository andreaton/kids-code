import os

path = chap_name

if not os.path.exists(path):
    os.makedirs(path)

filename = img_alt + '.jpg'
with open(os.path.join(path, filename), 'wb') as temp_file:
    temp_file.write(buff)