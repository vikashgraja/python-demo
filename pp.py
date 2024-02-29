from fps import tes
import pandas as pd

l='/Users/vikashg/Downloads/customers-500000.csv'
def demo1(f):
    DF = pd.read_csv(f)
    print('ok')

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

a = [
        [demo1,[l]],
        [add,[2,4]],
        [mul,[2,6]],
]

if __name__ == '__main__':
    r = tes(a)
    print(r)
