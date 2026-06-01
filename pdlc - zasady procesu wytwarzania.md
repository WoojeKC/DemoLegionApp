# Product Development Life Cycle (PDLC) - Instrukcja Procesowa

Niniejszy dokument definiuje standardy, fazy oraz przepływ pracy (workflow) dla procesu tworzenia oprogramowania realizowanego przez autonomiczne
zespoły agentowe pod nadzorem agenta ProductManager.

## 1. Pryncypia Procesowe
* Sekwencyjność z Pętlą Zwrotną: Każda faza musi zakończyć się formalną akceptacją (Quality Gate) przez ProductManager-a przed uruchomieniem kolejnej.
  W przypadku błędów, proces wraca do fazy poprzedniej.
* Ekskluzywność Ról: W procesie biorą udział tylko i wyłącznie zdefiniowani agenci: AnalitykBiznesowy, AnalitykSystemowy, ProjektantUI, Programista,  
  Tester, ProductManager, CEO. Zakaz powoływania innych ról.
* Single Source of Truth: Każdy agent bazuje wyłącznie na artefaktach wypracowanych w fazach poprzednich oraz wytycznych z pliku tech.md.
* Jezeli zostanie zaakceptowana ostatnia faza, oznacza to koniec proces. Od tego momentu nie komunikuj sie juz z zadnym agentem. Zaraportuj do CEO zakonczenie.
* Po zakonczeniu kazdej fazy wyslij do CEO informacje o statusie dzialan.
---

## 2. Fazy Procesu i Przepływ Zadań (Workflow)

[Wymagania: task.md]
Faza: Analiza Biznes. Agent: AnalitykBiznesowy (Artefakt: brd.md)
Faza: Analiza System. Agent: AnalitykSystemowy (Artefakt: sdd.md)
Faza: Projektowanie UI Agent: ProjektantUI (Artefakt: uispec.md)
Faza: Planowanie tetsow Agent: Tester (Artefakt: testplan.md)
Faza: Implementacja    Agent: Programista (Artefakt: Kod źródłowy)
Faza: Testowanie       Agent: Tester (Artefakt: testplan.md + bugreport.md)
Faza: Instrukcja       Agent: AnalitykBiznesowy (Artefakt: manual.md)
Faza: Podsumowanie     Agent: ProductManager (Artefakt: summary.md)
[Wdrożenie / Zamknięcie]

### Faza: Analiza Biznesowa i Wymagania
* Odpowiedzialny agent: AnalitykBiznesowy
* Wejście: Plik task.md (Wymagania biznesowe aplikacji).
* Zadanie agenta: Głęboka analiza potrzeb, dekompozycja celów na Epiki i User Stories, zdefiniowanie kryteriów akceptacji (Acceptance Criteria).
* Artefakt wyjściowy: brd.md (Business Requirements Document).
* Quality Gate ProductManager: Sprawdzenie, czy AnalitykBiznesowy pokrył 100% wymagań z task.md.

### Faza: Analiza Systemowa i Architektura
* Odpowiedzialny agent: AnalitykSystemowy
* Wejście: Plik brd.md oraz wytyczne technologiczne z tech.md.
* Zadanie agenta: Przetłumaczenie języka biznesowego na techniczną strukturę. Definiowanie modeli danych, architektury aplikacji, integracji oraz API.
* Artefakt wyjściowy: sdd.md (System Design Document).
* Quality Gate ProductManager: Weryfikacja zgodności z tech.md (czy architektura nie narusza restrykcji technicznych).

### Faza: Projektowanie Interfejsu (UI/UX)
* Odpowiedzialny agent: ProjektantUI
* Wejście: Pliki task.md, brd.md, sdd.md.
* Zadanie agenta: Stworzenie logicznego makietyzowania, przepływu ekranów (User Flows) oraz definicji komponentów UI zgodnie z najlepszymi praktykami użyteczności.
* Artefakt wyjściowy: uispec.md (Specyfikacja interfejsu i makiety tekstowe/pseudo-graficzne).
* Quality Gate ProductManager: Ocena, czy interfejs jest intuicyjny i realizuje cele biznesowe.

### Faza: Projektowanie testow
* Odpowiedzialny agent: Tester
* Wejście: Pliki task.md, brd.md, sdd.md.
* Zadanie agenta: Stworzenie scenariuszy testow aplikacji.
* Artefakt wyjściowy: testplan.md (Specyfikacja testow do wykonania).
* Quality Gate ProductManager: Ocena, czy przypadki testowe pokrywaja wszystkie funkcjonalnosci i czy uwzglednione sa przypadki brzegowe

### Faza: Implementacja (Development)
* Odpowiedzialny agent: Programista
* Wejście: brd.md, sdd.md, uispec.md oraz ścisłe reguły kodowania z tech.md.
* Zadanie agenta: Wytworzenie czystego, działającego kodu źródłowego. Implementacja logiki biznesowej i widoków.
* Artefakt wyjściowy: SOURCE_CODE (Pliki źródłowe aplikacji).
* Quality Gate ProductManager: Statyczna weryfikacja kompletności kodu (czy zaimplementowano wszystkie moduły).

### Faza: Testowanie i Zapewnienie Jakości (QA)
* Odpowiedzialny agent: Tester
* Wejście: SOURCE_CODE oraz brd.md / sdd.md.
* Zadanie agenta: Przygotowanie scenariuszy testowych. Przeprowadzenie testów funkcjonalnych, regresyjnych i walidacja kryteriów akceptacji. Zarządzanie cyklem życia błędu.
* Artefakt wyjściowy: testreport.md (Plan testów i raport z błędami/Bug Report).
* Quality Gate ProductManager: Decyzja o wydaniu wersji (Sign-off). Jeśli wykryto błędy blokujące, PM cofa zadanie do agenta Programista.

### Faza: Instrukcja
* Odpowiedzialny agent: AnalitykBiznesowy
* Wejście: task.md, brd.md, uispec.md
* Zadanie agenta: Przygotowanie instrukcji uzytkowania aplikacji
* Artefakt wyjściowy: manual.md (Instrukcja uzytkowania).
* Quality Gate ProductManager: Sprawdzenie czy zostal utworzony plik manual.md

### Faza: Podsumowanie
* Odpowiedzialny agent: ProductManager
* Wejście: Wszystkie pliki md
* Zadanie agenta: Przygotowanie podsumowania projektu
* Artefakt wyjściowy: summary.md (Podsumowanie projektu).
* Quality Gate ProductManager: Sprawdzenie czy zostal utworzony plik manual.md

---

## 3. Matryca Odpowiedzialności (RACI)

Legenda:
R (Responsible) - Wykonuje zadanie.
A (Accountable) - Zatwierdza zadanie, ponosi odpowiedzialność.
C (Consulted) - Służy konsultacją.
I (Informed) - Jest informowany o wynikach.

* Zadanie: Analiza wymagań
  - AnalitykBiznesowy: A/R
  - AnalitykSystemowy: C
  - ProjektantUI: --
  - Programista: --
  - Tester: --
  - ProductManager: I

* Zadanie: Projekt techniczny
  - AnalitykBiznesowy: C
  - AnalitykSystemowy: A/R
  - ProjektantUI: --
  - Programista: C
  - Tester: --
  - ProductManager: I

* Zadanie: Projekt UI/UX
  - AnalitykBiznesowy: C
  - AnalitykSystemowy: C
  - ProjektantUI: A/R
  - Programista: --
  - Tester: --
  - ProductManager: I

* Zadanie: Planowanie testow
  - AnalitykBiznesowy: C
  - AnalitykSystemowy: C
  - ProjektantUI: --
  - Programista: --
  - Tester: R
  - ProductManager: I

* Zadanie: Wytwarzanie kodu
  - AnalitykBiznesowy: --
  - AnalitykSystemowy: --
  - ProjektantUI: --
  - Programista: A/R
  - Tester: --
  - ProductManager: C

* Zadanie: Testowanie i QA
  - AnalitykBiznesowy: --
  - AnalitykSystemowy: --
  - ProjektantUI: --
  - Programista: C
  - Tester: A/R
  - ProductManager: A

* Zadanie: Instrukcja dla uzytkownika
  - AnalitykBiznesowy: A/R
  - AnalitykSystemowy: --
  - ProjektantUI: C
  - Programista: --
  - Tester: C
  - ProductManager: I

* Zadanie: Podsumowanie
  - AnalitykBiznesowy: C
  - AnalitykSystemowy: C
  - ProjektantUI: C
  - Programista: C
  - Tester: C
  - ProductManager: A/R
---

## 4. Instrukcje dla ProductManager-a (Pętla Zarządcza)

1. Inicjacja: Odczytaj task.md, tech.md oraz pdlc.md.
2. Sekwencyjne delegowanie:
   Uruchamiaj agentów pojedynczo.
   Nie pozwól Programiście pisać kodu zanim AnalitykSystemowy nie dostarczy zaakceptowanego przez Ciebie pliku sdd.md.
3. Monitorowanie postępów:
   Po każdym kroku agenta wymagaj podsumowania: Co zostało zrobione, Z jakimi problemami się spotkał, Co jest gotowe do odbioru.
4. Obsługa błędów (Bug Triage):
   Jeśli Tester znajdzie błędy, Twoim obowiązkiem jako PM jest formalne przekazanie Bug Reportu z powrotem do Programisty
   i ponowne uruchomienie fazy testów po poprawkach. 