import flet as ft

def main(page: ft.Page):
    page.title="LISTA DE LA COMPRA"

    
    texto=ft.Text(value="Lista de la compra:",color="blue",size=50)
    page.add(texto)

    textField_Nombre=ft.TextField(hint_text="Escribe tu nombre",label="Nombre")
    page.add(textField_Nombre)

    textField_dia=ft.Text(value="Día/Mes de la compra")
    page.add(textField_dia)

    slider_dia=ft.Slider(min=0,max=7,divisions=7,label="Dia:{value}")
    page.add(slider_dia)

    slider_mes=ft.Slider(min=0,max=12,divisions=12,label="Mes:{value}")
    page.add(slider_mes)

    dropDown_Menu_frutas=ft.Dropdown(width=300,label="Frutas",options=[ft.dropdown.Option("Manzana")])
    page.add(dropDown_Menu_frutas)
    dropDown_Menu_frutas.options.append(ft.dropdown.Option("Frutas"))
    page.update()
    dropDown_Menu_frutas.options.append(ft.dropdown.Option("Verduras"))
    page.update()
    dropDown_Menu_frutas.options.append(ft.dropdown.Option("Carnes"))
    page.update()
    dropDown_Menu_frutas.options.append(ft.dropdown.Option("Otros"))
    page.update()

    class Contador(ft.UserControl):
        def sumar(self, e):
            self.contador += 1
            self.text.value = str(self.contador)
            self.update()
        def build(self):
            self.contador = 0
            self.text = ft.Text(str(self.contador))
            return ft.Row([self.text, ft.ElevatedButton("Añadir", on_click=self.sumar)])
    page.add(Contador())


    texto2=ft.Text(value="Lista total",color="red",size=20)
    page.add(texto2)

    def boton_guardar_lista(e):
        texto2.value = f"Lista total de {textField_Nombre.value} el día {slider_dia.value} del mes {slider_mes.value}: \n {} {dropDown_Menu_frutas.value}:"
        page.update()
        
    boton=ft.FloatingActionButton(icon=ft.icons.FAVORITE, on_click=boton_guardar_lista)
    page.add(boton)

ft.app(target=main)