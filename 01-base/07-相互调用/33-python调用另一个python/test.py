import os
arg_a = 10
arg_b = 20
os.system("python2.7 file_a.py arg_a arg_b")
os.system("python2.7 file_a.py %d" % arg_a)
os.system("python2.7 file_a.py {}".format(arg_b))
