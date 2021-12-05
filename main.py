from PIL import Image
import os

for image in os.listdir('./images'):
    print(str(image).split('.'))
    name = str(image).split('.')[0]
    image = Image.open('./images/'+image)

    newimage = image.resize((500, 500))
    newimage.save('./resized/' + name + '_500.jpg')
