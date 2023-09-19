from PIL import Image, ImageDraw, ImageFont
import math
import tkinter
from tkinter import filedialog 
tkinter.Tk().withdraw() #close the root window
in_path = filedialog.askopenfilename()
img=Image.open(in_path)

template_img = Image.open('Template Image/template.jpg') #open image

""" Cooridinates of template where we have to paste brand_service_img : upper left corner(100,50), bottom right corner(1080,788)
From Coordinates, we obtain height and width of image we have to paste on template :
Width = 1080-100 = 980 
Height = 788-50 = 738 """
brand_service_img=img.resize((980,738))
new_template_img = template_img.copy() #copy image
new_template_img.paste(brand_service_img,(100,50,1080,788)) #paste image
# new_template_img.show()
#output_img.show()

"""To input text over template"""

def create_image(size, bgColor, message, font, fontColor):
    W, H = size
    image = Image.new('RGB', size, bgColor)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)/2, (H-h)/2), message, font=font, fill=fontColor)
    return image

"""(0,788),(432,852)
Width = 432-0 = 432
Height = 852-788 = 64
"""
brandFont = ImageFont.truetype('Fonts/PromoTest-Normal-BF63b78802deb68.otf', 32)
# brand_name = 'Oops Upside Yo Head' #For Hairstyle Image
# brand_name = 'Vandana Luthra Curls and Curves-VLCC' #For BridalMakeup Image
# brand_name = "LOreal" #For HairStraightening Image
brand_name = input("Enter brand name: ")
BrandNameImage = create_image((432,64), '#DFCAD1', brand_name, brandFont,'white')
BrandNameImage.save('Template Image/brand_name_img.jpg')
# BrandNameImage.show()

template_img2= Image.open('Template Image/template2.jpg') #open image
newBrandNameImage = Image.open('Template Image/brand_name_img.jpg') 
# newBrandNameImage.show()
brand_template_img = template_img2.copy() #copy image
"""While Pasting we have to take 4 tuples defining the left, upper, right, and lower pixel co-ordinate"""
brand_template_img.paste(newBrandNameImage,(0,788,432,852))
brand_template_img.save('Template Image/brandTemplate.jpg')
# brand_template_img.show()

"""(0,852),(1080,1080)
Width = 1080-0 = 1080
Height = 1080-852 = 228
"""
serviceFont = ImageFont.truetype('Fonts/EquipExtended W03 Light.ttf', 80)
# service_name = 'Hairstyling In Houston' #For Hairstyle Image
# service_name = 'Bridal Makeup' #For BridalMakeup Image
# service_name = "Permanent Hair Straightening" #For HairStraightening Image
service_name = input("Enter service name: ")
ServiceNameImage = create_image((1080,228), 'white', service_name, serviceFont, '#4E4945')
ServiceNameImage.save('Template Image/service_name_img.jpg')
# ServiceNameImage.show()

template_img3 = Image.open('Template Image/brandTemplate.jpg') #open image
newServiceNameImage = Image.open('Template Image/service_name_img.jpg')
# newServiceNameImage.show()
service_template_img = template_img3.copy() #copy image
"""While Pasting we have to take 4 tuples defining the left, upper, right, and lower pixel co-ordinate"""
service_template_img.paste(newServiceNameImage,(0,852,1080,1080))
service_template_img.save('Template Image/serviceTemplate.jpg')
service_template_img.show()


