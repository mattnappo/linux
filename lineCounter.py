import os
global ln_cnt
ln_cnt = 0
def file_len(fname):
    global ln_cnt
    print(fname + "\n")
    try:
        with open(fname, "r") as f:
            for i, l in enumerate(f):
                pass
        ln_cnt = ln_cnt + i + 1
    except UnicodeDecodeError:
        print("unreadable file")

def looper(directory):
    files = os.listdir(directory)
    for x in range(len(files)):
        f = files[x]
        if os.path.isdir(directory + "/" + f) == True:
            print(f + " is a dir")
            looper(directory + "/" + f)
        else:
            print("\n\nDIR::" + directory + "\n\n")
            file_len(directory + "/" + f)
            print(f + " counted")
            print("[+] " + str(ln_cnt))
root = "new"
looper(root)
print(ln_cnt)
