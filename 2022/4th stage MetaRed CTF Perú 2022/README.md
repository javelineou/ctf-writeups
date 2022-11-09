#  4th stage MetaRed CTF Perú 2022 Write Up
This isn't a full write up. Only the challenge I remember since they close the CTF site and didn't share it to public.

## > Take my key
Suppose users Alice and Bob enter into a key agreement with p = 101 and g = 17. Suppose. Alice chooses x = 19 and Bob chooses y = 13. Determine the key they will share.

Diffie Hellman key exchange
https://www.dcode.fr/diffie-hellman-key-exchange

## > Variables and more variables
Considere un sistema RSA con p=7, q= 11 and = e=13, encuentre el texto plano correspondiente a c=17.

RSA cipher
https://www.dcode.fr/rsa-cipher

## > Beautiful place to visit in Peru
Do you know the beautiful places that Peru has? I'll give you some clues so you can discover them. A file has been transferred with the list of some interesting places in Peru that you should know. Find out which place we recommend you visit.
Locate a clue that will lead you to discover the chosen place

### Steps
Given a .pcapng file, we can open it using Wireshark. First, we open the hierarchy protocol statistics to see the protocol summaries. 

![image](https://user-images.githubusercontent.com/63649797/200838175-035c2cc3-16b5-430f-8b38-44913842d744.png) <br>

There are 2 interesting protocols here which is HTTP and FTP. After looking through the packets, there is an interesting files in the FTP packets (turismo.zip and a .txt file). Seems like the user uploaded files since there is a ``STOR`` command. We can try to extract the FTP-data by following the TCP stream > show raw -> save as.

![image](https://user-images.githubusercontent.com/63649797/200838225-31433c1c-9e69-4bf4-94ac-febbcd490253.png) <br>

Now we have a protected zip file. Turns out the .txt file is actually the password. So now we can open the zip and the flag is shown.
![image](https://user-images.githubusercontent.com/63649797/200838259-81038efb-fb3f-427d-b89e-426932a84369.png) <br>

## > Popular Peruvian food
Another .pcapng forensic challenge. Similar like before, but instead the it is TELNET packets (which is insecure since it transfers the data in plaintext).

![image](https://user-images.githubusercontent.com/63649797/200838274-87fe400f-8d5c-4cfb-b7e8-8cf65a250c8a.png)<br>

```
Flag: Tallarines_a_la_huancaina
```
