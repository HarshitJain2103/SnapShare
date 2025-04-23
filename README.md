SnapShare – Gesture-based File and Text Sharing App
Project Overview
SnapShare is a lightweight tray application that allows users to share text, files, and images seamlessly over a local network. The app uses intuitive hand gestures for interactions and provides a smooth user experience with minimal setup.

Key Features
Gesture-based Interaction: Control the app using simple hand gestures (closed fist for "copy", open hand for "paste").

Hotkey Activation: Trigger the app with a hotkey (Control + M), which activates the webcam to recognize your gesture.

Local Network Sharing: Share data (text, files, images) over your local network with ease.

How it Works
SnapShare is activated with a simple hotkey Control + M. Once triggered, the webcam activates and detects the user's gesture.

How to Use
1. User A – Copying Data
Press Control + M to activate the app and perform the copy gesture (closed fist).

Select a file or text to copy.

SnapShare confirms the gesture and notifies User A that the selected data has been copied.

A local server is automatically set up on User A’s device, storing the copied data in memory.

Periodic broadcasts are sent over the local network, making the server discoverable by other SnapShare users.

2. User B – Pasting Data
User B presses Control + M and performs the paste gesture (open hand).

SnapShare detects the gesture and searches for active servers on the local network.

The available server (User A’s) is displayed, and User B selects it to send a connection request.

3. Approval Flow
User A receives a prompt to approve or deny the connection.

Upon clicking Yes, the transfer begins.

4. File Received
Once approved, the file is transferred and saved in SnapShareDownloads folder on User B’s system (if the folder doesn’t exist, it’s created automatically).

Both users are notified when the file has been successfully received.

Special Behavior
Text: If the copied data is text, it will be stored directly in User B’s clipboard.

Files/Images/Screenshots: These are saved into the SnapShareDownloads folder on User B’s system.

Technologies Used
Python (for development)

MediaPipe (for gesture detection)

OpenCV (for webcam integration)

Socket Programming (for local network communication)

Installation
Clone the repository to your local machine.

bash
Copy
Edit
git clone https://github.com/yourusername/snapshare.git
cd snapshare
Create and activate a virtual environment.

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies.

bash
Copy
Edit
pip install -r requirements.txt
Run the application.

bash
Copy
Edit
python app.py
Usage
To activate SnapShare, press Control + M.

Perform the appropriate hand gestures (closed fist to copy, open hand to paste).

Follow the on-screen instructions to share data with other users over the local network.

Contribution
Feel free to fork the repository and submit pull requests. For bugs or feature requests, please open an issue in the repository.

License
This project is licensed under the MIT License – see the LICENSE file for details.
