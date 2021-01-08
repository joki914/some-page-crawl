import requests, os


for i in range(600000,700000):
        msv = 2017000000+i
        url = "https://static.dhcnhn.vn/student?id="+str(msv)
        res = requests.get(url)
        res.raise_for_status()
        imgFile = open(os.path.join('/home/jk914/Haui/K12_2020', os.path.basename(str(msv))), 'wb')
        for hihi in res.iter_content(100000):
                imgFile.write(hihi)
        imgFile.close()



