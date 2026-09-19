import matplotlib.pyplot as plt

def dibujar_grafico_barras(categorias, valores, titulo="Gráfico de Barras", etiqueta_x="Categorías", etiqueta_y="Valores"):
    plt.figure(figsize=(8, 5))
    
    plt.bar(categorias, valores, color='skyblue', edgecolor='black')
    
    plt.title(titulo, fontsize=14, fontweight='bold', pad=15)
    plt.xlabel(etiqueta_x, fontsize=12)
    plt.ylabel(etiqueta_y, fontsize=12)
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

ejemplo_categorias = ['Manzanas', 'Plátanos', 'Naranjas', 'Uvas']
ejemplo_valores = [15, 24, 12, 18]

dibujar_grafico_barras(
    categorias=ejemplo_categorias, 
    valores=ejemplo_valores, 
    titulo="Inventario de Frutas", 
    etiqueta_x="Frutas", 
    etiqueta_y="Cantidad disponible"
)