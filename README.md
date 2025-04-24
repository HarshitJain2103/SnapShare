# 🚀 SnapShare  
**Empowering Smart Campuses with Gesture-Based Local Sharing**  
*A lightweight tray application for seamless sharing of text, files, and images using hand gestures over the local network — no internet required.*

---

## 📌 Problem Statement  
**Problem Statement 11 – Build a Smart Campus Infrastructure Toolkit**

---

## 🎯 Objective  
SnapShare is designed to support smart campuses by enabling gesture-based, touch-free data sharing between devices on the same local network. In classrooms, labs, or libraries, students and faculty can quickly exchange notes, screenshots, and files without internet, cables, or cloud storage.

This plug-and-play tray app simplifies collaboration while enhancing safety and digital interaction in educational environments.

---

## 🧠 Team & Approach  
**Team Name:** HackHazards

**Team Members:**  
- Harshit Jain  
- Raghav Tiwari
- Adithya V
- Ravent Dhaiya

**Our Approach:**  
We set out to simplify how students and faculty share content on campus — reducing reliance on email, pen drives, and messaging apps.  
- **Why this problem:** Existing sharing tools often need internet, sign-ins, or manual pairing. SnapShare skips all of that using gestures and local connectivity.  
- **Challenges tackled:**  
  - Real-time gesture recognition  
  - Peer discovery in local networks  
  - Secure transfer with approval prompts  
- **Breakthroughs:**  
  - Hotkey-triggered webcam-based gesture detection  
  - On-demand FastAPI server for hosting data locally  
  - Pop-up approval to prevent accidental transfers  

---

## 🛠️ Tech Stack  
**Core Technologies Used:**  
- **Frontend/UI:** Tkinter (tray icon, pop-up prompts)  
- **Gesture Detection:** MediaPipe + OpenCV  
- **Local Server (temporary):** FastAPI (for hosting data on sender's machine)  
- **Networking:** UDP broadcasting for peer discovery over LAN  
- **File Handling:** OS & clipboard-based logic

**Sponsor Technologies Used:**  
_None used_

---

## ✨ Key Features  
✅ Copy data using a hand gesture (ASL “3”)  
✅ Paste using an open palm gesture  
✅ Runs in system tray and is hotkey activated (Ctrl + M)  
✅ Transfers text, files, images, and screenshots over LAN  
✅ Shows approval prompt before any data is shared  
✅ Automatically saves received content to local folder or clipboard  

---

## 📽️ Demo & Deliverables  
**Demo Video:** https://youtu.be/Q8lbBUbyUSY  
**Pitch Deck / Slides:** [Add Google Slides or PDF link here]

---

## ✅ Tasks & Bonus Checklist  
✅ Followed 2 official social channels and filled the form  
✅ Bonus Task 1: Shared badges + filled form (2 points)  
✅ Bonus Task 2: Signed up on Sprint.dev + filled form (3 points)  

---

## 🧪 How to Run the Project  

**Requirements:**  
- Python 3.10  
- pip
- tensorflow
- MediaPipe  
- OpenCV  
- FastAPI  
- Tkinter (pre-installed in most Python setups)

**Setup Instructions:**  
```bash
# Clone the repo
git clone https://github.com/HarshitJain2103/SnapShare.git

# Navigate to the project folder
cd SnapShare

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```
**📦 File Storage:**
-Text is copied directly to clipboard
-Files and images are saved to SnapShareDownloads/ on the receiver's machine

**🔒 Privacy & Safety:**
-Data is only transferred when the sender approves
-Temporary servers are only hosted during active gestures
-No internet needed — works 100% over LAN

**🧬 Future Scope:**
-📈 Smart Classroom Dashboard: Track peer-to-peer usage (non-sensitive metadata)
-🛡️ Enhanced encryption for private institutions
-🌐 Cross-platform support for Linux/macOS
-⚙️ Admin Mode: Enable/disable SnapShare on lab machines centrally

**📎 Resources / Credits:**
-MediaPipe by Google
-FastAPI
-OpenCV
-All contributors and testers who helped refine SnapShare

**🏁 Final Words:**
-SnapShare was built to bring intuitive, real-time data sharing to educational spaces. From classrooms to hackathons, it bridges the gap between hardware and human gestures. The experience of developing this tool during HackHazards was as rewarding as the solution itself.
