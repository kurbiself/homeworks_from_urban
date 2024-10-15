import requests
from PIL import Image

url = 'https://ru.wikipedia.org/wiki'
r = requests.get(url)
print(r.ok)
print(r.text)
print(r.headers)


image = Image.open("Dash.jpg")
rotated_image = image.rotate(60)
rotated_image.save("rotated_Dash.jpg")
print('Формат картинки:',image.format)
coordinates = (100, 40, image.width, image.height)
crop_image = image.crop(coordinates)
crop_image.save("new.jpg")
