import sys

# /c:/Users/wagner/Desktop/Modulo5PythonBasico/aula1_questao5.py
# Script para mostrar uma lista de emojis e emojizar uma frase fornecida pelo usuário.


try:
    import emoji
except ImportError:
    print("Biblioteca 'emoji' não encontrada. Instale com: pip install emoji")
    sys.exit(1)

EMOJIS = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:",
}

def emojize_text(text: str) -> str:
    # Tenta usar o parâmetro 'language' (disponível em versões mais recentes).
    try:
        return emoji.emojize(text, language="alias")
    except TypeError:
        # Fallback para versões antigas da biblioteca
        return emoji.emojize(text)

def main():
    print("Emojis disponíveis:\n")
    for char, code in EMOJIS.items():
        print(f"{char} - {code}")
    print("\nDigite uma frase e ela será emojizada:")
    user_input = input().strip()
    result = emojize_text(user_input)
    print("\nFrase emojizada:\n")
    print(result)

if __name__ == "__main__":
    main()