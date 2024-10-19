from fasthtml.common import *

def get_sidebar():
    return Div(
        Form(
            hx_post="/img_gen_form_submit",
            hx_target="#test-display",
            hx_swap="outerHTML",

        )(
            Select(
                Option(
                    "Option 1"
                ),
                Option(
                    "Option 2"
                ),
                cls="select select-bordered w-full max-w-xs",
                name="selectOption"
            ),
            Input(type="text", id="promptInput", name="promptInput", placeholder="A cat drinking tea"),
            Button(
                "Submit",
                cls="btn btn-square"
            )
        ),
        cls="flex flex-col space-y-4 w-[400px] p-1 bg-gray-500 text-white rounded"
    )
    # return Div(

    #     Select(
    #         Option(
    #             "Option 1"
    #         ),
    #         Option(
    #             "Option 2"
    #         ),
    #         cls="select select-bordered w-full max-w-xs",

    #     ),
#     cls="flex flex-col space-y-4 w-[300px] p-1 bg-gray-500 text-white rounded"
    # )

def get_taskwindow():
   return Div(
       Div(
           cls="flex justify-center bg-red-200 h-[512px] w-[512px]",
           id="test-display",
       ),
       cls="flex-1 p-5 bg-gray-700 text-white rounded"
   ) 

def main_page():
    sidebar = get_sidebar()
    return Div(
            sidebar,
            get_taskwindow(),
            cls="flex w-full max-w h-[874px] px-4 py-2 space-x-4"
    )