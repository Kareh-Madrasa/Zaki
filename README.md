### What is Zaki?
- Zaki is an ambitious AI bot that I'm making, which is going to support tool calling in the near future, going to be entirely async, and will be my main bot.

### Features as of the 0.0.0 pre-alpha version

### How to configure your bot?

- **1** rename _settings.py.example to just _settings.py
- **2.** insert your bot token and groq api key from the following links:
- **2.1** https://discord.com/developers/applications/123
- **2.2** https://console.groq.com/
- **3** Set your bot's instructions in the _settings.py file

### How to run Zaki?
- Run the following command depending on your OS while in the bot directory

Linux Debian 13 Trixie and Ubuntu 25+
```bash
sudo apt install python3.13-venv && pip install discord groq openai aiosqlite aiohttp --break-system-packages && python main.py
```

Windows 10/11
```powershell
pip install discord groq openai aiosqlite aiohttp --break-system-messages && python main.py
```

### CONTACTS
The only current way to contact me is Discord, my username is: devionn_ 
