<h1 align="center">Discord Bot Template</h1>
<p align="center"><a href="https://github.com/OreoDivision/python-bot-template#about">About</a> ⦿ <a href="https://github.com/OreoDivision/python-bot-template#setup">Setup</a> ⦿ <a href="https://github.com/OreoDivision/python-bot-template#adding-commands">Add Commands</a></p>

## About
This is a bot template to help you get a bot working in no time! This supplyes you with a `.env` file for your token!

## Setup
#### Clone the repo: 
```console
$ git clone https://github.com/OreoDivision/python-bot-template
$ cd python-bot-template
```
#### Install dependencies:
```console
$ pip i -r requirements.txt
```
#### Env values:
Rename [`.env.example`](https://github.com/OreoDivision/python-bot-template/blob/main/.env.example) to `.env` and fill out teh fields
### Edit the help command
Go to [`./cogs/help.py`](https://github.com/OreoDivision/python-bot-template/blob/main/cogs/help.py) to start editing the file to make it yours.
### Finally, start the bot.
```console
$ python3 main.py
```
## Adding Commands
How to add commands:
### Copy the example
Go to [`example.py`](https://github.com/OreoDivision/python-bot-template/blob/main/example.py) and copy its contents.
### Make a new file
Make a new file in the cogs folder. The file has to be named the command name.
### Past
Past the contents of [`example.py`](https://github.com/OreoDivision/python-bot-template/blob/main/example.py) into your new file!
### Code
Now code any code you want in your command