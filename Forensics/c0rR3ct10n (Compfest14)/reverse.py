#Reverse hex value

filename = "lemaoo.png"
output_filename = "out.png"

f = open(filename, "rb")
s = f.read()
f.close()
f = open(output_filename, "wb")
f.write(s[::-1])
f.close()