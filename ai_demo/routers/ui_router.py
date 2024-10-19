from ai_demo.routers.init_app import app
from ai_demo.ui.image_generation import main_page

@app.get('/image-generation-page')
def img_gen_page():
    return main_page()

@app.post('/img_gen_form_submit')
def test(promptInput:str, selectOption: str):
    #  print(f"promptInput: {promptInput}")
    print(f"promptInput: {promptInput}\nselectOption: {selectOption}")