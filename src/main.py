#flet import
# if this errors for you ->pip install flet
import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet.core.control_event import ControlEvent


print('project started')



def main(page: ft.Page) -> None: # Main Method
    print("Entered main method")
    page.title = "ArgBot Converter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'dark'
    page.window_width = 600
    page.window_height = 400
    page.window_resizable = False

    #import text
    text_import: TextField = TextField(label='URL', text_align=ft.TextAlign.CENTER, width=300)
    button_submit: ElevatedButton = ElevatedButton(text="Import & Download",width=300, disabled=True)
    
    page.add(
        Column(
            controls=[
                text_import,
                button_submit
            ],
            alignment=ft.MainAxisAlignment.CENTER, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            width=page.width 
        )
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main)

