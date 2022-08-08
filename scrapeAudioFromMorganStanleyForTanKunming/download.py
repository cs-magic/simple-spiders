import requests

# ----------------------------------------
# downloading a specific audio file from morgan stanley
# for Tan Kunming, by Nan Chuan， 2021-12-22
# ----------------------------------------


# ----------------------------------------
# missing some heads usually doesn't affect, here is for a real simulation just copied all from chrome
# ----------------------------------------
headers_str = '''DNT: 1
Referer: https://www.morganstanley.com/
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'''
headers_dict = dict(i.split(": ", 1) for i in headers_str.splitlines())


# ----------------------------------------
# output name is arbitrary(including file suffix), the only one concern is to save via 'wb', i.e. binary format
# the max step differs according to file itself, you need to have a look at file source, along with the real file download address
# ----------------------------------------
output_file = "download.ts"
max_steps = 20
with open(output_file, 'wb') as f:
    for step in range(1, max_steps+1):
        print(f'downloading segament{step}' )
        url = f'https://bcbolt446c5271-a.akamaihd.net/media/v1/hls/v4/clear/644391012001/a1fe6e0d-7378-474f-b811-e0acf2351a3b/ab901fc0-06cc-46f1-b75d-d344123d3550/5x/segment{step}.ts?' \
              'akamai_token=exp=1640180615~acl=/media/v1/hls/v4/clear/644391012001/a1fe6e0d-7378-474f-b811-e0acf2351a3b/ab901fc0-06cc-46f1-b75d-d344123d3550/*~hmac=a664ad96f0313123ccc94666a07761097863c3609fbc8e90b60494b951f42b55'

        res = requests.get(url, headers=headers_dict)
        f.write(res.content)

# ----------------------------------------
# the final file generated still need to be converted to final target format via some tools, like:
# https://www.aconvert.com/audio/m2ts-to-mp3/
# ----------------------------------------