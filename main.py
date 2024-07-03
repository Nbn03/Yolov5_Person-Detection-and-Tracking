import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


import cv2
import torch
from tracker import *
model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt', force_reload=True)

cap = cv2.VideoCapture('human_detect_video.mp4')

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (1020, 500))

def points(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)


cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', points)

yline = 500
offset = 6
# counter =set()

tracker = Tracker()
while True:
    counter = []
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    list = []
    for index, row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        nm = str(row['name'])
        list.append([x1, y1, x2, y2])
    boxes_ids = tracker.update(list)
    text_position = (34, 67)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cx = int(x + w) // 2
        cy = int(y + h) // 2

        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
        if yline < h:
            print(x, end=',')
            print(y, end=',')
            print(w, end=',')
            print(h)
            cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
            counter.append(id)

        values = ''
        for ids in counter:
            values = values + str(ids) + ','

        # print(values)

        count = len(counter)
        # print(count)
        cv2.putText(frame, str(count), text_position, cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 2, )
        cv2.line(frame, (0, yline), (1280, yline), (0, 0, 0), 1)

    frame = cv2.resize(frame, (1020, 500))
    # out.write(frame)
    cv2.imshow('FRAME', frame)
    count = 0

    if cv2.waitKey(0) & 0xFF == 27:
        break


cap.release()
# out.release()
cv2.destroyAllWindows()



    
    
