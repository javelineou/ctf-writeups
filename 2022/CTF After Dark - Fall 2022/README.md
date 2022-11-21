# CTF After Dark - Fall 2022
A quarterly CTF held by ACM Cyber at UCLA to culminate the workshop series, Cyber Academy.

## > When It All Began (OSINT)
Starting off with some detective work... Can you figure out when the domain for ACM Cyber's website was created? Answer will be of the form: flag{YYYY-MM-DD} https://acmcyber.com/

### Step: https://whois.domaintools.com/acmcyber.com
```
flag{2019-09-29}
```
## > Back in My Day (OSINT)
What was the first IP address uclaacm.com was hosted on? Place your answer within flag{}

### Step: https://viewdns.info/iphistory/?domain=uclaacm.com
```
flag{192.64.119.64}
```
## > Beanstalking (OSINT)
Lima Bean is a senior at Rice University. He used to work as a Project Manager for Super Secure Systems, but recently got a job at Brick. What's his current job title?

### Steps:
Duckduckgo dorking with "Lima Bean" and "Super Secure Systems" as exact words filter. We get the flag from a LinkedIn profile.
```
flag{fr0m_beans_t0_bricks}
```
## > Hello There (OSINT)
A short time ago, in an Internet close, close by... a certain Cyber Officer definitely did not create an OSINT challenge that definitely is not hiding on a certain social media site owned by Microsoft. Do show your CTF skills by finding the (hypothetical) flag or do not. There is no try.

### Steps:
Hints from the desc:
1. Site owned by microsoft -> Github or LinkedIn
2. "Cyber Officer" refers to an officer that works at ACM UCLA.
3. The author name was "Laura"

Hence, this leads to a GitHub repo owned by the author. One repo called "definitely-not-an-osint-challenge" looks interesting since it is fit to the description. Looking at the commit's history, we can find the flag.

```
flag{th1s_isn't_th3_fl4g_y0u're_l00king_f0r}
```

## > Pokemon Adventures 1-3 (OSINT)
Given three photos of Pokemon Go maps, the challenge asked to find the building/eatery names that is nearby the photos.
```
PokemonGo 1/3: flag{Anderson_School_of_Management}
PokemonGo 2/3: flag{bomb_shelter}
PokemonGo 3/3: flag{ackerman_student_union}
```
## > Where is my Supersuit? (OSINT)
Where is my [supersuit](https://acmcyber.com/static/files/2b88871584d66cff/secretsuit.png)? (Hints for submission: Enter as flag{street_address}, all lowercase. Separate word with underscores. Use standard street abbreviations (i.e. blvd, ln, dr).)

### Steps:
The challenge is quite ambiguous since it doesn't really tell what the exact challenge is. However, it asked me to enter a street address as a flag.
A bit research about The Incredibles, the road's name that is used in the film is actually the same street where Pixar Studios are in California.
```
flag{1200_park_ave}
```

## > Day and Night (Steg)
Los Angeles is so different and [beautiful](https://acmcyber.com/static/files/7983b9ad984e324b/los_angeles.jpg) at night. The key to taking such beautiful photos is to do it in BLACKANDWHITE, and always point your camera towards the skyline, facing out, I guess.

### Steps:
The "facing out, I guess" refers to OutGuess, and the BLACKANDWHITE refers to the stegkey. Using outguess we can get the result, ``outguess -r los_angeles.jpg flag.txt -k BLACKANDWHITE``
It turns out that the result is a .png file, so we can change the type file into ``flag.png`` and we get a QR code which reveals the flag. \
![image](https://user-images.githubusercontent.com/63649797/203041341-93c1fde4-5ad3-4aab-bb14-5308742f13e2.png)
```
flag{pandas_zebras_and_orcas}
```

## > No Flags?? (File)
This individual known as [megamind](https://acmcyber.com/static/files/51026a428002bf94/megamind.pdf) has gotten quite the ego, he's even taunting the very cool people in Cyber! Show them that we do, in fact, have the inappropriate word that the popular meme mentions!

### Steps:
Given a .pdf file of a megamind meme in a braille pattern. Open it in hex editor and scroll to the most bottom, we get a flag. \
![image](https://user-images.githubusercontent.com/63649797/203041746-0743f043-72aa-415f-9492-71c56b995176.png)
```
flag{no_compan1onship}
```

## > Senobnesieh (steg)
lla ta siht rebmemer t'nod I ???senobnesieh deman retcarahc noteleks suolucidir [siht](https://acmcyber.com/static/files/e8350154bad3f643/senobnesieh.lmao) s'ereht yltnerappa dna dab gnikaerb gnihctawer m'I. [wow](https://github.com/JavDomGom/videostego)

### Steps:
Given a .mp4 video and a github repo of videostego tool, so this is quite straightforward. \
![image](https://user-images.githubusercontent.com/63649797/203041489-bc79d996-0f35-4527-b7e2-a4c24a77cc59.png)
```
flag{newer_mandela_effect_just_dropped}
```

## > Moanin (Steg)
Any true jazzer knows that you're always supposed to listen in mono. I got [this track](https://acmcyber.com/static/files/ff112ae182d2bab0/moanin.wav) from my dad's old records. It's a bit scratched in some spots. Could you help me convert it to mono, and maybe even remove the scratching? (the flag is 1 word, wrap it with flag{})

### Steps:
Given a .wav file of a music. As stated in the desc, it is a stereo music and we need to split it into 2 mono channels. The "scratch in some spots" led me to the next hint which is to show it into spectogram. Thus, we can see a word that is cut in a half. Combine both parts of word from both mono channels, we can see the word/flag. \

![image](https://user-images.githubusercontent.com/63649797/203041794-c34b77c8-7af0-4314-a7c1-9c78e1b1085a.png)
```
flag{groanin}
``` 
