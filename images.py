from PIL import Image
import os
def convert(extension):
    image1=Image.open('sapmle.jpg')
    #image1.show()
    image1.save('sample.{ext}'.format(ext=extension))


#for converting more than one file to different extension
def morethanone():
    for f in os.listdir('.'):
        #check whether the files in the current directory ends with .jpg
        if f.endswith('.jpg'):
            #opens the file, splits the filename and the file extension into different variables 
            i=Image.open(f)
            fn,text=os.path.splitext(f)
            i.save('pngs/{}.png'.format(fn))    #saves the image in the png format

convert('png')
convert('gif')