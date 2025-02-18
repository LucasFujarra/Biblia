#---_ Bíblia Sagrada ✞ APP 1.0 _---
#---_ By Lucas Fujarra _---
#---_ https://github.com/LucasFujarra _---

import json
import requests
import streamlit as st

def get_bible_text(book, chapter):
    url = f"https://bible-api.com/{book}+{chapter}?translation=almeida"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        verses = data['verses']
        chapter_text = ""
        for verse in verses:
            chapter_text += f"{verse['verse']}: {verse['text']}\n"
        return chapter_text
    else:
        return "Erro ao buscar o texto."


def get_max_chapter(book):
    chapters = {
        "Gênesis": 50,
        "Êxodo": 40,
        "Levítico": 27,
        "Números": 36,
        "Deuteronômio": 34,
        "Josué": 24,
        "Juízes": 21,
        "Rute": 4,
        "1 Samuel": 31,
        "2 Samuel": 24,
        "1 Reis": 22,
        "2 Reis": 25,
        "1 Crônicas": 29,
        "2 Crônicas": 36,
        "Esdras": 10,
        "Neemias": 13,
        "Ester": 10,
        "Jó": 42,
        "Salmos": 150,
        "Provérbios": 31,
        "Eclesiastes": 12,
        "Cânticos": 8,
        "Isaías": 66,
        "Jeremias": 52,
        "Lamentações": 5,
        "Ezequiel": 48,
        "Daniel": 12,
        "Oseias": 14,
        "Joel": 3,
        "Amós": 9,
        "Obadias": 1,
        "Jonas": 4,
        "Miqueias": 7,
        "Naum": 3,
        "Habacuque": 3,
        "Sofonias": 3,
        "Ageu": 2,
        "Zacarias": 14,
        "Malaquias": 4,
        "Mateus": 28,
        "Marcos": 16,
        "Lucas": 24,
        "João": 21,
        "Atos": 28,
        "Romanos": 16,
        "1 Coríntios": 16,
        "2 Coríntios": 13,
        "Gálatas": 6,
        "Efésios": 6,
        "Filipenses": 4,
        "Colossenses": 4,
        "1 Tessalonicenses": 5,
        "2 Tessalonicenses": 3,
        "1 Timóteo": 6,
        "2 Timóteo": 4,
        "Tito": 3,
        "Filemom": 1,
        "Hebreus": 13,
        "Tiago": 5,
        "1 Pedro": 5,
        "2 Pedro": 3,
        "1 João": 5,
        "2 João": 1,
        "3 João": 1,
        "Judas": 1,
        "Apocalipse": 22
    }
    return chapters.get(book, 0)

st.set_page_config(
    page_title="Bíblia Sagrada",
    page_icon="📖",
    layout="wide",
        
)

st.title("Bíblia Sagrada ✞")
st.markdown('''João Ferreira de Almeida''')

col1, col2 = st.columns(2)

with col1:

    book = st.selectbox(
        " Escolha o Livro da Bíblia",
        ("Gênesis", "Êxodo", "Levítico", "Números", "Deuteronômio", "Josué", "Juízes", "Rute", "1 Samuel", "2 Samuel", "1 Reis", "2 Reis", "1 Crônicas", "2 Crônicas", "Esdras", "Neemias", "Ester", "Jó", "Salmos", "Provérbios", "Eclesiastes", "Cânticos", "Isaías", "Jeremias", "Lamentações", "Ezequiel", "Daniel", "Oseias", "Joel", "Amós", "Obadias", "Jonas", "Miqueias", "Naum", "Habacuque", "Sofonias", "Ageu", "Zacarias", "Malaquias", "Mateus", "Marcos", "Lucas", "João", "Atos", "Romanos", "1 Coríntios", "2 Coríntios", "Gálatas", "Efésios", "Filipenses", "Colossenses", "1 Tessalonicenses", "2 Tessalonicenses", "1 Timóteo", "2 Timóteo", "Tito", "Filemom", "Hebreus", "Tiago", "1 Pedro", "2 Pedro", "1 João", "2 João", "3 João", "Judas", "Apocalipse"),
    )

with col2:

    max_chapters = get_max_chapter(book)
    chapter = st.selectbox("Escolha o capítulo:", list(range(1, max_chapters + 1)))

try:
    chapter = int(chapter)
    text = get_bible_text(book.title(), chapter)
    st.text(text)

except ValueError:
    st.error("Por favor, insira um valor numérico válido para o capítulo.")
except Exception as e:
    st.error(f"Ocorreu um erro: {e}")


    


