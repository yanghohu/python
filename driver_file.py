import win32api
import platform
import os
import sys
import os.path
import socket
import datetime,time
import pandas as pd
import glob

###############################################################################
# python install pywin32
# pip install pywin32
###############################################################################

###############################################################################
# drives : 하드드라이브 본인에 맞는 드라이브 나옴
################################################################################
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1] 


osname = platform.platform()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

# ###############################################################################
# # filefind : 파일 확장자 ,파일 사이즈 찾기 
# ################################################################################
def filefind(dest):
    for root, dirs, files in os.walk(dest):
        for filename in files:
            try:
                relativepath = os.path.join(root,filename) # 상대경로
                abspath = os.path.abspath(relativepath) # 절대경로
                name, ext = os.path.splitext(filename) #  파일명과 확장자 분리
                if(ext[0:1] == '.'):
                    ext_sp = ext[1:len(ext)]
                else:
                    ext_sp = ext
                    
                file_size_byte = os.stat(relativepath).st_size
                createday = datetime.datetime.fromtimestamp(os.path.getctime(relativepath)).strftime('%Y%m%d') #파일입력일
                modifyday = datetime.datetime.fromtimestamp(os.path.getmtime(relativepath)).strftime('%Y%m%d') #파일수정일
                f.write(hostname +"@@")
                f.write(ip + "@@")
                f.write(osname+"@@")
                f.write(abspath + "@@")
                f.write(filename + "@@")
                f.write(str(file_size_byte)+"@@")
                f.write(ext_sp+"@@")
                f.write(modifyday +"@@")
                f.write(createday +"@@")
                f.write("\n")
            except Exception as ex:
                continue


###############################################################################
#           : 드라이브 별로 찾기 (filefind 호출 )
###############################################################################
for dr in drives:
    dr = dr.replace(":\\","") 
    print(ip + "_" + dr) 
    print(ip + "_" + dr + " start job ")
    print("python driver_file.py " + dr + ": " + dr)
    f = open(ip + "_" + dr + ".txt", 'w+',-1,"utf-8") #windows    
    filefind(dr + ":\\")
    f.close()
    print(ip + "_" + dr + " end job ") 
 


###############################################################################
#         : 컬럼
###############################################################################
cols = ["hostname","ip","osname","abspath","filename","file_size_byte","ext_sp","modifyday","createday","final_del"]
print(cols)

###############################################################################
#         : 위에서 찾은 파일 합치기
###############################################################################
data_concat = pd.DataFrame()
data_concat1 = pd.DataFrame()

for dr in drives:
    dr = dr.replace(":\\","") 
    print (ip + "_" + dr + ".txt")
    for f in glob.glob(ip + "_" + dr + ".txt"):
        df = pd.read_csv(f,delimiter="@@",index_col=None, header=0, encoding='UTF8',error_bad_lines=False,names=cols)         
        data_concat1 = pd.concat([df], ignore_index=True,names=cols)
        data_concat = data_concat.append(data_concat1,ignore_index=True) 

###############################################################################
#         : 중복파일 찾기 및 저장 (구현 아직 안 되었음) 판다스 구현
###############################################################################
print(data_concat.head(1)) 
print(data_concat.shape)  
ext_sp = (data_concat["ext_sp"] == "mp4") | (data_concat["ext_sp"] == "avi")
 
data_concat_filter = data_concat[ext_sp]

print(data_concat_filter[data_concat_filter.filename.duplicated()].sort_values(['filename','createday'],ascending=[True,False]))

data_sort_concat_filter = data_concat_filter[data_concat_filter.filename.duplicated()].sort_values(['filename','createday'],ascending=[True,False])

data_sort_concat_filter.to_csv("중복파일.txt",sep="^",index=False,na_rep='NaN')
