import ssl
import urllib.request
import re
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

contents = urllib.request.urlopen("https://chromedriver.chromium.org/downloads", context=ctx).read()
contents = contents.decode("utf-8")

matchobj = re.search("ChromeDriver.+[0-9]\..*", "If you are using Chrome version 95, please download ChromeDriver 95.0.4638.17")
if matchobj:
 result = matchobj.group(0)
else:
 result = ""
result = result.replace("ChromeDriver ","")

f = open("chromedriver.txt", "r")
last_version = f.read()
print("---" + last_version + "---")
print("---" + result + "---")
f.close()
if last_version != result:
    f1 = open("chromedriver.txt", "w+")
    f1.write(result)
    f1.close()
    sys.exit(-1)
