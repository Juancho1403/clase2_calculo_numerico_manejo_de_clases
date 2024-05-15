import flet as ft# Importo la libreria flet para trabajar la interfaz grafica 
import random #Importo la libreria random para generar numeros aleatorios para la matriz

def main(page: ft.Page):#Esta funcion es el punto de entrada para la aplicacion flet
    #Propiedades de la ventana
    page.title = "Generación de Matrices"#Nombre
    page.bgcolor = "#00FF7F"  # Color / Turquesa
    page.window_resizable = False # Para no redimensionar la ventana 
    page.window_width = 800 #Ancho
    page.window_height = 500#Largo
    page.padding = 30# forma un borde la ventana 
    #Alinea los elementos de la interfaz
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #vertical 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER#Horizontal
    page.window_center()#Centra la ventana 
    #Crear elementos de la interfaz del usuario
    result = ft.TextField(disabled=True, multiline=True)
    conversion_title = ft.Text("Método de Gauss-Seidel", size=25, color="black")
    #Metodo de gauss seidel ramdon
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
    #Metodo de gauss seidel
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
    #Metodo que limpia el campo de texto 
    def clear_fields(e):
        result.value = ""
        result.color = ft.colors.BLACK
        page.update()
    #Agrega elementos a la pagina 
    page.add(ft.Container(ft.Column([
        conversion_title,
        ft.ElevatedButton("Método de Gauss-Seidel", on_click=gauss_seidel_random),
        ft.ElevatedButton("Limpiar", on_click=clear_fields),
        ft.Container(
            content=result,
            padding=10,
            border=ft.border.all(1, "black"),
        )
    ])))

ft.app(target=main)#Iniciar la aplicacion
