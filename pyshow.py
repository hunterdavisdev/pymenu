import sys, os
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk
import time

root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
canvas = tkinter.Canvas(root,width=w,height=h,bd=0, highlightthickness=0, relief='ridge')
canvas.pack()
canvas.configure(background='black')


def showPIL(pilImage):
    imgWidth, imgHeight = pilImage.size
 # resize photo to full screen 
    ratio = min(w/imgWidth, h/imgHeight)
    imgWidth = int(imgWidth*ratio)
    imgHeight = int(imgHeight*ratio)
    pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)   
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.update_idletasks()
    root.update()
#    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))


dirname = os.path.dirname(__file__)
slides_path = os.path.join(dirname, "slides")
names = os.listdir(slides_path)
print(dirname)

while True:
    for file in names:
        file_path = os.path.join(dirname, file)
        print(file_path)
        print(file)
        if file[-4:] == ".jpg":
            file=Image.open(os.path.join(slides_path, file))
            showPIL(file)

        time.sleep(5)