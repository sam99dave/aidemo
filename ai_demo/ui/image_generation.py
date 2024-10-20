from fasthtml.common import *

def get_sidebar():
    return Div(
        Form(
            hx_post="/img_gen_form_submit",
            hx_target='#imagegen-window',
            hx_swap="innerHTML",

        )(
            # Select(
            #     Option(
            #         "Option 1"
            #     ),
            #     Option(
            #         "Option 2"
            #     ),
            #     cls="select select-bordered w-full max-w-xs py-2",
            #     name="selectOption"
            # ),
            Input(type="text", id="promptInput", name="promptInput", placeholder="A cat drinking tea"),
            Input(type="number", name="width", placeholder="Width"),
            Input(type="number", name="height", placeholder="Height"),
            Input(type="number", name="steps", placeholder="Inference Steps"),
            Button(
                "Submit",
                cls="btn btn-square w-[80px] h-[50px]"
            )
        ),
        cls="flex flex-col space-y-4 w-[300px] p-1 bg-gray-500 text-white rounded"
    )


def get_resizer():
    return Div(
        cls="resizer bg-green-100"
    )

def get_taskwindow():
   return Div(
        Div(
            "Output Image Will Come here",
            cls='w-[784px] h-[784px]'
        ),
        cls="flex justify-center w-screen items-center",
        id='imagegen-window'
   ) 

def get_img_container(src_url= ""):
    return Img(
        src=src_url,
        alt='Generated Image',
        cls="w-[784px] h-[784px]"
    )

def main_page():
    sidebar = get_sidebar()
    return Div(
            sidebar,
            get_taskwindow(),
            cls="flex w-full max-w h-[874px] px-4 py-2 space-x-4"
    )