#flet import
# if this errors for you ->pip install flet
import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet.core.control_event import ControlEvent
import validators
import os

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
    default_location = os.path.join(os.path.expanduser("~"),"Downloads")

    #import text
    text_url: TextField = TextField(label='URL', text_align=ft.TextAlign.CENTER, width=300)
    button_submit: ElevatedButton = ElevatedButton(text="Import & Download",width=300, disabled=True)
    button_location: ElevatedButton = ElevatedButton(text = "Choose Location", width = 140)
    
    location_display: TextField = TextField(
        value=default_location,
        read_only=True,
        text_align=ft.TextAlign.LEFT,
        width=240,
        label="Download location"
    )

    def get_directory_result(e: ft.FilePickerResultEvent):
        if e.path:
            location_display.value = e.path
            page.update()
        
    directory_pick = ft.FilePicker(on_result=get_directory_result)
    
    def validate(e: ControlEvent) -> None:
        url = text_url.value.strip() # gets rid of spaces
        if validators.url(url) and url.startswith("https://www.youtube.com/watch?v"):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        
        page.update()

    
    def submit(e: ControlEvent) -> None:
        print("URL to download: ", text_url.value)
        print("Download location: ",location_display.value)
        download(text_url.value, location_display.value)

    def open_directory_dialog(e):
        directory_pick.get_directory_path()
    
    text_url.on_change = validate
    button_submit.on_click = submit
    button_location.on_click = open_directory_dialog




    page.overlay.append(directory_pick)

    page.add(
        Column(
            controls=[
                text_url,
                Row(
                    controls=[
                        location_display,
                        button_location
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                button_submit
            ],
            alignment=ft.MainAxisAlignment.CENTER, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            width=page.width,
            spacing=20
        )
    )
    page.update()



if __name__ == "__main__":
    ft.app(target=main)