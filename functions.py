def openFile(filename):
    f = open(filename,'r')
    input = f.read()
    f.close()
    return input