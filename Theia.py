from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from GeoTrans import *
from ImageFiltering import *
import config


def loadImage():
    filename = filedialog.askopenfilename()

    img = PIL.Image.open(filename)
    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img		# Keep reference to PhotoImage so Python's garbage collector
                                # does not get rid of it making the image dissapear
    config.current_image = img

root = Tk()
root.title("Theia")

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(row=0, column=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

canvas = Canvas(mainframe, width=800, height=600)
canvas.grid(row=0, column=0, rowspan=3)		# put in row 0 col 0 and span 2 rows
canvas.columnconfigure(0, weight=3)

buttons_frame = ttk.Frame(mainframe)
buttons_frame.grid(row=0, column=1, sticky=N)

load_image_button = ttk.Button(buttons_frame, text="Load Image...", command=loadImage)
load_image_button.grid(row=0, column=1, sticky=N+W+E, columnspan=2, pady=10)

#####################
# Rotation Section #
#####################

rotate_button_label = ttk.Label(buttons_frame, text="Rotation").grid(row=1, column=1, columnspan = 2, sticky=N, pady=8)

rotate_left_button = ttk.Button(buttons_frame, text="Rotate Left", command=lambda: rotate(canvas, True))
rotate_left_button.grid(row=2, column=1, sticky=N, padx=5)

rotate_right_button = ttk.Button(buttons_frame, text="Rotate Right", command=lambda: rotate(canvas, False))
rotate_right_button.grid(row=2, column=2, sticky=N, padx=5)
ttk.Separator(buttons_frame, orient=HORIZONTAL).grid(row=3, columnspan=3, sticky=(W, E),pady=8)

#######################
# Translation Section #
#######################

ttk.Label(buttons_frame, text="Translation").grid(row=4, column=1, columnspan=2)

delta_x_label = ttk.Label(buttons_frame, text="X dir.").grid(row=5, column=1)
delta_y_label = ttk.Label(buttons_frame, text="Y dir.").grid(row=5, column=2)

delta_x_entry = ttk.Entry(buttons_frame, width=9)
delta_x_entry.grid(row=6, column=1)
delta_y_entry = ttk.Entry(buttons_frame, width=9)
delta_y_entry.grid(row=6, column=2)

wrap_around = BooleanVar()
wrap_around_check = ttk.Checkbutton(buttons_frame, text="Wrap around", variable=wrap_around)
wrap_around_check.grid(row=7, column=1, columnspan=2, pady=5)

translation_button = ttk.Button(buttons_frame, text="Translate",
                                command=lambda: translate(canvas, int(delta_x_entry.get()),
                                                          int(delta_y_entry.get()), wrap_around.get()))

translation_button.grid(row=8, column=1, columnspan=2, sticky=W+E, pady=5)

ttk.Separator(buttons_frame, orient=HORIZONTAL).grid(row=9, columnspan=3, sticky=(W, E), pady=5)

###################
# Scaling Section #
###################
ttk.Label(buttons_frame, text="Scaling").grid(row=10, column=1, columnspan=2, pady=(0, 8))

scaling_factor = ttk.Entry(buttons_frame, width=5)
scaling_factor.grid(row=11, column=1)

ttk.Label(buttons_frame, text="%").grid(row=11, column=1, sticky=E, padx=8)
scaling_button = ttk.Button(buttons_frame, text="Scale", command=lambda: scale(canvas, int(scaling_factor.get())))
scaling_button.grid(row=11, column=2, sticky=(W, E))

ttk.Separator(buttons_frame, orient=HORIZONTAL).grid(row=12, columnspan=3, sticky=(W, E), pady=10)

####################
# Shearing Section #
####################

ttk.Label(buttons_frame, text="Shearing").grid(row=13, column=1, columnspan=2, pady=(0, 8))
ttk.Label(buttons_frame, text="Lambda").grid(row=14, column=1)

#################################
#     X Direction Shearing      #
#################################
shearing_factor_x = ttk.Entry(buttons_frame, width=5)
shearing_factor_x.grid(row=15, column=1)

shearing_button_x = ttk.Button(buttons_frame, text="X dir. Shear",
                               command=lambda: shear(canvas, float(shearing_factor_x.get()), True))
shearing_button_x.grid(row=15, column=2, sticky=(W, E))

#################################
#     Y Direction Shearing      #
#################################

shearing_factor_y = ttk.Entry(buttons_frame, width=5)
shearing_factor_y.grid(row=16, column=1)

shearing_button_y = ttk.Button(buttons_frame, text="Y dir. shear",
                               command=lambda: shear(canvas, float(shearing_factor_y.get()), False))
shearing_button_y.grid(row=16, column=2, sticky=(W, E))

ttk.Separator(buttons_frame, orient=HORIZONTAL).grid(row=17, columnspan=3, sticky=(W, E), pady=10)

#####################
# Filtering Section #
#####################

ttk.Label(buttons_frame, text="Filtering").grid(row=18, column=1, columnspan=2, pady=(0, 8))

matrix_frame = ttk.Frame(buttons_frame)
matrix_frame.grid(row=19, column=1, columnspan=2)

#########
# ROW 1 #
#########

a11 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a11.grid(row=0, column=0, padx=4, pady=4)

a12 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a12.grid(row=0, column=1, padx=4, pady=4)

a13 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a13.grid(row=0, column=2, padx=4, pady=4)

#########
# ROW 2 #
#########

a21 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a21.grid(row=1, column=0, padx=4, pady=4)

a22 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a22.grid(row=1, column=1, padx=4, pady=4)

a23 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a23.grid(row=1, column=2, padx=4, pady=4)

#########
# ROW 3 #
#########

a31 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a31.grid(row=2, column=0, padx=4, pady=4)

a32 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a32.grid(row=2, column=1, padx=4, pady=4)

a33 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a33.grid(row=2, column=2, padx=4, pady=4)

filter_button = ttk.Button(buttons_frame, text="Filter",
                           command=lambda: filter(canvas, [ [float(a11.get()), float(a12.get()), float(a13.get())],
                                                            [float(a21.get()), float(a22.get()), float(a23.get())],
                                                            [float(a31.get()), float(a32.get()), float(a33.get())] ] ) )

filter_button.grid(row=20, column=1, columnspan=2, sticky=(W, E))
root.mainloop()
