What better way to learn a language than to speak it?
LangAI is a full-stack speaking practice application that allows users to answer questions verbally, converts their speech to text, and (in future iterations) evaluates grammar and vocabulary usage.

The app currently supports Spanish as the target language and is designed to expand to additional languages in the future.

Tech Stack

Frontend: React (Vite) + MediaRecorder API

Backend: FastAPI (Python)

Speech-to-Text: OpenAI Whisper

Text-to-Speech: Google Cloud Text-to-Speech (Neural2 voices)

Status

Work in Progress

The backend transcription and text-to-speech pipeline are functional.
The frontend is actively being developed to handle recording, playback, and API communication more cleanly.

Future plans include:

Multi-language support

Adaptive question selection

Grammar and vocabulary scoring (Using hugging face models)

Deployment on home lab

This project is being built as a hands-on learning experience in full-stack development and speech AI integration, and combines my passion for technology and language into one app.
