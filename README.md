 WebCam Motion Detection & Email Alert System

A Python-based **motion detection system** that monitors webcam footage, detects movement, captures the frame, and automatically **emails the image** using Gmail’s SMTP server.

Built to explore **computer vision, automation, and secure email integration** — similar to basic security camera systems.

---

##  Features

- Real-time webcam feed analysis with OpenCV  
- Automatic motion detection via frame differencing  
- Snapshot capture when movement is detected  
- Sends an email with the detected image attached  
- Uses Gmail App Passwords + SSL for secure email delivery  

---

## Tech Stack

| Component | Purpose |
|------------|----------|
| **Python 3** | Core language |
| **OpenCV** | Motion detection & image capture |
| **smtplib + ssl** | Secure email delivery |
| **filetype** | Detect attachment format dynamically |
| **EmailMessage API** | MIME-compliant message creation |

---
## Files
- main.py is the main backend logic
- emailing.py is the function python file responsible for sending out the alert

