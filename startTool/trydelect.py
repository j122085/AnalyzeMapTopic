import time
import os
nowdate=time.strftime("%Y%m%d", time.localtime())
savedir="../data/104json"
savedir="../data/104json"+"/"+nowdate
command = "rm -rf %s"
command = command % savedir
print(command)
result =os.system(command)
if result == 0:
	print ("刪除檔案成功")
else:
	print ("刪除檔案沒成功")
