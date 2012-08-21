import urllib2

req = urllib2.Request("http://www.cartoonnetworkasia.com/cha-ching/mv_1.php")
response = urllib2.urlopen(req)
page = response.read()

with open("chaching1.txt", "w") as f:
    f.write(page)


