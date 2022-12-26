# niteCTF 2022
niteCTF is a jeopardy style CTF for students interested in cybersecurity. niteCTF is designed to help students explore newer domains in cybersecurity as well as help existing professionals practise their skills. Created by Cryptonite, a student project team of Manipal Institute of Technology.

## > 4dm1n_c0ntR0L (web)
Get admin control in the website somehow
Flag format: nitectf{}

### Steps:
Basic SQL injection. Payload username: ``' or true-- `` password:``a``
```
nitectf{w3nT_1nT0_Th3_s3rV3r}
```

## > Boys (misc/osint)
The new Head of Crime Analytics is named - The Deep. The Deep addresses the Crime team and Cassandra brings cupcakes for the team. They fired most of the staff because of past tweets that were critical of Homelander. Homelander as paranoid as ever believes that the boys has yet another plan to take down Vought International. As one of the members from the few left behind it is upon your shoulders to crack down on the boys' plan to take down Vought by looking into the suspicious

GitHub user who goes by the name sk1nnywh1t3k1d or face Homelander's wrath.

### Steps:
Given a Github profile with 1 repository inside. Checking the commits history to see deleted lines or files.
![commits](https://user-images.githubusercontent.com/63649797/209476423-f8b59335-1aba-4dc5-8bd9-c355da57344a.JPG) 

The bit.ly will redirect us to ``secret_message.wav`` which has a common robot noise. I immediately open my Audacity to see the spectogram.

![audacity](https://user-images.githubusercontent.com/63649797/209476432-5849f3e2-779e-4929-b15d-5fc286a08a34.png) \
The next bitly showed a shuffled image with a red-colored text on it. Unshuffle it manually with photoshop will show ``HUGHIECAMPBELL392@GMAIL.COM`` \
![hughie](https://user-images.githubusercontent.com/63649797/209476437-3c8e8e17-fb07-4e29-a939-949bbd026ec8.png) 

Then I reverse check the email using epieos.com which results a google calendar service that is set to public.
![emailreverse](https://user-images.githubusercontent.com/63649797/209476441-b133c9b8-9b70-418b-849c-a0ff2340948c.JPG) \
![flag](https://user-images.githubusercontent.com/63649797/209476443-fad8a7cf-3065-4542-9493-d0d555547b77.JPG) \
```
niteCTF{v0ught_n33ds_t0_g0_d0wn}
```


## > Travel (misc/osint)
I give you my favourite photo.. Travel back in time for me please..

### Steps:
Given a ``owl.jpg``. Inspect the exif will give ``bit.ly/mytodooolist`` which will redirect to a Google Jamboard.

Duplicate/copy the jamboard to a new file, then drag/slide the first note to see a hidden message behind it.

![jamboard](https://user-images.githubusercontent.com/63649797/209476497-9adfe728-f9e9-4786-946e-a52857751580.JPG)

Since the description and the title points to "travel back in time", it's likely that this refers to web.archive.org. Inspecting the captured site and it will lead to the flag. 

![base64](https://user-images.githubusercontent.com/63649797/209476500-dc9f2ced-9d7b-4c43-8fcb-c2128823095d.JPG)
![flag](https://user-images.githubusercontent.com/63649797/209476504-2aea17fa-2171-4cb5-83e4-e38e2121d76b.JPG)
```
nitectf{y0u_w3nt_b4ck_1n_t1m3}
```

## > Basically, I locked up (crpyto)
Given an encryption file
```
def new_encryption(file_name, password):
  with open(file_name, "rb") as f:
    plaintext = f.read()
  assert(len(password) == 8)
  assert(b"HiDeteXT" in plaintext)
  add_spice = lambda b: 0xff & ((b << 1) | (b >> 7))
  ciphertext = bytearray(add_spice(c) ^ ord(password[i % len(password)]) for i, c in enumerate(plaintext))
  with open(file_name + "_encrypted", "wb") as f:
    f.write(ciphertext)

def new_decryption(file_name, password):
  with open(file_name + "_encrypted", "rb") as f:
    ciphertext = f.read()
  remove_spice = lambda b: 0xff & ((b >> 1) | (b << 7))
  plaintext = bytearray(remove_spice(c ^ ord(password[i % len(password)])) for i, c in enumerate(ciphertext))
  with open(file_name + "_decrypted", "wb") as f:
    f.write(plaintext)

password = REDACTED

new_encryption("Important", password)
new_decryption("Important", password)
```

### Steps:
Change the password value to ``HiDeteXT`` as stated in the encryption function. Run the program and we get the flag.
```
NITE{BrUT3fORceD_y0uR_wAy_iN}
```

## > itsybitsyrsa (crypto)
you have n , e , c . can you figure out the message ?
n = very big modulus (500k chars)
e = 19
c = not so big ciphertext

### Steps:
It is a vulnerability where it happens that m^e^ mod n =  m^e^. 
https://crypto.stackexchange.com/questions/80311/attack-rsa-with-very-big-module-n-and-very-small-e-7
https://github.com/S-H-E-L-L/DeconstructCTF/blob/main/crypto/RSA-2.md
```
nitectf{rsa_can_be_very_adaptable}
```

## > undodge (rev)
Given a .rar file that contains a unity game. The game is classic "catch-the-ball" game and dodge the spike. Each ball caught will earn 1 point. And every 10 points, 1 letter of the flag will given. Also, each point earned, the ball and spike will go faster and faster.

![game](https://user-images.githubusercontent.com/63649797/209476532-c9790a32-2504-445d-a36d-9afca959a0e7.jpg)

### Steps:
After a bit of googling about ``reverse engineering, unity game``, I found a [writeup](https://tripoloski1337.github.io/ctf/2019/09/09/reverse-engineering-unity-game.html) about reversing a unity game.


It shows that we can disassemble and interpret it into high level programming language using a debugger called **[dnSpy](https://github.com/dnSpy/dnSpy)**.

To access the main code/functions, we can open the ``Assembly-CSharp.dll`` with the debugger (located at Undodge/managed/ folder). \
![functions](https://user-images.githubusercontent.com/63649797/209476537-7709e127-e253-4468-8a50-8d439fe66129.JPG)

After take a look all the functions, I can conclude that every 10 points, the Flagchar functions will be called and return a letter. At this point, I can just open the Flagchar function one by one and write the letters but that would be no fun.

So I tried to modify the gameplay and play the modified game. For instance, I found this Spike class which controls the spike gravity. It looks like that gravity of the spike is incremented ``+=`` every time. So, I made it decremented ``-=`` until eventually the spike didn't even show xD.

![spike func](https://user-images.githubusercontent.com/63649797/209476543-a840f368-af82-41c2-b162-8ffc56df0d7c.JPG)

I also found this scoring function where I could change the scoring system.

![scoring func](https://user-images.githubusercontent.com/63649797/209476550-895dae97-378c-45da-99ec-1ed719c406fb.JPG)

I changed the ball scoring system from incremented by 1 ``this.score++``, to by 10 ``this.score+=10``. \
I also removed the ``if spike caught`` logic, so even if I caught the spike, the game is still on.

![scoring edit func](https://user-images.githubusercontent.com/63649797/209476556-e1b53bf8-698a-4bb2-8316-64ced859aeb5.JPG)

Save it. And it's time to play. I just need to collect several ball easily and I got the flag.

![flag](https://user-images.githubusercontent.com/63649797/209476562-c59aac12-5fa8-4508-9ef5-3bda8206e2b3.jpg)

```
niteCTF{_what_a_player__}
```
