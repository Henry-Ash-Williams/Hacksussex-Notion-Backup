# HackSussex Notion Backup 


<p align="center">
    <img width="20%" src="https://raw.githubusercontent.com/Henry-Ash-Williams/Hacksussex-Notion-Backup/master/assets/HackSussex-Circle-Trans-Grad-Ring.png">

![Discord](https://img.shields.io/discord/611921273932611595?style=flat-square&logo=discord&logoColor=%23eee&link=https%3A%2F%2Fdiscord.gg%2FnhVwrBs8uh&label=Join%20our%20Discord%20)
</p>

Backup the Hacksussex notion page to a compressed tar archive. 

## Setup 

1. Clone the repository 

    `$ git clone git@github.com:Henry-Ash-Williams/Hacksussex-Notion-Backup`

    `$ cd Hacksussex-Notion-Backup`

2. Start the virtual environment 

    `$ python3 -m venv [venv name]`

    `$ source [venv name]/bin/activate` 

3. Install dependencies 

    `$ pip3 install -r requirements.txt`

4. Set environment variables 

    `$ echo "NOTION_BEARER_TOKEN=[notion integration token] > .env`

5. Run the script 

    `$ python3 notion-backup-script.py `
