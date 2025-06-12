# Snort Challenge - The Basics

> **Date**: 2025-05-29<br>
> **Categories**: SOC | Tool | Sniffing | Analyzing<br>
> **Difficulty**: ~~Unknown~~ | ~~Easy~~ | Medium | ~~Hard~~ <br>
> **Reference**: https://tryhackme.com/room/snortchallenges1<br>

--- 

## Summary
In this challenge, different tasks had to be solved with Snort.


---

## Tasks
This challenge deals with the creation of Snort rules in different chapters.

### Writing IDS Rules (HTTP)
#### Question
> Navigate to the task folder and use the given pcap file. Write a rule to detect all TCP packets from or to port 80.<br>
> *What is the number of detected packets you got?*

#### Approach
I created the following rule:

```alert tcp any any <> any 80 (msg: "HTTP traffic detected"; sid:1000001; rev:1;)```

Then I executed following command:

```snort -r mx-3.pcap -c local.rules -A full -l .```

![Result](screenshots/1_writing_ids_rules_(http)_screenshot_2.png)

#### Answer
> 164
--- 

#### Question
> Investigate the log file.<br>
> *What is the destination address of packet 63?*

#### Approach
In the last question, a log file was created, which is read in with snort as follows. I have set the parameter `-n 63` so that I can examine the 63rd packet without a long search:

```snort -r snort.log.1748543592 -n 63```

![Result](screenshots/1_writing_ids_rules_(http)_screenshot_3.png)

#### Answer
> 216.239.59.99
---

#### Question
> Investigate the log file.<br>
> *What is the ACK number of packet 64?*

#### Approach
```snort -r snort.log.1748543592 -n 64```

![Result](screenshots/1_writing_ids_rules_(http)_screenshot_4.png)

#### Answer
>0x2E6B5384
---

#### Question
> Investigate the log file.<br>
> *What is the SEQ number of packet 62?*

#### Approach
```snort -r snort.log.1748543592 -n 62```

![Result](screenshots/1_writing_ids_rules_(http)_screenshot_5.png)

#### Answer
>0x36C21E28
---

#### Question
> Investigate the log file.<br>
> *What is the TTL of packet 65?*

#### Approach
```snort -r snort.log.1748543592 -n 65```

![Result](screenshots/1_writing_ids_rules_(http)_screenshot_6.png)

#### Answer
> 128
---

#### Question
> Investigate the log file.<br>
> *What is the source IP of packet 65?*

#### Approach
```snort -r snort.log.1748543592 -n 65```

![Result](screenshots/1_writing_ids_rules_(http)_screenshot_7.png)

#### Answer
> 145.254.160.237
---

#### Question
> Investigate the log file.<br>
> *What is the source port of packet 65?*

#### Approach
```snort -r snort.log.1748543592 -n 65```

![Result](screenshots/1_writing_ids_rules_(http)_screenshot_8.png)

#### Answer
> 3372
---

### Writing IDS Rules (FTP)
#### Question
> Navigate to the task folder. Use the given pcap file.<br>
> Write a **single** rule to detect **all TCP port 21**  traffic in the given pcap.<br>
> *What is the number of detected packets?*

#### Approach
I created the following rule:

```alert tcp any any <> any 21 (msg: "FTP traffic detected"; sid:1000001; rev:1;)```

Then I executed the following command:

```snort -r mx-3.pcap -c local.rules -A full -l .```

![Rule FTP](screenshots\2_writing_ids_rules_(ftp)_screenshot_1.png)

#### Answer
> 307
---

#### Question
> Investigate the log file.<br>
> *What is the FTP service name?*

#### Approach
At first I tried reading the generated log from the previous question and ```grep``` the Keyword *ftp* like this:

```snort -r snort.log.1748544782 | grep - i "ftp"```

I didn't receive any useful output. That's why I tried to use ```strings``` and ```grep``` to analyze the logfile for the *ftp* keyword:

```strings snort.log.1748544782 | grep -i "ftp"```

Then I received the following output:

![Result](screenshots\2_writing_ids_rules_(ftp)_screenshot_2.png)

#### Answer
> Microsoft FTP Service
---

#### Question
> **Clear the previous log and alarm files.** <br>
Deactivate/comment on the old rules.<br>
Write a rule to detect failed FTP login attempts in the given pcap.<br>
> *What is the number of detected packets?*

#### Approach
You can write snort rules that detects content within the packets. Since ftp traffic is not encrypted it is easy to read the communication between server and client. I researched for the ftp response code for a failed login attempt, which is ```530```.

So the new snort rule I created looks like this:
```alert tcp any any <> any 21 (msg: "FTP login attempt failed"; content: "530"; sid:1000001; rev:1;)```

Then I used the newly created rule on the given pcap file:

```snort -r ftp-png-gif.pcap -c local.rules -A full -l .```

Then I received the following output:

![Result](screenshots\2_writing_ids_rules_(ftp)_screenshot_3.png)

#### Answer
> 41
---

#### Question
> **Clear the previous log and alarm files.**<br>
> Deactivate/comment on the old rule.<br>
> Write a rule to detect successful FTP logins in the given pcap.<br>
> *What is the number of detected packets?*

#### Approach
Similar to the previous task I researched for the ftp response code of a successful login attempt, which is ```230```.

So the new snort rule I created looks like this:
```alert tcp any any <> any 21 (msg: "FTP login successful"; content: "230"; sid:1000001; rev:1;)```

Then I used the newly created rule on the given pcap file:

```snort -r ftp-png-gif.pcap -c local.rules -A full -l .```

![Result](screenshots\2_writing_ids_rules_(ftp)_screenshot_4.png)

#### Answer
> 1
---

#### Question
> **Clear the previous log and alarm files.**<br>
> Deactivate/comment on the old rule.<br>
> Write a rule to detect FTP login attempts with a valid username but no password entered yet.<br>
> *What is the number of detected packets?*

#### Approach
The ftp response code for the given scenario is ```331```.

```alert tcp any any <> any 21 (msg: "FTP valid username, no password"; content: "331"; sid:1000001; rev:1;)```

Then I used the newly created rule on the given pcap file:

```snort -r ftp-png-gif.pcap -c local.rules -A full -l .```

![Result](screenshots\2_writing_ids_rules_(ftp)_screenshot_5.png)

#### Answer
> 42
---

#### Question
> **Clear the previous log and alarm files.**<br>
> Deactivate/comment on the old rule.<br>
> Write a rule to detect FTP login attempts with the "Administrator" username but no password entered yet.<br>
> *What is the number of detected packets?*

#### Approach
Like before I just added the additional content keyword **Administrator**.

```alert tcp any any <> any 21 (msg: "FTP valid username, no password"; content: "Administrator"; content: "331"; sid:1000001; rev:1;)```

Then I used the newly created rule on the given pcap file:

```snort -r ftp-png-gif.pcap -c local.rules -A full -l .```

![Result](screenshots\2_writing_ids_rules_(ftp)_screenshot_6.png)

#### Answer
> 7
---

### Writing IDS Rules (PNG)
#### Approach

### Writing IDS Rules (Torrent Metafile)
#### Approach

### Troubleshooting Rule Syntax Errors
#### Approach

### Using External Rules (MS17-010)
#### Approach

### Using External Rules (Log4j)
#### Approach



---

## Tools and commands used
_TODO: List tools
