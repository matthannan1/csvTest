import os
import getpass
#import os

#homedir = os.environ['HOME']
#print(homedir)
print(os.getenv('HOME', 0))

print("Is this good?: ", os.path.expanduser('~'))



username = getpass.getuser()
print(username)

for user in [ '', 'hannamj', 'postgres' ]:
    lookup = '~' + user
    print(lookup, ':', os.path.expanduser(lookup))