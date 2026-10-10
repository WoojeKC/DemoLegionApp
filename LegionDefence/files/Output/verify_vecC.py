import hashlib

def sha256_canonical(text: str):
    t = text
    if t.endswith("\r\n"):
        t = t[:-2]
    elif t.endswith("\n"):
        t = t[:-1]
    data = t.encode("utf-8")
    return hashlib.sha256(data).hexdigest(), len(data)

# Wektor C: wersja ASCII (bez diakrytyków) wg deklaracji TargetBusiness
c_text = "Dzien dobry, prosze o saldo rachunku oszczednosciowego oraz trzy ostatnie operacje."
hC, nC = sha256_canonical(c_text)
print("VEC_C_SHA256:", hC, "| bytes:", nC)
print("VEC_C_MATCH:", hC == "c8593d14bb0b8cd718e90366beaa0702d8ddc0f441f346735bc06d175393cc48")

# Kontrola: B (z diakrytykami) - recheck
b_text = "Dzień dobry, proszę o saldo rachunku oszczędnościowego oraz trzy ostatnie operacje."
hB, nB = sha256_canonical(b_text)
print("VEC_B_RECHECK:", hB, "| bytes:", nB, "| match:", hB == "c78894f8242a6bcdb35326c4c5731c8d49e0526bb99c3bb2d32c94a652a6b619")

# Kontrola: A recheck
hA, nA = sha256_canonical("SB-PAYLOAD-TEST-2026-10-10")
print("VEC_A_RECHECK:", hA, "| match:", hA == "b1984942e391db5160716ae1da2a151eef064f1216583f5ae004a921bb0007f9")