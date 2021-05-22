import cv2
import numpy as np
import tqdm
import shutil
import os
from getpoints import getpoints
from overlapping_interval import overlapping_interval
# new_out = [510, 1965, 1995, 2010, 2035, 2040, 3455, 4260, 5980]
name = '../results/detfps60fd2normalbatplusballinterval/'


try:
    shutil.rmtree(name)
except:
    print('does not exist')
os.makedirs(name, exist_ok=True)
cap = cv2.VideoCapture('../../data/video.mp4')
 
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('results/red_cricket.mp4',fourcc, 20, (1280,720))
k = 0
# frames_int = [ frames_sorted[i] for i in frames_from_int]
num_out, bat, ball, cor_bat, cor_ball = getpoints()

frame_from_int = overlapping_interval(bat,ball,cor_bat,cor_ball)
while cap.isOpened():
    
    ret, frame = cap.read()
    # print(frame.shape)
    # break
    if ret == True:
        if k in frames_from_int:
            cv2.imwrite(name+str(k)+'.jpg',frame)
     
        # b = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        # out.write(b)
    else:
        break
    k+=1
    if k%200 ==0:
        print(f'reading fram {k}')
    
cap.release()
# out.release()
cv2.destroyAllWindows()