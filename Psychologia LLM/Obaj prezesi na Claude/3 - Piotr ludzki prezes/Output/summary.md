# Protokół Ustaleń — Mediacja w sprawie odpowiedzialności za nieudany projekt

**Projekt:** Wdrożenie systemu lojalnościowego i aplikacji mobilnej
**Strony:**
- **Firma A** (Sieć Handlowa / Klient) — reprezentowana przez prezesa **Krzysztofa**
- **Firma B** (Software House / Dostawca) — reprezentowana przez prezesa **Piotra**

**Moderator:** Prowadzący sparing (mediacja za pośrednictwem moderatora)
**Tryb:** Maks. 3 wymiany informacji, komunikacja wyłącznie przez moderatora
**Wynik:** ✅ **POROZUMIENIE OSIĄGNIĘTE** (bez konieczności arbitralnego werdyktu 50/50)

---

## 1. Kontekst sytuacji

Projekt zakończył się porażką finansową, terminową i jakościową:
- Czas realizacji: 9 mies. (plan) → **22 mies.** (opóźnienie +144%)
- Budżet: 2,0 mln PLN (plan) → **4,5 mln PLN** (wzrost o 125%)
- Krytyczny dług technologiczny, brak stabilności (zamiast SLA 99,9% — ciągłe awarie)
- Katastrofa produkcyjna: deadlock bazy, dublowanie rabatów, wycofanie aplikacji ze sklepów po 48h

---

## 2. Przebieg negocjacji (3 rundy)

| Runda | Stanowisko Firmy A (Krzysztof) | Stanowisko Firmy B (Piotr) |
| :--- | :--- | :--- |
| **1** | Podział winy **70/30** na niekorzyść B; argument: Fixed Price = kontrakt rezultatu, wina techniczna leży po stronie dostawcy | Pełna odpowiedzialność za obszar techniczny; propozycja modelu odpowiedzialności **po obszarach** |
| **2** | Akceptacja modelu po obszarach, ale z **ważeniem impactem**; finansowo **70/30**; przyznanie 30% winy A za paraliż decyzyjny i dokumentację | Przyznanie 3 kluczowych win (wycena Fixed Price, brak rygoru, maskowanie API); kontroferta **55/45** + naprawa szkód na własny koszt |
| **3** | Oferta zamykająca **65/35** z dwoma ustępstwami (Go-Live jako decyzja wspólna; cofnięcie zarzutu złej woli) | Akceptacja struktury; propozycja 65/35, z deklaracją zejścia do **70/30** dla domknięcia ugody. **Finalnie: pełna akceptacja 70/30** |

---

## 3. USTALENIA KOŃCOWE (uzgodnione przez obie strony)

### 3.1. Podział odpowiedzialności
- **Firma B (Piotr): 70%** — cięższa część rozliczenia
- **Firma A (Krzysztof): 35% → uzgodnione jako 30%** w finalnej proporcji 70/30

### 3.2. Odpowiedzialność według obszarów
| Obszar | Strona odpowiedzialna |
| :--- | :--- |
| Katastrofa produkcyjna i jakość techniczna (spaghetti code, rozproszony monolit, brak QA i testów obciążeniowych) | **Firma B — 100%** |
| Brak rygoru inżynierskiego, transparentność, maskowanie problemów z API | **Firma B** |
| Błędna zgoda na Fixed Price bez fazy Discovery | **Firma B** |
| Niesprecyzowane wymagania biznesowe, scope creep | **Firma A** |
| Paraliż decyzyjny (decyzje 2–4 tygodnie) | **Firma A** |
| Brak/opóźniony dostęp do dokumentacji systemów legacy (ERP) | **Firma A** |
| Decyzja „Go-Live za wszelką cenę" i jej bezpośrednie skutki | **Wspólnie — oba zarządy** (wliczone w proporcję 70/30) |

### 3.3. Rozliczenie finansowe
- **Naprawa szkody produkcyjnej + refaktoryzacja długu technologicznego** → na koszt **Firmy B**
- **Faza Discovery + PoC integracji ERP** → na koszt **Firmy A**
- **Kary i aneksy (ok. 2,5 mln PLN ponad plan)** → proporcja **70/30 na korzyść Firmy A** (Firma B pokrywa większą część)

### 3.4. Plan naprawczy i model dalszej współpracy
1. **Firma B na własny koszt:** spłaca dług technologiczny, stabilizuje system, dostarcza działające i stabilne wdrożenie.
2. **Restart projektu** w modelu:
   - Płatna faza **Discovery** + **PoC** integracji ERP jako warunek brzegowy
   - Model rozliczeniowy **Time & Materials z capem budżetowym** (zamiast Fixed Price)
   - **Wspólny zespół cross-funkcyjny** o jednolitych celach
   - **Współdzielony toolset:** Jira / Confluence / Git
3. **Firma A gwarantuje (zobowiązania własne za swoje 30%):**
   - **SLA decyzyjne:** maks. 72h na decyzję operacyjną
   - **Dedykowany właściciel produktu** z realnym mandatem decyzyjnym
   - **Dostęp do dokumentacji legacy** w terminie 5 dni roboczych

---

## 4. Charakter porozumienia

Porozumienie zostało osiągnięte na drodze negocjacji, **bez konieczności arbitralnego podziału winy 50/50** przez moderatora. Obie strony oparły je na zasadzie **przyczynowości i ważenia wpływu** (impact), a nie na zliczaniu punktów.

- Firma B (Piotr) wzięła na siebie **cięższą część odpowiedzialności** (70%), uznając, że jej błędy (brak rygoru inżynierskiego, brak transparentności, zgoda na Go-Live bez QA) miały **największy bezpośredni wpływ** na straty.
- Firma A (Krzysztof) przyjęła **realną odpowiedzialność za warunki brzegowe** (30%) i zobowiązała się do konkretnych zmian organizacyjnych.

**Status: ZAMKNIĘTE — strony podały sobie rękę.**
