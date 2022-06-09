# Change the "/" to ":" on "file_name" so we can convert to Pascal VOC format

import json

with open('../raw_data/annotations copy.json', 'r') as f:
  data = json.load(f)


for image in data['images']:
	for key, value in image.items():
         if key == 'file_name':
             image[key] = image[key].replace('/',':')


with open('../raw_data/annotations copy.json', "w") as a_file:
    json.dump(data, a_file)
    a_file.close()
