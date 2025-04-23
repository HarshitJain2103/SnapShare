# 🚀 SnapShare

**Introducing SnapShare** – a lightweight tray application designed for seamless sharing of text, files, and images over your local network using just hand gestures.

---

## ✨ Features

- 📋 Copy and paste data using intuitive hand gestures:
  - **3(in ASL)** → Copy  
  - ✋ **Open hand** → Paste  
- 💻 Runs silently in the system tray  
- 🌐 Works over your **local network (LAN)**  
- ⚡ Transfers **text**, **files**, **images**, and **screenshots**  
- 🔐 Connection approval system ensures data is only shared when allowed  

---

## 🛠 How It Works

### 🔑 Activation

SnapShare is triggered with a simple hotkey:  
**`Ctrl + M`**

This activates your webcam to detect hand gestures.

---

### 👤 User A – The Sender

1. User A presses **Ctrl + M** and performs the **Copy gesture** after selecting a file/text/Screenshot.
2. SnapShare:
   - Recognizes the gesture ✅  
   - Copies the selected text/file 🗂️/Screenshot to clipboard  
   - Notifies the user 📣  
   - Starts a **local server** to store the copied data temporarily  
   - Begins **broadcasting on the LAN**, making User A discoverable

---

### 🧑‍🤝‍🧑 User B – The Receiver

1. User B performs the **paste gesture**
2. SnapShare:
   - Detects the paste gesture  
   - Scans the network for available users  
   - Displays a list (e.g., “User A” appears)
   - User B selects User A and clicks **Connect**

---

### ✅ Approval Flow

- User A receives a pop-up prompt:
  - _“User B wants to access your clipboard. Allow?”_
- If approved:
  - Data transfer begins immediately and both users are notified
  - If denied: Nothing is shared and user B is notified "Access Denied!"

---

### 📂 File Storage

- If the data was a **file, image, or screenshot**:
  - It is saved in the `SnapShareDownloads` folder on User B’s device  
  - (Folder is auto-created if it doesn’t exist)

- If it was **text**:
  - It is directly copied into User B’s clipboard

---

## 📸 Demo Preview

Ctrl + M ➜ 3(as in ASL) ➜ SnapShare starts server ➜ ✋ on another system ➜ User detected ➜ Connect ➜ Prompt ➜ Transfer complete.

---

## 📦 Installation & Usage

1. Clone the repo:
  git clone https://github.com/HarshitJain2103/SnapShare.git
  
2. Install dependencies:
  pip install -r requirements.txt

4. Run the app:
   python main.py

---

## 📜 License

This project is licensed under a custom license. Commercial use, redistribution, or modification without the author's explicit permission is strictly prohibited ./LICENSE.

---

## 🙌 Acknowledgments

Special thanks to: 
- Everyone who helped test across multiple devices  
- Recommended different features for the app.
---

## 🤖 Built with love at [HACKHAZARDS 2025]

