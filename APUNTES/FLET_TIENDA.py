import flet as ft
#PAGINA TOTAL
def main(page: ft.Page):
    dropDown_Menu_frutas=""
    dropDown_Menu_verduras=""
    dropDown_Menu_bebidas=""
    dropDown_Menu_postres=""
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

    #TEXTO ABAJO
    texto2=ft.Text(value="Lista total",color="red",size=20)
    page.add(texto2)

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

    #VERDURAS
    dropDown_Menu_verduras=ft.Dropdown(width=300,label="Verduras",options=[ft.dropdown.Option("Pepino"),
                                                                            ft.dropdown.Option("Rábano"),
                                                                            ft.dropdown.Option("Berengena"),
                                                                            ft.dropdown.Option("Lechuga"),
                                                                            ft.dropdown.Option("Pimiento"),
                                                                            ft.dropdown.Option("Zanahoria"),
                                                                            ft.dropdown.Option("Tomate"),
                                                                            ft.dropdown.Option("Melón"),
                                                                            ft.dropdown.Option("Sandía"),
                                                                            ft.dropdown.Option("Calabacín"),
                                                                            ft.dropdown.Option("Remolacha")])
    page.update()

    #BEBIDAS
    dropDown_Menu_bebidas=ft.Dropdown(width=300,label="Bebidas",options=[ft.dropdown.Option("Botella agua 0,5L"),
                                                                            ft.dropdown.Option("Botella agua 1L"),
                                                                            ft.dropdown.Option("Botella agua 2L"),
                                                                            ft.dropdown.Option("Latas cocacola"),
                                                                            ft.dropdown.Option("Cocacola 1L"),
                                                                            ft.dropdown.Option("Latas fanta"),
                                                                            ft.dropdown.Option("Fanta 1L"),
                                                                            ft.dropdown.Option("Latas Nestea"),
                                                                            ft.dropdown.Option("Monster"),
                                                                            ft.dropdown.Option("Red Bull"),
                                                                            ft.dropdown.Option("Vino")])
    page.update()

    #POSTRES
    dropDown_Menu_postres=ft.Dropdown(width=300,label="Postres",options=[ft.dropdown.Option("Tarta de queso"),
                                                                            ft.dropdown.Option("Danonino"),
                                                                            ft.dropdown.Option("Petisui"),
                                                                            ft.dropdown.Option("Flan"),
                                                                            ft.dropdown.Option("Natillas"),
                                                                            ft.dropdown.Option("Yogur")])
    page.update()

    #FILAS
    fila=ft.Row(controls=[dropDown_Menu_frutas,dropDown_Menu_verduras,dropDown_Menu_bebidas,dropDown_Menu_postres])
    page.add(fila)

    #AÑADIR ELEMENTOS
    Vañadir_elementos=[]
    def GUARDAR():
        dropDown_Menu_frutas = ft.dropdown.Option.get()
        dropDown_Menu_verduras = ft.dropdown.Option.get()
        dropDown_Menu_bebidas = ft.dropdown.Option.get()
        dropDown_Menu_postres = ft.dropdown.Option.get()
        Vañadir_elementos.append(dropDown_Menu_frutas)
        Vañadir_elementos.append(dropDown_Menu_verduras)
        Vañadir_elementos.append(dropDown_Menu_bebidas)
        Vañadir_elementos.append(dropDown_Menu_postres)
        ft.dropdown.Option.delete(0,len(dropDown_Menu_frutas))
        ft.dropdown.Option.delete(0,len(dropDown_Menu_verduras))
        ft.dropdown.Option.delete(0,len(dropDown_Menu_bebidas))
        ft.dropdown.Option.delete(0,len(dropDown_Menu_postres))
        print(dropDown_Menu_frutas)
        print(dropDown_Menu_verduras)
        print(dropDown_Menu_bebidas)
        print(dropDown_Menu_postres)
    #BOTON LISTA
    boton2=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=GUARDAR)
    page.add(boton2)
    page.update()

ft.app(target=main)