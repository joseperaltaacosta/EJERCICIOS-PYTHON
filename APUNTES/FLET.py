import flet as ft

def main(page: ft.Page):
    page.title="FLET"
    def cambiarColor(e):
        texto.color="brown"
        page.update()
    def cambiarTextos(e):
        for i in range (10):
            text=ft.Text(value=f"Texto numero {i}", size=30)
            page.add(text)
    #Componente texto
    texto=ft.Text(value="Introducción a Flet",color="blue",size=50)
    page.add(texto) #add hace dos cosas: 1-Añadir 2-Actualizar
    texto.value="Cambiando datos"
    page.update()
    #Componente Boton
    boton=ft.FloatingActionButton(icon=ft.icons.FAVORITE, on_click=cambiarTextos)
    page.add(boton)

ft.app(target=main)