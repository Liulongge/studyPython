
#!/usr/bin/python
import sys
def test1(a, b, c):
    print('{} {} {}'.format(a, b, c))
    return 0

def test2(a, b, c):
    return a + b + c

if __name__ == '__main__':
  test1(sys.argv[1], sys.argv[2], sys.argv[3])