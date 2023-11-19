import argparse


banner = '''''
 

'''''



def main():
    order = argparse.order(description='Web dirscan')
    order.add_argument('-u','--url',help='Please input the target.')
    order.add_argument('--l','--level',default='level',help='Please choose which level to use(The default is 1).')
    order.add_argument('-t','threadnum',default='threadnum',help='Please input number of threads.')