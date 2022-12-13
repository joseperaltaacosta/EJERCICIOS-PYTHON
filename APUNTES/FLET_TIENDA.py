import flet as ft
#PAGINA TOTAL
def main(page: ft.Page):
    page.title="LISTA DE LA COMPRA"

    #TITULO
    texto=ft.Text(value="Lista de la compra:",color="blue",size=50)
    page.add(texto)


    #NOMBRE DE LA PERSONA
    textField_Nombre=ft.TextField(hint_text="Escribe tu nombre",label="Nombre")
    page.add(textField_Nombre)


    #DIA DE LA COMPRA
    textField_dia=ft.Text(value="Día/Mes de la compra")
    page.add(textField_dia)
    slider_dia=ft.Slider(min=0,max=7,divisions=7,label="Dia:{value}")
    page.add(slider_dia)


    #MES DE LA COMPRA
    slider_mes=ft.Slider(min=0,max=12,divisions=12,label="Mes:{value}")
    page.add(slider_mes)


    #FRUTAS
    dropDown_Menu_frutas=ft.Dropdown(width=300,label="Frutas",options=[ft.dropdown.Option("Manzana roja"),
                                                                        ft.dropdown.Option("Manzana verde"),
                                                                        ft.dropdown.Option("Aguacate"),
                                                                        ft.dropdown.Option("Albaricoque"),
                                                                        ft.dropdown.Option("Arándano"),
                                                                        ft.dropdown.Option("Cereza"),
                                                                        ft.dropdown.Option("Ciruela"),
                                                                        ft.dropdown.Option("Coco"),
                                                                        ft.dropdown.Option("Kiwi"),
                                                                        ft.dropdown.Option("Lima"),
                                                                        ft.dropdown.Option("Naranja")])
    page.update()


    #CONTADOR FRUTAS
    class Contador(ft.UserControl):
        def sumar(self, e):
            self.contador += 1
            self.text.value = str(self.contador)
            self.update()
        def build(self):
            self.contador = 0
            self.text = ft.Text(str(self.contador))
            return ft.Row([self.text, ft.ElevatedButton("Añadir", on_click=self.sumar)])
    #page.add(Contador())


    #VERDURAS
    dropDown_Menu_verduras=ft.Dropdown(width=300,label="Verduras",options=[ft.dropdown.Option("Pepino")])
    #page.add(dropDown_Menu_verduras)
    dropDown_Menu_verduras.options.append(ft.dropdown.Option("Rábano"))
    page.update()
    dropDown_Menu_verduras.options.append(ft.dropdown.Option("Berengena"))
    page.update()
    dropDown_Menu_verduras.options.append(ft.dropdown.Option("Lechuga"))
    page.update()
    dropDown_Menu_verduras.options.append(ft.dropdown.Option("Pimiento"))
    page.update()
    dropDown_Menu_verduras.options.append(ft.dropdown.Option("Zanahoria"))
    page.update()
    dropDown_Menu_verduras.options.append(ft.dropdown.Option("Tomate"))
    page.update()
    dropDown_Menu_verduras.options.append(ft.dropdown.Option("Melón"))
    page.update()
    dropDown_Menu_verduras.options.append(ft.dropdown.Option("Sandía"))
    page.update()
    dropDown_Menu_verduras.options.append(ft.dropdown.Option("Calabacín"))
    page.update()
    dropDown_Menu_verduras.options.append(ft.dropdown.Option("Remolacha"))
    page.update()


    #CONTADOR VERDURAS
    class Contador2(ft.UserControl):
        def sumar2(self, e):
            self.contador2 += 1
            self.text2.value = str(self.contador2)
            self.update()
        def build(self):
            self.contador2 = 0
            self.text2 = ft.Text(str(self.contador2))
            return ft.Row([self.text2, ft.ElevatedButton("Añadir", on_click=self.sumar2)])
    #page.add(Contador2())


    #BEBIDAS
    dropDown_Menu_bebidas=ft.Dropdown(width=300,label="Bebidas",options=[ft.dropdown.Option("Botella agua 0,5L")])
    #page.add(dropDown_Menu_bebidas)
    dropDown_Menu_bebidas.options.append(ft.dropdown.Option("Botella agua 1L"))
    page.update()
    dropDown_Menu_bebidas.options.append(ft.dropdown.Option("Botella agua 2L"))
    page.update()
    dropDown_Menu_bebidas.options.append(ft.dropdown.Option("Latas cocacola"))
    page.update()
    dropDown_Menu_bebidas.options.append(ft.dropdown.Option("Cocacola 1L"))
    page.update()
    dropDown_Menu_bebidas.options.append(ft.dropdown.Option("Latas fanta"))
    page.update()
    dropDown_Menu_bebidas.options.append(ft.dropdown.Option("Fanta 1L"))
    page.update()
    dropDown_Menu_bebidas.options.append(ft.dropdown.Option("Latas Nestea"))
    page.update()
    dropDown_Menu_bebidas.options.append(ft.dropdown.Option("Monster"))
    page.update()
    dropDown_Menu_bebidas.options.append(ft.dropdown.Option("Red Bull"))
    page.update()
    dropDown_Menu_bebidas.options.append(ft.dropdown.Option("Vino"))
    page.update()


    #CONTADOR BEBIDAS  
    class Contador3(ft.UserControl):
        def sumar3(self, e):
            self.contador3 += 1
            self.text3.value = str(self.contador3)
            self.update()
        def build(self):
            self.contador3 = 0
            self.text3 = ft.Text(str(self.contador3))
            return ft.Row([self.text3, ft.ElevatedButton("Añadir", on_click=self.sumar3)])
    #page.add(Contador3())


    #FILAS
    fila=ft.Row(controls=[dropDown_Menu_frutas,dropDown_Menu_verduras,dropDown_Menu_bebidas])
    fila_contadores = ft.Row(spacing=250,controls=[Contador(), Contador2(),Contador3()])
    page.add(fila)
    page.add(fila_contadores)

    #LISTA TOTAL
    texto2=ft.Text(value="Lista total",color="red",size=20)
    page.add(texto2)
    def boton_guardar_lista(e):
        texto2.value = f"Lista total de {textField_Nombre.value} el día {slider_dia.value} del mes {slider_mes.value}: \n {dropDown_Menu_frutas.value}:"
        page.update()
    boton=ft.FloatingActionButton(icon=ft.icons.FAVORITE, on_click=boton_guardar_lista)
    page.add(boton)

ft.app(target=main)