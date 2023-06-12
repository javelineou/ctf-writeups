# KWCTF 2023

### Welcome (Misc)

Halo, selamat pagi semua peserta KodingWorks League CTF 2023. Selamat mengikuti kompetisi dan tetap semangat !!!

Let's start hacking bruhhh 🔥🔥🔥

Flag: KWCTF{tetap_semangat_dan_sehat_selalu}

### Dollar (Misc)

Mr Crab says: "uang uang aku suka uang 🤑 bantu aku menghitung uang uang ku ini!"

#### Steps
Given a folder which contains a lot of other folders with images of dollars. We can make a script to enumerate all the image files based on its size.
```
import os
path = "/home/kali/Downloads/dollar/dompet"

for i in range(1,35):
    sum = 0
    for filename in os.listdir(path + str(i)):
        folder = "dompet" + str(i) + "/"
        path2 = "/home/kali/Downloads/dollar/" + folder + filename
        size = os.stat(path2).st_size
        
        if size == 427929:
            sum += 50
        elif size == 420419:
            sum += 20
        elif size == 463137:
            sum += 5    
        elif size == 435488:
            sum += 10
        elif size == 379921:
            sum += 2
        elif size == 382596:
            sum += 1
        elif size == 334847:
            sum += 100
    print(sum)

```
Then it outputs a hex code: ``75 87 67 84 70 123 98 52 110 121 52 107 95 100 48 108 49 52 50 95 65 107 117 95 112 117 110 95 115 51 110 52 78 57``, which shows the flag when converted to text.

Flag: KWCTF{b4ny4k_d0l142_Aku_pun_s3n4N9}

### XXI (Misc/OSINT)
Given an image of XXI cinema in one of a shopping mall in Indonesia. The description said that the author left a review about the cinema.
Checking the exif data of the image, we can get the location where the foto taken.
```
Latitude: 6 deg 57' 51.00" S
Longitude: 110 deg 23' 57.20" E
```
Now that we know what mall it is, we can find it on google review and look for the flag.

Flag: KWCTF{W4rmup_d0ang_p4st1_g4mp4ng}

### EZ en be pe (Crypto)
Given an encrypted text. We can simply decode it with CyberChef.

From base64 > from base32 > from hex > from decimal > from octal > from binary.

Flag: KWCTF{pemanasan_dulu_ga_sieee}

### LSBook (Forensic)
Salah satu member grup facebook meme membuat teknik steganografi agar meme yang bersifat sarkasme tidak terdengar oleh oknum:v ,nah bisakah kamu memecahkannya?

#### Step
Given a .wav file that contains some data. The author gave the stego encryption source code to the challenge so we can simply reverse it to decode.
```
import wave
song = wave.open("song_embedded.wav", mode='rb')

# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Extract the LSB of each byte
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

# Convert byte array back to string
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))

# Cut off at the filler characters
decoded = string.split("###")[0]
print("Sucessfully decoded: "+decoded)
song.close()
```
The result is a hex code of a ZIP file. Unfortunately the zip is protected. I tried with john and hashcat but no result. So I checked the challenge again and the .wav again. Then I realize that the .wav is actually a sound of someone speaking in a fast motion. I checked with Audacity and slow down the speed/tempo and I heard the password ``kulkaslgduapintu``.

Flag: FLAG: KWCTF{R0b0t5_4r3_4lw4y5_h3ar1ng_0v3r_y0u}

### History (Forensic)
Given a folders which contains 12.000 QR code image. Let's read it one by one.

```
import os
from PIL import Image
import zbarlight

path = '/home/kali/Downloads/history/'
output_file = '/home/kali/Downloads/historyhex.txt'

for i in range(12832, -1, -1):
    filename = "{:05d}.png".format(i)
    file_path = os.path.join(path, filename)
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as image_file:
            image = Image.open(image_file)
            image.load()
        
        codes = zbarlight.scan_codes(['qrcode'], image)
        
        if codes:
            with open(output_file, 'a') as f:
                f.write(str(codes))
                
    else:
        print(filename, 'does not exist')

```
The result is a hex code of an .mp4 file but in reverse. I found it because the last byte of the hex code contains signature file of .mp4 but reversed. ``mosippytf -> ftypisom (66 74 79 70 69 73 6F 6D)``

Flag: FLAG: KWCTF{Congr4tss_Y0u_H4v3_F1nished_Scann3d}
