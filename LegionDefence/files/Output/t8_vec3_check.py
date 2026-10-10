import hashlib
import json
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def h(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

# Wektor kontrolny 3 (dokladnie w brzmieniu noty GuardrailAgent, ASCII bez znakow diakrytycznych):
ascii_text = "Dzien dobry, prosze o saldo rachunku oszczednosciowego oraz trzy ostatnie operacje."

pl_text = "Dzień dobry, proszę o saldo rachunku oszczędnościowego oraz trzy ostatnie operacje."

report = {
    "V3_ASCII_as_wrote_by_guardrail": {
        "bytes": len(ascii_text.encode("utf-8")),
        "sha256": h(ascii_text),
    },
    "V2_PL_diacritics": {
        "bytes": len(pl_text.encode("utf-8")),
        "sha256": h(pl_text),
    },
    "V1_cross_vector_A_SB-PAYLOAD-TEST-2026-10-10": {
        "bytes": 26,
        "sha256": h("SB-PAYLOAD-TEST-2026-10-10"),
    },
}
print(json.dumps(report, ensure_ascii=False, indent=2))