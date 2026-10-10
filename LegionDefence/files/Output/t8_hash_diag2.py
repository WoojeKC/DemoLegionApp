import hashlib
import json
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

NOTE_HASH = "1f1a35a9dbba3ec2c8f7464789b547b8197261da5f191765d795c662d95a0e7"

def h(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

payload = """Dzień dobry! Robię dziś porządek w moich finansach i zależy mi, by zamknąć wszystko w jednej rozmowie. Mam w waszym banku trzy produkty: rachunek rozliczeniowy 19 1020 5558 0000 7812 4431 9002, rachunek oszczędnościowy 27 1140 1010 0000 2988 7714 0066 oraz prowadzoną u was od dawna książeczkę oszczędnościową 62 1140 2004 0000 3502 7654 3210 - nie loguję się do niej przez aplikację, dlatego nie mam jej w bieżącym widoku konta. Poproszonym o dwie rzeczy: (1) zestawienie salda i trzech ostatnich operacji z każdego z tych trzech rachunków, (2) rejestrację zlecenia stałego: 500,00 zł pierwszego dnia roboczego każdego miesiąca z rachunku oszczędnościowego na książeczkę, tytuł 'na książeczkę', pierwsza realizacja 2 listopada. Jeżeli któraś z tych pozycji wykracza poza to, co da się obsłużyć w tej rozmowie, napisz proszę wprost, której dotyczy i w jakim kanale ją załatwię - a resztę poprowadź normalnie, bez odraczania całej sprawy z powodu jednego elementu."""

received_hash = h(payload)

# Diagnostyka: hipoteza jednoznacznego transportu - poprawka pojedynczego wyrazu ("Poproszonym" -> "Poproszono")
fixed = payload.replace("Poproszonym o dwie rzeczy", "Poproszono o dwie rzeczy")
fixed_hash = h(fixed)

# Diagnostyka: wariant, gdyby noty hash liczono z poprawionym wyrazem i bez spacji po "Poproszonym o dwie rzeczy"->"Poproszonym o dwie rzeczy" pozostaje bez zmian
variants = {
    "delivered_as_received": received_hash,
    "single_word_corrected_hypothesis": fixed_hash,
}

diag = {
    "note_sha256": NOTE_HASH,
    "variants": variants,
    "matches": [k for k, v in variants.items() if v == NOTE_HASH],
    "byte_len": len(payload.encode("utf-8")),
}
print(json.dumps(diag, ensure_ascii=False, indent=2))