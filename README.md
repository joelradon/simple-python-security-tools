
# simple-python-security-tools

## Table of contents
* [Port Scanner](#port-scanner)
* [XSS Scanner](#xss-scanner)
* [SSH Brute Force](#ssh-brute-force)
* [Zip Password Cracker](#zip-passwsord-cracker)
* [PDF Password Cracker](#pdf-password-cracker)


## Port Scanner

This tool is used to scan for open ports on a host or range of IPs

```
python3 port_scanner.py -host 192.168.1.2 --ports 1-1024
```

## XSS Scanner

This tools is used to scan websites for XSS weaknesses. It also makes sure the host is up and has no issues like certificates

```
python3 xss_scanner.py
```

(You will be prompted to enter a valid URL to scan)
	
## SSH Brute Force

This tool performs brute force atttempts via ssh. (It uses top_1000_passwords.txt by default)

```
python3 ssh_bruteforce.py --host 192.168.1.2 -u root -P top_1000_passwords.txt
```


## Zip Password Cracker

This tool use a dictionary attack to crack passwords on zip files. (You will be prompted to enter a valid file location. It uses top_1000_passwords.txt by default)

```
python3 zip_bruteforce.py
```


## PDF Password Cracker

This tool use a dictionary attack to crack passwords on pdf files. (You will be prompted to enter a valid file location. It uses top_1000_passwords.txt by default)


```
$python3 pdf_cracker.py
````
