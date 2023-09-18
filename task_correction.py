from PIL import Image, ImageDraw, ImageFont

template_img = Image.open('Input Image/template.jpg') #open image

""" Cooridinates of template where we have to paste brand_service_img : upper left corner(100,50), bottom right corner(1080,788)
From Coordinates, we obtain height and width of image we have to paste on template :
Width = 1080-100 = 980 
Height = 788-50 = 738 """

brand_service_img = Image.open('Input Image/BridalMakeup.jpg').resize((980,738))
brand_service_img = Image.open('Input Image/HairStraightning.jpg').resize((980,738))
brand_service_img = Image.open('Input Image/Hairstyle.jpg').resize((980,738))

"""While Pasting we have to take 4 tuples defining the left, upper, right, and lower pixel co-ordinate"""
output_img = template_img.copy() #copy image
output_img.paste(brand_service_img,(100,50,1080,788))


"""(91,938),(970,995)"""
# Call draw Method to add 2D graphics in an image
service_name = ImageDraw.Draw(output_img)

serviceFont = ImageFont.truetype('Fonts/EquipExtended W03 Light.ttf', 80)

# Add Text to an image
service_name.text((100, 920), "Vandana Luthra Curls and Curves (VLCC)", font=serviceFont, fill=("#4E4945"))


output_img.show()