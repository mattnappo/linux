import tools, random
while(True):
    a = tools.sha256(str(random.random()))
    print(tools.sha256(str(random.random())) + tools.sha256(str(random.random())) + tools.sha256(str(random.random())) + a[0:12])
