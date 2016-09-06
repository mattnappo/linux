import zipfile
def main():
    zipfilename = input("Enter zfile name: ")
    dictionary = input("Enter dictionary: ")
    password = None
    zip_file = zipfile.ZipFile(zipfilename)
    with open(dictionary, 'r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            try:
                zip_file.extractall(pwd=password)
                password = "[+] Password found: %s" % password
            except:
                print("[-] Password failed: %s" % password)
    print (password)