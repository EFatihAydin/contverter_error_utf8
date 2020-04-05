
file = open("./data.txt" , encoding = 'utf-8')
data = file.readlines()

liste=[]

for string in data:
	string=string.replace('Ã¼','ü')
	string=string.replace('ÅŸ','ş')
	string=string.replace('ÄŸ','ğ')
	string=string.replace('Ã§','ç')
	string=string.replace('Ä±','ı')
	string=string.replace('Ã¶','ö')
	string=string.replace('Ãœ','Ü')
	string=string.replace('Ã–','Ö')
	string=string.replace('Ä°','İ')
	string=string.replace('Å','Ş')
	string=string.replace('Ä','Ğ')
	string=string.replace('Ã‡','Ç')
	string=string.replace("ý","ı")
	string=string.replace("ð","ğ")
	string=string.replace("þ","ş")
	string=string.replace("Ð","Ğ")
	string=string.replace("Ý","İ")
	string=string.replace("Þ","Ş")
	string=string.lower()
	liste.append(string)

with open('./dosya_out.txt' , 'w' , encoding = 'utf-8') as fl:
    for i in liste:
        fl.write(str(i))
