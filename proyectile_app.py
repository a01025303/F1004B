import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def proyectile_no_drag(v_0, theta_degree, y_0, t_start, t_end, g = 9.81):
    
    # Calcular la trayectoria sin resistencia del aire
    
    return r_x, r_y


def proyectile_drag(v_0, theta_degree, y_0, m, rho, C, A, dt, N, g=9.81):
    
    # Calcular la trayectoria con resistencia del aire

    return a_x_list, a_y_list, v_x_list, v_y_list, v_list, x_list, y_list, t_list


def plot_trayectories(x_no_drag,y_no_drag,x_drag,y_drag,x_max,y_max,grid_size,title="Trayectoria del Proyectil"):
    
    fig = plt.Figure(figsize=(15,9))

    # Crear el gráfico

    return fig


def get_trayectory_plots():#Define los argumentos de entrada necesarios

    # Calcular Trayectoria sin resistencia
    r_x, r_y = proyectile_no_drag(v_0, theta_degree, y_0, t_start, t_end)

    # Declarar condiciones iniciales para trayectoria con resistenca del aire

    [a_x_list, a_y_list, 
     v_x_list, v_y_list, v_list, 
     x_list, y_list, t_list] = proyectile_drag(v_0, theta_degree, y_0, m, rho, C, A, dt, N)

    # Asegúrate que hayas definido la función plot_trayectories() de manera correcta.
    fig = plot_trayectories(r_x,r_y,x_list, y_list,100,40,5)

    return fig


if __name__ == "__main__":

    # Crea aquí tu aplicación de Streamlit

    
    # Algunas funciones para escribir texto

    #st.title('')
    #st.subheader('')
    #st.write('')
    
    # Componentes para entradas streamlit

    # st.slider()
    # st.button()
    # st.checkbox()
    # st.radio()
    # st.selectbox()
    # st.text_input()
    # st.number_input()

    # Declarar condiciones iniciales, ya sea como variables o componentes
    # de streamlit

    fig = get_trayectory_plots() #Define los argumentos de entrada necesarios
    
    # Para agregar un gráfico de matplotlib podemos usar st.pyplot
    st.pyplot(fig)