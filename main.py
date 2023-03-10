# Import the nicegui
import clock_page
import welcome_page
import theme

from nicegui import ui


# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame('Welcome'):
        welcome_page.content()


# this call shows that you can also move the whole page creation into a separate file
clock_page.create()


ui.run(title='Clock Welcome Application')
"""



# Create the ui
ui.input(label='Text', placeholder='start typing',
         on_change=lambda e: result.set_text('you typed: ' + e.value),
         validation={'Input too long': lambda value: len(value) < 20})


result = ui.label()

def frame(navtitle: str):
    '''Custom page frame to share the same styling and behavior across all pages'''
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    with ui.header().classes('justify-between text-white'):
        ui.label('Modularization Demo').classes('font-bold')
        ui.label(navtitle)
        with ui.row():
            menu()
    with ui.row().classes('absolute-center'):
        yielddef clearing_clock_show():
    ui.clear

# the button
ui.button('Click me!', on_click=lambda: ui.notify(f'You clicked me!'))

ui.run()
"""
