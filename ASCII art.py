import pyfiglet 
data = pyfiglet.figlet_format('python')
print(data)

#Changing fonts
data = pyfiglet.figlet_format('python', font = 'digital')
print(data)

#Get list of fonts
fonts = pyfiglet.FigletFont.getFonts()
fonts = list(fonts)
print("Total Number of Fonts available are : ",len(fonts))
 
#Print 10 font styles...
for font in fonts[:10]:
    print(font)
