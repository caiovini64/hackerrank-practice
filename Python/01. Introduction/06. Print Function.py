# https://www.hackerrank.com/challenges/python-print/problem
# Score: 20.0

if __name__ == '__main__':
    
    n = int(input())
    list = []
    
    
    while n > 0: 
        list.insert(0, n)
        n = n - 1
    
    list.sort()
     
    for x in list: 
        print(x, end='')