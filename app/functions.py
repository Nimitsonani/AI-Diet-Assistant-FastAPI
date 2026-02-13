import markdown
import requests
import json
import jinja2
import pdfkit
import os
from dotenv import load_dotenv

load_dotenv('.env')

with open('./app/prompt.txt') as file:
    system_prompt = file.read()

my_list=[{"role":"system","content":system_prompt},
         {"role":"assistant","content":"Hi! i am your personal Diet Assistant Nova."}]



def make_pdf(my_dict):
    for i in my_dict:
        if 'Meal' in i:
            for j in my_dict[i]:
                    my_dict[i][j] = markdown.markdown(my_dict[i][j])
        else:
            my_dict[i] = markdown.markdown(my_dict[i])

    context = {'my_dict': my_dict}

    template_loader = jinja2.FileSystemLoader('./templates')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('pdf.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf=os.getenv('WKHTML_PATH'))
    pdfkit.from_string(output_text, './pdf/diet_plan.pdf', configuration=config)


def get_response(user_data):
    my_list.append({"role":"user","content":str(user_data)})

    payload = {
                'model': 'mistral-large-latest',
                "messages" : my_list
    }
    headers = {
        'Authorization': f'Bearer {os.getenv("MISTRAL_API_KEY")}',
        'Content-Type': 'application/json'
    }

    res = requests.post(url='https://api.mistral.ai/v1/chat/completions', json=payload, headers=headers)
    try:
        res = res.json()
    except Exception as e:
        print(res.text)
        print(e)
        return False

    try:
        content = res['choices'][0]['message']['content']
        if '"diet_meal_generated":"yes"' in content[:800]:
            first_curly_index = content.index('{')
            content = content[first_curly_index:]
            content = content.replace('```', '')
            my_list.append({"role": "assistant", "content": content})
            ans = json.loads(content,strict=False)
            print(ans)
            make_pdf(ans)
            return 'pdf_generated'
        else:
            ans = markdown.markdown(content,extensions=['extra'])

    except Exception as e:
        print(res)
        print(e)
        return False
    else:
        my_list.append({"role":"assistant","content":ans})
        return ans
