import urllib
data = urllib.request.urlopen("http://www.mattnappo.com/code/workspace/Hidden/access.py")
replacements = ( ('hacker','haxor'), ('elite','eleet'), ('a','4'), ('e','3'),
                 ('l','1'), ('o','0'), ('t','+') )
my_string = data.readlines()
new_string = my_string
for old, new in replacements:
    new_string = new_string.replace(old, new)
print ( new_string )