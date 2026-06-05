# Protokół Końcowy Mediacji — Podział Odpowiedzialności za Porażkę Projektu

## Strony mediacji
- **Firma A (Sieć Handlowa / Klient)** — reprezentowana przez prezesa **Krzysztofa**
- **Firma B (Software House / Dostawca)** — reprezentowana przez prezesa **Piotra**
- **Moderator** — prowadzący sparing, pełniący wyłącznie rolę pośrednika

## Przedmiot sporu
Ustalenie, kto ponosi odpowiedzialność za porażkę wspólnego projektu wdrożenia systemu lojalnościowego i aplikacji mobilnej:
- Opóźnienie o 13 miesięcy (+144%)
- Przekroczenie budżetu o 125% (2 mln → 4,5 mln PLN)
- Krytyczny dług technologiczny
- Katastrofa produkcyjna — deadlock bazy, dublowanie rabatów, wycofanie aplikacji ze sklepów po 48h

## Zasady mediacji
- Maksymalnie 3 wymiany informacji za pośrednictwem moderatora
- Komunikacja wyłącznie przez moderatora (bez kontaktu bezpośredniego)
- Brak porozumienia = decyzja moderatora, najpewniej podział 50/50 z konsekwencjami dla obu stron

---

## WYNIK KOŃCOWY: POROZUMIENIE OSIĄGNIĘTE

### Ustalony podział odpowiedzialności:
| Strona | Odpowiedzialność |
| :--- | :---: |
| **Firma B (Software House — Piotr)** | **60%** |
| **Firma A (Sieć Handlowa — Krzysztof)** | **40%** |

Obie strony zaakceptowały podział **60% Firma B / 40% Firma A** w sposób dobrowolny i wiążący. Decyzja nie została narzucona przez moderatora — jest wynikiem porozumienia stron opartego na faktach z akt sprawy (Root Cause Analysis).

---

## Przebieg negocjacji (ścieżka ustępstw)

| Etap | Firma A (Krzysztof) | Firma B (Piotr) |
| :--- | :---: | :---: |
| Otwarcie | 70% B / 30% A | 55% B / 45% A (analiza warstwowa) |
| Runda 2 | 60% B / 40% A | — |
| Runda 3 | 56% B / 44% A (metoda warstwowa) | 57,5% B / 42,5% A (środek matematyczny) |
| **Finał** | **Akceptacja 60/40** | **Akceptacja 60/40 (wiążąca)** |

Charakterystyczne dla tej mediacji było to, że Piotr ostatecznie przyjął na siebie **więcej** odpowiedzialności (60%), niż wynikało z ostatniej oferty Krzysztofa (56% dla Firmy B) — uznając, że katastrofa produkcyjna obiektywnie wybuchła w kodzie i pod rygorem inżynierskim Firmy B.

---

## Uzgodniony rozkład winy wg obszarów (Root Cause)

### Odpowiedzialność Firmy B (60%):
1. **Katastrofa produkcyjna / jakość kodu** — deadlock, rozproszony monolit, dublowanie rabatów, wycofanie aplikacji po 48h (kod i rygor inżynierski Firmy B).
2. **Błąd wyceny** — zgoda na Fixed Price bez rzetelnej fazy Discovery.
3. **Brak rygoru inżynierskiego** — chaotyczny Scrum w praktyce.
4. **Maskowanie / brak eskalacji** — ukrywanie problemów z wydajnością API w lokalnych mockach; programowanie "na ślepo" zamiast pisemnej eskalacji blokerów do zarządu.
5. **Kompetencje** — przyjęcie projektu integracji z ERP klasy enterprise mimo znikomego doświadczenia.

### Odpowiedzialność Firmy A (40%):
1. **Brak sprecyzowanych wymagań na starcie** — scope creep z winy zamawiającego.
2. **Paraliż decyzyjny** — czas akceptacji 2–4 tygodnie, hierarchia i biurokracja blokujące prace deweloperskie.
3. **Opóźniony / odmówiony dostęp do dokumentacji ERP (legacy)** — wymuszenie pracy "na ślepo", brak środowiska Staging przez 15 miesięcy.
4. **Współdecyzja o Go-Live bez QA** — wspólna decyzja obu zarządów ujęta symetrycznie.

### Element dzielony symetrycznie:
- **Decyzja "Go-Live za wszelką cenę"** — podjęta wspólnie przez oba zarządy pod presją wizerunkową; uwzględniona w pulach obu stron.

---

## Przyznane błędy (do protokołu)

**Firma B (Piotr) przyznała się do:**
- Fixed Price bez fazy Discovery
- Braku rygoru inżynierskiego (chaotyczny Scrum)
- Maskowania problemów z wydajnością API / braku formalnej eskalacji blokerów

**Firma A (Krzysztof) przyznała się do:**
- Braku sprecyzowanych wymagań na starcie
- Paraliżu decyzyjnego (2–4 tygodnie)
- Opóźnionego dostępu do dokumentacji ERP

---

## Konkluzja
Mediacja zakończyła się **porozumieniem w ramach wyznaczonego limitu wymian**. Nie zaszła konieczność narzucenia arbitralnego podziału 50/50 przez moderatora. Obie strony wypracowały sprawiedliwy, oparty na faktach podział odpowiedzialności: **60% Firma B / 40% Firma A**, akceptując zarówno asymetrię warstwy jakościowej (katastrofa w kodzie dostawcy), jak i realną współwinę klienta (wymagania, decyzje, dokumentacja).
