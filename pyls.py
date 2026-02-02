# version 1
import sys
import os
import stat
import time 
import pwd

target= sys.argv[1] if len(sys.argv)>1 else '.'
dir_list=list(os.scandir(target))
dir_list.sort(key=lambda e:e.name)
for entry in dir_list:
	st=entry.stat()
	permissions=stat.filemode(st.st_mode)
	size=st.st_size
	user=pwd.getpwuid(st.st_uid).pw_name
	mtime=time.ctime(st.st_mtime)
	name=entry.name
	print(f"{permissions} {size:<6d} {user} {mtime} {name}")





