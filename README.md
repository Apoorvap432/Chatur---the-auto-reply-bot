# 🎙️ Chatur - AI Voice Assistant Bot

**Chatur** is a Python-based voice assistant that uses **speech recognition, natural language processing, text-to-speech, and API integration** to perform hands-free tasks through voice commands.

The assistant continuously listens for the wake word **"Chatur"**, processes the user's command, performs the requested action, and provides spoken feedback.

---

## ✨ Features

### 🎤 1. Voice Recognition & Activation

* Continuously listens for the wake word **"Chatur"**.
* Uses the **Google Speech Recognition API** for speech-to-text conversion.
* Provides audio confirmation when activated.
* Configurable microphone sensitivity using an energy threshold.
* Supports adjustable speech timeout and phrase limits for better recognition.

---

### 🌐 2. Web Navigation

Open websites using simple voice commands.

| Voice Command   | Action         |
| --------------- | -------------- |
| `Open Google`   | Opens Google   |
| `Open YouTube`  | Opens YouTube  |
| `Open LinkedIn` | Opens LinkedIn |

The project uses Python's built-in `webbrowser` module to launch websites.

---

### 🎵 3. Music Streaming

Chatur includes a pre-configured music library containing YouTube links.

Use commands such as:

```text
Play TMKOC
Play Lover
Play Doraemon Song
```

#### Available Tracks

* TMKOC
* Never Ending Story
* Stranger Things Rap
* Lover
* Running Up That Hill
* Doraemon Song

The bot handles unavailable or unrecognized songs gracefully.

---

### 📰 4. News Aggregation

Chatur can fetch the latest news using **NewsAPI**.

Voice command:

```text
News
```

The assistant:

1. Fetches the latest news from India.
2. Retrieves the top 3 headlines.
3. Displays the headlines in the console.
4. Converts the headlines into speech using text-to-speech.

The application also includes timeout handling and error management for API failures.

---

### 💬 5. Custom Q&A System

Chatur includes a customizable question-answer system through `qaLibrary.py`.

Example questions:

```text
What is your name?
Tell me a joke
How are you?
```

The Q&A library is modular, making it easy to add new questions and responses without modifying the core bot logic.

---

### 🔊 6. Text-to-Speech Feedback

Chatur uses **pyttsx3** to provide spoken responses.

The assistant can:

* Confirm that a command was received.
* Inform the user about the action being performed.
* Read news headlines aloud.
* Respond to custom questions.
* Provide error messages through voice.

This allows the assistant to operate without requiring the user to constantly look at the screen.

---

## 🛠️ Tech Stack

| Technology                        | Purpose                            |
| --------------------------------- | ---------------------------------- |
| **Python 3.x**                    | Core programming language          |
| **SpeechRecognition**             | Speech-to-text conversion          |
| **Google Speech Recognition API** | Voice recognition                  |
| **pyttsx3**                       | Text-to-speech                     |
| **Requests**                      | API communication                  |
| **NewsAPI**                       | Fetching live news                 |
| **webbrowser**                    | Opening websites and YouTube links |

---

## 📁 Project Structure

```text
Chatur---the-auto-reply-bot/
│
├── main.py              # Core assistant logic
├── musicLibrary.py      # Music and YouTube links
├── qaLibrary.py         # Custom question-answer library
└── README.md            # Project documentation
```

---

## ⚙️ How It Works

The basic workflow of Chatur is:

```text
        ┌──────────────────┐
        │  User Speaks     │
        └────────┬─────────┘
                 ↓
        ┌──────────────────┐
        │ Speech Recognition│
        └────────┬─────────┘
                 ↓
        ┌──────────────────┐
        │ Command Parsing  │
        └────────┬─────────┘
                 ↓
        ┌─────────────────────────────┐
        │       Action Selection      │
        └─────────────┬───────────────┘
                      ↓
       ┌──────────────┼───────────────┐
       ↓              ↓               ↓
   Web Search       Music            News
       │              │               │
       └──────────────┼───────────────┘
                      ↓
             ┌────────────────┐
             │ Text-to-Speech │
             └───────┬────────┘
                     ↓
             Voice Response
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Chatur---the-auto-reply-bot.git
```

Navigate to the project directory:

```bash
cd Chatur---the-auto-reply-bot
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install SpeechRecognition pyttsx3 requests
```

Depending on your operating system, you may also need an audio input library such as:

```bash
pip install PyAudio
```

### 3. Configure NewsAPI

Create an API key from [NewsAPI](https://newsapi.org/) and configure it in the project.

> **Important:** Do not commit your API key directly to GitHub. Use an environment variable or `.env` file instead.

### 4. Run the Assistant

```bash
python main.py
```

Once the application starts, say:

```text
Chatur
```

and wait for the assistant to activate.

---

## 🎯 Example Commands

```text
Chatur
Open Google

Chatur
Open YouTube

Chatur
Play Lover

Chatur
News

Chatur
What is your name?

Chatur
Tell me a joke
```

---

## 🧠 Learning Outcomes

This project demonstrates practical experience with:

* Speech recognition
* Text-to-speech synthesis
* Python automation
* API integration
* Voice command processing
* Exception handling
* Modular code organization
* Third-party Python libraries
* Debugging and logging
* Interactive user experience

---

## 💡 Use Cases

Chatur can be used as:

* 🎤 A personal voice assistant
* 🌐 A voice-controlled web navigation tool
* 🎵 A voice-controlled music player
* 📰 A hands-free news reader
* 💬 An interactive Q&A assistant
* 🖥️ A desktop automation tool

---

## 🔮 Future Enhancements

Possible improvements include:

* 🌦️ Weather API integration
* 📧 Email automation
* 📅 Calendar and reminder integration
* 🎵 Spotify or YouTube API integration
* 🧠 Machine-learning-based personalized responses
* 🌍 Multi-language voice support
* 📊 Voice command history and analytics
* 🏠 Smart-home device integration
* 🔐 Secure environment-variable-based API management
* 🤖 More advanced natural-language command processing

---

## 👩‍💻 Author

**Apoorva Panwar**

If you found this project useful or interesting, consider ⭐ starring the repository.
