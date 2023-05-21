# BYUCTF 2023
I only did OSINT challenges because when I joined the CTF it was 2 hours left remaining..

## OSINT
### It All Ads Up
People think I'm a sports guy but I really just love all the advertisements! Problem is, I take so many pictures, I can't remember where I got them! Can you find this one for me?
![image](https://github.com/javelineou/ctf-writeups/assets/63649797/981e0cd7-fa9c-4d72-91cd-931a317a12a4)

The pic obviously shows a hockey arena. Google/Duckduckgo the "sponsors/ads + hockey arena", will reveal the arena that is chosen.
```
byuctf{honda_center}
```

### It All Ads Up 2
Aargh! It happened again! I need to know where these ads came from!
![image](https://github.com/javelineou/ctf-writeups/assets/63649797/b5b1e9a2-440b-4476-92b4-3d6ba0ffe1e7)

Same steps as previous challenge.
```
byuctf{Crypto.com_Arena}
```

### Legoclones 1
For some reason completely incomprehensible to mankind, you have become sworn enemies of one of the BYUCTF organizers, Legoclones. In your efforts to defeat him, you have decided to go back to the origins of Legoclones to learn more about him. This is what you know so far:

-   He once claimed that he's been going by the moniker "Legoclones" for over a decade
-   There was a website that he adopted and fostered for about 3 years, based on a specific, niche area of Star Wars

Your goal now is to find this website that he claims as "his". When he retired from the website, he stated he was leaving it in the hands of Commander ????. What was the username of the person he turned the site over to?

https://clonetrooper.fandom.com/wiki/Clone_Wiki:Commanding_Officers

```
byuctf{Blyndblitz}
```

### Legoclones 2
Find fandom wiki first creation date by looking at the oldest history logs

https://clonetrooper.fandom.com/wiki/Clone_Trooper_Wiki?action=history&dir=prev&limit=20

### Legoclones 5
Since I was fairly young, I was still new to OPSEC and made a mistake - I posted my actual height for a short period before taking it down. Can you find it?

The flag will be the day of the month that I posted my height. For example, if it was January 2nd, the flag would be  `byuctf{02}`.

https://clonetrooper.fandom.com/wiki/User:Legoclones?oldid=8871
```
byuctf{22}
```
