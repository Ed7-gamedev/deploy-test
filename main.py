import flet as ft


def main(page: ft.Page):
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        
        
        ft.Container(
            width= 500,
            height= 500,
            
            bgcolor= 'green',
        )
        
        
        
        
        
        
    )
    
    
    
    pass


ft.app(target= main)
