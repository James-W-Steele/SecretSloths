from PIL import Image,ImageColor
lettonum = {'`': 0, '~': 1, '1': 2, '!': 3, '2': 4, '@': 5, '3': 6, '#': 7, '4': 8, '$': 9, '5': 10, '%': 11, '6': 12, '^': 13, '7': 14, '&': 15, '8': 16, '*': 17, '9': 18, '(': 19, '0': 20, ')': 21, '-': 22, '_': 23, '=': 24, '+': 25, '[': 26, '{': 27, ']': 28, '}': 29, '\\': 30, '|': 31, ';': 32, ':': 33, "'": 34, '"': 35, ',': 36, '<': 37, '.': 38, '>': 39, '/': 40, '?': 41, 'q': 42, 'w': 43, 'e': 44, 'r': 45, 't': 46, 'y': 47, 'u': 48, 'i': 49, 'o': 50, 'p': 51, 'a': 52, 's': 53, 'd': 54, 'f': 55, 'g': 56, 'h': 57, 'j': 58, 'k': 59, 'l': 60, 'z': 61, 'x': 62, 'c': 63, 'v': 64, 'b': 65, 'n': 66, 'm': 67, 'Q': 68, 'W': 69, 'E': 70, 'R': 71, 'T': 72, 'Y': 73, 'U': 74, 'I': 75, 'O': 76, 'P': 77, 'A': 78, 'S': 79, 'D': 80, 'F': 81, 'G': 82, 'H': 83, 'J': 84, 'K': 85, 'L': 86, 'Z': 87, 'X': 88, 'C': 89, 'V': 90, 'B': 91, 'N': 92, 'M': 93, ' ': 94}
numtolet = {0: '`', 1: '~', 2: '1', 3: '!', 4: '2', 5: '@', 6: '3', 7: '#', 8: '4', 9: '$', 10: '5', 11: '%', 12: '6', 13: '^', 14: '7', 15: '&', 16: '8', 17: '*', 18: '9', 19: '(', 20: '0', 21: ')', 22: '-', 23: '_', 24: '=', 25: '+', 26: '[', 27: '{', 28: ']', 29: '}', 30: '\\', 31: '|', 32: ';', 33: ':', 34: "'", 35: '"', 36: ',', 37: '<', 38: '.', 39: '>', 40: '/', 41: '?', 42: 'q', 43: 'w', 44: 'e', 45: 'r', 46: 't', 47: 'y', 48: 'u', 49: 'i', 50: 'o', 51: 'p', 52: 'a', 53: 's', 54: 'd', 55: 'f', 56: 'g', 57: 'h', 58: 'j', 59: 'k', 60: 'l', 61: 'z', 62: 'x', 63: 'c', 64: 'v', 65: 'b', 66: 'n', 67: 'm', 68: 'Q', 69: 'W', 70: 'E', 71: 'R', 72: 'T', 73: 'Y', 74: 'U', 75: 'I', 76: 'O', 77: 'P', 78: 'A', 79: 'S', 80: 'D', 81: 'F', 82: 'G', 83: 'H', 84: 'J', 85: 'K', 86: 'L', 87: 'Z', 88: 'X', 89: 'C', 90: 'V', 91: 'B', 92: 'N', 93: 'M', 94: ' '}
def decrypt_text(data):
    x = 3
    result = ''
    while x != (len(data)+3):
        letternums = data[x-3:x]
        if letternums[1] < 48:
            result += numtolet[letternums[0] - letternums[2]]
        else:
            result += numtolet[letternums[0] + letternums[2]]
        x += 3
    return result

def extract_data_from_image(image, height, width):
    result = '' # this function reads the data in base 3 from the given image.
    zero_count = 0
    nums = ["1", "2", "3"]
    for y in range(height):
        for x in range(width):
            pixel = image[x, y]
            if x % 2 == 0:
                reference_r = pixel[0]
                reference_g = pixel[1]
                reference_b = pixel[2]
            if x % 2 != 0:
                count = 0
                if pixel[0] == reference_r:
                    count += 1
                else:
                    index = 0
                if pixel[1] == reference_g:
                    count += 1
                else:
                    index = 1
                if pixel[2] == reference_b:
                    count += 1
                else:
                    index = 2
                if count == 3:
                    zero_count += 1
                    result += "0"
                if count == 2:
                    result += nums[index]
                    zero_count = 0
    while len(result[:-zero_count]) % 12 != 0:
        zero_count -= 1
    return result[:-zero_count]

def decrypt_image(imagefile):
    image = Image.open(imagefile)
    imagemanip = image.load()
    height = image.size[0]
    width = image.size[1]
    data = extract_data_from_image(imagemanip, height, width)
    data = convert_to_decimal(data)
    print(decrypt_text(data))
def convert_to_decimal(data): # takes in a string of numbers to convert to decimal from base 3.
    result = []
    x = 4
    while x != len(data)+4:
        chars = data[x-4:x]
        number = 1 * int(chars[0])
        number += 3 * int(chars[1])
        number += 9 * int(chars[2])
        number += 27 * int(chars[3])
        result.append(number)
        x += 4
    return result
decrypt_image(input("Put directory of image here:"))