# 특정 폴더로 이미지 모으기 + 이미지 특정 부분만 자르기
# from final project 

import glob
import os
import zipfile
import os.path
import shutil
import time
import matplotlib.pyplot as plt
import cv2

path2='./res/'
li2= os.listdir(path2)

#sname=['S001','S002','S003','S004','S006']

#Lname=['L1','L2','L3','L4','L8','L9','L12','L13','L19','L20','L22','L23','L25','L26']

sname=['S001','S002','S003','S006']
Lname=['L1','L2','L3']
ename=['E01','E02','E03']

test=[6,7,8]

try:
    os.mkdir('./es')
except:
    pass

co1=0
co2=0
co3=0

for la in li2:
    for s in sname:

        time.sleep(1)

        for L in Lname:
            for e in ename:

                path=path2+la+'/'+s+'/'+L+'/'+e+'/'

                for i in range(1,20):

                    if i in test:              
                        temp_jpg=path+'C'+str(i)+'.jpg'
#                         temp_txt=path+'C'+str(i)+'.txt'
                        

                        if os.path.isdir('./es/'+e)== False:
                                 os.mkdir('./es/'+e)

                        if e == 'E01':
                            co1+=1
                            tmp_path='./es/'+e+'/'+e+'_'+str(co1)+'.jpg'
                            tmp_txt ='./es/'+e+'/'

                        elif e == 'E02':
                            co2+=1
                            tmp_path='./es/'+e+'/'+e+'_'+str(co2)+'.jpg'                           
                            tmp_txt ='./es/'+e+'/'

                        elif e == 'E03':
                            co3+=1                            
                            tmp_path='./es/'+e+'/'+e+'_'+str(co3)+'.jpg'   
                            tmp_txt ='./es/'+e+'/'

#                         try:
#                              shutil.copy(temp_txt, tmp_txt)
#                         except:
#                             pass

                        try:
                            shutil.copy(temp_jpg, tmp_path)
                        except:
                            pass
                        
f1=glob.glob('./es/E01/*')
f2=glob.glob('./es/E02/*')
f3=glob.glob('./es/E03/*')

print(len(f1),len(f2),len(f3))

try:
    os.mkdir('./roi')
except:
    pass

try:
    os.mkdir('./roi/E01')
    os.mkdir('./roi/E02')
    os.mkdir('./roi/E03')    
except:
    pass

c1=1
for fn in f1:
    img=cv2.imread(fn,cv2.IMREAD_COLOR)
    height, width = img.shape[:2]

    cwi=width//2
    che=height//2
    
    roi=img[che-200:che+200,cwi-200:cwi+200]
    
    cv2.imwrite('./roi/E01/roi'+str(c1)+'.jpg',roi)
    c1+=1
    
c2=1
for fn in f2:
    
    img=cv2.imread(fn,cv2.IMREAD_COLOR)
    height, width = img.shape[:2]

    cwi=width//2
    che=height//2
    
    roi=img[che-200:che+200,cwi-200:cwi+200]
    
    cv2.imwrite('./roi/E02/roi'+str(c2)+'.jpg',roi)
    c2+=1
    
c3=1
for fn in f3:
    img=cv2.imread(fn,cv2.IMREAD_COLOR)
    height, width = img.shape[:2]

    cwi=width//2
    che=height//2
    
    roi=img[che-200:che+200,cwi-200:cwi+200]
    
    cv2.imwrite('./roi/E03/roi'+str(c3)+'.jpg',roi)
    c3+=1
    
print(che-200,che+200,cwi-200,cwi+200)