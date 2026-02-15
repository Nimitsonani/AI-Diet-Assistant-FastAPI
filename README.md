# AI Diet Assistant - FastAPI

This is a diet planning web application built with FastAPI.

The user interacts through a chat-style interface.  
The system collects health and lifestyle details step-by-step, generates a structured diet plan using an LLM, and exports the final result as a downloadable PDF.

---

## What This Project Does

The application works like a guided consultation.

Instead of asking everything at once, it collects information gradually:

- Age  
- Weight  
- Height  
- Activity level  
- Dietary goals  
- Food preferences  

Once all required inputs are collected and confirmed, the data is sent to a Large Language Model.

The model generates a structured diet plan in JSON format.  
That structured output is then rendered into HTML and converted into a PDF file.

So the system combines:

- Conversational data collection  
- Structured LLM output  
- Server-side HTML rendering  
- PDF generation  

---

## Chat Interface

[![Chat Page](https://github.com/user-attachments/assets/4b19c0ad-0c82-4444-a881-ba2eb7cbe385)](https://github.com/user-attachments/assets/4b19c0ad-0c82-4444-a881-ba2eb7cbe385)

---

## How It Works Internally

1. The user interacts with the chat UI.
2. The backend stores responses progressively.
3. Once all required inputs are gathered, the system constructs a structured prompt.
4. The LLM returns a JSON-based diet plan.
5. The JSON is injected into a Jinja2 HTML template.
6. The HTML is converted into a PDF using `pdfkit` (wkhtmltopdf).
7. The generated PDF is saved and made available for download.

The LLM is used only for generating the plan content.  
Formatting and PDF generation are handled server-side.

---

## Tech Stack

- FastAPI
- Python
- Jinja2 (HTML templating)
- pdfkit (wkhtmltopdf)
- Mistral LLM API
- HTML / CSS

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

## Running Locally

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory:

```
MISTRAL_API_KEY=your_mistral_api_key
WKHTML_PATH=path_to_wkhtmltopdf_executable
```

- `MISTRAL_API_KEY` is required for generating the diet plan.
- `WKHTML_PATH` should point to your local wkhtmltopdf executable.

3. Run the project:

```
python main.py
```

---

## Sample Output

A sample generated diet plan PDF is included in the `pdf/` folder to demonstrate the output format.
