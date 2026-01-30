# 🤖 Jarvis – AI Powered Voice Assistant

Jarvis is a **Python-based AI voice assistant** inspired by Alexa/Jarvis, capable of understanding voice commands, performing system tasks, holding intelligent conversations, and **remembering user information across sessions**.

This project demonstrates the integration of **Machine Learning, Natural Language Processing (NLP), Large Language Models (LLMs), and system automation** in a modular and scalable architecture.

---

## ✨ Features

- 🎤 **Speech-to-Text** voice input  
- 🔊 **Text-to-Speech** voice output  
- 🧠 **Machine Learning based intent classification**  
- 🤖 **LLM (ChatGPT API) powered conversational intelligence**  
- 🧠 **Persistent memory** (remembers user information across sessions)  
- 🖥️ **System automation** (open applications, get date/time)  
- 🧩 **Clean and modular architecture** for easy scalability  

---

## 🏗️ Architecture Overview

```

Voice Input
↓
Speech Recognition
↓
Intent Classifier (ML)
↓
Known Intent ───▶ Skill Modules
Unknown Intent ─▶ LLM (ChatGPT)
↓
Text-to-Speech Output

```

---

## 📁 Project Structure

```

JARVIS_AI/
│
├── ai/                # ML model & LLM brain
├── core/              # Listener, Speaker, Command Router
├── skills/            # System & datetime actions
├── memory/            # Persistent memory system
├── utils/             # Configuration files
├── main.py            # Entry point
├── requirements.txt   # Dependencies
└── README.md

````

---

## 🚀 Technologies Used

- **Python**
- **SpeechRecognition**
- **pyttsx3**
- **scikit-learn**
- **Natural Language Processing (NLP)**
- **OpenAI / ChatGPT API**
- **Machine Learning**

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/riju4924/JARVIS_AI.git
cd JARVIS_AI
````

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add OpenAI API Key

Create a file:

```
utils/config.py
```

```python
OPENAI_API_KEY = "your_api_key_here"
```

### 5️⃣ Run Jarvis

```bash
python main.py
```

---

## 🎤 Example Voice Commands

* **“Jarvis what is the time”**
* **“Jarvis open calculator”**
* **“Jarvis explain machine learning”**
* **“Jarvis remember my name is Riju”**
* **“Jarvis what is my name”**
* **“Jarvis stop”**

---

## 🧠 Key Learning Outcomes

* Machine learning–based intent classification
* Voice-driven AI system design
* Modular software architecture
* Integration of LLMs with traditional ML
* Persistent memory handling

---

## 🔮 Future Enhancements

* GUI dashboard (Tkinter / PyQt)
* Offline LLM support
* Context-aware conversational memory
* Cloud deployment

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Mrinmoy Mukherjee**
B.Tech CSE (AI/ML) Student
