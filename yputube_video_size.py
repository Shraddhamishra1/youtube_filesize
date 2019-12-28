import urllib, os
link = "https://www.youtube.com/watch?v=2hcRs3mbCyw"
print ("opening url:", link)
site = urllib.urlopen(link)
meta = site.info()
# print ("Content-Length:", meta.getheaders("Content-Length"))

f = open("/home/shradhha/Desktop/out.txt", "rb")
print ("File on disk:",len(f.read()))
f.close()


f = open("/home/shradhha/Desktop/out.txt", "wb")
f.write(site.read())
site.close()
f.close()

f = open("/home/shradhha/Desktop/out.txt", "rb")
print ("File on disk after download:",len(f.read()))

print ("os.stat().st_size returns:", os.stat("/home/shradhha/Desktop/out.txt").st_size)

if (len(f.read()) > 360000):
	print("Yes Download")
else:
	print("NO")

f.close()
