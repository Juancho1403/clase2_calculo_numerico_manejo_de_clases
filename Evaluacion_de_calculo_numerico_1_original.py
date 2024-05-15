



import flet as ft 
import random 
def main(page: ft.Page): 
    page.title = "Menu Principal" 
    page.bgcolor = "#00FF7F" 
    page.window_resizable = False 
    page.window_width = 800 
    page.window_height = 500 
    page.padding = 30 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    page.window_center()
    
   
    def navigate_to_eval1(e): 
        page.clean() 
        eval1(page) 
    def navigate_to_eval2(e): 
        page.clean() 
        eval2(page)
    def navigate_to_main(e): 
        page.clean() 
        main(page)
    
     
    page.add(ft.Container(ft.Column([ 
        ft.Text("Menu Principal", size=25, color="black"), 
        ft.ElevatedButton("Evaluación 1", on_click=navigate_to_eval1), 
        ft.ElevatedButton("Evaluación 2", on_click=navigate_to_eval2), 
    ])))
def eval1(page: ft.Page):
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
    regresar_button = ft.ElevatedButton("Regresar", on_click=lambda e: page.go("/")) 
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
            return "Ingresa solo números respectivos para dicha conversion de numeros" 
    def ternary(n: int) -> str: 
        if n == 0: 
            return '0' 
        nums = [] 
        while n: 
            n, r = divmod(n, 3) 
            nums.append(str(r)) 
        return ''.join(reversed(nums)) 
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
    def clear_result(e): 
        txt.value = "" 
        result.value = "" 
        txt.update() 
        result.update() 
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
            ft.ElevatedButton("Limpiar", on_click=clear_result, width=100), 
        ]), 
        result, 
        regresar_button 
    ]))) 
def eval2(page: ft.Page): 
    regresar_button = ft.ElevatedButton("Regresar", on_click=lambda e: page.go("/")) 
    def gauss_seidel_random(e): 
        matrix = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)] 
        b = [random.randint(1, 9) for _ in range(3)] 
        x0 = [0, 0, 0] 
        tol = 1e-6 
        max_iter = 1000 
        x = gauss_seidel_method(matrix, b, x0, tol, max_iter) 
        matrix_text = "\n".join([" ".join(map(str, row)) for row in matrix]) 
        result.value = "matriz original:\n" + str(matrix_text) + "\n\nvector b:\n" + str(b) + "\n\nvector x (solucion):\n" + str(x) 
        result.color = ft.colors.BLACK 
        page.update() 
    def gauss_seidel_manual(e): 
        try: 
            matrix = [[float(field.value) for field in matrix_input_fields[i:i+3]] for i in range(0, 9, 3)] 
            b = [float(field.value) for field in b_input_fields] 
            x0 = [0, 0, 0] 
            tol = 1e-6 
            max_iter = 1000 
            x = gauss_seidel_method(matrix, b, x0, tol, max_iter) 
            matrix_text = "\n".join([" ".join(map(str, row)) for row in matrix]) 
            result.value = "matriz original:\n" + str(matrix_text) + "\n\nvector b:\n" + str(b) + "\n\nvector x (solucion):\n" + str(x) 
            result.color = ft.colors.BLACK 
            page.update() 
        except ValueError: 
            result.value = "por favor ingresa numeros o pulsa el boton random" 
            result.color = ft.colors.RED 
            page.update() 
    def gauss_seidel_method(A, b, x0, tol, max_iter): 
        n = len(b) 
        for _ in range(max_iter): 
            x = x0.copy() 
            for i in range(n): 
                x[i] = b[i] 
                for j in range(n): 
                    if j != i: 
                        x[i] -= A[i][j] * x[j] 
                x[i] /= A[i][i] 
            if sum((x[i] - x0[i])**2 for i in range(n)) < tol**2: 
                return x 
        return x 
    def clear_fields(e): 
        for field in matrix_input_fields + b_input_fields: 
            field.value = "" 
            result.value = "" 
            result.color = ft.colors.BLACK 
            page.update() 
    page.title = "Gauss-Seidel Metodo" 
    page.bgcolor = "#00FF7F" 
    page.window_resizable = False 
    page.window_width = 800 
    page.window_height = 690 
    page.padding = 30 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    page.window_center() 
    result = ft.TextField(disabled=True, multiline=True) 
    conversion_title = ft.Text("Métodode Gauss-Seidel", size=25, color="black") 
    matrix_input_fields = [] 
    for i in range(3): 
        row = [] 
        for j in range(3): 
            field = ft.TextField(width=50, height=30) 
            row.append(field) 
            matrix_input_fields.append(field) 
        page.add(ft.Row([ft.Text(f"a:")] + row)) 
    b_input_fields = [] 
    for i in range(3): 
        field = ft.TextField(width=50, height=30) 
        b_input_fields.append(field) 
        page.add(ft.Row([ft.Text(f"b:")] + [field])) 
    page.add(ft.Container(ft.Column([ 
        conversion_title, 
        ft.Row([ 
            ft.ElevatedButton("Random", on_click=gauss_seidel_random), 
            ft.ElevatedButton("Manual", on_click=gauss_seidel_manual), 
            ft.ElevatedButton("Limpiar", on_click=clear_fields) 
        ]), 
        ft.Container( 
            content=result, 
            padding=7, 
            border=ft.border.all(1, "black"), 
         ), 
        regresar_button 
    ])))
   
ft.app(target=main)
