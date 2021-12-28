Title: Pernet <br>
Desc: Pernet? hmmm sedikit familiar , coba di teliti dengan baik <br>
Target: https://drive.google.com/file/d/1xYRN-Y9yn7mNbio18MDLF-KuWUeHu1Wq/view <br>
Tools: <br>
- John the ripper <br>
- Fernet decryptor (https://cryptography.io/en/latest/fernet/) <br>

Steps:
1. Use john the ripper for both zip files. I got the password for 'soal.zip' which is 14245. Inside it, there is soal.txt
```
key = C2Atb_FurGUNDKMdogsnrhrGzeKUNoL406KlTI2Ka8U=
ciphertext = gAAAAABhxek5agIt5-kOfBC9nUrJTNcpYjqvoCbh4sDHY4ILltpmVYORK7fX3lIs_Q0CpZWUDnPWPv-FSH8zuHqKEqf6S3JfUQ==
```

For the 'flag.zip', I tried john and hashcat, and unable to get the password

2. Let's decrypt the cipher message. Since the title is "Pernet", maybe we can use Fernet encryption.
Also, I saw the `gAAAAAB` at the beginning. This has to do with the base64 encoding, but Fernet ciphertexts usually always begin with that post-base64 encode. <br>

And.. yep it worked <br>
![image](https://user-images.githubusercontent.com/63649797/147545422-b56349a2-9efb-4201-99d3-9a5f58a802cf.png)

3. Now insert '97932' to flag.zip and flag is captured!

Flag
```
lastctf{y4p_s3d1k1t_bumbu_crypt0_f3rn3t_h3h3}
```
