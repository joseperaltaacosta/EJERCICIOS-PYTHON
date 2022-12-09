import flet as ft

def main(page: ft.Page):
    page.title="FLET"
    def cambiarColor(e):
        texto.color="brown"
        page.update()
    def cambiarTextos(e):
        texto.value=textField_Nombre.value
        page.update()
    #Componente texto
    texto=ft.Text(value="Introducción a Flet",color="blue",size=50)
    page.add(texto) #add hace dos cosas: 1-Añadir 2-Actualizar
    texto.value="Cambiando datos"
    page.update()
    #Componente Boton
    boton=ft.FloatingActionButton(icon=ft.icons.FAVORITE, on_click=cambiarTextos)
    page.add(boton)
    
    textField_Nombre=ft.TextField(hint_text="Escribe tu nombre",label="Nombre")
    page.add(textField_Nombre)

    dropDown_Menu=ft.Dropdown(width=300,options=[ft.dropdown.Option("Vieja")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Nueva"))
    page.update()

    slider_edad=ft.Slider(min=0,max=100,divisions=100,label="Edad:{value}")
    page.add(slider_edad)

ft.app(target=main)