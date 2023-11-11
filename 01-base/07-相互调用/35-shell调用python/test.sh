#!/bin/bash

# shell调用python文件中的函数并传递参数
a=' hello '
b=' world '
c=10
d=1
e=2
f=3
python -c "import test; test.test1('$a', '$b', '$c')"

result=$(python -c "import test; print(test.test2('$d', '$e', '$f'))")
if [ $result != 0 ];then
    echo result is True $result
else
    echo result is not True $result
fi

echo '======'

# shell 调用python文件并传递参数

python2 ./test.py $d $e $f