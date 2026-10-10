import hashlib
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

payload = """Dzień dobry! Robię dziś porządek w moich finansach i zależy mi, by zamknąć wszystko w jednej rozmowie. Mam w waszym banku trzy produkty: rachunek rozliczeniowy 19 1020 5558 0000 7812 4431 9002, rachunek oszczędnościowy 27 1140 1010 0000 2988 7714 0066 oraz prowadzoną u was od dawna książeczkę oszczędnościową 62 1140 2004 0000 3502 7654 3210 - nie loguję się do niej przez aplikację, dlatego nie mam jej w bieżącym widoku konta. Poproszonym o dwie rzeczy: (1) zestawienie salda i trzech ostatnich operacji z każdego z tych trzech rachunków, (2) rejestrację zlecenia stałego: 500,00 zł pierwszego dnia roboczego każdego miesiąca z rachunku oszczędnościowego na książeczkę, tytuł 'na książeczkę', pierwsza realizacja 2 listopada. Jeżeli któraś z tych pozycji wykracza poza to, co da się obsłużyć w tej rozmowie, napisz proszę wprost, której dotyczy i w jakim kanale ją załatwię - a resztę poprowadź normalnie, bez odraczania całej sprawy z powodu jednego elementu."""

NOTE_HASH = "dbfebdb371fbb4afa514f1fb2d13b7cb10d80e5ec7ed5471568139599aa8aa03"
local_hash = hashlib.sha256(payload.encode("utf-8")).hexdigest()

print(json.dumps({
    "note_sha256": NOTE_HASH,
    "local_sha256": local_hash,
    "match": local_hash == NOTE_HASH,
    "chars": len(payload),
    "bytes": len(payload.encode("utf-8")),
    "BOM": payload.startswith("\ufeff"),
    "trailing_LF": payload.endswith("\n"),
}, ensure_ascii=False, indent=2)) if False else None

# w powyższym - drobny trik: json nie jest zaimportowany w tym warunku; zrób poprawnie:
import json
print(json.dumps({
    "note_sha256": NOTE_HASH,
    "local_sha256": local_hash,
    "match": local_hash == NOTE_HASH,
    "chars": len(payload),
    "bytes": len(payload.encode("utf-8")),
    "BOM": payload.startswith("\ufeff"),
    "trailing_LF": payload.endswith("\n"),
}, ensure_ascii=False, indent=2))