One of the easiest ways we can try to hack the application is by finding hidden features in the application. Sometimes, applications will expose sensitive functionality to users via secret URLs. If we can find such URLs, we might be able to perform actions that a regular user is not supposed to do.
To find hidden URLs, we will use a tool called **dirb**. 

This tool uses a **brute-force approach**, by taking a list of potential page names and testing one by one if they exist in your website. This approach works because people use predictable names numerous times.

```md
dirb http://192.168.1.224/ /usr/share/wordlists/dirb/common.txt
```

Example Explained:

dirb is the tool in kali linux used

http://192.168.1.224/  is the example url used which we will scan.

/usr/share/wordlists/dirb/common.txt  is a dictionary file built-in.

