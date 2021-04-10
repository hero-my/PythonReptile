
# 增加header
from urllib import request
import base64
import re



from com.hero.main.util_AES import aesDecrypt

key = 'YhG78Plkl56Htrqw'
p = ['x', 'y', 'z', '0', '1', '2', '3', '4', '5']
url = 'https://xppmh104.com/style.php?act=style&aid=528&cid=19500'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

req = request.Request(url=url, headers=headers)
response = request.urlopen(req)
html = response.read().decode('utf-8')
# html = re.search(r'<span\sid=\"txtimgid(.*)</span>', html)
html = re.findall(r'[a-zA-Z0-9=]{37}', html)

txt =''
img = txt[txt.find(' = "') + 4:]
img = aesDecrypt(key, img)

with open('test.png', 'wb') as f:
    f.write(base64.b64decode(img))

