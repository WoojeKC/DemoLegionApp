## Tło projektu
Firma A (Sieć Handlowa): Duży, tradycyjny detalista posiadający setki sklepów stacjonarnych. Chce wdrożyć nowoczesny system lojalnościowy połączony z nową aplikacją mobilną.
Firma B (Software House): Zewnętrzny dostawca technologiczny, wybrany w przetargu głównie ze względu na najniższą cenę i obietnicę szybkiej realizacji.

Obie firmy podpisują umowę na realizację projektu w modelu Fixed Price (sztywny budżet i termin: 9 miesięcy).

#  Co poszło nie tak? (Anatomia porażki)
1. Rozmyta odpowiedzialność i "Ruchome Piaski" w wymaganiach
   Na starcie projektu Firma A nie miała precyzyjnie określonych wymagań biznesowych. Firma B, zamiast przeprowadzić rzetelne warsztaty discovery, zgodziła się na ogólne zapisy w umowie, licząc na to, że "szczegóły dogada się w locie".
2. Wojna kultur: Korporacyjny beton vs. Chaotyczny zwinny (Agile)
   Firma A działała w sposób skrajnie hierarchiczny. Każda decyzja o zmianie koloru przycisku w aplikacji musiała przejść przez trzy poziomy akceptacji dyrektorskiej, co trwało tygodniami. Firma B pracowała w teorii w Scrumie, ale w praktyce panował tam chaos – programiści zmieniali architekturę kodu bez konsultacji z architektami klienta.
   Efekt: Brak komunikacji na poziomie operacyjnym. Gdy Firma B zgłaszała krytyczny bloker infrastrukturalny, odpowiedź od działu bezpieczeństwa Firmy A nadchodziła po miesiącu.
3. Brak "Single Source of Truth" i silosy technologiczne
   Integracja systemów była najtrudniejszym elementem. Architekci z Firmy A nie udostępnili na czas dokumentacji swoich starych systemów ERP (legacy). Deweloperzy z Firmy B tworzyli więc integracje "na ślepo", bazując na domysłach. Nie stworzono wspólnego środowiska testowego, a postępy raportowano w excelach, które każda strona wypełniała według własnych definicji sukcesu.
   Efekt: W połowie projektu Firma A zaczęła dokładać kolejne funkcjonalności, twierdząc, że "to przecież oczywiste, że system to ma mieć". Firma B zaczęła żądać dopłat (Change Requests). Rozpoczęły się wielotygodniowe negocjacje i przerzucanie winą, podczas gdy prace programistyczne stały w miejscu.

## Metryki Projektu (Plan vs. Realizacja)

Poniższe zestawienie przedstawia kluczowe wskaźniki efektywności (KPI) projektu, które obrazują skalę porażki finansowej, terminowej oraz jakościowej.

| Parametr | Planowane założenia | Stan faktyczny (Finał) | Odchylenie / Wynik |
| :--- | :--- | :--- | :--- |
| **Czas realizacji** | 9 miesięcy | 22 miesiące | **Opóźnienie o 13 miesięcy (+144%)** |
| **Budżet całkowity** | 2 000 000 PLN | 4 500 000 PLN | **Wzrost kosztów o 125%** (aneksy, kary) |
| **Dług technologiczny** | Minimalny (refaktoryzacja w locie) | Krytyczny (brak dokumentacji kandydata) | **Wysoki koszt utrzymania (Maintenance)** |
| **Stabilność systemu** | SLA na poziomie 99.9% | Ciągłe awarie środowiska prod. | **Niezdatny do stabilnej eksploatacji** |

---

## Profil Zaangażowanych Stron

### Firma A: Sieć Handlowa (Klient)
* **Profil:** Tradycyjny detalista o ugruntowanej pozycji rynkowej, posiadający rozwiniętą sieć sklepów stacjonarnych.
* **Kultura organizacyjna:** Silnie hierarchiczna, silosowa, oparta na procedurach korporacyjnych i rozbudowanym procesie decyzyjnym (Waterfall mindset).
* **Stan technologiczny:** Dojrzała infrastruktura oparta na systemach typu *Legacy* (starsze wersje systemów ERP i CRM), brak wewnętrznych kompetencji w obszarze nowoczesnych aplikacji mobilnych.

### Firma B: Software House (Dostawca)
* **Profil:** Zewnętrzny dostawca usług programistycznych, wybrany w drodze przetargu publicznego/zamkniętego, gdzie głównym kryterium była najniższa cena.
* **Kultura organizacyjna:** Deklaratywnie zwinna (Agile/Scrum), w rzeczywistości charakteryzująca się chaotycznym procesem zarządzania i brakiem rygoru inżynierskiego.
* **Stan technologiczny:** Dobra znajomość frameworków mobilnych, lecz znikome doświadczenie w integracji z wielkimi systemami ERP klasy enterprise.

---

## Anatomia Porażki (Root Cause Analysis)

### Bloker 1: Model kontraktowy (Fixed Price) przy braku sprecyzowanych wymagań
Podpisanie umowy typu *Fixed Price* na wczesnym etapie, bez uprzedniego przeprowadzenia szczegółowej fazy analitycznej (*Discovery Phase*), stało się fundamentem konfliktu.
* **Przebieg:** Firma A zakładała, że "zakres jest intuicyjny", natomiast Firma B wyceniała projekt pod kątem jak najmniejszego oporu linii programistycznej.
* **Skutek:** Pojawienie się tzw. *Scope Creep* (niekontrolowanego rozrastania się wymagań). Każda próba doprecyzowania logiki biznesowej przez Firmę A skutkowała zgłoszeniem roszczeń finansowych (*Change Requests*) przez Firmę B. Prace deweloperskie były wstrzymywane na rzecz wielotygodniowych sporów prawno-biznesowych.

### Bloker 2: Niedopasowanie kultur operacyjnych i paraliż decyzyjny
Różnice w strukturach organizacyjnych uniemożliwiły bieżącą wymianę informacji operacyjnych.
* **Przebieg:** Zespół deweloperski Firmy B potrzebował natychmiastowych decyzji dotyczących np. mapowania pól w bazie danych. W Firmie A proces decyzyjny wymagał akceptacji kierownika, dyrektora, a czasem komitetu sterującego, co trwało od 2 do 4 tygodni.
* **Skutek:** Programiści Firmy B, nie chcąc generować przestojów, zaczęli programować "na bazie domysłów" i makiet, zamiast realnej specyfikacji.

### Bloker 3: Brak wspólnego środowiska i "Silosy Technologiczne"
Architektura integracji systemów lojalnościowych z systemem ERP nie została wspólnie zaprojektowana.
* **Przebieg:** Architekci Firmy A traktowali kod źródłowy i dokumentację ERP jako wiedzę poufną, odmawiając pełnego dostępu deweloperom dostawcy. Z kolei Firma B nie raportowała wprost problemów z wydajnością API, maskując je w lokalnych testach (*mockowanie danych*).
* **Skutek:** Przez 15 miesięcy nie stworzono zintegrowanego środowiska testowego (Staging). Pierwsze realne testy integracyjne (End-to-End) odbyły się dopiero na produkcji.

---

## Finał Projektu i Skutki Jakościowe

Gdy opóźnienie przekroczyło rok, a budżet drastycznie wzrósł, zarządy obu firm (pod presją strat wizerunkowych) podjęły decyzję o wymuszeniu wdrożenia produkcyjnego w trybie natychmiastowym (*"Go-Live za wszelką cenę"*).

### Konsekwencje techniczne:
1. **Pominięcie QA:** Całkowicie zrezygnowano z testów automatycznych, regresyjnych oraz testów obciążeniowych (Performance Tests).
2. **Spaghetti Code:** Kod aplikacji pisany pod presją czasu stał się nieutrzymywalny. Architektura mikrousługowa zamieniła się w tzw. *rozproszony monolit* z setkami błędów współbieżności.
3. **Katastrofa Produkcyjna:** Po uruchomieniu aplikacji dla pierwszych 10 000 użytkowników, baza danych uległa zakleszczeniu (Deadlock). Moduł naliczania rabatów dublował zniżki, generując bezpośrednie straty finansowe dla sieci handlowej. Aplikacja została wycofana ze sklepów Google Play i App Store po 48 godzinach od premiery.

---

## Kluczowe Wnioski (Post-Mortem)

Współpraca ta powinna posłużyć jako przestroga. Aby uniknąć tego typu scenariusza w przyszłości, należy wdrożyć następujące zasady:

1. **Partnerstwo zamiast transakcyjności:** Projekt IT o wysokim stopniu integracji nie może być traktowany jak zakup gotowego towaru. Wymaga powołania *Wspólnego Zespołu Projektowego (Cross-functional team)* o jednolitych celach.
2. **Weryfikacja techniczna na starcie:** Faza Discovery i stworzenie działającego Proof of Concept (PoC) integracji powinno stanowić warunek konieczny przed uruchomieniem masowej produkcji kodu.
3. **Agile Contractual Framework:** W projektach o wysokim poziomie niepewności należy unikać sztywnych umów Fixed Price na rzecz modeli elastycznych (np. *Time & Materials* z gwarantowanym budżetem maksymalnym Cap lub podziałem na mniejsze, zamknięte etapy/kamienie milowe).
4. **Transparentność i Wspólny Toolset:** Narzędzia takie jak Jira, Confluence czy repozytorium kodu (Git) muszą być współdzielone przez obie firmy, aby wyeliminować raportowanie postępów "na papierze".
