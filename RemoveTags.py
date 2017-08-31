def removeTag(string):
    start=string.find('<')
    while start!=-1:
        end=string.find('>',start)
        string=string[:start]+' '+ string[end + 1:] #remove tags and put space in place of it
        start=string.find('<')
    return string.split()
#print (removeTag('<b>Hello</b>this is <i>a test</i>'))