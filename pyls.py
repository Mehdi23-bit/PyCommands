import sys,os
import stat,time,pwd

dict_= sys.argv[1] if len(sys.argv)>1 else '.' 

dir_list=os.scandir(dict_)

for entry in dir_list:
	st=os.stat(entry.name)
	permissions=stat.filemode(st.st_mode)
	size=st.st_size
	user=pwd.getpwuid(st.st_uid).pw_name
	mtime=time.ctime(st.st_mtime)
	name=entry.name
	print(f"{permissions} {size} {user} {mtime} {name}")





