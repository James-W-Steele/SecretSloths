from PIL import Image,ImageColor
image = Image.open("NFTLibrary/"+input("place image name here:"))
imagemanip = image.load()
height = image.size[0]
width = image.size[1]
result = []
x = 0
y = 0
done = 0
def filtre(value):
    if value >254:
        return 254
    if value <1:
        return 1
    return(value)
while done < (height*width):
    pixel = imagemanip[x, y]
    if pixel != (255,255,255,255):
        r = int(filtre(pixel[0]))
        g = int(filtre(pixel[1]))
        b = int(filtre(pixel[2]))
        result2 = [[r, g, b, ((r+g+b)/3), x, y]]
        result += result2
    x+=1
    if x == width:
        x = 0
        y += 1
    done += 1
print(result)