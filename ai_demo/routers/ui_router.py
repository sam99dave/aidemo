from ai_demo.routers.init_app import app
from ai_demo.ui.image_generation import *
from ai_demo.backend.image_gen import *
from ai_demo.backend.storage_management import *

@app.get('/image-generation-page')
def img_gen_page():
    print("Rendering the Main Page for Image Generation(Text-2-Image)!")
    return main_page()

@app.post('/img_gen_form_submit')
def imagegen_api_call(promptInput:str, width: str, height: str):
    print(f'Form has been submitted, HF model will soon be called!')
    print(f"promptInput: {promptInput}\nwidth: {width}\nheight: {height}")

    if not width.isnumeric():
        width = 1024
    if not height.isnumeric():
        height = 1024
    
    payload = {
        'inputs': promptInput,
        # 'parameters': {
        #     'target_size': {
        #     'width': width,
        #     'height': height       
        #     }
        # }
    }

    image = generate_image(payload)

    image.save('/tmp/local-save.png')
    
    public_url = upload_supabse('/tmp/local-save.png')

    return get_img_container(src_url=public_url)