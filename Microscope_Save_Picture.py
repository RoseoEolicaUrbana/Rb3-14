import cv2
from datetime import datetime


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")


while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y__%H:%M:%S")     	# dd/mm/YY H:M:S
        # SPACE pressed
        img_name = "microscope_frame_{}.png".format(dt_string)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

cam.release()

cv2.destroyAllWindows()



