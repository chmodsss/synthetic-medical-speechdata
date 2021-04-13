
with open("mtsamples.txt", 'r') as f:
    data = f.readlines()

data1 = [d for dd in data for d in dd.split('\n')]
data1 = [d.lstrip() for d in data1 if len(d)>1]

dataw = '\n'.join(data1)

with open("mtsamples_new.txt",'w') as f:
    f.write(dataw)
