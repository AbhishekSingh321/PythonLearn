# 🔊 Text-to-Speech (TTS) Comparison in Python

This repository demonstrates **four different Text-to-Speech (TTS) implementations in Python**, from offline engines to advanced AI-based voice generation.
The goal is to **compare features, quality, performance, and use-cases** so you can choose the right TTS tool for your project.

---

## 📁 Project Structure

```
TTS/
│
├── output/
│   ├── voice_tts1.mp3
│   ├── voice_tts2.mp3
│   ├── voice_tts3.mp3
│   ├── voice_tts4.mp3
│
├── tts1.py          # pyttsx3 (Offline TTS)
├── tts2.py          # gTTS (Google Text-to-Speech)
├── tts3.py          # edge-tts (Microsoft Neural Voices)
├── tts4.py          # ElevenLabs (AI Voice)
│
├── .env             # API keys
├── requirements.txt
└── README.md
```

---

## 🚀 Implemented TTS Engines

### 1️⃣ pyttsx3 (Offline Text-to-Speech)

**File:** `tts1.py`

* Fully offline
* Uses system-installed voices
* Fast and lightweight

**Pros**

* No internet required
* Adjustable rate & volume
* Good for local scripts

**Cons**

* Robotic voice
* No emotion or pitch control

**Best Use Case**

* Offline tools
* Accessibility scripts
* System automation

---

### 2️⃣ gTTS (Google Text-to-Speech)

**File:** `tts2.py`

* Uses Google Translate TTS
* Internet required
* Supports multiple languages

**Pros**

* Simple API
* Good pronunciation
* Multilingual support

**Cons**

* Limited voice control
* Depends on Google service

**Best Use Case**

* Language learning
* Simple narration
* Demo projects

---

### 3️⃣ edge-tts (Microsoft Neural TTS)

**File:** `tts3.py`

* Uses Microsoft Edge Neural Voices
* High-quality natural speech
* Free and powerful

**Pros**

* Neural voices
* Rate, pitch, and volume control
* Multiple accents

**Cons**

* Internet required
* No deep emotion control

**Best Use Case**

* YouTube narration
* Podcasts
* Professional voiceovers (free)

---

### 4️⃣ ElevenLabs (AI Voice Generation)

**File:** `tts4.py`

* State-of-the-art AI voices
* Human-like emotions
* Requires API key

**Pros**

* Ultra-realistic voices
* Multilingual
* Emotional tone support

**Cons**

* Paid limits
* API dependency

**Best Use Case**

* Audiobooks
* AI assistants
* Commercial applications

---

## 📊 Comparison Table

| Feature           | pyttsx3    | gTTS       | edge-tts   | ElevenLabs         |
| ----------------- | ---------- | ---------- | ---------- | ------------------ |
| Internet Required | ❌ No       | ✅ Yes      | ✅ Yes      | ✅ Yes              |
| Voice Quality     | ⭐⭐         | ⭐⭐⭐        | ⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐              |
| Emotion Control   | ❌ No       | ❌ No       | ⚠️ Limited | ✅ Yes              |
| Speed Control     | ✅ Yes      | ⚠️ Limited | ✅ Yes      | ✅ Yes              |
| Pitch Control     | ❌ No       | ❌ No       | ✅ Yes      | ✅ Yes              |
| Multilingual      | ⚠️ Limited | ✅ Yes      | ✅ Yes      | ✅ Yes              |
| Offline Support   | ✅ Yes      | ❌ No       | ❌ No       | ❌ No               |
| Commercial Use    | ✅ Yes      | ⚠️ Limited | ✅ Yes      | ⚠️ Depends on plan |

---

## 🛠 Installation

### 1️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Variables (ElevenLabs)

Create a `.env` file:

```
ELEVENLABS_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

```
python tts1.py
python tts2.py
python tts3.py
python tts4.py
```

Generated audio files will be saved in the `output/` directory.

---

## 🎯 Which TTS Should You Choose?

* **Offline & simple** → `pyttsx3`
* **Quick multilingual demo** → `gTTS`
* **Best free neural voice** → `edge-tts`
* **Most realistic AI voice** → `ElevenLabs`

---

## 📌 Learning Outcome

By completing this project, you will:

* Understand different TTS engines
* Compare offline vs cloud-based TTS
* Learn voice control parameters
* Build AI voice-based applications

---

## 📚 References

Official documentation and resources used in this project:

* **pyttsx3**: [https://pypi.org/project/pyttsx3/](https://pypi.org/project/pyttsx3/)
* **gTTS (Google Text-to-Speech)**: [https://pypi.org/project/gTTS/](https://pypi.org/project/gTTS/)
* **edge-tts (Microsoft Neural TTS)**: [https://pypi.org/project/edge-tts/](https://pypi.org/project/edge-tts/)
* **ElevenLabs API Docs**: [https://elevenlabs.io/docs/developers/quickstart](https://elevenlabs.io/docs/developers/quickstart)

---
