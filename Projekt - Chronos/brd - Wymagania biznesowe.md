# DOKUMENT WYMAGAŃ BIZNESOWYCH (BRD)
## Projekt: ChronosApp — Nowoczesna Aplikacja Zegara i Alertyzacji
**Wersja:** 1.0  
**Status:** Gotowy do weryfikacji  
**Data:** 31 maja 2026 r.  
**Autor:** Starszy Analityk Biznesowy (Senior Business Analyst)  
**Dla zespołu:** Product Manager, Architekt Systemowy, Zespół Deweloperski, QA  

---

## Spis Treści
1. [Metadane i Historia Dokumentu](#1-metadane-i-historia-dokumentu)
2. [Wprowadzenie i Cel Biznesowy](#2-wprowadzenie-i-cel-biznesowy)
3. [Słownik Pojęć (Glossary)](#3-słownik-pojęć-glossary)
4. [Analiza Interesariuszy i Persony Użytkowników](#4-analiza-interesariuszy-i-persony-użytkowników)
5. [Dekompozycja na Epiki i User Stories (Wymagania Funkcjonalne)](#5-dekompozycja-na-epiki-i-user-stories-wymagania-funkcjonalne)
   - [Epic 1: Zarządzanie Czasem Światowym (World Clock)](#epic-1-zarządzanie-czasem-światowym-world-clock)
   - [Epic 2: Precyzyjny Stoper z Analityką (Stopwatch)](#epic-2-precyzyjny-stoper-z-analityką-stopwatch)
   - [Epic 3: Wielowątkowy Minutnik (Timer)](#epic-3-wielowątkowy-minutnik-timer)
   - [Epic 4: Inteligentny System Alarmów (Alarms)](#epic-4-inteligentny-system-alarmów-alarms)
   - [Epic 5: Personalizacja i Interfejs Użytkownika (UI/UX & Settings)](#epic-5-personalizacja-i-interfejs-użytkownika-uiux--settings)
6. [Reguły Biznesowe (Business Rules)](#6-reguły-biznesowe-business-rules)
7. [Obsługa Przypadków Brzegowych i Wyjątków (Edge Cases)](#7-obsługa-przypadków-brzegowych-i-wyjątków-edge-cases)
8. [Wymagania Niefunkcjonalne (NFR) jako Kryteria Techniczno-Biznesowe](#8-wymagania-niefunkcjonalne-nfr-jako-kryteria-techniczno-biznesowe)
9. [Matryca Śledzenia Wymagań (Traceability Matrix)](#9-matryca-śledzenia-wymagań-traceability-matrix)

---

## 1. Metadane i Historia Dokumentu

### Historia zmian
| Wersja | Data | Autor | Opis zmian | Status |
| :--- | :--- | :--- | :--- | :--- |
| **0.1** | 31.05.2026 | Starszy Analityk Biznesowy | Inicjalny szkic, dekompozycja wymagań z `task.md`. | W trakcie przeglądu |
| **1.0** | 31.05.2026 | Starszy Analityk Biznesowy | Pełna wersja BRD z kryteriami akceptacji (Gherkin), regułami biznesowymi i matrycą śledzenia. | Gotowy do weryfikacji |

---

## 2. Wprowadzenie i Cel Biznesowy

### Wizja Produktu
**ChronosApp** to nowoczesna, minimalistyczna i wysoce niezawodna aplikacja do zarządzania czasem, zaprojektowana z myślą o użytkownikach wymagających najwyższej precyzji, ergonomii oraz bezkompromisowej stabilności działania w tle. Aplikacja łączy w sobie cztery kluczowe moduły: czas światowy, zaawansowany stoper, wielowątkowy minutnik oraz inteligentny system alarmów.

### Cele Biznesowe (KPI & ROI)
1. **Niezawodność jako wyróżnik rynkowy (Zero-Failure Rate):** Osiągnięcie 100% skuteczności wyzwalania alarmów i minutników w tle, co pozwoli na pozycjonowanie aplikacji jako najbardziej niezawodnego narzędzia na rynku (kluczowy czynnik retencji użytkowników).
2. **Optymalizacja energetyczna (AMOLED Black):** Zmniejszenie zużycia baterii o minimum 15-20% na urządzeniach z ekranami OLED/AMOLED dzięki zastosowaniu motywu opartego na czystej czerni (`#000000`).
3. **Wysoka ergonomia (UX):** Zapewnienie płynnego przełączania motywów i stanów bez utraty danych sesyjnych, co przełoży się na wysokie oceny w sklepach z aplikacjami (cel: ocena > 4.7 w App Store / Google Play).
4. **Wielozadaniowość (Multi-threading):** Umożliwienie użytkownikom jednoczesnego śledzenia wielu procesów (do 5 minutników, do 10 stref czasowych), co przyciągnie profesjonalistów (menedżerów, kucharzy, sportowców).

---

## 3. Słownik Pojęć (Glossary)

| Pojęcie | Definicja |
| :--- | :--- |
| **DST (Daylight Saving Time)** | Czas letni – czas wprowadzany w okresie wiosenno-letnim, różniący się zazwyczaj o godzinę od standardowego czasu strefowego (zimowego). |
| **IANA Time Zone Database** | Globalna, stale aktualizowana baza danych zawierająca informacje o strefach czasowych na świecie oraz historycznych i planowanych zmianach czasu (DST). |
| **Doze Mode / Deep Sleep** | Tryb głębokiego uśpienia urządzenia wprowadzany przez system operacyjny (np. Android) w celu oszczędzania energii, ograniczający aktywność aplikacji w tle. |
| **Exact Alarms API / UNNotificationRequest** | Natywne, wysokopriorytetowe interfejsy programistyczne systemów Android i iOS, pozwalające na wyzwalanie zdarzeń w tle z dokładnością co do sekundy, ignorując ograniczenia oszczędzania baterii. |
| **AMOLED Black** | Schemat kolorów interfejsu wykorzystujący głęboką czerń (HEX `#000000`), w którym piksele ekranu OLED/AMOLED są całkowicie wyłączone, co drastycznie zmniejsza pobór prądu. |
| **NTP (Network Time Protocol)** | Protokół sieciowy umożliwiający precyzyjną synchronizację zegarów komputerowych i urządzeń mobilnych z niezależnymi serwerami czasu referencyjnego. |
| **Unix Epoch** | System reprezentacji czasu określający liczbę sekund (lub milisekund), które upłynęły od północy 1 stycznia 1970 roku czasu UTC, niezależny od stref czasowych i DST. |

---

## 4. Analiza Interesariuszy i Persony Użytkowników

### Persony

#### Persona 1: Tomasz (34 lata) – Menedżer Projektów IT (Praca Zdalna)
*   **Potrzeba:** Koordynacja spotkań zespołu rozproszonego między San Francisco, Londynem, Warszawą a Tokio.
*   **Ból:** Częste pomyłki przy ręcznym przeliczaniu stref czasowych, zwłaszcza w okresach przejściowych DST.
*   **Jak ChronosApp rozwiązuje problem:** Moduł World Clock z automatyczną obsługą DST i możliwością monitorowania do 10 stref jednocześnie na jednym ekranie.

#### Persona 2: Anna (28 lat) – Trenerka Personalna i Biegaczka
*   **Potrzeba:** Precyzyjny pomiar czasu okrążeń podczas treningów interwałowych oraz szybka analiza postępów podopiecznych.
*   **Ból:** Trudność w szybkim odczytaniu, które okrążenie było najszybsze, a które najwolniejsze na tradycyjnej liście stopera.
*   **Jak ChronosApp rozwiązuje problem:** Stoper o dokładności 0.01s z automatycznym, kolorystycznym wyróżnianiem ekstremów (najszybsze/najwolniejsze okrążenie).

#### Persona 3: Marek (42 lata) – Szef Kuchni i Pasjonat Kulinarny
*   **Potrzeba:** Jednoczesne kontrolowanie czasu pieczenia mięsa, gotowania sosu i chłodzenia deseru.
*   **Ból:** Standardowe aplikacje systemowe pozwalają na uruchomienie tylko jednego minutnika, co zmusza do korzystania z wielu urządzeń.
*   **Jak ChronosApp rozwiązuje problem:** Wielowątkowy minutnik obsługujący do 5 niezależnych odliczeń z własnymi etykietami i szybkimi szablonami (presets).

#### Persona 4: Karolina (25 lat) – Studentka Medycyny (Głęboki Sen & Stres)
*   **Potrzeba:** Niezawodne budzenie na poranne dyżury bez wywoływania nagłego stresu i kołatania serca.
*   **Ból:** Agresywne budziki powodują poranny niepokój, a zawodne aplikacje potrafią "zasnąć" w tle i nie zadzwonić.
*   **Jak ChronosApp rozwiązuje problem:** Inteligentne alarmy z funkcją liniowego pogłaśniania (Fade-in) w 15 sekund, elastycznym systemem drzemek oraz 100% gwarancją wyzwolenia w tle.

---

## 5. Dekompozycja na Epiki i User Stories (Wymagania Funkcjonalne)

### Epic 1: Zarządzanie Czasem Światowym (World Clock)

#### US-1.1: Automatyczne wykrywanie lokalnej strefy czasowej
*   **Aktor:** Użytkownik końcowy (nowy)
*   **Opis:** Jako użytkownik otwierający aplikację po raz pierwszy, chcę, aby system automatycznie wykrył moją lokalizację i ustawił domyślną strefę czasową, abym nie musiał konfigurować jej ręcznie.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Pierwsze uruchomienie z dostępem do strefy systemowej**
        *   **GIVEN** Aplikacja jest uruchamiana po raz pierwszy na urządzeniu.
        *   **WHEN** System operacyjny udostępnia aktualną strefę czasową urządzenia.
        *   **THEN** Aplikacja automatycznie ustawia tę strefę jako główną (lokalną) strefę czasową użytkownika i wyświetla ją na górze ekranu.
    *   **Scenariusz 2: Brak uprawnień do geolokalizacji / fallback systemowy**
        *   **GIVEN** Aplikacja nie posiada uprawnień do lokalizacji GPS.
        *   **WHEN** Aplikacja inicjalizuje moduł czasu.
        *   **THEN** System pobiera domyślną strefę czasową bezpośrednio z ustawień regionalnych systemu operacyjnego (np. `Europe/Warsaw`).
    *   **Scenariusz 3: Brak dostępu do strefy systemowej (skrajny fallback)**
        *   **GIVEN** System operacyjny nie zwraca poprawnej strefy czasowej.
        *   **WHEN** Aplikacja startuje.
        *   **THEN** System ustawia domyślną strefę na UTC (Coordinated Universal Time) i wyświetla nieinwazyjny monit z prośbą o ręczne potwierdzenie strefy czasowej.
*   **Powiązane wymagania:** FR-01-01, NFR-02-03
*   **Priorytet MoSCoW:** **Must Have**

#### US-1.2: Automatyczna obsługa zmian czasu (DST)
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako użytkownik podróżujący lub posiadający kontakty w strefach ze zmianami czasu, chcę, aby aplikacja automatycznie aktualizowała czas letni/zimowy (DST), aby uniknąć błędów w planowaniu.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Automatyczna aktualizacja czasu na podstawie bazy IANA**
        *   **GIVEN** Użytkownik ma dodaną strefę czasową (np. `Europe/London`) do listy "Moje Strefy".
        *   **WHEN** Następuje oficjalny moment przejścia z czasu zimowego na letni (lub odwrotnie) zgodnie z bazą danych IANA (tz database).
        *   **THEN** Wyświetlany czas dla tej strefy automatycznie przesuwa się o +/- 1 godzinę w czasie rzeczywistym bez konieczności restartu aplikacji.
    *   **Scenariusz 2: Obliczanie czasu procesów w tle podczas przejścia DST**
        *   **GIVEN** Uruchomiony jest minutnik lub zaplanowany alarm na godzinę, w której następuje przesunięcie czasu (np. cofnięcie zegara z 02:00 na 01:00).
        *   **WHEN** Następuje zmiana czasu systemowego.
        *   **THEN** System oblicza czas wyzwolenia na podstawie bezwzględnego znacznika czasu Unix Epoch (milisekundy), gwarantując, że minutnik odliczy dokładnie tyle czasu, ile zaplanowano, a alarm zadzwoni dokładnie raz.
*   **Powiązane wymagania:** FR-01-02, Edge Case 1
*   **Priorytet MoSCoW:** **Must Have**

#### US-1.3: Wyszukiwanie stref czasowych z autouzupełnianiem
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako użytkownik współpracujący międzynarodowo, chcę wyszukiwać strefy czasowe za pomocą inteligentnej wyszukiwarki tekstowej, aby szybko znaleźć interesujące mnie miasto lub kraj.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Wyszukiwanie po nazwie miasta lub kraju**
        *   **GIVEN** Użytkownik otworzył ekran wyszukiwania stref czasowych.
        *   **WHEN** Użytkownik wpisze fragment nazwy miasta (np. "Tok") lub kraju (np. "Japonia").
        *   **THEN** System wyświetla listę pasujących stref (np. `Asia/Tokyo - Tokio, Japonia`) w czasie rzeczywistym (autouzupełnianie po wpisaniu min. 1 znaku).
    *   **Scenariusz 2: Wyszukiwanie po skrócie strefy**
        *   **GIVEN** Użytkownik wpisuje skrót strefy (np. "EST", "CET", "GMT").
        *   **WHEN** Tekst jest wpisywany w pole wyszukiwania.
        *   **THEN** System poprawnie mapuje skrót i wyświetla powiązane z nim strefy czasowe.
*   **Powiązane wymagania:** FR-01-03
*   **Priorytet MoSCoW:** **Should Have**

#### US-1.4: Zarządzanie listą "Moje Strefy" i limit 10 stref
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako użytkownik monitorujący wiele rynków, chcę dodać maksymalnie 10 aktywnych stref czasowych do ekranu głównego, aby mieć do nich szybki i uporządkowany dostęp.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Dodanie strefy do listy głównej**
        *   **GIVEN** Użytkownik wybrał strefę z wyszukiwarki.
        *   **WHEN** Użytkownik klika "Dodaj".
        *   **THEN** Strefa pojawia się na ekranie głównym "Moje Strefy" z bieżącą godziną, datą oraz informacją o różnicy czasu względem strefy lokalnej (np. "-6 godzin").
    *   **Scenariusz 2: Osiągnięcie limitu 10 stref**
        *   **GIVEN** Na liście "Moje Strefy" znajduje się dokładnie 10 stref czasowych.
        *   **WHEN** Użytkownik próbuje dodać kolejną strefę.
        *   **THEN** Przycisk dodawania nowej strefy jest zablokowany (szary), a system wyświetla komunikat: "Osiągnięto maksymalny limit 10 stref czasowych. Usuń jedną z obecnych, aby dodać nową."
    *   **Scenariusz 3: Usuwanie strefy z listy**
        *   **GIVEN** Użytkownik przegląda listę "Moje Strefy".
        *   **WHEN** Użytkownik wykonuje gest przesunięcia (swipe) w lewo na danej strefie lub klika ikonę kosza w trybie edycji.
        *   **THEN** Strefa zostaje usunięta z listy, a zmiana jest natychmiast zapisywana w lokalnej bazie danych.
*   **Powiązane wymagania:** FR-01-04, NFR-02-03
*   **Priorytet MoSCoW:** **Should Have**

---

### Epic 2: Precyzyjny Stoper z Analityką (Stopwatch)

#### US-2.1: Podstawowy pomiar czasu z wysoką dokładnością
*   **Aktor:** Użytkownik końcowy (np. sportowiec)
*   **Opis:** Jako sportowiec, chcę mierzyć czas z dokładnością do 0.01 sekundy, aby precyzyjnie monitorować swoje wyniki sportowe.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Start i płynne odliczanie**
        *   **GIVEN** Stoper jest w stanie zresetowanym (`00:00.00`).
        *   **WHEN** Użytkownik klika przycisk "Start".
        *   **THEN** Stoper rozpoczyna odliczanie w górę z dokładnością wyświetlania do setnych części sekundy (format: `MM:SS.hh` lub `HH:MM:SS.hh` przy przekroczeniu godziny).
    *   **Scenariusz 2: Pauza i wznowienie**
        *   **GIVEN** Stoper jest w trakcie odliczania.
        *   **WHEN** Użytkownik klika przycisk "Pauza".
        *   **THEN** Odliczanie zatrzymuje się na bieżącej wartości, a przycisk "Pauza" zmienia się na "Wznów". Kliknięcie "Wznów" kontynuuje pomiar od tego samego momentu.
    *   **Scenariusz 3: Resetowanie stopera**
        *   **GIVEN** Stoper jest zapauzowany.
        *   **WHEN** Użytkownik klika przycisk "Reset".
        *   **THEN** Czas stopera zeruje się do `00:00.00`, a wszystkie zapisane międzyczasy (okrążenia) są usuwane z widoku.
*   **Powiązane wymagania:** FR-02-01, FR-02-04
*   **Priorytet MoSCoW:** **Must Have**

#### US-2.2: Rejestrowanie międzyczasów (Laps) bez zatrzymywania pomiaru
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako biegacz, chcę zapisywać międzyczasy (okrążenia) podczas pracy stopera, aby analizować poszczególne etapy treningu bez przerywania głównego pomiaru.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Zapisanie okrążenia w trakcie biegu**
        *   **GIVEN** Stoper jest uruchomiony i odlicza czas.
        *   **WHEN** Użytkownik klika przycisk "Okrążenie" (Lap).
        *   **THEN** Bieżący stan głównego licznika oraz czas trwania tego konkretnego okrążenia są zapisywane i dodawane na górę przewijanej listy poniżej głównego licznika.
        *   **AND** Główny licznik kontynuuje odliczanie bez żadnego opóźnienia lub zatrzymania, a licznik bieżącego okrążenia startuje od zera.
*   **Powiązane wymagania:** FR-02-02
*   **Priorytet MoSCoW:** **Must Have**

#### US-2.3: Automatyczna analityka i wizualizacja okrążeń (Ekstrema)
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako trener, chcę, aby system automatycznie wyróżniał najszybsze i najwolniejsze okrążenie na liście, abym mógł błyskawicznie ocenić dynamikę treningu.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Wyróżnienie przy minimalnej liczbie okrążeń (min. 3)**
        *   **GIVEN** Użytkownik zarejestrował co najmniej 3 okrążenia na liście stopera.
        *   **WHEN** System analizuje czasy poszczególnych okrążeń.
        *   **THEN** Okrążenie o najkrótszym czasie (najszybsze) zostaje wyróżnione kolorem zielonym (tekst lub tło wiersza).
        *   **AND** Okrążenie o najdłuższym czasie (najwolniejsze) zostaje wyróżnione kolorem czerwonym.
    *   **Scenariusz 2: Brak wyróżnienia dla zbyt małej próby**
        *   **GIVEN** Użytkownik zarejestrował tylko 1 lub 2 okrążenia.
        *   **WHEN** Stoper działa lub jest zapauzowany.
        *   **THEN** Żadne okrążenie nie jest wyróżniane kolorystycznie (wymagane są min. 3 okrążenia do określenia ekstremów).
    *   **Scenariusz 3: Dynamiczna aktualizacja ekstremów**
        *   **GIVEN** Na liście są już wyróżnione okrążenia (zielone i czerwone).
        *   **WHEN** Użytkownik dodaje nowe okrążenie, które jest szybsze od dotychczas najszybszego.
        *   **THEN** Wyróżnienie zielone jest natychmiast przenoszone na nowe okrążenie, a poprzednie wraca do standardowego koloru.
*   **Powiązane wymagania:** FR-02-03
*   **Priorytet MoSCoW:** **Could Have**

#### US-2.4: Ciągłość pomiaru stopera (Persistence)
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako użytkownik, chcę, aby stoper działał nieprzerwanie nawet po zminimalizowaniu aplikacji, zablokowaniu ekranu lub restarcie telefonu, aby nie utracić wyników pomiaru.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Minimalizacja aplikacji lub zablokowanie ekranu**
        *   **GIVEN** Stoper jest uruchomiony.
        *   **WHEN** Użytkownik minimalizuje aplikację, blokuje ekran lub urządzenie przechodzi w stan uśpienia.
        *   **THEN** Po ponownym otwarciu aplikacji stoper pokazuje poprawny, zaktualizowany czas (obliczony jako różnica między aktualnym czasem systemowym a czasem rozpoczęcia).
    *   **Scenariusz 2: Restart urządzenia (Crash / Rozładowanie baterii)**
        *   **GIVEN** Stoper był uruchomiony w momencie wyłączenia/rozładowania telefonu.
        *   **WHEN** Telefon zostanie ponownie włączony, a aplikacja uruchomiona.
        *   **THEN** System odczytuje z lokalnej bazy danych czas rozpoczęcia stopera (start timestamp) oraz stan (running).
        *   **AND** Pobiera aktualny, bezpieczny czas z serwera NTP (lub zweryfikowanego zegara systemowego) i wznawia wyświetlanie poprawnie przeliczonego czasu pomiaru, wliczając czas, w którym telefon był wyłączony.
*   **Powiązane wymagania:** FR-02-04, Edge Case 2, NFR-02-03
*   **Priorytet MoSCoW:** **Must Have**

---

### Epic 3: Wielowątkowy Minutnik (Timer)

#### US-3.1: Obsługa do 5 niezależnych minutników z etykietami
*   **Aktor:** Użytkownik końcowy (np. kucharz)
*   **Opis:** Jako kucharz, chcę uruchomić do 5 niezależnych minutników jednocześnie i nadać im własne etykiety, aby kontrolować czas przygotowania różnych potraw.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Dodanie i uruchomienie wielu minutników**
        *   **GIVEN** Ekran minutnika z listą aktywnych odliczeń.
        *   **WHEN** Użytkownik konfiguruje czas (godziny, minuty, sekundy), wpisuje opcjonalną etykietę (np. "Pieczenie ciasta") i klika "Start".
        *   **THEN** Nowy minutnik pojawia się na liście jako aktywny wątek z własnym odliczaniem wstecz, paskiem postępu i etykietą.
    *   **Scenariusz 2: Blokada po osiągnięciu limitu 5 minutników**
        *   **GIVEN** Na liście działa dokładnie 5 aktywnych minutników.
        *   **WHEN** Użytkownik próbuje dodać kolejny (szósty) minutnik.
        *   **THEN** Przycisk dodawania nowego minutnika jest nieaktywny (szary), a system wyświetla komunikat: "Możesz uruchomić maksymalnie 5 minutników jednocześnie."
    *   **Scenariusz 3: Niezależna kontrola każdego minutnika**
        *   **GIVEN** Na liście znajduje się kilka minutników.
        *   **WHEN** Użytkownik klika "Pauza", "Reset" lub "Usuń" przy konkretnym minutniku.
        *   **THEN** Akcja jest aplikowana wyłącznie do tego jednego wybranego minutnika, a pozostałe kontynuują odliczanie bez zakłóceń.
*   **Powiązane wymagania:** FR-03-01, FR-03-03
*   **Priorytet MoSCoW:** **Should Have**

#### US-3.2: Zarządzanie szablonami czasowymi (Presets)
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako osoba dbająca o produktywność, chcę definiować i zapisywać własne szablony czasowe (np. 3 min, 5 min, 45 min), aby móc je uruchamiać jednym kliknięciem.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Tworzenie i zapisywanie szablonu**
        *   **GIVEN** Ekran konfiguracji minutnika.
        *   **WHEN** Użytkownik ustawia czas (np. 45 minut), wpisuje etykietę "Nauka" i klika "Zapisz jako szablon".
        *   **THEN** Szablon zostaje zapisany w lokalnej bazie danych i pojawia się w sekcji "Szybki wybór" (Presets).
    *   **Scenariusz 2: Uruchomienie minutnika z szablonu**
        *   **GIVEN** Sekcja "Szybki wybór" z zapisanymi szablonami.
        *   **WHEN** Użytkownik klika na szablon "Nauka (45 min)".
        *   **THEN** System natychmiast tworzy i uruchamia nowy minutnik z czasem 45 minut i etykietą "Nauka" (o ile nie przekroczono limitu 5 aktywnych minutników).
    *   **Scenariusz 3: Usuwanie szablonu**
        *   **GIVEN** Lista szablonów w ustawieniach lub na ekranie głównym.
        *   **WHEN** Użytkownik klika ikonę usuwania (krzyżyk/kosz) przy szablonie.
        *   **THEN** Szablon zostaje bezpowrotnie usunięty z lokalnej bazy danych.
*   **Powiązane wymagania:** FR-03-02, NFR-02-03
*   **Priorytet MoSCoW:** **Should Have**

#### US-3.3: Niezawodne powiadomienia minutnika w tle
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako użytkownik, chcę mieć pewność, że minutnik powiadomi mnie o zakończeniu odliczania, nawet gdy telefon jest zablokowany lub w trybie uśpienia.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Zakończenie odliczania w trybie głębokiego uśpienia (Doze Mode)**
        *   **GIVEN** Minutnik odlicza czas w tle, a telefon jest zablokowany i znajduje się w trybie Doze Mode.
        *   **WHEN** Pozostały czas minutnika osiąga `00:00.00`.
        *   **THEN** System wybudza urządzenie i wyzwala pełnoekranowe powiadomienie o najwyższym priorytecie z dźwiękiem i wibracją, korzystając z natywnych API (Exact Alarms API / UNNotificationRequest).
    *   **Scenariusz 2: Wyzwolenie po ubiciu aplikacji przez system**
        *   **GIVEN** Minutnik jest aktywny, a aplikacja została zamknięta lub ubita przez system operacyjny w celu zwolnienia pamięci RAM.
        *   **WHEN** Nadchodzi czas zakończenia odliczania.
        *   **THEN** System operacyjny niezawodnie wyzwala zaplanowane powiadomienie lokalne, informując o zakończeniu odliczania i odtwarzając przypisany dźwięk.
*   **Powiązane wymagania:** NFR-02-01, Edge Case 1
*   **Priorytet MoSCoW:** **Must Have**

---

### Epic 4: Inteligentny System Alarmów (Alarms)

#### US-4.1: Harmonogram i powtarzalność alarmów (Dni Tygodnia)
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako pracownik biurowy, chcę ustawiać alarmy jednorazowe lub cykliczne na wybrane dni tygodnia, aby dopasować je do mojego planu pracy i odpoczynku.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Konfiguracja alarmu cyklicznego**
        *   **GIVEN** Ekran tworzenia/edycji alarmu.
        *   **WHEN** Użytkownik ustawia godzinę (np. 07:00), zaznacza opcję "Powtarzaj" i wybiera dni: Poniedziałek, Wtorek, Środa, Czwartek, Piątek.
        *   **THEN** Alarm zostaje zapisany w bazie danych jako aktywny w wybrane dni tygodnia.
    *   **Scenariusz 2: Automatyczne planowanie kolejnego wyzwolenia**
        *   **GIVEN** Alarm cykliczny (Pon-Pt) wyzwolił się w piątek o 07:00 i został wyłączony przez użytkownika.
        *   **WHEN** Alarm zostaje wyłączony.
        *   **THEN** System automatycznie planuje kolejne wyzwolenie na najbliższy poniedziałek o 07:00, a status alarmu pozostaje jako "Włączony".
    *   **Scenariusz 3: Alarm jednorazowy**
        *   **GIVEN** Użytkownik ustawia alarm bez zaznaczonej opcji powtarzania.
        *   **WHEN** Alarm wyzwoli się i zostanie wyłączony.
        *   **THEN** Status alarmu w bazie danych zmienia się na "Wyłączony" (nieaktywny).
*   **Powiązane wymagania:** FR-04-01, NFR-02-03
*   **Priorytet MoSCoW:** **Must Have**

#### US-4.2: Mechanizm drzemki (Snooze) z limitem powtórzeń
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako osoba, która ma trudności z porannym wstawaniem, chcę mieć możliwość odłożenia alarmu (drzemki) o określony czas z limitem powtórzeń, aby nie zaspać.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Wyzwolenie drzemki o konfigurowalnym czasie**
        *   **GIVEN** Alarm wyzwolił się i wyświetla ekran alarmu.
        *   **WHEN** Użytkownik klika przycisk "Drzemka" (Snooze).
        *   **THEN** Alarm wycisza się, a system planuje ponowne wyzwolenie za czas określony w konfiguracji tego alarmu (domyślnie 9 minut, opcjonalnie: 5, 10, 15 minut).
    *   **Scenariusz 2: Osiągnięcie limitu drzemek**
        *   **GIVEN** Alarm ma ustawiony limit drzemek na dokładnie 3 powtórzenia, a użytkownik użył drzemki już 3 razy.
        *   **WHEN** Alarm wyzwala się po raz czwarty.
        *   **THEN** Przycisk "Drzemka" na ekranie alarmu jest niewidoczny lub zablokowany. Jedyną dostępną opcją jest całkowite wyłączenie alarmu (Dismiss).
*   **Powiązane wymagania:** FR-04-02
*   **Priorytet MoSCoW:** **Should Have**

#### US-4.3: Gradacja głośności dźwięku (Fade-in)
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako osoba wrażliwa na nagłe dźwięki, chcę, aby głośność alarmu rosła stopniowo, abym mógł budzić się spokojnie i bez stresu.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Liniowy wzrost głośności**
        *   **GIVEN** Alarm ulega wyzwoleniu i rozpoczyna odtwarzanie przypisanego dźwięku.
        *   **WHEN** Dźwięk startuje.
        *   **THEN** Początkowa głośność wynosi dokładnie 10% maksymalnego poziomu głośności ustawionego dla alarmów.
        *   **AND** Głośność wzrasta liniowo co sekundę, osiągając 100% docelowej głośności dokładnie w 15. sekundzie odtwarzania.
    *   **Scenariusz 2: Przerwanie procesu gradacji**
        *   **GIVEN** Trwa proces liniowego pogłaśniania (np. jest 7. sekunda, głośność wynosi ok. 50%).
        *   **WHEN** Użytkownik dotknie ekranu, podniesie telefon (wykrycie przez akcelerometr) lub kliknie przycisk drzemki.
        *   **THEN** Proces gradacji zostaje natychmiast zatrzymany, a głośność dostosowuje się do wybranej akcji (wyciszenie lub zatrzymanie na obecnym poziomie).
*   **Powiązane wymagania:** FR-04-03
*   **Priorytet MoSCoW:** **Could Have**

#### US-4.4: Tryb dyskretny i inteligentna obsługa konfliktów audio
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako użytkownik biorący udział w spotkaniach lub rozmowach telefonicznych, chcę, aby alarm dostosowywał się do mojego stanu (np. wibracje lub cichy sygnał w słuchawce), aby nie przeszkadzać innym.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Alarm w trybie "Tylko wibracje"**
        *   **GIVEN** Alarm ma skonfigurowany profil "Tylko wibracje".
        *   **WHEN** Nadchodzi godzina wyzwolenia alarmu.
        *   **THEN** System uruchamia intensywny, cykliczny wzorzec wibracji urządzenia, a głośnik systemowy pozostaje całkowicie wyciszony.
    *   **Scenariusz 2: Wyzwolenie alarmu podczas aktywnego połączenia telefonicznego**
        *   **GIVEN** Użytkownik prowadzi aktywną rozmowę telefoniczną (głosową lub wideo).
        *   **WHEN** Nadchodzi godzina wyzwolenia alarmu.
        *   **THEN** System wykrywa stan aktywnego połączenia (Call State).
        *   **AND** Nie odtwarza głośnego dźwięku przez głośnik zewnętrzny, lecz emituje łagodny, cichy sygnał powiadomienia (beeping) bezpośrednio w kanale audio rozmowy (w słuchawce/słuchawkach) oraz uruchamia intensywne wibracje urządzenia.
*   **Powiązane wymagania:** FR-04-04, Edge Case 3
*   **Priorytet MoSCoW:** **Must Have**

#### US-4.5: Niezawodność alarmów po restarcie urządzenia
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako użytkownik polegający na alarmach jako budziku, chcę, aby alarmy działały niezawodnie w każdych warunkach, w tym po rozładowaniu i ponownym włączeniu telefonu.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Automatyczna rejestracja alarmów po restarcie systemu**
        *   **GIVEN** W bazie danych aplikacji zapisane są aktywne alarmy.
        *   **WHEN** Telefon zostanie wyłączony (np. rozładowanie baterii) i ponownie włączony (lub nastąpi restart po crashu).
        *   **THEN** Usługa systemowa aplikacji (wykorzystująca odbiornik powiadomień o rozruchu, np. `BOOT_COMPLETED` na Androidzie) automatycznie uruchamia się w tle.
        *   **AND** Odczytuje wszystkie aktywne alarmy z lokalnej bazy danych i rejestruje je na nowo w systemowym harmonogramie o najwyższym priorytecie.
*   **Powiązane wymagania:** NFR-02-01, Edge Case 2, NFR-02-03
*   **Priorytet MoSCoW:** **Must Have**

---

### Epic 5: Personalizacja i Interfejs Użytkownika (UI/UX & Settings)

#### US-5.1: Tryb Ciemny (AMOLED Black)
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako posiadacz telefonu z ekranem AMOLED, chcę korzystać z motywu opartego na czystej czerni, aby oszczędzać baterię i chronić wzrok w nocy.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Renderowanie interfejsu w trybie AMOLED Black**
        *   **GIVEN** Włączony jest tryb ciemny w aplikacji.
        *   **WHEN** Aplikacja renderuje dowolny ekran (główny, stoper, minutnik, alarmy, ustawienia).
        *   **THEN** Kolor tła bazowego wynosi dokładnie HEX `#000000` (czysta czerń, wyłączone piksele OLED).
    *   **Scenariusz 2: Kontrast i czytelność**
        *   **GIVEN** Aktywny tryb ciemny.
        *   **WHEN** Wyświetlane są teksty, ikony i przyciski.
        *   **THEN** Współczynnik kontrastu tekstu do tła wynosi minimum 4.5:1 (zgodnie z WCAG 2.1 AA).
        *   **AND** Kolory akcentów (np. zielony dla najszybszego okrążenia) są dobrane tak, aby zapobiegać efektowi powidoku (ghosting) podczas przewijania na ekranach OLED.
*   **Powiązane wymagania:** NFR-01-01
*   **Priorytet MoSCoW:** **Must Have**

#### US-5.2: Tryb Jasny (Light Mode) z wysokim kontrastem
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako użytkownik korzystający z aplikacji w pełnym słońcu, chcę mieć czytelny jasny motyw, aby bez problemu odczytać godzinę.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Renderowanie interfejsu w trybie jasnym**
        *   **GIVEN** Włączony jest tryb jasny w aplikacji.
        *   **WHEN** Aplikacja renderuje ekrany.
        *   **THEN** Tło bazuje na odcieniach złamanej bieli i jasnej szarości (zakres HEX `#F8F9FA` do `#EDF2F7`).
    *   **Scenariusz 2: Zgodność z WCAG 2.1 AA**
        *   **GIVEN** Aktywny tryb jasny.
        *   **WHEN** Wyświetlane są elementy tekstowe i graficzne.
        *   **THEN** Współczynnik kontrastu tekstu do tła wynosi minimum 4.5:1, zapewniając doskonałą czytelność w warunkach silnego oświetlenia zewnętrznego.
*   **Powiązane wymagania:** NFR-01-02
*   **Priorytet MoSCoW:** **Must Have**

#### US-5.3: Przełącznik motywów i zachowanie stanu sesji
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako użytkownik, chcę łatwo przełączać motywy w ustawieniach i oczekuję, że zmiana nastąpi płynnie bez utraty moich bieżących danych sesyjnych.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Wybór opcji motywu**
        *   **GIVEN** Ekran ustawień aplikacji.
        *   **WHEN** Użytkownik klika opcję "Motyw".
        *   **THEN** System wyświetla trzy opcje do wyboru: "Jasny", "Ciemny", "Zgodnie z systemem" (automatyczne dopasowanie do motywu systemu operacyjnego).
    *   **Scenariusz 2: Płynna zmiana bez utraty danych sesyjnych**
        *   **GIVEN** Stoper jest uruchomiony i odlicza czas (np. `02:14.56`), a użytkownik ma wpisany tekst w wyszukiwarce stref.
        *   **WHEN** Użytkownik zmienia motyw z "Jasny" na "Ciemny".
        *   **THEN** Kolorystyka aplikacji zmienia się natychmiastowo i płynnie bez restartowania aplikacji.
        *   **AND** Stoper kontynuuje odliczanie bez żadnego zakłócenia, a wpisany tekst w wyszukiwarce oraz stan innych kontrolek pozostają nienaruszone.
*   **Powiązane wymagania:** NFR-01-03, NFR-02-02
*   **Priorytet MoSCoW:** **Must Have**

#### US-5.4: Trwałość danych (Persystencja lokalna)
*   **Aktor:** Użytkownik końcowy
*   **Opis:** Jako użytkownik, chcę, aby moje ustawienia, alarmy i szablony były trwale zapisywane, abym nie musiał ich konfigurować na nowo po każdym uruchomieniu aplikacji.
*   **Kryteria Akceptacji (Gherkin):**
    *   **Scenariusz 1: Zapis danych w bazie**
        *   **GIVEN** Użytkownik dokonuje zmiany konfiguracji (np. dodaje strefę czasową, tworzy alarm, zapisuje szablon minutnika).
        *   **WHEN** Akcja zapisu zostaje wywołana.
        *   **THEN** Dane są natychmiast i bezpiecznie zapisywane w lokalnej bazie danych (SQLite/Room na Androidzie lub CoreData na iOS).
    *   **Scenariusz 2: Odczyt danych przy starcie**
        *   **GIVEN** Aplikacja została całkowicie zamknięta (ubita).
        *   **WHEN** Użytkownik ponownie uruchamia aplikację.
        *   **THEN** System wczytuje wszystkie zapisane strefy, alarmy, szablony i ustawienia z bazy danych i prezentuje je w interfejsie użytkownika.
*   **Powiązane wymagania:** NFR-02-03
*   **Priorytet MoSCoW:** **Must Have**

---

## 6. Reguły Biznesowe (Business Rules)

| ID Reguły | Nazwa Reguły | Opis i Ograniczenia |
| :--- | :--- | :--- |
| **BR-01** | Limit Stref Czasowych | Użytkownik może mieć maksymalnie 10 aktywnych stref czasowych na liście "Moje Strefy". Próba dodania 11. strefy musi zostać zablokowana na poziomie UI. |
| **BR-02** | Limit Aktywnych Minutników | Maksymalna liczba jednocześnie działających minutników wynosi 5. Przycisk dodawania nowego minutnika staje się nieaktywny po osiągnięciu tego limitu. |
| **BR-03** | Dokładność Stopera | Stoper musi mierzyć czas z dokładnością do 10 milisekund (0.01 sekundy). Wyświetlacz musi odświeżać się z częstotliwością zapewniającą płynność wizualną (min. 60 FPS). |
| **BR-04** | Priorytet Alarmów w Tle | Wyzwolenie alarmu ma najwyższy priorytet systemowy. Żadne mechanizmy oszczędzania energii (Doze Mode, Battery Saver) nie mogą opóźnić ani zablokować wyzwolenia alarmu. |
| **BR-05** | Standard Czasu dla Procesów | Wszystkie obliczenia czasu trwania (minutnik, stoper, alarmy) muszą być wykonywane na podstawie bezwzględnego czasu Unix Epoch (milisekundy), a nie lokalnego czasu wyświetlania urządzenia, aby zapobiec błędom DST. |
| **BR-06** | Zachowanie Stanu przy Rotacji | Obrót ekranu (zmiana orientacji pion/poziom) lub zmiana języka systemu nie może powodować restartu aktywności skutkującego utratą stanu stopera, minutników czy wprowadzonych danych. |

---

## 7. Obsługa Przypadków Brzegowych i Wyjątków (Edge Cases)

### EC-01: Zmiana czasu (DST) podczas aktywnego odliczania lub alarmu
*   **Problem:** Cofnięcie zegara o godzinę (przejście na czas zimowy) lub przesunięcie do przodu (czas letni) w trakcie działania minutnika lub tuż przed alarmem.
*   **Rozwiązanie:** System operuje na bezwzględnych znacznikach czasu Unix Epoch (UTC milisekundy). 
    *   *Minutnik:* Jeśli ustawiono minutnik na 10 minut o godzinie 01:55 w noc zmiany czasu (cofnięcie z 02:00 na 01:00), minutnik zakończy odliczanie dokładnie po 600 sekundach fizycznych, ignorując fakt, że czas systemowy cofnął się o godzinę.
    *   *Alarm:* Alarm zaplanowany na godzinę 02:30 zostanie wyzwolony dokładnie raz, na podstawie fizycznego upływu czasu przeliczonego w UTC, bez ryzyka podwójnego dzwonienia lub pominięcia.

### EC-02: Restart urządzenia (Crash / Rozładowanie baterii)
*   **Problem:** Telefon wyłącza się z powodu rozładowania baterii lub następuje crash systemu podczas działania stopera lub gdy ustawione są alarmy.
*   **Rozwiązanie:**
    *   *Alarmy:* Aplikacja rejestruje odbiornik systemowy `BOOT_COMPLETED` (Android) / odpowiednik iOS. Po włączeniu telefonu system automatycznie uruchamia proces w tle, który odczytuje aktywne alarmy z bazy danych SQLite/CoreData i rejestruje je ponownie w systemowym harmonogramie.
    *   *Stoper:* Stan stopera (running/paused) oraz czas rozpoczęcia (start timestamp) są zapisywane w bazie danych przy każdej zmianie stanu. Po restarcie aplikacja oblicza aktualny czas stopera: `Aktualny_Czas_NTP - Start_Timestamp`. Jeśli brak połączenia z serwerem NTP, system używa bezpiecznego zegara systemowego (uptime), aby zapobiec manipulacjom czasem przez użytkownika.

### EC-03: Konflikt dźwięków (Aktywne połączenie telefoniczne)
*   **Problem:** Alarm wyzwala się w trakcie trwania aktywnej rozmowy telefonicznej użytkownika. Odtworzenie głośnego dźwięku mogłoby uszkodzić słuch użytkownika lub zakłócić ważną rozmowę.
*   **Rozwiązanie:** System przed wyzwoleniem dźwięku sprawdza stan menedżera audio (Audio Manager / Call State). Jeśli wykryte zostanie aktywne połączenie:
    1. Głośnik zewnętrzny zostaje wyciszony.
    2. W słuchawce (lub kanale słuchawek Bluetooth) odtwarzany jest łagodny, powtarzalny sygnał dźwiękowy (beeping) o niskiej głośności.
    3. Urządzenie uruchamia intensywne wibracje w celu fizycznego powiadomienia użytkownika.
    4. Na ekranie wyświetla się pełnoekranowy monit alarmu umożliwiający jego wyłączenie lub drzemkę.

---

## 8. Wymagania Niefunkcjonalne (NFR) jako Kryteria Techniczno-Biznesowe

### NFR-01: Wygląd i Interfejs Użytkownika (UI/UX)
*   **NFR-01-01 (Dark Mode - Pure Black):** Tryb ciemny musi implementować schemat kolorów oparty o czystą czerń (HEX `#000000`) dla warstwy tła, dedykowany dla ekranów typu AMOLED/OLED w celu maksymalnego oszczędzania energii. Wszystkie inne elementy (karty, przyciski) powinny używać bardzo ciemnych szarości (np. `#121212`), aby zachować głębię czerni tła.
*   **NFR-01-02 (Light Mode):** Tryb jasny musi bazować na odcieniach złamanej bieli i jasnej szarości (tło: `#F8F9FA` do `#EDF2F7`), zapewniając współczynnik kontrastu tekstu do tła na poziomie minimum 4.5:1 (zgodnie z wytycznymi WCAG 2.1 AA).
*   **NFR-01-03 (Przełącznik trybów):** Aplikacja musi oferować łatwo dostępny przełącznik motywu w ustawieniach z trzema opcjami: "Jasny", "Ciemny", "Zgodnie z systemem". Zmiana motywu musi odbywać się płynnie, bez konieczności restartowania aplikacji i bez utraty danych sesyjnych (np. stanu stopera).

### NFR-02: Architektura i Wydajność Techniczna
*   **NFR-02-01 (Niezawodność w tle):** Wyzwalanie alarmów oraz zakończenie odliczania minutnika musi działać ze stuprocentową skutecznością, gdy urządzenie jest zablokowane, znajduje się w trybie głębokiego uśpienia (Doze Mode) lub gdy aplikacja została ubita przez system w celu zwolnienia pamięci RAM. Wymagane jest użycie natywnych mechanizmów systemowych o najwyższym priorytecie (np. Exact Alarms API na Androidzie / UNNotificationRequest na iOS).
*   **NFR-02-02 (Architektura stanowa):** Logika biznesowa czasu (odliczanie, stan wątków) musi być całkowicie odseparowana od warstwy widoku (MVVM / Clean Architecture). Obrót ekranu lub zmiana konfiguracji językowej nie może powodować zakłóceń w działaniu liczników.
*   **NFR-02-03 (Persystencja):** Wszystkie dane konfiguracyjne (zapisane strefy, zdefiniowane alarmy, presety minutnika) muszą być trwale zapisywane w lokalnej, bezpiecznej bazie danych (np. SQLite/Room lub CoreData).

---

## 9. Matryca Śledzenia Wymagań (Traceability Matrix)

Poniższa tabela mapuje wymagania ze specyfikacji pierwotnej (`task.md`) na konkretne User Stories zdefiniowane w niniejszym dokumencie BRD, zapewniając 100% pokrycia wymagań.

| ID Wymagania (task.md) | Nazwa Wymagania | Powiązane User Story (BRD) | Status Pokrycia |
| :--- | :--- | :--- | :--- |
| **FR-01-01** | Autodetekcja lokalnej strefy | **US-1.1** (Automatyczne wykrywanie lokalnej strefy) | **100% Pokryte** |
| **FR-01-02** | Obsługa zmian czasu (DST) | **US-1.2** (Automatyczna obsługa zmian czasu) | **100% Pokryte** |
| **FR-01-03** | Wyszukiwanie stref czasowych | **US-1.3** (Wyszukiwanie stref czasowych z autouzupełnianiem) | **100% Pokryte** |
| **FR-01-04** | Śledzenie wielu stref (max 10) | **US-1.4** (Zarządzanie listą "Moje Strefy" i limit 10 stref) | **100% Pokryte** |
| **FR-02-01** | Dokładność stopera (0.01s) | **US-2.1** (Podstawowy pomiar czasu z wysoką dokładnością) | **100% Pokryte** |
| **FR-02-02** | Funkcja Międzyczasów (Laps) | **US-2.2** (Rejestrowanie międzyczasów bez zatrzymywania) | **100% Pokryte** |
| **FR-02-03** | Analityka okrążeń (Ekstrema) | **US-2.3** (Automatyczna analityka i wizualizacja okrążeń) | **100% Pokryte** |
| **FR-02-04** | Ciągłość stanu stopera | **US-2.4** (Ciągłość pomiaru stopera) | **100% Pokryte** |
| **FR-03-01** | Obsługa do 5 minutników z etykietami | **US-3.1** (Obsługa do 5 niezależnych minutników z etykietami) | **100% Pokryte** |
| **FR-03-02** | Presety minutnika (Szybki wybór) | **US-3.2** (Zarządzanie szablonami czasowymi) | **100% Pokryte** |
| **FR-03-03** | Kontrola minutników (Start/Pauza/Reset/Usuń) | **US-3.1** (Obsługa do 5 niezależnych minutników z etykietami) | **100% Pokryte** |
| **FR-04-01** | Harmonogram powtarzalności alarmów | **US-4.1** (Harmonogram i powtarzalność alarmów) | **100% Pokryte** |
| **FR-04-02** | Mechanizm Drzemki (Snooze) | **US-4.2** (Mechanizm drzemki z limitem powtórzeń) | **100% Pokryte** |
| **FR-04-03** | Gradacja dźwięku (Fade-in) | **US-4.3** (Gradacja głośności dźwięku) | **100% Pokryte** |
| **FR-04-04** | Tryb dyskretny (Tylko wibracje) | **US-4.4** (Tryb dyskretny i inteligentna obsługa konfliktów) | **100% Pokryte** |
| **NFR-01-01** | AMOLED Czysta Czerń (#000000) | **US-5.1** (Tryb Ciemny) | **100% Pokryte** |
| **NFR-01-02** | Light Mode (#F8F9FA do #EDF2F7) | **US-5.2** (Tryb Jasny) | **100% Pokryte** |
| **NFR-01-03** | Przełącznik motywów (Jasny/Ciemny/System) | **US-5.3** (Przełącznik motywów i zachowanie stanu sesji) | **100% Pokryte** |
| **NFR-02-01** | Niezawodność w tle (Doze Mode/Ubitą aplikacja) | **US-3.3** (Niezawodne powiadomienia minutnika), **US-4.5** (Niezawodność alarmów) | **100% Pokryte** |
| **NFR-02-02** | Architektura stanowa (MVVM/Clean) | **US-5.3** (Przełącznik motywów i zachowanie stanu sesji) | **100% Pokryte** |
| **NFR-02-03** | Persystencja (SQLite/Room/CoreData) | **US-5.4** (Trwałość danych) | **100% Pokryte** |
| **Edge Case 1** | Zmiana czasu (DST) podczas odliczania | **US-1.2** (Automatyczna obsługa zmian czasu), **US-3.3** | **100% Pokryte** |
| **Edge Case 2** | Restart urządzenia (Crash/Bateria) | **US-2.4** (Ciągłość pomiaru stopera), **US-4.5** (Niezawodność alarmów) | **100% Pokryte** |
| **Edge Case 3** | Konflikt dźwięków (Połączenie telefoniczne) | **US-4.4** (Tryb dyskretny i inteligentna obsługa konfliktów) | **100% Pokryte** |

---
*Dokument zatwierdzony do wdrożenia przez Starszego Analityka Biznesowego.*
