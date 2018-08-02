def read(filename):
    y = open(filename,'r')
    print y.readlines()
    y.close()
 
read('example.txt')
 
