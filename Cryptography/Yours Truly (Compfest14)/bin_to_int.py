from Crypto.Util.number import bytes_to_long

with open('Downloads/message.enc', mode='rb') as file:
    bin = file.read()
    dec = bytes_to_long(bin)
    print("decimal:\n", dec)