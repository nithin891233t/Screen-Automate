# VocalMotion:A Voice and Gesture Automation System

This project enables hands-free control of a computer screen through voice commands and hand gestures. It uses various Python libraries for speech recognition, gesture detection, browser automation, system monitoring, and more. This system aims to improve accessibility and provide a more intuitive user interface by combining voice and gesture-based interactions.

## Features

- **Voice Commands**: Control system tasks, search the web, and interact with applications using voice commands.
- **Hand Gestures**: Use hand movements detected through the camera to control the screen, mouse movements, and interact with the system.
- **System Monitoring**: Check CPU usage, memory status, and internet speed.
- **Automated Browser Control**: Perform automated web searches and navigate using voice commands.
- **Joke Teller**: Retrieve and read aloud jokes for user entertainment.
- **Currency Conversion**: Convert currencies using real-time exchange rates.
- **Screenshots & Automation**: Automate tasks such as taking screenshots and controlling system processes.
  
## Libraries Used

1. **`pyttsx3`**: Text-to-speech conversion for voice feedback.
2. **`speech_recognition`**: Recognizes voice commands and converts speech to text.
3. **`wikipedia`**: Fetches Wikipedia content for voice searches.
4. **`datetime`**: Retrieves the current time and date.
5. **`pyjokes`**: Provides jokes for entertainment.
6. **`cv2` (OpenCV)**: Handles video capture and image processing for hand gestures.
7. **`winsound`**: Plays system sounds for notifications.
8. **`psutil`**: Monitors system resources like CPU and memory.
9. **`requests`**: Fetches data from the web for API integration.
10. **`subprocess`**: Executes system commands and scripts.
11. **`pyautogui`**: Automates keyboard and mouse interactions.
12. **`speedtest`**: Measures internet speed.
13. **`selenium`**: Automates browser tasks using web drivers.
14. **`cvzone.HandTrackingModule`**: Detects hand gestures through video input.
15. **`mouse`**: Controls mouse movements based on hand gestures.
16. **`forex_python.converter`**: Converts currencies using real-time exchange rates.
17. **`webbrowser`**: Automates opening and controlling web browsers.

## How it Works

### Voice Commands
1. **Speech Recognition**: The program listens for voice commands using a microphone.
2. **Command Execution**: Based on the recognized speech, specific actions like web searches, system control, or task automation are executed.
3. **Voice Feedback**: The system responds with voice feedback using text-to-speech for confirmation and results.

### Hand Gestures
1. **Hand Tracking**: Using the webcam, the program detects hand gestures using OpenCV and `cvzone.HandTrackingModule`.
2. **Gesture-based Control**: Gestures can be mapped to different actions such as controlling the mouse, clicking, or switching between windows.

### System Monitoring
1. **CPU and Memory Usage**: Retrieves current system resource usage through `psutil` and announces it via voice feedback.
2. **Internet Speed Test**: Measures internet speed using `speedtest` and reads the results aloud.

### Browser Automation
1. **Web Search**: Perform Google searches or Wikipedia lookups using voice commands.
2. **Web Automation**: Open and control browser windows using Selenium and voice commands.

### Currency Conversion
1. **Real-time Conversion**: Converts currencies using `forex_python.converter` and provides real-time exchange rates.

## Setup Instructions

### Prerequisites

1. Python 3.x
2. A microphone for voice input.
3. A webcam for gesture detection.

### Required Libraries

Install the necessary libraries using pip:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyjokes opencv-python winsound psutil requests pyautogui speedtest-cli selenium cvzone mouse forex-python
```

### Additional Setup

1. **Selenium WebDriver**: Download and configure the appropriate WebDriver for your browser (e.g., Chrome, Firefox) for web automation. Place the WebDriver in the project directory.
2. **Webcam**: Ensure your webcam is connected and functional for gesture detection.

### Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/screen-control-voice-gestures.git
   ```

2. Run the Python script:
   ```bash
   python screen_control.py
   ```

3. Start giving voice commands or use hand gestures for interaction.

### Example Commands

- "What is the time?" – Fetches the current time.
- "Tell me a joke" – Reads a joke aloud.
- "Search Wikipedia for Python" – Searches Wikipedia for Python and reads the summary.
- "Open Google" – Opens Google in the web browser.
- Hand gestures – Control mouse movements and interact with the screen using hand gestures.

## Future Enhancements

- Integrating voice-to-text for improved web search interactions.
- Adding more gestures for detailed control of specific applications.
- Expanding system commands for better automation and multi-tasking.

## License
This project is licensed under the MIT License.

## Acknowledgements
Thanks to the open-source community for the libraries and resources that made this project possible.
