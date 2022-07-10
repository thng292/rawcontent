import csv

shtml = """<!DOCTYPE html><html><head><title>Answer</title><link rel="stylesheet" href="style.css"></head><body>"""
ehtml = """</body></html>"""

outFile = open("index.html",mode='w',encoding="utf-8")
inFile  = csv.reader(open("Answer.csv",mode='r',encoding="utf-8"))

outFile.write(shtml)

head = next(inFile)
person = []
for row in inFile :
    person.append(row)

for a in person: 
    outFile.write(f'<div class="content"><time>{a[0]}</time><h1>{a[2]}</h1><small>{a[1]}</small>')
    if a[3] :
        outFile.write(f'<h3>{head[3]}</h3><p>{a[3]}</p>')
    if a[4] :
        outFile.write(f'<h3>{head[4]}</h3><p>{a[4]}</p>')
    if a[76] :
        outFile.write(f'<h3>{head[76]}</h3><p>{a[76]}</p>')
    outFile.write(f'</div>')

for i in range(5,78) :
    if i in {75,76} :
        continue
    outFile.write(f'<div class="content"><h2>Về {head[i]}</h2>')
    for a in person :
        if a[i] :
            outFile.write(f'<p>{a[i]}<br> - <strong>{a[2]}</strong></p>')
    outFile.write(f'</div>')

outFile.write(ehtml)
outFile.close()