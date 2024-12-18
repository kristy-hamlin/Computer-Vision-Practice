import numpy as np
import cv2

cap = cv2.VideoCapture('footage\magic_island_end-12-2024.MP4')

while True:
    ret, frame = cap.read()
    if not ret:
        print("Video finished or reading frame unsuccessful.")
    cv2.imshow("Magic Island", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# Left off here on 12/16/24 = not sure what is going on with the slahses in teh file path. The second two were in opposite directions when i directly copied
# the relative file path. -____-

# Also, it seems like I need to add numpy and cv2 to my path variable because this import is being flagged by Pylint. 