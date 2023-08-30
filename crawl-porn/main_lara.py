from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool


from src.core import M3u8Download


def process(url, name: str=None):
    print("started task: ", url)
    M3u8Download(
        url,
        name,
        max_workers=64,
        num_retries=10,
        # base64_key='5N12sDHDVcx1Hqnagn4NJg=='
    )


def main():
    with open("./torrents.txt") as f:
        urls = [i for i in f.readlines() if i]
    
    with ProcessPoolExecutor(max_workers=12) as executor:
        futures = {executor.submit(process, url, format(i, "02d")) for i, url in enumerate(urls, 1)}
    
    for future in futures:
        print(f"Task {future.result()} is complete.")


if __name__ == "__main__":
    main()
