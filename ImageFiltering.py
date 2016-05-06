import config
import PIL.Image
from PIL import ImageTk


def filter(canvas, f):
    curr = config.current_image.load()
    x_size = config.current_image.size[0]
    y_size = config.current_image.size[1]

    new_img = PIL.Image.new('RGB', (x_size, y_size))

    for x in range(x_size):
        for y in range(y_size):
            red = green = blue = 0

            for filter_X in range(3):
                for filter_Y in range(3):
                    image_x = (x - 3 / 2 + filter_X + x_size) % x_size
                    image_y = (y - 3 / 2 + filter_Y + y_size) % y_size
                    rgb_val = curr[image_x, image_y]

                    red += rgb_val[0] * f[filter_X][filter_Y]
                    green += rgb_val[1] * f[filter_X][filter_Y]
                    blue += rgb_val[2] * f[filter_X][filter_Y]

            red = min(max(int(red), 0), 255)
            green = min(max(int(green), 0), 255)
            blue = min(max(int(blue), 0), 255)

            new_img.putpixel((x, y), (red, green, blue))

    tk_img = ImageTk.PhotoImage(new_img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = new_img      # Keep reference of current image
