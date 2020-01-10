from PIL import Image

def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')

# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

kitters = open_image('kitters.jpg')
cattos = open_image('cattos.jpg')

width, height = kitters.size
new = create_image(width, height)
pixels = new.load()

for i in range(width):
    for j in range(height):
        kitter_pixel = get_pixel(kitters, i, j)
        cattos_pixel = get_pixel(cattos, i, j)

        new_red = kitter_pixel[0] - cattos_pixel[0]
        new_green = kitter_pixel[1] - cattos_pixel[1]
        new_blue = kitter_pixel[2] - cattos_pixel[2]

        new_red = max([new_red, 0])
        new_green = max([new_green, 0])
        new_blue = max([new_blue, 0])

        pixels[i, j] = (new_red, new_green, new_blue)

save_image(new, 'diff.png')