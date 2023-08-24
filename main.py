import os
import json
from PIL import Image
from PIL.ExifTags import TAGS

#Get metadata from picDAT.json file
json_file_path = 'picDAT.json'
with open(json_file_path, 'r') as json_file:
    metadata = json.load(json_file)   
#print(metadata)
#print(metadata["0076"])
#metadata["0076"]["nickname"] = "HI"
#print(metadata)

#For every image in folder
folder_path = './imgs'
#image_names = os.listdir(folder_path)
#short_image_names = list(map(lambda s: s[4:-4],image_names))
#Scan folder for list of images
for file in os.listdir(folder_path):
    image = Image.open(folder_path + "/" + file)
    date = image.getexif()[306]
    imgData = {"name":file,"date":date}    
    if file[4:-4] in list(metadata.keys()):
        metadata[file[4:-4]] = {**metadata[file[4:-4]] ,**imgData} 
    else:
        metadata[file[4:-4]] =  imgData
    image.thumbnail((133,100))
    image.save("./thumbs/"+file)

output_file_path = 'metadata.json'
# Save the dictionary to the specified path as JSON
with open(output_file_path, 'w') as json_file:
    json.dump(metadata, json_file, indent=0)

#print(metadata)

# for tag_id in exifdata:
#     # get the tag name, instead of human unreadable tag id
#     tag = TAGS.get(tag_id, tag_id)
#     data = exifdata.get(tag_id)
#     # decode bytes 
#     if isinstance(data, bytes):
#         data = data.decode()
#     print(f"{tag:25}: {data}")
