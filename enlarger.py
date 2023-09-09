from PIL import Image,ImageColor
image2 = Image.new(mode="RGB", size=(720, 720), color=(0,0,0))
image = Image.open(input("put name here:"))
imagemanip = image.load()
imagemanip2 = image2.load()
def make_image_viewable(image, image2, width, length):
    x = 0
    y = 0
    num = 0
    p=0
    l=0
    rang = width*length
    while num < rang:
        z = 0
        pixel = image[x,y]
        while z != 30:
            c = 0
            while c != 30:
                image2[p+z,l+c] = (pixel[0],pixel[1],pixel[2])
                c+=1
                
            z+=1
            
        x += 1
        p+=30
        if x == width:
            y += 1
            p=0
            l+=30
            x = 0
        num += 1
make_image_viewable(imagemanip, imagemanip2, image.size[0], image.size[1])
image2.save("enlarged sloth.png")