import numpy as np
import cv2

# ### blue, green, read
# ### -1, cv2.IMREAD_COLOR: color image, no transparency
# ###  0, cv2.IMREAD_GRAYSCALE: grayscale mode
# ###  1, cv2.IMREAD_UNCHANGED: including alpha channel
# image = cv2.imread("assets/EIPR_2_4.png", 0)
# image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
# image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imwrite("new_EIPR_2_4.png", image)

# cv2.imshow("Image", image)
# ### 0 -> infinite, number -> number of seconds
# cv2.waitKey(0)
# cv2.destroyAllWindows()


### ===================== 2 
# cap = cv2.VideoCapture("assets/summer_bird.mp4")

# while True:
#     ret, frame = cap.read()
#     width = int(cap.get(3))
#     height = int(cap.get(4))

#     image = np.zeros(frame.shape, np.uint8)
#     smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy = 0.5)
#     image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
#     image[height//2:, width//2:] = smaller_frame
#     image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
#     image[height//2:, :width//2] = smaller_frame
    

#     cv2.imshow("frame", image)
#     if cv2.waitKey(1) == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()

### =====================3
cap = cv2.VideoCapture("assets/summer_bird.mp4")

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = cv2.line(frame, (0,0), (width, height), (255, 0, 0), 10) ### BGR
    image = cv2.line(image, (0, height), (width,0), (255, 255, 0), 10) ### BGR

    image = cv2.rectangle(image, (0,0), (width//2, height//2), (0, 0, 255, 0.5))
    image = cv2.circle(image, (width//2, height//2), 30, (255, 0, 255, 0.5))

    font = cv2.FONT_HERSHEY_COMPLEX
    image = cv2.putText(image, "Test CV", (200, height -10), font, 4, (0, 0, 0), 5, lineType=cv2.LINE_AA)
    
    cv2.imshow("frame", image)
    
    
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
