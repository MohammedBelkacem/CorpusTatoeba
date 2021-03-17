
f= open("kab_sentences_detailed.tsv",encoding='utf-8')

kabfr=open("C:/tal/tatobapairs/sentencesber.csv","w+",encoding='utf-8')


i=0
line=""
users=[]
for line in f:

        values = line.split("\t")
        #print (values)
        if values[3] not in users:
            users.append(values[3])

f.close()
kabfr.close()
print(users)
for user in users:
    kab=open(user+".txt","w+",encoding='utf-8')
    for adur in open("kab_sentences_detailed.tsv",encoding='utf-8'):
        values = adur.split("\t")
        if user==values[3]:
            kab.write(values[2]+"\n")
    kab.close()
    #exit()
