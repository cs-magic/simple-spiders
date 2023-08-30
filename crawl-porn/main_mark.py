# _*_ coding: utf-8 _*_
# _*_ author: anwenzen _*_
"""
editor: markshawn2020
date: Mar 6, 2023
"""
from argparse import ArgumentParser

from src.core import M3u8Download

if __name__ == '__main__':
    parser = ArgumentParser(description='需要 `ffmpeg` 支持')
    args = parser.parse_args()
    url = args.url
    
    parser.add_argument('url',
        help="index.m3u8 网址, e.g. https://t18.cdn2020.com:12342/video/m3u8/2022/05/21/460ca090/index.m3u8"
    )
    parser.add_argument('-n', '--output-name', help='如为空，则从url中提取')
    
    M3u8Download(
        url,
        max_workers=64,
        num_retries=10,
        # base64_key='5N12sDHDVcx1Hqnagn4NJg=='
    )
