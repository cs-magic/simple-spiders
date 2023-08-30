import os

from src.lib.string import get_name_from_url
from src.settings import OUTPUT_DIR

if __name__ == '__main__':
    
    with open("./torrents.txt") as f:
        urls = f.readlines()
        for (index, url) in enumerate(urls, 1):
            name = get_name_from_url(url)
            
            fp = OUTPUT_DIR / (name + ".mp4")
            
            print(fp)
            
            if fp.exists():
                os.rename(fp, OUTPUT_DIR / f"{index}.mp4")
                print("renamed")
