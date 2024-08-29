# Remote Screen Control for Theatrical Workshop

This project provides a system to remotely control the screens of participants' mobile devices in a theatrical workshop setting. Participants can "cede" their screens, allowing a central controller to send commands to change the screen color or display images. This interactive system is built using Flask, Flask-SocketIO, and standard web technologies.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [How It Works](#how-it-works)
7. [Future Improvements](#future-improvements)
8. [License](#license)

## Introduction

The Remote Screen Control project is designed for use in a theatrical workshop, allowing the facilitator to control the screens of participants' mobile devices in real-time. By utilizing their devices, participants can become part of a larger, synchronized visual experience, enhancing the immersive quality of the workshop.

## Features

- **Real-time screen control:** Change the background color or display an image on participants' devices.
- **Dynamic image URL input:** Easily input and send image URLs to be displayed on all connected devices.
- **WebSocket communication:** Provides low-latency interaction between the control interface and participant devices.
- **Easy to use:** Simple interface for both participants and the controller.

## Technologies Used

- **Backend:** Flask, Flask-SocketIO
- **Frontend:** HTML, CSS, JavaScript (with Socket.IO)
- **WebSockets:** For real-time, bidirectional communication

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/remote-screen-control.git
    cd remote-screen-control
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    Make sure `Flask` and `Flask-SocketIO` are included in your `requirements.txt` file.

4. **Run the application:**

    ```bash
    python app.py
    ```

    The application will start running on `http://localhost:3000`.

## Usage

1. **Start the Flask server** by running the command above.
2. **Participants access the main page** at `http://localhost:3000/` on their mobile devices and click "Cede Screen" to allow their screens to be controlled.
3. **Open the control interface** by navigating to `http://localhost:3000/controle` on your computer or another device.
4. **Use the control interface** to:
   - Change the screen color of all connected devices by clicking the appropriate button.
   - Input a URL into the text field and click "Show Image" to display that image on all connected devices.

## How It Works

- **Participants** connect their devices to the main page and "cede" their screens, establishing a WebSocket connection with the server.
- **The server** listens for events and handles commands sent from the control interface.
- **The control interface** sends commands (e.g., change color, display image) to the server, which then broadcasts these commands to all connected participant devices.
- **Participant devices** receive these commands via WebSockets and update their displays accordingly.

## Future Improvements

- **Add authentication:** To ensure that only authorized users can control the screens.
- **Add more control options:** Such as playing sounds, displaying text, or animating the screens.
- **Improve validation:** For input URLs to ensure they are valid and safe before broadcasting.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
