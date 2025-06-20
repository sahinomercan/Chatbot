import re

DATA_FILE = "data/sahinhukuk-icerik.txt"


def load_paragraphs(path=DATA_FILE):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    # Split on blank lines
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return paragraphs


PARAGRAPHS = load_paragraphs()


def find_answer(query):
    words = query.lower().split()
    best_score = 0
    best_par = None
    for par in PARAGRAPHS:
        lower = par.lower()
        score = sum(1 for w in words if w in lower)
        if score > best_score:
            best_score = score
            best_par = par
    return best_par if best_par else "Üzgünüm, sorunuza uygun bir yanıt bulamadım."


def main():
    print("Chatbot hazır. Çıkmak için 'q' yazın.")
    while True:
        question = input("Soru: ").strip()
        if question.lower() in {"q", "quit", "exit"}:
            break
        print("Cevap: " + find_answer(question) + "\n")


if __name__ == "__main__":
    main()
