#---_ Bíblia Sagrada ✞ CLI 1.0 _---
#---_ By Lucas Fujarra _---
#---_ https://github.com/LucasFujarra _---

import json
import requests
import os
import time

def logo():             
        print("███████████████████████████████████")
        print("█████████ Bíblia Sagrada ██████████")
        print("███████████████████████████████████")
    


def get_bible_text(book, chapter):
    url = f"https://bible-api.com/{book}+{chapter}?translation=almeida"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        verses = data.get('verses', [])
        if verses:
            for verse in verses:
                print(f"{verse['verse']}: {verse['text']}")
        else:
            time.sleep(2)
            print("Nenhum versículo encontrado para o capítulo especificado.")
            os.system("cls")

    else:
        print("Erro ao buscar o texto.")
        os.system("cls")

def main():
    while True:
        os.system("cls")
        logo()
        book = input("Digite o Livro da Bíblia: ").title()
        chapter = input("Digite o número do capítulo: ")
        
        try:
            chapter = int(chapter)
            get_bible_text(book, chapter)
            
            another_search = input("Deseja buscar novamente (s/n)? ")
            os.system("cls")
            if another_search.lower() != 's':
                break

        except ValueError:
            print("Por favor, insira valores numéricos válidos para o capítulo.")
            time.sleep(2)
            os.system("cls")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            time.sleep(2)
            os.system("cls")

if __name__ == "__main__":
    main()