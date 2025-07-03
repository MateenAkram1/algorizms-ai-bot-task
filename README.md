
# 🛣️ Uqaab Voice Assistant Prototype

A lightweight AI chatbot and voice recognition assistant for truck drivers and dispatchers to interact with the **Uqaab system** using natural language commands.

> 🎙️ Speak naturally — get quick system replies like:  
> “Update my route to Lahore” or “What’s my next delivery?”

---

## 📌 Features

✅ Real-time **voice-to-text** (Vosk ASR)  
✅ Intent detection via **rule-based NLP**  
✅ Simulated **system responses**  
✅ Optional **text-to-speech (TTS)** feedback  
✅ Simple **Gradio web interface**

---

## 🛠️ Tech Stack

| Component       | Library/Tool         |
|----------------|----------------------|
| Programming    | Python 3.x           |
| Speech-to-Text | [Vosk](https://alphacephei.com/vosk/) (offline ASR) |
| NLP            | Rule-based matching  |
| UI             | [Gradio](https://www.gradio.app/) |
| TTS (optional) | `pyttsx3`            |

---

## 💬 Supported Voice Commands

- `Update my route to [City]`
- `What’s my next job?`
- `When is my next delivery?`
- `Cancel my current job`
- `Confirm drop-off in [City]`

---

## 🚀 Setup Instructions

### 1. Clone This Repo

```bash
git <Link>
cd directory
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
vosk
sounddevice
numpy
pyttsx3
gradio
```

### 3. Download & Setup Vosk Model

Download an English model (e.g., [vosk-model-small-en-us-0.15](https://alphacephei.com/vosk/models)) and extract it.

Place the extracted folder in the project directory and rename it to:

```
./model/
```

Example structure:

```
uqaab-voice-bot/
├── model/
│   ├── am
│   ├── conf
│   └── ...
```

---

## ▶️ Running the App

```bash
python main.py
```

Open the Gradio UI in your browser. Link will be provided in the terminal when you run the main.py.  
Click “🎙️ Press to Speak”, then say one of the supported phrases.

---

## 📂 Project Structure

```
.
├── main.py                # Gradio UI and logic
├── voice_input.py         # Vosk voice recorder with silence detection
├── intent_parser.py       # Rule-based NLP for command extraction
├── response_generator.py  # Simulated system response
├── text_to_speech.py      # Optional TTS using pyttsx3
├── model/                 # Vosk offline model folder
└── README.md
```

---

## 📈 Future Enhancements

- 📡 Integrate real Uqaab API endpoints  
- 🌐 Multilingual support with other Vosk models  
- 🗣️ Use webrtcvad for advanced VAD  
- 🧠 Switch to Rasa or Dialogflow for advanced NLP  
- 🖥️ Desktop version with PyQt or Electron

---

## 🧑‍💻 Developed By

**Mateen Akram**  

## 📄 License

This project is for internal prototyping and demonstration only. Not for production use.
