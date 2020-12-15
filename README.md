# Python

![](img/python.png)

## Content

- **[Projects](#projects)**
- **[Virtual environment](#virtual-environment)**
- **[Install libraries](#install-libraries-from-requirements.txt)**
- **[py file to exe](#py-file-to-exe)**

## Projects

Training with python, here there are a exercises of python made in:

- [HackerEarth challenges](HackerEarth)
- [Some exercises](Exercises)
- [ThePythonChallenge](ThePythonChallenge)
- [A chat between clients using a server](chat)
- [Two ways to transform text to speech](Text_to_speech)
- [Selenium](https://github.com/Kzarama/Selenium_Python)
- [Flask](https://github.com/Kzarama/flask)
- [Django](https://github.com/Kzarama/Django)
- [DDOS attack](ddos)
- [Keylogger](keylogger)
- [Conections of the router](router_conextions)
- [Downloader of music from youtube](youtube_downloader)
- [Games in python](https://github.com/Kzarama/Games_python)
- [Course of data analitics](https://github.com/Kzarama/Analitics)
- [Machine learning](https://github.com/Kzarama/machine_learning)

## Virtual environment

### First method

To create a venv

```bash
python3 -m venv .env
```

### Second method

To create a venv

```bash
virtualenv .env --python=python3.8
```

### To activate venv

#### In linux

```bash
source .env\bin\activate
```

#### In windows

```cmd
.env\Scrips\activate
```

## Install libraries from requirements.txt

```bash
pip install -r requirements.txt
```

```bash
pip freeze > requirements.txt
```

## py file to exe

Install pyinstaller

```bash
pip install pyinstaller
```

Create the exe with

```bash
pyinstaller FILE_NAME.py
```

Options:

- -F, --onefile: to create only one file
- -i, --icon: to add a icon in the exe
