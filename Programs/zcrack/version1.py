import optparse
import zipfile
from threading import Thread

def extract_zip(zfile,password):
    try:
        zfile.extractall(pwd = password)
        print("[+] Password Tried; Password Found:",password)
    except:
        print("[-] Password Tried; Password Failed:",password)
        pass
def Main():
    parser = optparse.OptionParser("Usage %prog "+\
                                   "-f <zipfile> -d <dictionary>")
    parser.add_option("-f",dest="zname",type="string",\
                      help="specify zip file")
    parser.add_option("-d",dest="dname",type="string",\
                      help="specify dictionary file")
    (options, arg) = parser.parse_args()
    if options.zname == None or options.dname == None:
        print(parser.usage)
    else:
        zname = options.zname
        dname = options.dname
    zfile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip("\n")
        t = Thread(target=extract_zip,args=(zfile, password))
        t.start()
if __name__ == "__main__":
    Main()