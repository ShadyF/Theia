import config
import PIL.Image
from PIL import ImageTk


def rotate(canvas, left):
    # Get current image and its dimensions
    curr = config.current_image.load()
    x_size = config.current_image.size[0]
    y_size = config.current_image.size[1]

    # Created a new flipped image
    rotated_img = PIL.Image.new('RGB', (y_size, x_size))
    # rotation = np.matrix(( (0, -1), (1, 0) ))

    # Calculate center of rotation
    cx = int(x_size / 2)
    cy = int(y_size / 2)

    # Calculate x and y offset of image in current orientation, used to bring
    # pixels back to (0,0) in the newly created flipped image
    min_x = min((0 - cy) + cx, (y_size - cy) + cx)
    min_y = min(-(0 - cx) + cy, -(x_size - cx) + cy)

    for x in range(x_size):
        for y in range(y_size):
            rgb_val = curr[x, y]        # get (R, G, B) tuple of current image pixel
            x_new = (y - cy) + cx if left else -(y - cy) + cx      # cos(0.5pi) * (x - cx) - sin(0.5pi) * (y - cy) + cx
            y_new = -(x - cx) + cy if left else (x - cx) + cy      # sin(0.5pi) * (x - cx) + cos(0.5pi) * (y - cy) + cy

            # This part is extremely slow
            if y_new-min_y in range(x_size) and x_new-min_x in range(y_size):
                rotated_img.putpixel((x_new-min_x, y_new-min_y), rgb_val)

    tk_img = ImageTk.PhotoImage(rotated_img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = rotated_img      # Keep reference of current image


def translate(canvas, xx, yy, wrap_around):
    curr = config.current_image.load()
    x_size = config.current_image.size[0]
    y_size = config.current_image.size[1]

    new_img = PIL.Image.new('RGB', (x_size, y_size))

    for x in range(x_size):
        for y in range(y_size):
            rgb_val = curr[x, y]
            x_new = x + xx if not wrap_around else (x + xx) % x_size
            y_new = y + yy if not wrap_around else (y + yy) % y_size

            if x_new in range(x_size) and y_new in range(y_size):
                new_img.putpixel((x_new, y_new), rgb_val)

    tk_img = ImageTk.PhotoImage(new_img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = new_img      # Keep reference of current image


def scale(canvas, factor):
    from math import floor
    curr = config.current_image.load()
    x_size = config.current_image.size[0]
    y_size = config.current_image.size[1]

    new_img = PIL.Image.new('RGB', (x_size, y_size))

    # x_ratio = original width / modified width
    # y_ratio = original height / modified height

    scaling_factor = 1 / (factor / 100)

    for x in range(x_size):
        for y in range(y_size):
            px = floor(x * scaling_factor)
            py = floor(y * scaling_factor)
            if px in range(x_size) and py in range(y_size):
                rgb_val = curr[px, py]
                new_img.putpixel((x, y), rgb_val)

    tk_img = ImageTk.PhotoImage(new_img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = new_img      # Keep reference of current image


def shear(canvas, factor, x_shear):
    curr = config.current_image.load()
    x_size = config.current_image.size[0]
    y_size = config.current_image.size[1]
    if x_shear:
        new_img = PIL.Image.new('RGB', (x_size + int(factor * y_size), y_size))
    else:
        new_img = PIL.Image.new('RGB', (x_size, y_size + int(factor * x_size)))

    for x in range(x_size):
        for y in range(y_size):
            rgb_val = curr[x, y]
            x_new = x + int(factor * y) if x_shear else x
            y_new = y if x_shear else y + int(factor * x)
            new_img.putpixel((x_new, y_new), rgb_val)

    tk_img = ImageTk.PhotoImage(new_img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = new_img      # Keep reference of current image
