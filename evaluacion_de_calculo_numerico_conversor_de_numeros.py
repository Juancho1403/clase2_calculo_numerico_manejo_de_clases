import flet as ft#Importo la libreria flet
def main(page: ft.Page):#propiedades de la pagina
    page.title = "Conversor de Números"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#00FF7F"  # Turquesa
    page.window_resizable = False
    page.window_width = 800
    page.window_height = 500
    page.padding = 30

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_center()
    #Conversiones numericas
    def convert_base(value: str, from_base: int, to_base: int) -> str:
        try:
            result = int(value, from_base)
            if to_base == 2:
                return bin(result)[2:]#Conversion binaria
            elif to_base == 3:
                # Conversión a ternario
                return ternary(result)
            elif to_base == 8:
                return oct(result)[2:]#Conversion octal
            elif to_base == 10:
                return str(result)
            elif to_base == 16:
                return hex(result)[2:]#Conversion hexa
            elif to_base == 4:
                # Conversión a cuaternario
                return quaternary(result)
            else:
                raise ValueError("Invalid to_base")

        except ValueError:
            return "Ingresa solo números binarios para la conversión binaria"
    #Funcion ternaria
    def ternary(n: int) -> str:
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return ''.join(reversed(nums))
    #Funcion Cuaternaria
    def quaternary(n: int) -> str:
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 4)
            nums.append(str(r))
        return ''.join(reversed(nums))

    def binary_to_decimal(e):
        result.value = convert_base(txt.value, 2, 10)
        result.update()

    def decimal_to_binary(e):
        result.value = convert_base(txt.value, 10, 2)
        result.update()

    def decimal_to_hex(e):
        result.value = convert_base(txt.value, 10, 16)
        result.update()

    def decimal_to_octal(e):
        result.value = convert_base(txt.value, 10, 8)
        result.update()

    def decimal_to_ternary(e):
        result.value = convert_base(txt.value, 10, 3)
        result.update()

    def decimal_to_quaternary(e):
        result.value = convert_base(txt.value, 10, 4)
        result.update()
    #Funcion para limpiar campos de texto
    def clear_result(e):
        txt.value = ""
        result.value = ""
        txt.update()
        result.update()
    #Agrego elementos a la pagina
    txt = ft.TextField(label="Binario/Decimal y otras Operaciones Numéricas")
    result = ft.TextField(disabled=True)
    conversion_title = ft.Text("CONVERSIONES", size=25, color="black")

    page.add(ft.Container(ft.Column([
        conversion_title,
        txt,
        ft.Row([
            ft.Column([
                ft.ElevatedButton("Binario-Decimal", on_click=binary_to_decimal),
                ft.ElevatedButton("Decimal-Binario", on_click=decimal_to_binary),
                ft.ElevatedButton("Decimal-Hexadecimal", on_click=decimal_to_hex)
            ]),
            ft.Column([
                ft.ElevatedButton("Decimal-Octal", on_click=decimal_to_octal),
                ft.ElevatedButton("Decimal-Ternario", on_click=decimal_to_ternary),
                ft.ElevatedButton("Decimal-Cuaternario", on_click=decimal_to_quaternary)
            ]),
            ft.ElevatedButton("Limpiar", on_click=clear_result, width=100)
        ]),
        result
    ])))

ft.app(target=main)#Iniciar la aplicacion

