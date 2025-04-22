import flet as ft


def main(page: ft.Page):

    page.bgcolor= 'white'
    
    
    page.add(
        
        
        ft.Container(
            width= 500,
            height= 500,
            bgcolor= 'green',
        )
        
    )
    
    
    
    


ft.app(target= main)
