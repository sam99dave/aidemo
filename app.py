from fasthtml.common import *
from ai_demo.routers.init_app import app
from ai_demo.ui.homepage import navbar, get_homepage_window
from ai_demo.routers import ui_router

# tlink = Script(src="https://cdn.tailwindcss.com")
# dlink = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
# app = FastHTML(hdrs=(tlink, dlink, picolink))

@app.get('/')
def entrypoint():
    return Body(
        navbar(),
        get_homepage_window(),
        cls="w-[100vw] h-[100vh] overflow-y-hidden"
    )



if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)
