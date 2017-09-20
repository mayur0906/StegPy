# Program template from assignment 3 used to complete the assignment
# Program template logic designed by Prof. David Levine[UTA].
# Program template written by Jerrin Jacob.
# Rest of program written by Mayur Muralidhar 1001434196

from PIL import Image


# to encode string to decimal to binary
def encode_map_string(input_string):
    # get the length of the input string
    length = len(input_string)
    binary = ""
    # looping through the length of string
    for i in range(0, length):
        # ord is to get the ASCII value of input string negate it the value of a and add 1 to it
        # format is to get the output in 6 bit format for your block
        binary += format((ord(input_string[i]) - ord('a') + 1), '06b')
    return binary

    # to encode numbers to decimal
def encode_map_numbers(input_numbers):
    # get the length of input numbers
    length = len(input_numbers)
    binary = ""
    for i in range(0, length):
        binary += format((ord(input_numbers[i]) - ord('0') + 27), '06b')
    return binary

def encode_map_period(input_period):
    # get the length of input numbers
    binary = ""
    binary += format((ord(input_period) - ord('.') + 37), '06b')
    return binary

def encode_map_space(input_space):
    # get the length of input numbers
    binary = ""
    binary += format((ord(input_space) - ord(' ') + 38), '06b')
    return binary

def encode_map_hiphen(input_space):
    # get the length of input numbers
    binary = ""
    binary += format((ord(input_space) - ord('-') + 39), '06b')
    return binary

def encode_map_single_quote(input_space):
    # get the length of input numbers
    binary = ""
    binary += format((ord(input_space) - ord('\'') + 40), '06b')
    return binary

def encode_map_double_quote(input_space):
    # get the length of input numbers
    binary = ""
    binary += format((ord(input_space) - ord('"') + 41), '06b')
    return binary

def encode_input(input):
    input_lower = input.lower()
    length = len(input)
    binary = ""
    for i in range(0,length):
        if(input_lower[i].isalpha()):
            binary = binary + encode_map_string(input_lower[i])
        elif(input_lower[i].isdigit()):
            binary = binary + encode_map_numbers(input_lower[i])
        elif(input_lower[i].isspace()):
            binary = binary + encode_map_space(input_lower[i])
        elif(input_lower[i] == "."):
            binary = binary + encode_map_period(input_lower[i])
        elif (input_lower[i] == "-"):
            binary = binary + encode_map_hiphen(input_lower[i])
        elif (input_lower[i] == "'"):
            binary = binary + encode_map_single_quote(input_lower[i])
        elif (input_lower[i] == "\""):
            binary = binary + encode_map_double_quote(input_lower[i])
    return binary

def decode_output(input):
      decoded_string = ""
      length = len(input)
      for i in range(0,length,6):
          number = int(input[i:i+6],2)
          if(number<27):
              decoded_string = decoded_string + chr(64+number)
          elif(number<37):
              decoded_string = decoded_string + chr(21+number)
          elif(number==37):
              decoded_string = decoded_string + chr(46)
          elif(number==38):
              decoded_string = decoded_string + chr(32)
          elif(number==39):
              decoded_string = decoded_string + chr(45)
          elif(number==40):
              decoded_string = decoded_string + chr(39)
          elif(number==41):
              decoded_string = decoded_string + chr(34)
          elif(number==50):
              decoded_string = decoded_string + chr(126)
      return decoded_string

def check_tilde(bin_text):
    if(int(bin_text,2)==50):
        return True
    else:
        return False

# Enter file name of image with hidden text here

carrier = Image.open("blahhh.png")



x_size = carrier.size[0]
y_size = carrier.size[1]



data = carrier.load()




binaryMessage = ""
textMessage = ""
x=0
y=0

# for i in range(10):
#     print(data[x,y],end=",")
#     x+=1


# for y in range(y_size):
#     for x in range(x_size):
#         binaryMessage+=bin(data[x,y])[-1]

if(carrier.mode == 'RGBA'):

    for i in range(x_size * y_size):

        binaryMessage += bin(data[x, y][0])[-1]
        x += 1
        if (x == x_size):
            x = 0
            y += 1


else:

    for i in range(x_size*y_size):

        binaryMessage += bin(data[x,y])[-1]
        x+=1
        if(x==x_size):
            x=0
            y+=1

textMessage = decode_output(binaryMessage)

print("Encoded data is :",end=" ")

for alphabet in textMessage:
    if(alphabet == '~'):
        break
    print(alphabet,end="")
print("")


# for x in range(x_size):
#     for y in range(y_size):
#         data[x,y] = 0

# carrier.save("blah.gif")
