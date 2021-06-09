import cv2
import numpy as np

net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg.txt')
classes = []
with open('coco.names.txt', 'r') as f:
    classes = f.read().splitlines()

cap = cv2.VideoCapture('slow_traffic_small.mp4')

while True:
    _, img = cap.read()
    height, width, _ = img.shape
    blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)  # used to set input from blobs to the network
    output_layers_names = net.getUnconnectedOutLayersNames()  # it gets output layer names
    layerOutputs = net.forward(output_layers_names)  # it forward the output names and obtain the outputs

    boxes = []  # initialize a list
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]  # starts from 6th element and calc the score and used to store all the predictions
            class_id = np.argmax(scores)  # store the higher score
            confidence = scores[class_id]  # assign the higher score in confidence variable
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # we need to extract the corner positions in order for us to present them with the use of OPENCV

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    # NON MAXIMUM SUPPRESSIONS FUNCTION USED TO ONLY KEEP FRAME OF HIHER SCORE BOXES
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    for i in indexes.flatten():  # here we identify each of the objects detected
        x, y, w, h = boxes[i]  # extract the info from the boxes
        label = str(classes[class_ids[i]])  # we extrat the classes id from coco files names
        confidence = str(round(confidences[i], 2))  # extract confiseces and put it n string and assgn to confidence
        color = colors[i]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)  # create a rectangle
        cv2.putText(img, label + " " + confidence, (x, y + 20), font, 2, (255, 255, 255), 2)  # put text

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

# yolo is state of art object detetcyolo is state of art object detetction algo anh hve become statndard way to detectobject detection earlier sliding window detection was used
# yolo you only look once high probabilities of the image are considered as object detected intersection over union; intersect area/ union area
# non max suppression: used to get single frame when multiple frames are there yolo is very fast algo and can detetct ojects very fast
# tion algo anh hve become statndard way to detectobject detection earlier sliding window detection was used
# yolo you only look once high probabilities of the image are considered as object detected intersection over union; intersect area/ union area
# non max suppression: used to get single frame when multiple frames are there yolo is very fast algo and can detetct ojects very fast
