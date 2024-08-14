import cv2

def main():
    #Create a video capture object
    capture0 = cv2.VideoCapture(0)
    capture1 = cv2.VideoCapture(1)


    #Check to see if the camera is opened successfully
    if not capture0.isOpened() or not capture1.isOpened():
        print("Could not open the cameras.")
        return
    
    #Create a window to display the video feed
    cv2.namedWindow("USB Camera 0")
    cv2.namedWindow("USB Camera 1")

    #Start the loop to read frames from the camera
    while True:
        #Capture the next frame from camera0
        ret0, frame0 = capture0.read()
        #Capture the next frame from camera1
        ret1, frame1 = capture1.read()

        #If frames are not captured successfully, break the loop
        if not ret0 or not ret1:
            print("ERROR")
            break

        #Display the frames in the windows
        cv2.imshow("USB Camera 0", frame0)
        cv2.imshow("USB Camera 1", frame1)

        #Press the 'q' key to quit
        if cv2.waitKey(1) == ord("q"):
            break

    #Close the cameras and the windows
    capture0.release()
    capture1.release()
    cv2.destroyAllWindows()

    if __name__ == "__main__":
        main()
