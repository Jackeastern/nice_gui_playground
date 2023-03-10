from nicegui import ui


def submit_button():
    ui.link('Clock', '/clock').classes(replace='text-white')


def update_result(result, update_value):
    result.set_text(f"Welcome: {update_value}")


def content() -> None:
    ui.input(label='Your Name', placeholder='Insert your name.',
             on_change=lambda e: update_result(result, e.value),
             validation={'Input too long': lambda value: len(value) < 20})
    result = ui.label()
    # the button
    ui.button('Submit', on_click=submit_button)
    # ui.label('This is the home page.').classes('text-h4 font-bold text-grey-8')
