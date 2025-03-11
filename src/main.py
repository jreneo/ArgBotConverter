#flet import
# if this errors for you ->pip install flet
import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet.core.control_event import ControlEvent
import validators

from downloader import download
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
    text_url: TextField = TextField(label='URL', text_align=ft.TextAlign.CENTER, width=300)
    button_submit: ElevatedButton = ElevatedButton(text="Import & Download",width=300, disabled=True)
    
    def validate(e: ControlEvent) -> None:
        url = text_url.value.strip() # gets rid of spaces
        if validators.url(url) and url.startswith("https://www.youtube.com/watch?v"):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        
        page.update()

    
    def submit(e: ControlEvent) -> None:
        print("URL to download: ", text_url.value)
        download(text_url.value)
    
    text_url.on_change = validate
    button_submit.on_click = submit





    page.add(
        Column(
            controls=[
                text_url,
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