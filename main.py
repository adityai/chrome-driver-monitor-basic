import ssl
import urllib.request
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

contents = urllib.request.urlopen("https://chromedriver.storage.googleapis.com/LATEST_RELEASE", context=ctx).read()
contents = contents.decode("utf-8")

f = open("/home/cabox/chromedriver.txt", "r")
last_version = f.read()
print("---" + last_version + "---")
print("---" + contents + "---")
f.close()
if last_version != contents:
    f1 = open("/home/cabox/chromedriver.txt", "w+")
    f1.write(contents)
    f1.close()
    sys.exit(-1)