import requests 
from rich import print
import os
import shutil 
import datetime
import json

INFO = '[[b green]+[/ b green]]'
WARNING = '[[b yellow]+[/b yellow]]'
ERROR = '[[b red]+[/b red]]'

def main():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    folder = f'hs_notion_backup_{timestamp}'

    os.mkdir(folder)

    headers = {
      'Authorization': f'Bearer {YOUR_INTEGRATION_TOKEN}',
      'Notion-Version': '2022-06-28',
      'Content-Type': 'application/json',
    }

    print(f"{INFO} Making request to notion API...")
    response = requests.post('https://api.notion.com/v1/search', headers=headers)
    print(f"{INFO} Done")

    if response.status_code != 200: 
        print(f"{ERROR} Request to notion API failed!")
        # TODO: Maybe also let people on discord know through another integration 
        return 


    for block in response.json()['results']:
        print(f"{INFO} Writing data...")
        with open(f'{folder}/{block["id"]}.json', 'w') as file:
            file.write(json.dumps(block))

        child_blocks = requests.get(
            f'https://api.notion.com/v1/blocks/{block["id"]}/children',
            headers=headers,
        )

        if child_blocks.json()['results']:
            os.mkdir(folder + f'/{block["id"]}')
            for child in child_blocks.json()['results']:
                with open(f'{folder}/{block["id"]}/{child["id"]}.json', 'w') as file:
                    file.write(json.dumps(child))
    print(f"{INFO} Done")
    print(f"{INFO} Creating archive...")
    
    archive = shutil.make_archive(f"hs_notion_backup_{timestamp}", folder, format="gztar")

    print(f"{INFO} Done, cleaning up...")
    os.rmdir(folder)

if __name__ == "__main__":
    main()
