import cv2

# webcam, capture video, convert to grayscale
# VideoCapture - device index or name of video file

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('assets/saved_video.avi', fourcc, 20.0, (640,480))
# SAVING A VIDEO
# Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size
# video. X264 gives very small size video)
# in Windows: DIVX (More to be tested and added)

print("press esc to stop, any other key to display grayscaled version of current frame")

if not cap.isOpened():
    cap.open(1)

if cap.isOpened():
    while(cap.isOpened()):
        # capture frame by frame
        ret, frame = cap.read() # ret = true/false, did you recieve a frame from a source?
        print(ret)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY) # convert frame to gray
        
        # saving the file
        out.write(gray)
        cv2.imshow('frame', gray) # show the converted frame

        k = cv2.waitKey(1)
        # waitKey(0) to let it wait indefinitely for a response from you - frame by frame analysis possible
        # waitKey(1) to wait only 1 second until it stops waiting - for continuous frame capture - output will be a video.
        if k == 27:
            print("exiting.")
            break;

    cap.release()
    cv2.destroyAllWindows()
