import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
import math

# Definir los datos de los nodos y barras
nodos = {
    1: (0, 0),
    2: (2, 0),
    3: (4, 0),
    4: (6, 0),
    5: (8, 0),
    6: (10, 0),
    7: (12, 0),
    8: (14, 0),
    9: (16, 0),
    10: (18, 0)
}

barras = [
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
    (6, 7), (7, 8), (8, 9), (9, 10)
]

# Cargas distribuidas: (nodo_inicio, nodo_fin, qx, qy)
cargas_distribuidas = [
    (1, 2, 0, -4),
    (2, 3, 0, -4),
    (3, 4, 0, -4),
    (4, 5, 0, -4),
    (5, 6, 0, -4),
    (6, 7, 0, -4),
    (7, 8, 0, -4),
    (8, 9, 0, -4),
    (9, 10, 0, -4)
]

# Cargas concentradas: (nodo, fx, fy)
cargas_concentradas = [
    (2, 0, -5),
    (4, 0, -10),
    (6, 0, -10),
    (8, 0, -10),
    (10, 0, -10)
]

# Reacciones: (nodo, fx, fy)
reacciones = [
    (1, 0, 20),
    (1, 10, 0),
    (10, 0, 10)
]

def dibujar_estructura():
    fig, ax = plt.subplots(figsize=(14, 4))

    # Dibujar barras
    for barra in barras:
        n1, n2 = barra
        x1, y1 = nodos[n1]
        x2, y2 = nodos[n2]
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=2)

    # Dibujar nodos
    for nodo, (x, y) in nodos.items():
        ax.add_patch(Circle((x, y), 0.1, color='black'))
        ax.text(x, y + 0.3, f'N{nodo}', ha='center')

    # Dibujar cargas distribuidas
    for carga in cargas_distribuidas:
        n1, n2, qx, qy = carga
        x1, y1 = nodos[n1]
        x2, y2 = nodos[n2]
        num_flechas = 5
        for i in range(1, num_flechas + 1):
            x = x1 + i * (x2 - x1) / (num_flechas + 1)
            y = y1 + i * (y2 - y1) / (num_flechas + 1)
            if qx != 0:
                dx = 0.4 * math.copysign(1, qx)
                dy = 0
            else:
                dx = 0
                dy = 0.4 * math.copysign(1, qy)
            ax.arrow(x, y, dx, dy, head_width=0.2, head_length=0.2, fc='blue', ec='blue')

    # Dibujar cargas concentradas
    for nodo, fx, fy in cargas_concentradas:
        x, y = nodos[nodo]
        if fx != 0:
            ax.arrow(x, y, fx * 0.4, 0, head_width=0.2, head_length=0.2, fc='red', ec='red')
        if fy != 0:
            ax.arrow(x, y, 0, fy * 0.4, head_width=0.2, head_length=0.2, fc='red', ec='red')

    # Dibujar reacciones
    for nodo, fx, fy in reacciones:
        x, y = nodos[nodo]
        if fx != 0:
            ax.arrow(x, y, fx * 0.2, 0, head_width=0.2, head_length=0.2, fc='green', ec='green')
        if fy != 0:
            ax.arrow(x, y, 0, fy * 0.2, head_width=0.2, head_length=0.2, fc='green', ec='green')

    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('Estructura 2D con Cargas')
    plt.show()

dibujar_estructura()
