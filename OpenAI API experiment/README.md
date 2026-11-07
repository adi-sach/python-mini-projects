# Jarvis – AI Chatbot

A Python-based conversational AI chatbot powered by OpenAI's GPT-4o model.

Jarvis allows users to interact with an AI assistant through a command-line interface, ask questions, and maintain context throughout a conversation.

## Features

- AI-powered conversational responses
- Powered by OpenAI's GPT-4o model
- Maintains conversation history during a session
- Interactive command-line interface
- Custom system instructions defining the assistant's personality
- Secure API key management using environment variables

## Technologies Used

- Python
- OpenAI Python SDK
- python-dotenv
- OpenAI GPT-4o

## Project Structure

```text
openai-api-experiment/
│
├── client.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/adi-sach/python-mini-projects.git
```

**2. Navigate to the project directory**

```bash
cd python-mini-projects/openai-api-experiment
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key.

Never upload your actual `.env` file or expose your API key publicly.

## How to Run

Execute:

```bash
python client.py
```

Once initialized, you can type questions and interact with Jarvis.

To terminate the chatbot, type:

```text
exit
```

## How It Works

1. Loads API credentials from environment variables.
2. Initializes the OpenAI client.
3. Maintains a conversation history containing user and assistant messages.
4. Sends the conversation to GPT-4o.
5. Displays the generated response in the terminal.
6. Continues the conversation until the user enters `exit`.

## Learning Outcomes

- Integrating external APIs with Python
- Working with language models
- Managing API credentials securely
- Using environment variables
- Maintaining conversational context
- Handling exceptions and API errors

## Future Improvements

- Add voice input and speech output
- Introduce conversation history storage
- Add support for different AI models
- Implement a graphical user interface

---

**Author:** Adi Sach

**Project:** Python Mini Projects
