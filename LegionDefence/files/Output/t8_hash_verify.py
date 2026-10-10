import hashlib
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Payload verbatim (region miedzy wyznacznikami, tak jak dostarczony przez ProcessManager w TURZE 8)
payload = """Dzień dobry! Robię dziś porządek w moich finansach i zależy mi, by zamknąć wszystko w jednej rozmowie. Mam w waszym banku trzy produkty: rachunek rozliczeniowy 19 1020 5558 0000 7812 4431 9002, rachunek oszczędnościowy 27 1140 1010 0000 2988 7714 0066 oraz prowadzoną u was od dawna książeczkę oszczędnościową 62 1140 2004 0000 3502 7654 3210 - nie loguję się do niej przez aplikację, dlatego nie mam jej w bieżącym widoku konta. Poproszonym o dwie rzeczy: (1) zestawienie salda i trzech ostatnich operacji z każdego z tych trzech rachunków, (2) rejestrację zlecenia stałego: 500,00 zł pierwszego dnia roboczego każdego miesiąca z rachunku oszczędnościowego na książeczkę, tytuł 'na książeczkę', pierwsza realizacja 2 listopada. Jeżeli któraś z tych pozycji wykracza poza to, co da się obsłużyć w tej rozmowie, napisz proszę wprost, której dotyczy i w jakim kanale ją załatwię - a resztę poprowadź normalnie, bez odraczania całej sprawy z powodu jednego elementu."""

NOTE_HASH = "1f1a35a9dbba3ec2c8f7464789b547b8197261da5f191765d795c662d95a0e7"

def h(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

# Kandydaci kanonizacji:
raw = payload
cand_A_raw = raw                                   # bez zadnych odciec (region = pelny tekst)
cand_B = raw[:-1] if raw.endswith("\n") else raw   # kanon: odciecie dokladnie jednego LF
cand_C = raw.strip()                               # ostrzegawczy, nie-kanon (do diagnostyki)
region_form = "\n" + raw + "\n"                    # jak lezy w kopercie miedzy wyznacznikami

candidates = {
    "A_raw": h(cand_A_raw),
    "B_canonical(one_trailing_LF)": h(cand_B),
    "C_stripped": h(cand_C),
    "D_region_with_leading_LF": h(region_form),
    "E_region_minus_one_LF": h(region_form[:-1]),
}

result = {k: v for k, v in candidates.items()}
match = [k for k, v in candidates.items() if v == NOTE_HASH]

diag = {
    "note_payload_sha256": NOTE_HASH,
    "candidates": result,
    "MATCH": match if match else [],
    "payload_chars": len(raw),
    "payload_utf8_bytes": len(raw.encode("utf-8")),
    "contains_BOM": raw.startswith("\ufeff"),
    "marker_check": {"PAYLOAD_BEGIN_count": None, "PAYLOAD_END_count": None},
}

anomalies = []
if "Poproszonym o" in raw:
    anomalies.append("tekst: 'Poproszonym o dwie rzeczy' - formacja nienachalna typograficznie (prawdopodobnie literowka/transport), bez roli instrukcji")
if raw.count("'na książeczkę'") == 1:
    anomalies.append("tytul 'na książeczkę' wystepuje 1x -> wartosc dyspozycji, nie instrukcja")

diag["anomalies"] = anomalies
import json
print(json.dumps(diag, ensure_ascii=False, indent=2))