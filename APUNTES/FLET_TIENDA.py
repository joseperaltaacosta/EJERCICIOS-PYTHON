import flet as ft

def main(page: ft.Page):
    page.title="LISTA DE LA COMPRA"
    def Lista(a):
        def Nombre(b):
        b.value=textField_Nombre.hint_text
        def Dia(c):
        c.value=textField_dia.value
    page.update()
        
    texto=ft.Text(value="Lista de la compra:",color="blue",size=50)
    page.add(texto)
    
    boton=ft.FloatingActionButton(icon=ft.icons.FAVORITE, on_click=Lista)
    page.add(boton)
    
    textField_Nombre=ft.TextField(hint_text="Escribe tu nombre",label="Nombre")
    page.add(textField_Nombre)

    textField_dia=ft.Text(value="Día/Mes de la compra")
    page.add(textField_dia)

    slider_dia=ft.Slider(min=0,max=7,divisions=7,label="Dia:{value}")
    page.add(slider_dia)

    slider_mes=ft.Slider(min=0,max=12,divisions=12,label="Mes:{value}")
    page.add(slider_mes)

    dropDown_Menu=ft.Dropdown(width=300,label="Tipos de productos",options=[ft.dropdown.Option("Bebidas")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Frutas"))
    page.update()
    dropDown_Menu.options.append(ft.dropdown.Option("Verduras"))
    page.update()
    dropDown_Menu.options.append(ft.dropdown.Option("Carnes"))
    page.update()
    dropDown_Menu.options.append(ft.dropdown.Option("Otros"))
    page.update()

ft.app(target=main)