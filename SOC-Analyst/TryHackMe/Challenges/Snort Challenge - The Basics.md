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

![alt alert tcp any any <> any 80 (msg: "HTTP traffic detected"; sid:1000001;rev:1)](screenshots/1_writing_ids_rules_(http)_screenshot_1.png)

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
#### Approach

### Writing IDS Rules(PNG)
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
