# Password Strength Calculator

The script shows level of password strength from 1(very weak) to 10(very strong)

# Quickstart

Before checking your password you may to download blacklist.txt file from this repository to folder
with script or create own file(file name at your discretion)
For example, we create blacklist.txt with contents:
>12345
>qwerty
>Password1

Launch on Linux( Python 3.5 ) or Windows as simple
```bash
$ python password_strength.py blacklist.txt
# You will see
Password: *****
Password strength: 5
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)