# Shimamu Bot
A personal discord bot that is in Work in Progress

## Setup
Download the latest `Lavalink.jar` from [here](https://github.com/Frederikam/Lavalink/releases).

Make a new directory to store the binary

Create an `application.yaml` inisde this directory. Example [here](https://github.com/Frederikam/Lavalink/blob/master/LavalinkServer/application.yml.example)

- You shouldn't be required to change anything except for the server address

Open a command line then change to the directory where the `Lavalink.jar` is stored then run the command whenever you want the server to be up:
```
java -jar Lavalink.jar
```

Create a file called `config.py` then copy-paste the following:
```py
token = '' # Your bot's token here
```

## Requirements
- Discord.py
- async-Kirara
- wavelink + a lavalink server
- [aiowiki](https://github.com/Gelbpunkt/aiowiki)
- pywal
- pillow
- beautifulsoup4

