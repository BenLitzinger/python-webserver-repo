import streamlit as st

def process_csv(file, mult):
    df = pd.read_csv(file)
    
    df = df * mult
    
    return df

def main():
    st.title("CSV Datei bearbeiten")

    # Datei hochladen
    uploaded_file = st.file_uploader("Datei auswählen", type=["csv"])

    if uploaded_file is not None:
        # Daten bearbeiten
        df = process_csv(uploaded_file)

        # Tabelle anzeigen
        st.dataframe(df)

        # Download-Link für die bearbeitete Datei
        csv_as_string = df.to_csv(index=False)
        csv_as_bytes = io.BytesIO(csv_as_string.encode())
        st.download_button("Daten herunterladen", csv_as_bytes, "bearbeitete_daten.csv")

        # Eingabefelder für Zahlenfehler
        st.header("Zahlenfehler korrigieren")

        # Beispiel für drei Zahlenfehler (kann angepasst werden)
        error1 = st.number_input("Fehler 1:", value=0, step=1)
        error2 = st.number_input("Fehler 2:", value=0, step=1)
        error3 = st.number_input("Fehler 3:", value=0, step=1)

if __name__ == "__main__":
    main()