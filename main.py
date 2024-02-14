import streamlit as st

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
