from fasthtml.common import *

image_loading_js = """
        // Function to change the text of the div
        function handleAfterRequest() {
            console.log("HTMX request completed!");
            const textDiv = document.getElementById('output-placeholder');
            textDiv.innerText = 'Generation in Progress';  // Change to your desired text
        }
"""

replace_span = """
        // Function to replace the original span with a loading span (Used during generating image)
        function replaceSpan() {
            // Select the original span
            const originalSpan = document.getElementById('originalSpan');

            // Create a new span element with the desired classes
            const newSpan = document.createElement('span');
            newSpan.className = 'loading loading-ring loading-lg';

            // Replace the original span with the new span
            originalSpan.parentNode.replaceChild(newSpan, originalSpan);
        }
"""

def get_sidebar():
    return Div(
        Form(
            Script(replace_span),
            hx_post="/img_gen_form_submit",
            hx_target='#imagegen-window',
            hx_swap="innerHTML",
            ## NOTE: Some issue with below line (adding onclick to the Form Button does the Job!)
            # hx_on='htmx:afterRequest: handleAfterRequest()',
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
                onclick='replaceSpan()',
                cls="btn btn-square w-[80px] h-[50px]"
            )
        ),
        # A("Progress Status", id="output-placeholder"),
        cls="flex flex-col space-y-4 w-[300px] p-1 bg-gray-500 text-white rounded"
    )


def get_resizer():
    return Div(
        cls="resizer bg-green-100"
    )

def get_taskwindow():
   return Div(
        Div(
            Span("Output Image Will Come here", id='originalSpan'),
            id='output-placeholder', # used with `image_loading_js`
            cls='flex w-[784px] h-[784px] justify-center items-center',
            
        ),
        cls="flex justify-center w-screen items-center",
        id='imagegen-window'
   ) 

def get_img_container(src_url= ""):
    src_url = f"{src_url}download=image.png" # converting the public url to be downloadable
    return Img(
        src=src_url,
        alt='Generated Image',
        cls="w-[784px] h-[784px]"
    ), A(
        "Donwload",
        href=src_url,
    )

def main_page():
    sidebar = get_sidebar()
    return Div(
            sidebar,
            get_taskwindow(),
            cls="flex w-full max-w h-[874px] px-4 py-2 space-x-4"
    )