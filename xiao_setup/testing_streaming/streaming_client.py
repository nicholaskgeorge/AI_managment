
# The MIT License (MIT)
#
# Copyright (c) Sharil Tumin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#-----------------------------------------------------------------------------

# run this on Linux PC with opencv-python module

import cv2

dropped = 0 # drop frames count

#vid = cv2.VideoCapture('rtsp://ali78:Tvbfu781@192.168.4.44:80') # 

# 192.168.4.44 - esp32cam
#vid = cv2.VideoCapture('http://192.168.4.44/ali/Baba40Robrs') # open webcam capture

# 192.168.4.70 - XIAO esp32s3
print("establish connection")
vid = cv2.VideoCapture('http://172.20.10.2:80/xiao/Hi-Xiao-Ling') # open webcam capture
print("conection established")
while True:
    ret, frame = vid.read() # get frame-by-frame
    #print(vid.isOpened(), ret)
    if frame is not None:
        if dropped > 0: dropped = 0 # reset

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Video-44',gray_frame) # display frame
        if cv2.waitKey(22) & 0xFF == ord('q'): # press q to quit
            break
    else:
        dropped += 1
        if dropped > 100:
           print("Server is down")
           break

# Done, clear all resources
vid.release()
cv2.destroyAllWindows()
print("Video stop")


