#---_ Bíblia Sagrada ✞ App 2.0 _---
#---_ By Lucas Fujarra _---
#---_ https://github.com/LucasFujarra _---

import json
import requests
import streamlit as st

def get_bible_text(book, chapter):
    url = f"https://raw.githubusercontent.com/MaatheusGois/bible/main/versions/pt-br/{selection}/{book}/{book}.json"
    response = requests.get(url)
    if response.status_code == 200:
        chapter = int(chapter) - 1
        data = response.json()
        chapter_text = data['chapters'][chapter]
        formatted_text = ""
        for verse_num, verse_text in enumerate(chapter_text, 1):
            formatted_text += f"{verse_num}: {verse_text}\n"
        return formatted_text
    else:
        return "Erro ao buscar o texto."


def get_max_chapter(book):
    chapters = {
        "gn": 50, "ex": 40, "lv": 27, "nm": 36, "dt": 34, "js": 24, "jud": 21, "rt": 4,
        "1sm": 31, "2sm": 24, "1kgs": 22, "2kgs": 25, "1ch": 29, "2ch": 36, "ezr": 10,
        "ne": 13, "et": 10, "job": 42, "ps": 150, "prv": 31, "ec": 12, "so": 8, "is": 66,
        "jr": 52, "lm": 5, "ez": 48, "dn": 12, "ho": 14, "jl": 3, "am": 9, "ob": 1,
        "jn": 4, "mi": 7, "na": 3, "hk": 3, "zp": 3, "hg": 2, "zc": 14, "ml": 4,
        "mt": 28, "mk": 16, "lk": 24, "jo": 21, "act": 28, "rm": 16, "1co": 16,
        "2co": 13, "gl": 6, "eph": 6, "ph": 4, "cl": 4, "1ts": 5, "2ts": 3, "1tm": 6,
        "2tm": 4, "tt": 3, "phm": 1, "hb": 13, "jm": 5, "1pe": 5, "2pe": 3, "1jo": 5,
        "2jo": 1, "3jo": 1, "jd": 1, "re": 22
    }
    return chapters.get(book, 0)

st.set_page_config(
    page_title="Bíblia Sagrada",
    page_icon="📖",
    layout="wide",
)

st.title("Bíblia Sagrada ✞")


options = ["aa", "acf", "arc", "kja","nvi" ]
selection = st.pills("Versão", options, selection_mode="single",default= "nvi")

if selection == "aa":
    version_Name = "Almeida Revisada Imprensa Bíblica"
elif selection == "acf":
    version_Name = "Almeida Corrigida e Revisada Fiel"
elif selection == "arc":
    version_Name = "Almeida Revista e Corrigida"
elif selection == "nvi":
    version_Name = "Nova Versão Internacional"
elif selection == "kja":
    version_Name = "King James Fiel"
else:
    version_Name = ""

st.markdown(f'''{version_Name}''')

col1, col2 = st.columns(2)

with col1:
    book_abbreviations = {
        "Gênesis": "gn", "Êxodo": "ex", "Levítico": "lv", "Números": "nm", "Deuteronômio": "dt",
        "Josué": "js", "Juízes": "jud", "Rute": "rt", "1 Samuel": "1sm", "2 Samuel": "2sm",
        "1 Reis": "1kgs", "2 Reis": "2kgs", "1 Crônicas": "1ch", "2 Crônicas": "2ch", "Esdras": "ezr",
        "Neemias": "ne", "Ester": "et", "Jó": "job", "Salmos": "ps", "Provérbios": "prv",
        "Eclesiastes": "ec", "Cânticos": "so", "Isaías": "is", "Jeremias": "jr", "Lamentações": "lm",
        "Ezequiel": "ez", "Daniel": "dn", "Oseias": "ho", "Joel": "jl", "Amós": "am", "Obadias": "ob",
        "Jonas": "jn", "Miqueias": "mi", "Naum": "na", "Habacuque": "hk", "Sofonias": "zp",
        "Ageu": "hg", "Zacarias": "zc", "Malaquias": "ml", "Mateus": "mt", "Marcos": "mk",
        "Lucas": "lk", "João": "jo", "Atos": "act", "Romanos": "rm", "1 Coríntios": "1co",
        "2 Coríntios": "2co", "Gálatas": "gl", "Efésios": "eph", "Filipenses": "ph", "Colossenses": "cl",
        "1 Tessalonicenses": "1ts", "2 Tessalonicenses": "2ts", "1 Timóteo": "1tm", "2 Timóteo": "2tm",
        "Tito": "tt", "Filemom": "phm", "Hebreus": "hb", "Tiago": "jm", "1 Pedro": "1pe",
        "2 Pedro": "2pe", "1 João": "1jo", "2 João": "2jo", "3 João": "3jo", "Judas": "jd",
        "Apocalipse": "re"
    }
    
    book_name = st.selectbox(
        "Escolha o Livro da Bíblia",
        list(book_abbreviations.keys())
    )
    book = book_abbreviations[book_name]

if 'current_book' in st.session_state:
    if st.session_state.current_book != book:
        st.session_state.chapter = 1
else:
    st.session_state.current_book = book

st.session_state.current_book = book


with col2:
    if 'chapter' not in st.session_state:
        st.session_state.chapter = 1  
    max_chapters = get_max_chapter(book)
    chapter = st.selectbox("Escolha o capítulo:", list(range(1, max_chapters + 1)),index=st.session_state.chapter - 1)

try:
    chapter = int(chapter)
    text = get_bible_text(book, chapter)
    st.text(text)
    st.session_state.chapter = chapter
    

except ValueError:
    st.error("Por favor, insira um valor numérico válido para o capítulo.")
except Exception as e:
    st.error(f"Ocorreu um erro: {e}")




col1, col2,col3,col4,col5 = st.columns(5,gap="large",vertical_alignment="center")

with col2:
    if st.button("◀"):
        if st.session_state.chapter > 1:
            st.session_state.chapter = st.session_state.chapter - 1
            st.rerun()
with col3:
    st.text(f"Capítulo {chapter}")

with col4:
    if st.button("▶"):
        if st.session_state.chapter < max_chapters:
            st.session_state.chapter = st.session_state.chapter + 1
            st.rerun()
        else:
            st.success("Você chegou ao final do Livro")







