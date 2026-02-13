from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, FileResponse

from app.functions import get_response, my_list

app = FastAPI()
template = Jinja2Templates(directory='templates')


@app.get('/')
def home(request:Request):
    return template.TemplateResponse(name='home.html',request=request)

count=0
@app.get('/count')
def home():
    global count
    count+=1
    return count


process_running=False

@app.get('/chat')
def chat(request:Request):
    return template.TemplateResponse(name='chat.html',request=request,context={'my_list':my_list})

@app.post('/chat')
def chat(user_data = Form(...)):
    global process_running
    if not process_running:
        process_running = True

        response_nova = get_response(user_data)
        if response_nova:
            process_running=False
            return RedirectResponse(url='/chat',status_code=303)
        return 'Nova is not available right now. try later'
    return RedirectResponse(url='/chat', status_code=303)

@app.get('/download')
def download():
    return FileResponse(path='./pdf/diet_plan.pdf', filename='diet_plan.pdf', media_type='pdf')