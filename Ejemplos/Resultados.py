import pandas as pd
from IPython.display import display, Math
import openseespy.opensees as ops

def formato_valor(val): return "0.00000" if val == 0 else f"{val:.5f}" if abs(val) >= 1e-3 else f"{val:.5e}"

def mostrar_reacciones_latex(Nodos):

    # Obtenemos las reacciones nodales
    ops.reactions()
    datos = []

    for n in Nodos:
        reacciones = ops.nodeReaction(n)
        datos_formateados = [formato_valor(r) for r in reacciones]
        datos.append([n] + datos_formateados)  # Nodo, Fx, Fy, Mz

    df = pd.DataFrame(datos, columns=['Nodo', 'Fx', 'Fy', 'Mz'])

    # Encabezado LaTeX
    latex_str = r"""
    \begin{array}{cccc}
    \hline
    \textbf{Nodo} & \textbf{Fx (kN)} & \textbf{Fy (kN)} & \textbf{Mz (kN-m)} \\
    \hline
    """

    # Filas del DataFrame
    for _, fila in df.iterrows():
        latex_str += f"{int(fila['Nodo'])} & {fila['Fx']} & {fila['Fy']} & {fila['Mz']} \\\\ \n"

    latex_str += r"\hline" + "\n" + r"\end{array}"

    display(Math(latex_str))

def mostrar_desplazamientos_latex(Nodos):
    datos = []

    for n in Nodos:
        nodeDisp = ops.nodeDisp(n)
        datos_formateados = [formato_valor(r) for r in nodeDisp]
        datos.append([n] + datos_formateados)                           # Nodo, Ux, Uy, Rz

    df = pd.DataFrame(datos, columns=['Nodo', 'Ux', 'Uy', 'Rz'])        # Desplazamientos

    # Encabezado LaTeX
    latex_str = r"""
    \begin{array}{cccc}
    \hline
    \textbf{Nodo} & \textbf{Ux (m)} & \textbf{Uy (m)} & \textbf{Rz (rad)} \\
    \hline
    """

    # Filas del DataFrame
    for _, fila in df.iterrows():
        latex_str += f"{int(fila['Nodo'])} & {fila['Ux']} & {fila['Uy']} & {fila['Rz']} \\\\ \n"

    latex_str += r"\hline" + "\n" + r"\end{array}"

    display(Math(latex_str))

def mostrar_fuerzaslocales_latex(Ele):
    # Obtenemos las reacciones nodales
    datos_Ele = []

    for n in Ele:
        Fuerzas = ops.eleResponse(n, 'localForce')
        datos_formateados = [formato_valor(r) for r in Fuerzas]
        datos_Ele.append([n] + datos_formateados)  # Nodo, N, V, M

    df_Ele = pd.DataFrame(datos_Ele, columns=['Elemento', 'Ni', 'Vi', 'Mi', 'Nj', 'Vj', 'Mj'])

    # Encabezado LaTeX
    latex_str = r"""
    \begin{array}{ccccccc}
    \hline
    \textbf{Elemento} & \textbf{Ni (kN)} & \textbf{Nj (kN)} & \textbf{Vi (kN-m)} & \textbf{Vj (kN)} & \textbf{Mi (kN)} & \textbf{Mj (kN-m)} \\
    \hline
    """

    # Filas
    for _, fila in df_Ele.iterrows():
        latex_str += f"{int(fila['Elemento'])} & {fila['Ni']} & {fila['Nj']} & {fila['Vi']} & {fila['Vj']} & {fila['Mi']} & {fila['Mj']} \\\\ \n"

    latex_str += r"\hline" + "\n" + r"\end{array}"

    display(Math(latex_str))

def mostrar_deformaciones_latex(Ele):
    datos = []                          # Obtenemos las reacciones nodales

    for n in Ele:
        deformaciones = ops.basicDeformation(n)
        datos_formateados = [formato_valor(r) for r in deformaciones]
        datos.append([n] + datos_formateados)  # Nodo, Fx, Fy, Mz

    df = pd.DataFrame(datos, columns=['Elemento', 'Ux', 'Uy', 'Rz'])

    # Encabezado LaTeX
    latex_str = r"""
    \begin{array}{cccc}
    \hline
    \textbf{Elemento} & \textbf{Ux (m)} & \textbf{Uy (m)} & \textbf{Rz (rad)} \\
    \hline
    """

    # Filas del DataFrame
    for _, fila in df.iterrows():
        latex_str += f"{int(fila['Elemento'])} & {fila['Ux']} & {fila['Uy']} & {fila['Rz']} \\\\ \n"

    latex_str += r"\hline" + "\n" + r"\end{array}"

    display(Math(latex_str))

def desplazamientosNodos_Matlab(D):
    datos = []
    for i, val in enumerate(D):
        nodo = i + 1  # Nodo base 1
        datos.append([nodo, formato_valor(val)])

    # Convertir a DataFrame
    df = pd.DataFrame(datos, columns=['Nodo', 'Desplazamiento'])

    # Construir cadena LaTeX
    latex_str = r"""
    \begin{array}{cc}
    \hline
    \textbf{Nodo} & \textbf{Desplazamiento (m)} \\
    \hline
    """

    for _, fila in df.iterrows():
        latex_str += f"{int(fila['Nodo'])} & {fila['Desplazamiento']} \\\\ \n"

    latex_str += r"\hline" + "\n" + r"\end{array}"

    # Mostrar en Jupyter o IPython
    display(Math(latex_str))

def reacciones_Matlab(Q):
    datos = []
    for i, val in enumerate(Q):
        nodo = i + 1
        datos.append([nodo, formato_valor(val)])

    # Convertir a DataFrame
    df = pd.DataFrame(datos, columns=['Nodo', 'Fuerza'])

    # Construir cadena LaTeX
    latex_str = r"""
    \begin{array}{cc}
    \hline
    \textbf{Nodo} & \textbf{Fuerza (m)} \\
    \hline
    """

    for _, fila in df.iterrows():
        latex_str += f"{int(fila['Nodo'])} & {fila['Fuerza']} \\\\ \n"

    latex_str += r"\hline" + "\n" + r"\end{array}"

    # Mostrar en Jupyter o IPython
    display(Math(latex_str))

def fuerzasinternas_Matlab(g_list, k_list, D):
    # Generar datos
    datos = []
    for i, (g, k) in enumerate(zip(g_list, k_list), start=1):
        d_local = D[g]
        p_local = k @ d_local
        p_format = [formato_valor(f) for f in p_local]
        datos.append([i] + p_format)

    # Crear DataFrame
    df = pd.DataFrame(datos, columns=["Elemento", "pi (kN)", "pj (kN)"])

    # Crear tabla LaTeX
    latex_str = r"""
    \begin{array}{ccc}
    \hline
    \textbf{Elemento} & \textbf{pi (kN)} & \textbf{pj (kN)} \\
    \hline
    """

    for _, fila in df.iterrows():
        latex_str += f"{int(fila['Elemento'])} & {fila['pi (kN)']} & {fila['pj (kN)']} \\\\ \n"

    latex_str += r"\hline" + "\n" + r"\end{array}"

    # Mostrar
    display(Math(latex_str))

def deformacionesElementos_Matlab(g_list, D):
    
    datos = []
    for i, g in enumerate(g_list, start=1):
        d_local_i = D[g]
        d_local = d_local_i[1] - d_local_i[0]  # Esto es un solo valor (float)
        d_format = formato_valor(d_local)     # Solo formateamos ese único valor
        datos.append([i, d_format])           # Guardamos [Elemento, Deformación]

    # Crear DataFrame
    df = pd.DataFrame(datos, columns=["Elemento", "Deformación (m)"])

    # Crear tabla LaTeX
    latex_str = r"""
    \begin{array}{cc}
    \hline
    \textbf{Elemento} & \textbf{Deformación (m)} \\
    \hline
    """

    for _, fila in df.iterrows():
        latex_str += f"{int(fila['Elemento'])} & {fila['Deformación (m)']} \\\\ \n"

    latex_str += r"\hline" + "\n" + r"\end{array}"

    display(Math(latex_str))

def analisis_gravitacional():
    ops.constraints('Plain')
    ops.numberer('Plain')
    ops.system('BandGeneral')
    ops.algorithm('Linear')
    ops.integrator('LoadControl', 1.)

    ops.analysis('Static')
    ok = ops.analyze(1)
    if ok == 0:
        print('Análisis Gravitacional Exitoso')
    else:
        print('Error en el Análisis')