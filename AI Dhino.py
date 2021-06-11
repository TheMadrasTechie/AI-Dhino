from scipy.spatial import distance as dist
from imutils.video import VideoStream
import numpy as np
import time
import cv2
import imutils
from PIL import ImageGrab
from pynput.keyboard import Key,    Controller
keyboard = Controller()
a =0
tim = time.time()
while True:
    maini = ImageGrab.grab(bbox=(550,150,1400,350))
    maini = np.array(maini)
    #main = ImageGrab.grab(bbox=(550,150,840,350))
    print(a)
    main = ImageGrab.grab(bbox=(690,200,840+a,320))
    main = np.array(main)
    main = cv2.cvtColor(main, cv2.COLOR_BGRA2RGB)
    blurI_ = cv2.GaussianBlur(main, (11, 11), 0)
    edged = cv2.Canny(blurI_, 75, 200)
    #cv2.imshow("edge",edged)
    cv2.line(maini, (int(maini.shape[1]/6), 0), (int(maini.shape[1]/6), int(maini.shape[0])), (0,255,0), 2)
    cv2.line(maini, (0, int((maini.shape[0])/2)), (int(maini.shape[1]), int((maini.shape[0])/2)), (0,255,0), 2)
    cv2.line(maini, (int(maini.shape[1]/6)*2, 0), (int(maini.shape[1]/6)*2, int(maini.shape[0])), (0,255,0), 2)
    cv2.line(main, (int(main.shape[1]/6), 0), (int(main.shape[1]/6), int(main.shape[0])), (0,255,0), 2)
    cv2.line(main, (0, int((main.shape[0])/2)), (int(main.shape[1]), int((main.shape[0])/2)), (0,255,0), 2)
    #cv2.line(main, ((int(main.shape[1]/2)), 0), ((int(main.shape[1]/2)), 0), (0,255,0), 2)
    cv2.line(main, (int(main.shape[1]/6)*2, 0), (int(main.shape[1]/6)*2, int(main.shape[0])), (0,255,0), 2)
    #dino = ImageGrab.grab(bbox=(690,250,1400,350))
    ##print(main.shape[1]/6)
    ##print(main.shape[0]/2)
    #dino = cv2.cvtColor(dino, cv2.COLOR_BGRA2RGB)
    #dino = np.array(dino)
    gray = cv2.cvtColor(main,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    corners = cv2.goodFeaturesToTrack(gray, 50, 0.1, 10)
    corners = np.int0(corners)
    i=0    
    if(40<int(time.time()-tim)<42):
    	a = 10
    if(50<int(time.time()-tim)<52):
    	a = 20	
    if(55<int(time.time()-tim)<57):
    	a = 30		
    if(60<int(time.time()-tim)<62):
    	a = 50
    if(65<int(time.time()-tim)<67):
    	a = 70				
    for corner in corners:
        x,y = corner.ravel()
        if(len(corners)>5):
          #print(y)	 
          #if(0<y<int(main.shape[0]/2)):	
          if(int((main.shape[0]/6)*5)<y<int(main.shape[0])):
        #if((int(main.shape[1]/6)<x<(int(main.shape[1]/6)*2))and(int((main.shape[0])/2)<y<int((main.shape[0])))):
           #print("jump\t"+str(len(corners)))
           keyboard.release(Key.down)
           keyboard.press(Key.up)
           break
          #elif(int(main.shape[0]/2)<y<int(main.shape[0])):
          if(0<y<int((main.shape[1]/6)*5)):
           #print("down\t"+str(len(corners)))
           keyboard.release(Key.up)
           keyboard.press(Key.down)
           break 
        cv2.circle(main,(x,y),3,(255,0,0),5)
        i=i+1
        #print(len(corners))
    # keyboard.press(Key.down)
    # keyboard.press(Key.up)
    #cv2.imshow("dino", main)
    cv2.imshow("Main", maini)
    key = cv2.waitKey(1) & 0xFF 
    if key == ord("q"):
        break
cv2.destroyAllWindows()