# simple-python-security-tools
##Simple Security tools written in Python


###port_scanner.py usage:

$python3 port_scanner.py -host 192.168.1.2 --ports 1-1024


###xss_scanner.py usage:

$python3 xss_scanner.py
(You will be prompted to enter a valid URL to scan)



###ssh_bruteforce.py usage:

$python3 ssh_bruteforce.py --host 192.168.1.2 -u root -P top_1000_passwords.txt


###zip_bruteforce.py usage:

$python3 zip_bruteforce.py
(You will be prompted to enter a valid file location. It uses top_1000_passwords.txt by default)


###pdf_cracker.py usage:

$python3 pdf_cracker.py
(You will be prompted to enter a valid file location. It uses top_1000_passwords.txt by default)
