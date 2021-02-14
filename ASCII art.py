import pyfiglet 
data = pyfiglet.figlet_format('python')
print(data)

#changing fonts
data = pyfiglet.figlet_format('python', font = 'digital')
print(data)

#get list of fonts
fonts = pyfiglet.FigletFont.getFonts()
fonts = list(fonts)
print("Total Number of Fonts available are : ",len(fonts))
 
#print 10 font styles...
for font in fonts[:10]:
    print(font)