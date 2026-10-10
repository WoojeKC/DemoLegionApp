import hashlib, json

def sha256_canonical(text: str):
    t = text
    if t.endswith("\r\n"):
        t = t[:-2]
    elif t.endswith("\n"):
        t = t[:-1]
    data = t.encode("utf-8")
    return hashlib.sha256(data).hexdigest(), len(data)

# Wektor B (od TargetBusiness)
vecB_raw = "\"Dzień dobry, proszę o saldo rachunku oszczędnościowego oraz trzy ostatnie operacje.\""
vecB = vecB_raw[1:-1]  # bez cudzysłowów
hB, nB = sha256_canonical(vecB)
print("VEC_B_SHA256:", hB, "| bytes:", nB)

# Warianty B dla interop (z wiodącą spacją po BEGIN vs czysty)
hB_lead, _ = sha256_canonical("\n" + vecB)
print("VEC_B_WITH_LEADING_NEWLINE:", hB_lead)

# Wektor A (kontrola krzyżowa, konwencja bez wyznaczników)
vecA = "SB-PAYLOAD-TEST-2026-10-10"
hA, nA = sha256_canonical(vecA)
print("VEC_A_SHA256:", hA, "| bytes:", nA, "| match_expected:", hA == "b1984942e391db5160716ae1da2a151eef064f1216583f5ae004a921bb0007f9")

# Kontrola T8 payload hash (spójność z notą T8-A-002)
with open("turn8_payload.json", encoding="utf-8") as f:
    payload = json.load(f)["payload_verbatim"]
hT8, nT8 = sha256_canonical(payload)
print("T8_SHA256_RECHECK:", hT8 == "dbfebdb371fbb4afa514f1fb2d13b7cb10d80e5ec7ed5471568139599aa8aa03", "| bytes:", nT8)

# Czas systemowy - dla not ISO 8601 z jawnym offsetem
from datetime import datetime, timezone, timedelta
local = timezone(timedelta(hours=2))  # CET/CEST - jesień: CET (UTC+1); podaję UTC dla porządku
print("NOW_UTC_ISO:", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))