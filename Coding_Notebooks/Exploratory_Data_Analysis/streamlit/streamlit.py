from operator import mod
import streamlit as st
import pickle 

st.title('democracy index')

def show_model():
    with open('streamlit/fig.pkl', 'rb') as pickle_in:
        figure = pickle.load(pickle_in)
    figure.show()

def show_model1():
    with open('streamlit/fig1.pkl', 'rb') as pickle_in:
        figure1 = pickle.load(pickle_in)
    figure1.show()

def show_model2():
    with open('streamlit/fig2.pkl', 'rb') as pickle_in:
        figure2 = pickle.load(pickle_in)
    figure2.show()

def show_model3():
    with open('streamlit/fig3.pkl', 'rb') as pickle_in:
        figure3 = pickle.load(pickle_in)
    figure3.show()

if st.button('figure'):
    show_model()

if st.button('figure1'):
    show_model1()

if st.button('figure2'):
    show_model2()

if st.button('figure3'):
    show_model3()
