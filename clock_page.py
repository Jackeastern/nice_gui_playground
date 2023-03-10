import theme

from nicegui import ui


def create() -> None:

    @ui.page('/clock')
    def clock_page():
        with theme.frame('- Example A -'):
            ui.label('Example A').classes('text-h4 text-grey-8')
