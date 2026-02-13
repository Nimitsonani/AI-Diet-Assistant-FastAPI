# AI Diet Assistant - FastAPI

An AI-powered diet planning web application built using FastAPI.  
The application collects user health and lifestyle information, generates a personalized diet plan using a Large Language Model API, and creates a structured downloadable PDF report.

---

## Chat Page

[![Chat Page](https://github.com/user-attachments/assets/4b19c0ad-0c82-4444-a881-ba2eb7cbe385)](https://github.com/user-attachments/assets/4b19c0ad-0c82-4444-a881-ba2eb7cbe385)

---

## Features

- Interactive chat-based diet consultation
- Collects user data step-by-step (age, weight, goals, activity level, etc.)
- Generates personalized diet plans using an LLM API
- Exports the final plan as a structured PDF

---

## Tech Stack

- FastAPI
- Python
- Jinja2
- pdfkit (wkhtmltopdf)
- Markdown
- Mistral LLM API
- HTML/CSS (Templates)

---

## Project Structure

AI-Diet-Assistant-FastAPI  
│  
├── app/  
│   ├── route.py  
│   ├── functions.py  
│   ├── prompt.txt  
│  
├── templates/  
├── pdf/  
├── main.py  
├── requirements.txt  

---

## How It Works

1. The user interacts with the chat interface.
2. The system collects required health and lifestyle details step-by-step.
3. After confirmation, the LLM generates a structured diet plan in JSON format.
4. The plan is converted to HTML using Jinja2.
5. The HTML is rendered into a downloadable PDF using pdfkit.

---

## Setup Instructions

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory and add:

```
MISTRAL_API_KEY= your_mistral_api_key
WKHTML_PATH= path_to_wkhtmltopdf_executable
```

3. Run the project

```bash
python main.py
```

---

## Sample Output

A sample generated diet plan PDF is included in the repository in the PDF folder to demonstrate the output format.
