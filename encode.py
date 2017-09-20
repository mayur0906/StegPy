# Program template from assignment 3 used to complete the assignment
# Program template logic designed by Prof. David Levine[UTA].
# Program template written by Jerrin Jacob.
# Rest of program written by Mayur Muralidhar

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

def encode_map_tilde(input_space):
    # get the length of input numbers
    binary = ""
    binary += format((ord(input_space) - ord('~') + 50), '06b')
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
        elif (input_lower[i] == "~"):
            binary = binary + encode_map_tilde(input_lower[i])
    return binary

def decode_output(self,input):
      decoded_string = ""
      length = len(input)
      if(self.padding_bits > 0):
          length = length - (6*self.padding_bits)
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
      return decoded_string


# Enter the image to be used as a carrier here.
carrier = Image.open("mallmap.png")


x_size = carrier.size[0]
y_size = carrier.size[1]



data = carrier.load()

# Enter the message to be hidden here.
message=""

print("Accepted special characters is ' \" <space> . ")
print("Character limit is ",x_size*y_size," for this image")
# for i in range(11):
#     message+='a'
# print(message)

message = input("Enter message : ")

message+='~'
binaryOfMessage = encode_input(message)
print(binaryOfMessage)
x=0
y=0
# print(y_size)
# print(binaryOfMessage)
# print(len(binaryOfMessage))

if(carrier.mode == 'RGBA'):
    for bit in binaryOfMessage:
        # print("x = ",x," y = ",y)
        pixel = bin(data[x, y][0])[2:]
        # print("Before : ",data[x,y])
        # print("(",pixel[-1],",",bit,")")
        if (pixel[-1] != bit):
            # print("Yes",end=",")
            if (bit == '0'):
                # print(int(pixel[:-1]+'0'),2)
                data[x, y] = (int(pixel[:-1] + '0', 2),data[x, y][1],data[x, y][2])
            else:
                data[x, y] = (int(pixel[:-1] + '1', 2),data[x, y][1],data[x, y][2])

                # print("No",end=",")
        # print("After : ",data[x,y])
        x += 1

        if (y == y_size):
            y = 0
            x += 1
        if (x == x_size):
            y += 1
            x = 0

else:

    for bit in binaryOfMessage:
        # print("x = ",x," y = ",y)
        pixel = bin(data[x,y])[2:]
        # print("Before : ",data[x,y])
        # print("(",pixel[-1],",",bit,")")
        if(pixel[-1] != bit):
            # print("Yes",end=",")
            if(bit=='0'):
                # print(int(pixel[:-1]+'0'),2)
                data[x,y] = int(pixel[:-1]+'0',2)
            else:
                data[x,y] = int(pixel[:-1]+'1',2)

            # print("No",end=",")
        # print("After : ",data[x,y])
        x+=1


        if(y==y_size):
            y=0
            x+=1
        if (x==x_size):
            y+=1
            x=0


# Change result file here
carrier.save("blahhh.png")
