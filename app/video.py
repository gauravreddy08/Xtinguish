import cv2
import tensorflow as tf
import numpy as np
import tempfile

def get_intensity(img):
    img = cv2.resize(frame, (1000, 600))
    img = cv2.GaussianBlur(img, (15, 15), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 100, 111], dtype='uint8')
    upper = np.array([70, 250, 255], dtype='uint8')

    mask = cv2.inRange(hsv, lower, upper)
    count = cv2.countNonZero(mask)

    if count >= 80000:
        return "High Intensity"
    elif count <= 10000:
        return "Low Intensity"
    else:
        return "Medium Intensity"

video = './assets/video.mp4'
video = cv2.VideoCapture(video)
count = 0
label = ''
class_names=['Fire', 'No Fire']
writer = None
model = tf.keras.models.load_model('./models/baseline_model.hdf5')
while True:
    (ret, frame) = video.read()
    if not ret:
        break
    else:
        output = frame.copy()
        if count%250==0:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (224, 224))
            preds = model.predict(np.expand_dims(img, axis=0))
            label = class_names[int(np.round(preds[0]))]

        if label=='Fire':
            i = get_intensity(frame)
            if i=='Low Intensity': color = (0, 255, 0)
            elif i=='Medium Intensity': color = (0, 255, 255)
            else : color = (0, 0, 255)

            cv2.putText(output, i, (118, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1.25, color, 4)


        cv2.putText(output, label, (35, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1.25, (0, 0, 0), 4)

        if writer is None:
            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            (H, W) = output.shape[:2]
            writer = cv2.VideoWriter("./assets/output.avi", fourcc, 30, (W, H), True)
        writer.write(output)
        count += 1
        cv2.imshow("Output", output)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break








