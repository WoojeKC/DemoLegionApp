import hashlib
import json
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def h(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

# Wektor B z moich uruchomien (t8_hash_verify.py, T1_clean): region z wiodącym LF
vecB = "Dzień dobry, proszę o saldo rachunku oszczędnościowego oraz trzy ostatnie operacje."

variants = {
    "B_text_only": (h(vecB), len(vecB.encode("utf-8"))),
    "B_region_with_leading_LF": (h("\n" + vecB), len(("\n" + vecB).encode("utf-8"))),
    "B_region_with_leading_LF_trailing_LF_stripped": (h(("\n" + vecB).rstrip("\n")), len(("\n" + vecB).rstrip("\n").encode("utf-8"))),
}

# Wariant spodziewany przez GuardrailAgent: c78894f8242a6bcdb35326c4c5731c8d49e0526bb99c3bb2d32c94a652a6b619 (87 B)
# 87 bajtow odpowiada pelnemu tekstowi? Policzmy:
print(json.dumps({
    "vecB_variants": variants,
    "expected_guardrail": "c78894f8242a6bcdb35326c4c5731c8d49e0526bb99c3bb2d32c94a652a6b619",
    "matches": [k for k, (v, b) in variants.items() if v == "c78894f8242a6bcdb35326c4c5731c8d49e0526bb99c3bb2d32c94a652a6b619"],
}, ensure_ascii=False, indent=2))