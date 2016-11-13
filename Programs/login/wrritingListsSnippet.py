list = [1, 2, 3, 4]
with open("lister.txt", "w") as writer:
    for x in list:
        writer.write(str(x))
print("Done!")

raw = list()