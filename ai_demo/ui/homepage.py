from fasthtml.common import *

def navbar():
    return Div(
        Div(
            Div(
                Div(
                    Svg(
                        Path(
                            stroke_linecap="round",
                            stroke_linejoin="round",
                            stroke_width="2",
                            d="M4 6H16M4 12h8m-8 6h16"
                        ),
                        xmlns="http://www.w3.org/2000/svg",
                        cls="h-5 w-5",
                        fill="none",
                        viewBox="0 0 24 24",
                        stroke="currentColor"
                    ),
                    tabindex="0",
                    cls="btn btn-ghost lg"
                ),
                Ul(
                    Li(
                        A(
                            "Image Generation",
                            hx_on="click",
                            hx_get="/image-generation-page",
                            hx_swap="outerHTML",
                            hx_target="#homepage-section"
                        ),
                    ),
                    Li(
                        A(
                            "Chat App",
                            
                        )
                    ),
                    tabindex="0",
                    cls="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow"
                ),
                cls="dropdown"
            ),
            A(
                "AI DEMO",
                cls="btn btn-ghost text-x1"
            ),
            cls="navbar-start"
        ),
        cls="navbar bg-base-100",
    )

def get_homepage_window():
    return Div(
        "Hey this is the homepage!",
        cls="h-[70vh] flex items-center justify-center text-xl",
        id="homepage-section"
    )