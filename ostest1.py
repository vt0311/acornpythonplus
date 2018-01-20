import os

print('os.name:', os.name)
print()
print('os.path.abspath(''):', os.path.abspath('.'))
print()
print(os.environ['PATH'])
print()
f = os.popen("dir")
print(f.read())