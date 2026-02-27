# Name Vipin Saini
# Subject Internet of Things
# roll No : 24IMAI007
# Question 3:

'''
design and implement a real time object detection alert system using 
openCV and MQTT 
Scenario 
a security camera continously monitors a restricated area whenever a human face is detected in the video stream, an alert message must be 
puvlislhed to a monitorning system using MQTT protocol

Requirements
1 use OpenCV to:
capture live video from a camera
perform real- time face detection 

2 Use MQTT protocol to
publish an alert message when a face is detectd 
subscribe to the alert topic 
display recieved alert messages in real time 

3. implement 
publisher program (openCV + MQTT integratio)
Subscriber program (MQTT client)

4. the system must operate in near real time and handle events efficiently

Evalution will be based on 
correct OpenCV integration
Proper MQTT publish subscribe mechanism
code structure and clarity 
real time processing efficiency



'''

# publisher (OpenCV + MQTT integration)


import cv2
import paho.mqtt.client as mqtt
import time

# MQTT Configuration
BROKER = "localhost"
PORT = 1883
TOPIC = "security/face_alert"

# Create MQTT Client
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Start Video Capture
cap = cv2.VideoCapture(0)

last_alert_time = 0
alert_interval = 5   # seconds between alerts (avoid flooding)

print("Monitoring started...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # If face detected → Publish Alert
    if len(faces) > 0:
        current_time = time.time()
        if current_time - last_alert_time > alert_interval:
            alert_message = "ALERT: Human face detected in restricted area!"
            client.publish(TOPIC, alert_message)
            print("Alert Published!")
            last_alert_time = current_time

    cv2.imshow("Security Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
client.disconnect()

