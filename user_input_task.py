from PIL import Image, ImageDraw, ImageFont
import tkinter
from tkinter import filedialog 
tkinter.Tk().withdraw() #close the root window
in_path = filedialog.askopenfilename()
img=Image.open(in_path)

template_img = Image.open('Input Image/template.jpg') #open image

""" Cooridinates of template where we have to paste brand_service_img : upper left corner(100,50), bottom right corner(1080,788)
From Coordinates, we obtain height and width of image we have to paste on template :
Width = 1080-100 = 980 
Height = 788-50 = 738 """
brand_service_img=img.resize((980,738))
output_img = template_img.copy() #copy image
output_img.paste(brand_service_img,(100,50,1080,788)) #paste image
output_img.show()