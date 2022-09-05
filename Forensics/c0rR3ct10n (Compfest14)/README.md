## c0rR3ct10n - Compfest 14

**Desc**: Ngab is an adolescent boy well-known for his ability to solve thousands of hard riddles out there. When he just got back from his pilgrimage, Ngab found a note on his desk. 
>O' dear my apprentice, if thou are back from thy pilgrim, can thou correct this wallpaper maker for me? It is a widescreen-ratio up to full hd one, this should be easy right? Thanks as always. "Damn, you old man" Ngab says.

## Steps:
Given a corrupted .png file. After opening the hex file it appears the bytes of the file are reversed, so we need to reverse it.

After the image is reconstructed, a black-white image is appeared. My first impression is to convert the image into a binary of 0 and 1 with https://www.dcode.fr/binary-image. Then decode the binary to ascii with CyberChef and we get an URL that leads to another .jpg image (m00n.jpg)

![image](https://user-images.githubusercontent.com/63649797/188486204-a398b473-666a-4767-a155-a9e5ab9190f4.png)

The .jpg image is also corrupted and needed another reconstruction. The image is then reconstructed and reformatted again and we got a .png image with no dimension (width-height). We can calculate the width and height through the IHDR's CRC.

![image](https://user-images.githubusercontent.com/63649797/188486312-3870aee5-eaa8-4de3-88d8-d41ab9de08fc.png)

After the dimension is known, we are able to see the image and stegsolve it to get the flag.

Reference:
https://society.cyber.warwick.ac.uk/intakectfmissingbytes/
