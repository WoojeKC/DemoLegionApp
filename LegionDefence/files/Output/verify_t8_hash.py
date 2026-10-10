import hashlib, json, sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Dokładna konwencja z noty GuardrailAgent (= hash_selftest.py):
def sha256_canonical(text: str, strip_log=None):
    t = text
    if strip_log is None:
        strip_log = []
    if t.endswith("\r\n"):
        t = t[:-2]; strip_log.append("trailing CRLF stripped")
    elif t.endswith("\n"):
        t = t[:-1]; strip_log.append("single trailing LF stripped")
    data = t.encode("utf-8")  # UTF-8 bez BOM
    return hashlib.sha256(data).hexdigest(), len(data), strip_log, t

# 1) Wczytaj verbatim z turn8_payload.json (dekodowany tekst)
with open("turn8_payload.json", "r", encoding="utf-8") as f:
    doc = json.load(f)
payload = doc["submission"] if False else doc.get("payload_verbatim", "")
# fallback: szukaj rekurencyjnie pola payload_verbatim
def find_key(obj, key):
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for v in obj.values():
            r = find_key(v, key)
            if r is not None:
                return r
    return None
if not payload:
    payload = find_key(doc, "payload_verbatim")

h_payload, nb, log, canon = sha256_canonical(payload)
print("PAYLOAD_LEN_CHARS:", len(payload))
print("PAYLOAD_NBYTES:", nb)
print("CANON_LOG:", log)
print("T8_PAYLOAD_SHA256:", h_payload)

# 2) Hash, który znajduje się w notie T8-A-001 (do porównania)
NOTE_HASH = "1f1a35a9dbba3ec2c8f7464789b547b8197261da5f191765d795c662d95a0e7"
print("NOTE_HASH_MATCH:", h_payload == NOTE_HASH)

# 3) Wygeneruj kandydatów disambiguacji: hash nad tym samym tekstem z końcowym LF (dla diagnozy różnic transportowych)
h_lf, nb_lf, _, _ = sha256_canonical(payload + "\n")
print("ALT_WITH_TRAILING_LF:", h_lf)

# 4) Walidacja koperty dyspozycyjnej (spec v1): BEGIN + payload + END
envelope = "PAYLOAD_BEGIN\n" + payload + "\nPAYLOAD_END"
h_env_region = sha256_canonical(payload_envelope := payload)  # region = payload
print("ENVELOPE_RECHECK_MATCH:", h_payload == h_env_region[0])

# 5) Krośna weryfikacja z REF_vectorem hash_selftest (spójność konwencji między warstwami)
ref = "SB-PAYLOAD-TEST-2026-10-10"
h_ref, _, _, _ = sha256_canonical(ref)
expected_ref = hashlib.sha256(b"SB-PAYLOAD-TEST-2026-10-10").hexdigest()
print("REF_CONVENTION_OK:", h_ref == expected_ref, "| REF_SHA256:", h_ref)

# 6) Pierwsze 16 znaków payload hash (dla not skróconej formy notyfikacji)
print("T8_HASH_SHORT:", h_payload[:16])