import algorithm
import sys
import mysql.connector
from mysql.connector import errorcode
#how do we know their table name
def main():
    args = []
    for arg in sys.argv:
        args.append(arg)
    '''
    if len(args) != 2:
        print("Invalid Arguments")
        print("Usage: python main.py <path-to-mysql database>")
        exit()
    '''
    algorithm.start()

if __name__ == "__main__":
    main()