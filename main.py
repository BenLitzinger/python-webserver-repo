import streamlit as st
import pandas as pd
import io

def process_csv(file, mult):
    df = pd.read_csv(file)
    
    df = df * mult
    
    return df

def process_csv(file, mult):
    df = pd.read_csv(file)
    
    df = df * mult
    
    return df

def main():
    st.title("Einfache Streamlit-Seite")
    
    # Text anzeigen
    st.text("Willkommen zu Streamlit!")
    
    # Button anzeigen
    button_clicked = st.button("Klick mich")
    
    if button_clicked:
        st.success("Button wurde geklickt!")

if __name__ == "__main__":
    main()