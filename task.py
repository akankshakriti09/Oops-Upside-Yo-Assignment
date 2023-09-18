from PIL import Image, ImageDraw, ImageFont
#open image
img1 = Image.open('Input Image/template.jpg')
img2 = Image.open('Input Image/Oops2.jpg')

output_img = img1.copy() #copy image
output_img.paste(img2,(105, 50)) #paste image

# Call draw Method to add 2D graphics in an image
brand_name = ImageDraw.Draw(output_img)
service_name = ImageDraw.Draw(output_img)

# Custom font style and font size
brandFont = ImageFont.truetype('Fonts/PromoTest-Normal-BF63b78802deb68.otf', 33)
serviceFont = ImageFont.truetype('Fonts/EquipExtended W03 Light.ttf', 80)

# Add Text to an image
brand_name.text((50, 796), "Oops Upside Yo Head", font=brandFont, fill=("white"))
service_name.text((100, 920), "Hairstyling In Houston", font=serviceFont, fill=("#4E4945"))

#save output image in folder
output_img.save('Output Image/pillow_img.jpg')

#show output image
output_img.show()
