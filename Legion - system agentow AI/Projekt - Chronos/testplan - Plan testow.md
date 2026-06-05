# PLAN I SPECYFIKACJA TESTÓW (TEST PLAN & SPECIFICATION)
## Projekt: ChronosApp — Nowoczesna Aplikacja Zegara i Alertyzacji
**Wersja:** 1.0  
**Status:** Gotowy do weryfikacji  
**Data:** 31 maja 2026 r.  
**Autor:** Starszy Inżynier QA / QA Lead (Senior Quality Assurance Engineer)  
**Dla zespołu:** Product Manager, Architekt Systemowy, Zespół Deweloperski, QA  

---

## Spis Treści
1. [Wprowadzenie i Cel Dokumentu](#1-wprowadzenie-i-cel-dokumentu)
2. [Strategia i Metodologia Testów](#2-strategia-i-metodologia-testów)
3. [Środowisko Testowe i Narzędzia](#3-środowisko-testowe-i-narzędzia)
4. [Kryteria Wejścia i Wyjścia](#4-kryteria-wejścia-i-wyjścia)
5. [Szczegółowe Przypadki Testowe (Funkcjonalne)](#5-szczegółowe-przypadki-testowe-funkcjonalne)
   - [5.1. Zarządzanie Czasem Światowym (World Clock)](#51-zarządzanie-czasem-światowym-world-clock)
   - [5.2. Precyzyjny Stoper z Analityką (Stopwatch)](#52-precyzyjny-stoper-z-analityką-stopwatch)
   - [5.3. Wielowątkowy Minutnik (Timer)](#53-wielowątkowy-minutnik-timer)
   - [5.4. Inteligentny System Alarmów (Alarms)](#54-inteligentny-system-alarmów-alarms)
   - [5.5. Personalizacja i Ustawienia (Settings & UI/UX)](#55-personalizacja-i-ustawienia-settings--uiux)
6. [Testy Niefunkcjonalne (NFR)](#6-testy-niefunkcjonalne-nfr)
   - [6.1. AMOLED Black & Light Mode](#61-amoled-black--light-mode)
   - [6.2. Responsywność i Ergonomia Dotykowa](#62-responsywność-i-ergonomia-dotykowa)
   - [6.3. Dostępność (A11Y) i Zgodność z WCAG 2.1 AA](#63-dostępność-a11y-i-zgodność-z-wcag-21-aa)
   - [6.4. Wydajność Asynchroniczna i Brak Drgań Układu](#64-wydajność-asynchroniczna-i-brak-drgań-układu)
7. [Testy Przypadków Brzegowych i Destrukcyjne (Edge Cases)](#7-testy-przypadków-brzegowych-i-destrukcyjne-edge-cases)
   - [7.1. Przejścia Czasu Letniego/Zimowego (DST)](#71-przejścia-czasu-letniegozimowego-dst)
   - [7.2. Restart Urządzenia, Crash i Rozładowanie Baterii](#72-restart-urządzenia-crash-i-rozładowanie-baterii)
   - [7.3. Konflikt Audio i Aktywne Połączenie Telefoniczne](#73-konflikt-audio-i-aktywne-połączenie-telefoniczne)
   - [7.4. Ograniczenia Tła Przeglądarki (Tab Suspension / Doze Mode)](#74-ograniczenia-tła-przeglądarki-tab-suspension--doze-mode)
8. [Matryca Pokrycia Testowego (Traceability Matrix)](#8-matryca-pokrycia-testowego-traceability-matrix)

---

## 1. Wprowadzenie i Cel Dokumentu

Niniejszy dokument stanowi kompleksowy **Plan i Specyfikację Testów** dla aplikacji **ChronosApp** — nowoczesnej, minimalistycznej, jednostronicowej aplikacji (SPA) typu Local-First, służącej do zarządzania czasem i alertyzacji.

Celem dokumentu jest zdefiniowanie strategii testowej, środowiska, narzędzi oraz szczegółowych scenariuszy i przypadków testowych (zarówno funkcjonalnych, jak i niefunkcjonalnych), które pozwolą zweryfikować zgodność implementacji z wymaganiami biznesowymi (BRD), systemowymi (SDD) oraz specyfikacją interfejsu użytkownika (UI Spec).

Głównym priorytetem QA jest zapewnienie **stuprocentowej niezawodności wyzwalania alarmów i minutników w tle** oraz bezkompromisowej stabilności i precyzji działania aplikacji w warunkach skrajnych (zmiany czasu DST, restarty, uśpienie przeglądarki, konflikty audio).

---

## 2. Strategia i Metodologia Testów

W celu zapewnienia najwyższej jakości oprogramowania zastosowane zostanie podejście wielopoziomowe:

1. **Testowanie Statyczne (Static Testing):** Ciągła weryfikacja spójności wymagań (BRD, SDD, UI Spec) pod kątem logicznym i testowalności przed rozpoczęciem właściwej fazy testów dynamicznych.
2. **Testy Funkcjonalne (Functional Testing):**
   - **Testy Systemowe (System Testing):** Weryfikacja pełnych przepływów użytkownika (User Flows) w interfejsie graficznym.
   - **Testy Integracyjne (Integration Testing):** Weryfikacja poprawnej komunikacji między modułami JS (`db.js`, `state.js`, `clock.js`, `stopwatch.js`, `timer.js`, `alarm.js`), a także integracji z IndexedDB (Dexie.js), Web Workerami i Service Workerem.
3. **Testy Niefunkcjonalne (Non-Functional Testing):**
   - **Testy UI/UX i Wizualne:** Weryfikacja zgodności z tokenami wizualnymi, renderowania motywu AMOLED Black (`#000000`) i Light Mode, a także braku drgań układu (Layout Jitter).
   - **Testy Dostępności (A11Y):** Weryfikacja zgodności z wytycznymi WCAG 2.1 AA (kontrast, nawigacja klawiaturą, atrybuty ARIA, czytniki ekranu).
   - **Testy Responsywności i Ergonomii:** Testowanie na rzeczywistych urządzeniach mobilnych i emulatorach pod kątem obszarów dotykowych (Touch Targets min. 48x48px).
4. **Testowanie Przypadków Brzegowych i Destrukcyjne (Edge & Destructive Testing):**
   - Symulowanie nagłych awarii (crash aplikacji, restart systemu, rozładowanie baterii).
   - Symulowanie przejść DST (Daylight Saving Time).
   - Testowanie zachowania w tle (Doze Mode, dławienie wątków przez przeglądarkę).
   - Symulowanie konfliktów zasobów (aktywne połączenie telefoniczne, blokada Autoplay).

---

## 3. Środowisko Testowe i Narzędzia

### 3.1. Środowisko Testowe (Hardware & Software)
Testy zostaną przeprowadzone na zróżnicowanych platformach sprzętowych i systemowych, aby zapewnić pełną kompatybilność:

| Platforma | System Operacyjny | Przeglądarki | Uwagi |
| :--- | :--- | :--- | :--- |
| **Desktop PC** | Windows 11 / macOS Sonoma | Google Chrome (LTS), Mozilla Firefox, Safari, MS Edge | Testy wieloprzeglądarkowe, A11Y, klawiatura |
| **Smartphone (OLED)** | Android 14 (Samsung/Pixel) | Chrome Mobile, Samsung Internet | Testy AMOLED Black, wibracje, Doze Mode |
| **iPhone (OLED)** | iOS 17 | Safari Mobile | Testy Service Worker, AudioContext, iOS background |
| **Tablet** | iPadOS 17 / Android Tablet | Safari, Chrome | Testy responsywności (układ wielokolumnowy) |

### 3.2. Narzędzia Testowe (Testing Tools)
*   **Chrome DevTools:** Do debugowania stanu IndexedDB (Application -> IndexedDB), symulowania lokalizacji, manipulowania czasem systemowym, dławienia procesora (CPU throttling) oraz testowania responsywności.
*   **Lighthouse / Axe DevTools:** Do automatycznej weryfikacji dostępności (A11Y) i zgodności z WCAG 2.1 AA.
*   **Screen Readers (NVDA / VoiceOver):** Do testowania czytników ekranu i atrybutów `aria-live`.
*   **NTP Time Simulator / System Clock Manipulation:** Do testowania przejść DST i restartów urządzenia poprzez ręczną zmianę czasu systemowego w systemie operacyjnym hosta.
*   **Web Audio API Debugger:** Do monitorowania stanu `AudioContext` i poziomów głośności `GainNode`.

---

## 4. Kryteria Wejścia i Wyjścia

### 4.1. Kryteria Wejścia do Fazy Testów (Entry Criteria)
1. Zakończenie fazy implementacji kodu i pomyślne zbudowanie aplikacji (brak błędów kompilacji/transpilacji).
2. Dostarczenie stabilnej wersji uruchomieniowej (Single Page Application) na środowisko testowe (staging/test).
3. Pomyślne przejście testów dymnych (Smoke Tests) — aplikacja uruchamia się, baza danych IndexedDB inicjalizuje się bez błędów.
4. Zamknięcie i zatwierdzenie dokumentacji wymagań (BRD, SDD, UI Spec).

### 4.2. Kryteria Wyjścia z Fazy Testów (Exit Criteria)
1. Wykonanie 100% zaplanowanych przypadków testowych z niniejszego planu.
2. **Zero otwartych błędów o priorytecie Krytycznym (Blocker/Critical)** — w szczególności dotyczących niezawodności alarmów, utraty danych w IndexedDB, błędów obliczeń DST oraz awarii aplikacji.
3. **Zero otwartych błędów o priorytecie Wysokim (Major)** — w tym błędów renderowania AMOLED Black, niedostępności klawiatury (A11Y), braku responsywności.
4. Maksymalnie 3 otwarte błędy o priorytecie Niskim (Minor/Trivial), posiadające zatwierdzone obejście (workaround) lub zaplanowane do poprawy w kolejnym sprincie.
5. Osiągnięcie 100% pokrycia wymagań biznesowych i technicznych (Traceability Matrix).
6. Raport z testów podpisany i zatwierdzony przez QA Lead.

---

## 5. Szczegółowe Przypadki Testowe (Funkcjonalne)

### 5.1. Zarządzanie Czasem Światowym (World Clock)

#### TC-WC-01: Automatyczne wykrywanie lokalnej strefy czasowej (Pierwsze uruchomienie)
*   **Warunki wstępne:** Baza danych `ChronosDB` jest pusta (czysta instalacja/wyczyszczone dane przeglądarki). System operacyjny ma ustawioną strefę czasową `Europe/Warsaw`.
*   **Kroki:**
    1. Uruchom aplikację ChronosApp.
    2. Zweryfikuj sekcję "Lokalny Czas" na górze ekranu.
*   **Oczekiwany rezultat:** System automatycznie wykrywa strefę czasową urządzenia. W sekcji "Lokalny Czas" wyświetla się: "Warszawa, Polska (CET)" (lub odpowiednik IANA `Europe/Warsaw`), aktualna godzina, sekundy oraz data zgodna z czasem systemowym.

#### TC-WC-02: Fallback wykrywania strefy przy braku uprawnień
*   **Warunki wstępne:** Uprawnienia do geolokalizacji w przeglądarce są zablokowane. System operacyjny ma ustawioną strefę `Europe/Warsaw`.
*   **Kroki:**
    1. Uruchom aplikację.
    2. Zaobserwuj zachowanie modułu czasu.
*   **Oczekiwany rezultat:** Aplikacja nie zgłasza błędu. Pobiera strefę czasową bezpośrednio z ustawień regionalnych przeglądarki (`Intl.DateTimeFormat().resolvedOptions().timeZone`) i poprawnie ustawia `Europe/Warsaw` jako strefę główną.

#### TC-WC-03: Wyszukiwanie stref czasowych z autouzupełnianiem
*   **Warunki wstępne:** Użytkownik znajduje się na ekranie "Czas Światowy".
*   **Kroki:**
    1. Kliknij przycisk "[ + Dodaj nową strefę ]".
    2. W polu wyszukiwania modala wpisz tekst "Tok".
    3. Zweryfikuj listę wyników.
    4. Kliknij przycisk czyszczenia `[x]` w polu wyszukiwania.
    5. Wpisz skrót strefy "EST".
*   **Oczekiwany rezultat:** 
    - Po wpisaniu "Tok" lista filtruje się w czasie rzeczywistym, wyświetlając pozycję `Asia/Tokyo (Tokio, Japonia)`.
    - Kliknięcie `[x]` natychmiast czyści pole i przywraca pełną listę stref.
    - Po wpisaniu "EST" system poprawnie mapuje skrót i wyświetla strefy powiązane z Eastern Standard Time.

#### TC-WC-04: Zarządzanie listą "Moje Strefy" i limit 10 stref (BR-01)
*   **Warunki wstępne:** Na liście "Moje Strefy" znajduje się 9 stref czasowych.
*   **Kroki:**
    1. Kliknij "[ + Dodaj nową strefę ]", wyszukaj i dodaj dziesiątą strefę (np. `Asia/Tokyo`).
    2. Zweryfikuj stan przycisku "[ + Dodaj nową strefę ]" na ekranie głównym.
    3. Spróbuj wywołać modal dodawania strefy (np. poprzez konsolę lub skrót, jeśli to możliwe).
    4. Usuń jedną strefę z listy za pomocą gestu swipe lub ikony kosza.
    5. Zweryfikuj ponownie stan przycisku dodawania.
*   **Oczekiwany rezultat:**
    - Po dodaniu 10. strefy, przycisk "[ + Dodaj nową strefę ]" staje się nieaktywny (szary, zablokowany, `pointer-events: none`, `opacity: 0.5`). Wyświetla się komunikat: "Osiągnięto maksymalny limit 10 stref czasowych...".
    - Po usunięciu strefy, liczba stref spada do 9, przycisk dodawania natychmiast staje się ponownie aktywny. Zmiany są trwale zapisane w IndexedDB (tabela `zones`).

---

### 5.2. Precyzyjny Stoper z Analityką (Stopwatch)

#### TC-SW-01: Podstawowy pomiar czasu, pauza i reset (BR-03)
*   **Warunki wstępne:** Stoper jest w stanie zresetowanym (`00:00.00`).
*   **Kroki:**
    1. Kliknij przycisk "Start" (zielony).
    2. Odczekaj około 5 sekund i zaobserwuj płynność odliczania.
    3. Kliknij przycisk "Pauza" (czerwony).
    4. Kliknij przycisk "Wznów" (zielony), odczekaj 2 sekundy i kliknij "Pauza".
    5. Kliknij przycisk "Reset" (szary).
*   **Oczekiwany rezultat:**
    - Po kliknięciu "Start" stoper rusza natychmiast. Czas wyświetla się z dokładnością do setnych części sekundy (`MM:SS.hh`). Odświeżanie jest płynne (min. 60 FPS, brak migotania).
    - "Pauza" zatrzymuje odliczanie na dokładnej wartości (np. `00:05.23`).
    - "Wznów" kontynuuje odliczanie bez opóźnień i bez zerowania.
    - "Reset" zeruje licznik do `00:00.00` i usuwa wszelkie międzyczasy z widoku oraz z bazy danych `stopwatch_laps`.

#### TC-SW-02: Rejestrowanie międzyczasów (Laps) i dynamiczna analityka (US-2.2, US-2.3)
*   **Warunki wstępne:** Stoper jest zresetowany.
*   **Kroki:**
    1. Kliknij "Start".
    2. Po 3 sekundach kliknij "Okrążenie" (Lap).
    3. Po kolejnych 5 sekundach kliknij "Okrążenie".
    4. Po kolejnych 2 sekundach kliknij "Okrążenie".
    5. Zweryfikuj listę okrążeń poniżej stopera.
*   **Oczekiwany rezultat:**
    - Każde kliknięcie "Okrążenie" dodaje nowy wiersz na górę listy. Główny licznik działa nieprzerwanie bez żadnego mikro-zamrożenia.
    - Na liście znajdują się 3 okrążenia. System automatycznie analizuje czasy:
      - Okrążenie o najkrótszym czasie (np. Okrążenie 3 - 2.00s) zostaje wyróżnione kolorem jasnozielonym (`#2ECC71` / `#198754`).
      - Okrążenie o najdłuższym czasie (np. Okrążenie 2 - 5.00s) zostaje wyróżnione kolorem jasnoczerwonym (`#E74C3C` / `#DC3545`).
      - Okrążenie 1 (3.00s) pozostaje w kolorze standardowym.

#### TC-SW-03: Ciągłość pomiaru stopera po zamknięciu karty (Persistence)
*   **Warunki wstępne:** Stoper jest uruchomiony i odlicza czas (np. wystartował o 12:00:00).
*   **Kroki:**
    1. Zamknij kartę z aplikacją lub całkowicie zamknij przeglądarkę.
    2. Odczekaj dokładnie 30 sekund (mierzone na zewnętrznym zegarze).
    3. Uruchom ponownie przeglądarkę i otwórz ChronosApp.
    4. Przejdź do zakładki "Stoper".
*   **Oczekiwany rezultat:** Stoper jest w stanie "Running" (nadal działa). Wyświetlany czas uwzględnia fizyczny upływ czasu, kiedy aplikacja była zamknięta (czas jest obliczany asynchronicznie jako `Aktualny_Czas - start_epoch + elapsed_ms` z IndexedDB). Brak jakichkolwiek strat sekundowych.

---

### 5.3. Wielowątkowy Minutnik (Timer)

#### TC-TM-01: Uruchomienie wielu minutników z etykietami i limit 5 wątków (BR-02)
*   **Warunki wstępne:** Brak aktywnych minutników na liście.
*   **Kroki:**
    1. Skonfiguruj minutnik na 5 minut, wpisz etykietę "Makaron" i kliknij "Uruchom minutnik".
    2. Skonfiguruj drugi minutnik na 10 minut, wpisz etykietę "Sos" i kliknij "Uruchom minutnik".
    3. Dodaj kolejne 3 minutniki (razem 5 aktywnych).
    4. Zaobserwuj stan formularza konfiguracji oraz przycisków presetów.
    5. Spróbuj dodać szósty minutnik.
*   **Oczekiwany rezultat:**
    - Wszystkie 5 minutników działa niezależnie na liście. Każdy ma własny pasek postępu, etykietę i niezależne odliczanie wstecz.
    - Po osiągnięciu 5 aktywnych minutników, przycisk "Uruchom minutnik" oraz wszystkie przyciski presetów stają się nieaktywne (disabled, szare). Wyświetla się komunikat: "Możesz uruchomić maksymalnie 5 minutników jednocześnie."

#### TC-TM-02: Niezależna kontrola i usuwanie minutników
*   **Warunki wstępne:** Działają 3 minutniki: "Makaron" (running), "Sos" (running), "Warzywa" (running).
*   **Kroki:**
    1. Kliknij przycisk "Pauza" przy minutniku "Sos".
    2. Kliknij przycisk "Usuń" przy minutniku "Warzywa".
    3. Zaobserwuj stan pozostałych minutników.
*   **Oczekiwany rezultat:**
    - Minutnik "Sos" zostaje zapauzowany (pasek postępu staje się szary, odliczanie zatrzymuje się).
    - Minutnik "Warzywa" zostaje natychmiast usunięty z listy i z bazy danych IndexedDB.
    - Minutnik "Makaron" kontynuuje odliczanie bez żadnych zakłóceń czy zmian stanu.

#### TC-TM-03: Zarządzanie szablonami czasowymi (Presets)
*   **Warunki wstępne:** Użytkownik jest na ekranie "Minutnik". Sekcja "Szybki wybór" zawiera domyślne presety.
*   **Kroki:**
    1. Skonfiguruj czas na 45 minut, wpisz etykietę "Nauka" i kliknij "Zapisz jako szablon" (lub odpowiedni przycisk zapisu presetu).
    2. Zweryfikuj sekcję "Szybki wybór".
    3. Kliknij nowo utworzony preset "Nauka (45 min)".
    4. Usuń zapisany preset za pomocą ikony usuwania.
*   **Oczekiwany rezultat:**
    - Nowy preset "Nauka (45 min)" pojawia się w sekcji "Szybki wybór".
    - Kliknięcie presetu natychmiast tworzy i uruchamia aktywny minutnik z czasem 45 minut i etykietą "Nauka".
    - Usunięcie presetu trwale kasuje go z bazy danych `timer_presets` i usuwa z widoku UI.

---

### 5.4. Inteligentny System Alarmów (Alarms)

#### TC-AL-01: Konfiguracja alarmu cyklicznego i jednorazowego (US-4.1)
*   **Warunki wstępne:** Brak ustawionych alarmów.
*   **Kroki:**
    1. Kliknij "[ + Dodaj nowy alarm ]".
    2. Ustaw godzinę na 07:00, wpisz etykietę "Budzik Praca", zaznacz dni: Poniedziałek, Środa, Piątek. Kliknij "Zapisz".
    3. Utwórz drugi alarm na godzinę 08:00, etykieta "Lekarz", nie zaznaczaj żadnego dnia tygodnia (alarm jednorazowy). Kliknij "Zapisz".
    4. Zweryfikuj listę alarmów.
*   **Oczekiwany rezultat:**
    - Alarm "Budzik Praca" (07:00) jest aktywny (Switch ON). Wyświetla wyróżnione dni: `[Pn] [Śr] [Pt]`. W bazie danych `next_trigger_epoch` wskazuje na najbliższy nadchodzący dzień z tej grupy.
    - Alarm "Lekarz" (08:00) jest aktywny (Switch ON), oznaczony jako jednorazowy (brak powtarzania).

#### TC-AL-02: Mechanizm drzemki (Snooze) i limit powtórzeń (US-4.2)
*   **Warunki wstępne:** Alarm "Test Drzemki" jest skonfigurowany na bieżącą godzinę + 1 minuta, z włączoną drzemką (czas: 1 minuta, limit: 2 powtórzenia).
*   **Kroki:**
    1. Odczekaj na wyzwolenie alarmu.
    2. Po wyzwoleniu (ekran alarmu), kliknij przycisk "Drzemka" (Snooze).
    3. Odczekaj 1 minutę na ponowne wyzwolenie. Kliknij "Drzemka" po raz drugi.
    4. Odczekaj 1 minutę na trzecie wyzwolenie. Zaobserwuj dostępność przycisków na ekranie alarmu.
*   **Oczekiwany rezultat:**
    - Po pierwszym i drugim kliknięciu "Drzemka", alarm wycisza się, a w bazie danych `snooze_count` zwiększa się o 1. Alarm wyzwala się ponownie dokładnie po 1 minucie.
    - Przy trzecim wyzwoleniu (osiągnięto limit 2 drzemek), przycisk "Drzemka" jest niewidoczny lub zablokowany. Jedyną dostępną opcją jest "Wyłącz" (Dismiss).

#### TC-AL-03: Gradacja głośności dźwięku (Fade-in) (US-4.3)
*   **Warunki wstępne:** Alarm ma włączoną opcję "Fade-in" (stopniowe pogłaśnianie) i profil dźwiękowy "Standardowy".
*   **Kroki:**
    1. Wyzwól alarm.
    2. Przez pierwsze 15 sekund nasłuchuj głośności odtwarzanego dźwięku.
    3. W 7. sekundzie dotknij ekranu urządzenia lub kliknij przycisk drzemki.
*   **Oczekiwany rezultat:**
    - Dźwięk alarmu rozpoczyna się na bardzo cichym poziomie (dokładnie 10% głośności maksymalnej).
    - Głośność rośnie liniowo co sekundę, osiągając pełną moc (100%) dokładnie w 15. sekundzie.
    - Dotknięcie ekranu w 7. sekundzie natychmiast zatrzymuje proces gradacji (głośność nie rośnie dalej, alarm reaguje na akcję użytkownika).

---

### 5.5. Personalizacja i Ustawienia (Settings & UI/UX)

#### TC-SET-01: Przełącznik motywów i zachowanie stanu sesji (US-5.3)
*   **Warunki wstępne:** Stoper jest uruchomiony i odlicza czas (np. `01:15.40`). W wyszukiwarce stref czasowych wpisany jest tekst "New".
*   **Kroki:**
    1. Przejdź do zakładki "Ustawienia".
    2. W opcji "Motyw aplikacji" zmień wartość z "Jasny" na "Ciemny".
    3. Przejdź natychmiast do zakładki "Stoper" i zweryfikuj stan licznika.
    4. Przejdź do zakładki "Czas Światowy", otwórz modal dodawania strefy i zweryfikuj pole wyszukiwania.
*   **Oczekiwany rezultat:**
    - Kolorystyka aplikacji zmienia się natychmiastowo i płynnie na motyw ciemny (AMOLED Black).
    - Stoper nadal działa nieprzerwanie, pokazując poprawny, ciągły czas (np. `01:25.12`), bez resetu czy zatrzymania.
    - Wpisany tekst "New" w wyszukiwarce stref oraz stan wszystkich innych kontrolek w aplikacji są w pełni zachowane (brak przeładowania strony SPA).

#### TC-SET-02: Trwałość danych po twardym przeładowaniu (Persystencja)
*   **Warunki wstępne:** Użytkownik dodał 3 strefy czasowe, skonfigurował 2 alarmy oraz zapisał 1 preset minutnika.
*   **Kroki:**
    1. Wykonaj twarde przeładowanie strony w przeglądarce (Ctrl+F5 lub Cmd+Shift+R).
    2. Po ponownym załadowaniu aplikacji zweryfikuj zawartość wszystkich zakładek.
*   **Oczekiwany rezultat:** Wszystkie dane (strefy, alarmy, presety) są poprawnie wczytywane z IndexedDB i wyświetlane w UI. Stan aplikacji jest identyczny jak przed przeładowaniem.

---

## 6. Testy Niefunkcjonalne (NFR)

### 6.1. AMOLED Black & Light Mode

#### TC-NFR-01: Weryfikacja kolorystyki AMOLED Black (NFR-01-01)
*   **Warunki wstępne:** Włączony motyw ciemny (Dark Mode).
*   **Kroki:**
    1. Otwórz aplikację na urządzeniu z ekranem OLED/AMOLED.
    2. Za pomocą narzędzi deweloperskich (Chrome DevTools -> Elements -> Styles) zweryfikuj kolory tła.
*   **Oczekiwany rezultat:**
    - Główny kolor tła (`background-color` dla `<body>` lub głównego kontenera) wynosi dokładnie HEX `#000000` (czysta czerń).
    - Tła kart, paneli i modali używają bardzo ciemnej szarości (HEX `#121212`), zapewniając głębię i kontrast.
    - Współczynnik kontrastu tekstu głównego (`#FFFFFF`) do tła (`#000000`) wynosi 21:1 (spełnia normę WCAG AAA).

#### TC-NFR-02: Weryfikacja kolorystyki Light Mode (NFR-01-02)
*   **Warunki wstępne:** Włączony motyw jasny (Light Mode).
*   **Kroki:**
    1. Przełącz aplikację w tryb jasny.
    2. Zweryfikuj kolory tła i tekstu za pomocą DevTools.
*   **Oczekiwany rezultat:**
    - Główne tło aplikacji mieści się w zakresie HEX `#F8F9FA` do `#EDF2F7` (złamana biel/jasna szarość).
    - Tło kart i modali wynosi `#FFFFFF`.
    - Tekst główny ma kolor `#1A1A1A`, zapewniając kontrast powyżej 10:1 (zgodność z WCAG AA/AAA).

---

### 6.2. Responsywność i Ergonomia Dotykowa

#### TC-NFR-03: Responsywność układu (Mobile-First)
*   **Warunki wstępne:** Dostęp do narzędzi deweloperskich (Responsive Design Mode) lub różnych urządzeń.
*   **Kroki:**
    1. Zmniejsz szerokość ekranu do `<768px` (widok mobilny). Zweryfikuj układ nawigacji i kart.
    2. Zwiększ szerokość do `≥768px` (tablet).
    3. Zwiększ szerokość do `≥1200px` (desktop).
*   **Oczekiwany rezultat:**
    - **Mobile:** Nawigacja znajduje się na dole ekranu (Sticky Bottom Bar, wysokość 64px). Karty stref i alarmów zajmują pełną szerokość ekranu (1 kolumna).
    - **Tablet:** Układ zmienia się na dwukolumnowy.
    - **Desktop:** Nawigacja przenosi się na lewą stronę (Sidebar o szerokości 240px). Karty układają się w siatkę wielokolumnową (3-4 kolumny). Brak błędów nakładania się elementów (Layout Shifts).

#### TC-NFR-04: Ergonomia dotykowa i obszary klikalne (Touch Targets)
*   **Warunki wstępne:** Aplikacja uruchomiona na urządzeniu mobilnym.
*   **Kroki:**
    1. Zweryfikuj fizyczny rozmiar przycisków kontrolnych stopera (Start, Pauza, Okrążenie), minutnika oraz zakładek nawigacji.
    2. Zweryfikuj odstępy między przyciskami "Reset" i "Okrążenie" w stoperze.
*   **Oczekiwany rezultat:**
    - Wszystkie elementy interaktywne mają minimalny obszar dotykowy **`48px x 48px`** (lub są ostylowane tak, aby ich klikalna strefa miała ten wymiar).
    - Odstęp między sąsiadującymi przyciskami wynosi minimum **`8px`**, co uniemożliwia przypadkowe kliknięcie sąsiedniej kontrolki.

---

### 6.3. Dostępność (A11Y) i Zgodność z WCAG 2.1 AA

#### TC-NFR-05: Nawigacja klawiaturą i Focus Ring
*   **Warunki wstępne:** Urządzenie desktopowe, brak użycia myszy.
*   **Kroki:**
    1. Użyj klawisza `Tab` do poruszania się po całej aplikacji.
    2. Zweryfikuj widoczność wskaźnika skupienia (Focus Ring) na każdym elemencie.
    3. Użyj klawisza `Space` na przycisku "Start" stopera.
    4. Otwórz modal dodawania strefy i kliknij `Escape`.
*   **Oczekiwany rezultat:**
    - Każdy element interaktywny posiada wyraźną, kontrastową ramkę skupienia (`:focus-visible`) o szerokości min. 3px w kolorze `--color-primary`.
    - Kolejność tabulacji jest logiczna (od góry do dołu, od lewej do prawej).
    - Klawisz `Space` uruchamia/pauzuje stoper.
    - Klawisz `Escape` natychmiast zamyka modal.

#### TC-NFR-06: Atrybuty ARIA i czytniki ekranu
*   **Warunki wstępne:** Uruchomiony czytnik ekranu (np. NVDA na Windows lub VoiceOver na macOS/iOS).
*   **Kroki:**
    1. Przejdź do zakładki "Stoper" i uruchom go.
    2. Przejdź do przycisków opartych wyłącznie na ikonach (np. usuwanie strefy).
    3. Zweryfikuj odczytywane komunikaty.
*   **Oczekiwany rezultat:**
    - Wyświetlacze czasu posiadają atrybut `aria-live="polite"`, dzięki czemu czytnik nie odczytuje chaotycznie setnych części sekundy, lecz informuje o stanie na żądanie.
    - Przyciski ikonowe posiadają poprawne, tekstowe etykiety `aria-label` (np. `aria-label="Usuń strefę Londyn"`).
    - Przełączniki alarmów są odczytywane jako "Przełącznik, zaznaczone/niezaznaczone" (`role="switch"`, `aria-checked`).

---

### 6.4. Wydajność Asynchroniczna i Brak Drgań Układu

#### TC-NFR-07: Wydajność asynchroniczna (Brak blokowania wątku UI)
*   **Warunki wstępne:** Włączony CPU Throttling (6x slowdown) w Chrome DevTools. Stoper i 3 minutniki są uruchomione.
*   **Kroki:**
    1. Wykonaj intensywne operacje zapisu/odczytu (np. szybko dodawaj i usuwaj strefy czasowe).
    2. Zaobserwuj płynność animacji paska postępu minutnika oraz licznika stopera.
*   **Oczekiwany rezultat:** Interfejs użytkownika nie zamraża się ani nie klatkuje (brak Input Lag). Wszystkie operacje na IndexedDB są asynchroniczne (`async/await`), co pozwala na płynne renderowanie UI w wątku głównym.

#### TC-NFR-08: Brak drgań układu (No Layout Jitter)
*   **Warunki wstępne:** Stoper i minutniki są uruchomione.
*   **Kroki:**
    1. Obserwuj cyfry na wyświetlaczu stopera (w szczególności setne części sekundy `hh`) oraz minutnika.
    2. Zweryfikuj, czy sąsiednie elementy (np. przyciski pod licznikiem) przesuwają się podczas zmiany cyfr.
*   **Oczekiwany rezultat:** Cyfry zmieniają się płynnie, ale szerokość całego bloku licznika pozostaje idealnie stała. Wykorzystano font o stałej szerokości znaków (monospace), co całkowicie eliminuje drgania układu (Layout Jitter / Cumulative Layout Shift = 0).

---

## 7. Testy Przypadków Brzegowych i Destrukcyjne (Edge Cases)

### 7.1. Przejścia Czasu Letniego/Zimowego (DST)

#### TC-EC-01: Zmiana czasu (DST) w trakcie odliczania minutnika (EC-01)
*   **Warunki wstępne:** System operacyjny ma ustawioną strefę `Europe/Warsaw`. Czas systemowy jest ustawiony na 26 października 2025 r., godzina 01:55:00 (5 minut przed cofnięciem czasu z 02:00 na 01:00).
*   **Kroki:**
    1. Uruchom minutnik na dokładnie 10 minut (600 sekund) z etykietą "Test DST".
    2. Odczekaj na przejście czasu systemowego (cofnięcie o godzinę).
    3. Zaobserwuj moment wyzwolenia minutnika.
*   **Oczekiwany rezultat:** Minutnik odlicza czas na podstawie bezwzględnego znacznika Unix Epoch (milisekundy). Wyzwala się dokładnie po 600 sekundach fizycznych (o nowej godzinie 01:05), ignorując fakt, że czas systemowy cofnął się o godzinę.

#### TC-EC-02: Planowanie alarmu w noc zmiany czasu (DST)
*   **Warunki wstępne:** Czas systemowy ustawiony na noc przejścia na czas letni (przesunięcie z 02:00 na 03:00).
*   **Kroki:**
    1. Ustaw alarm jednorazowy na godzinę 02:30 (godzina, która fizycznie nie istnieje w tę noc).
    2. Zaobserwuj zachowanie systemu planowania.
*   **Oczekiwany rezultat:** System operacyjny/aplikacja poprawnie mapuje czas na bezwzględny timestamp UTC. Alarm powinien zostać automatycznie zaplanowany i wyzwolony na fizyczny odpowiednik czasu (np. natychmiast przy przejściu na 03:00 lub dokładnie 30 minut po godzinie 02:00 czasu fizycznego), zapobiegając pominięciu alarmu.

---

### 7.2. Restart Urządzenia, Crash i Rozładowanie Baterii

#### TC-EC-03: Odzyskiwanie stanu stopera po restarcie/crashu (EC-02)
*   **Warunki wstępne:** Stoper jest uruchomiony.
*   **Kroki:**
    1. W trakcie działania stopera, zasymuluj nagłe zamknięcie przeglądarki (ubicie procesu) lub zrestartuj urządzenie.
    2. Uruchom ponownie urządzenie i otwórz aplikację.
    3. Zweryfikuj stan stopera.
*   **Oczekiwany rezultat:** Stoper automatycznie wznawia działanie. Wyświetlany czas jest poprawnie przeliczony: `(Aktualny_Czas_Systemowy - start_epoch) + elapsed_ms` pobrane z tabeli `stopwatch_state` w IndexedDB. Pomiar jest ciągły i precyzyjny.

#### TC-EC-04: Rejestracja i wyzwolenie alarmów po restarcie urządzenia (BOOT_COMPLETED)
*   **Warunki wstępne:** Skonfigurowano aktywny alarm na godzinę 08:00. Urządzenie zostaje wyłączone o godzinie 23:00 i włączone ponownie o 07:30.
*   **Kroki:**
    1. Wyłącz i włącz ponownie telefon (lub zasymuluj restart środowiska).
    2. Nie uruchamiaj aplikacji ChronosApp ręcznie.
    3. Odczekaj do godziny 08:00.
*   **Oczekiwany rezultat:** Usługa tła (Service Worker wybudzany przez systemowe triggery / odbiornik `BOOT_COMPLETED` na platformach mobilnych) automatycznie rejestruje alarmy z bazy danych w systemowym harmonogramie. Alarm wyzwala się niezawodnie o godzinie 08:00 z pełnym ekranem powiadomienia i dźwiękiem.

---

### 7.3. Konflikt Audio i Aktywne Połączenie Telefoniczne

#### TC-EC-05: Wyzwolenie alarmu podczas aktywnego połączenia telefonicznego (EC-03)
*   **Warunki wstępne:** Użytkownik prowadzi aktywną rozmowę telefoniczną (lub symulujemy stan `Call State = Active` / zajęty Audio Focus w przeglądarce). Alarm jest ustawiony na bieżącą minutę.
*   **Kroki:**
    1. Nawiąż połączenie telefoniczne na urządzeniu testowym.
    2. Odczekaj na wyzwolenie alarmu.
    3. Zaobserwuj zachowanie głośnika zewnętrznego, słuchawki oraz wibracji.
*   **Oczekiwany rezultat:**
    - Głośnik zewnętrzny urządzenia pozostaje całkowicie wyciszony (ochrona słuchu użytkownika i brak zakłóceń rozmowy).
    - W kanale audio rozmowy (w słuchawce telefonu lub słuchawkach Bluetooth) emitowany jest łagodny, cichy, przerywany sygnał dźwiękowy (beeping).
    - Urządzenie uruchamia intensywny, fizyczny wzorzec wibracji (`navigator.vibrate`).
    - Na ekranie pojawia się pełnoekranowy monit alarmu umożliwiający jego wyłączenie.

#### TC-EC-06: Blokada Autoplay w przeglądarce (Autoplay Policy Bypass)
*   **Warunki wstępne:** Nowa sesja przeglądarki, w której polityka Autoplay blokuje dźwięki bez interakcji użytkownika.
*   **Kroki:**
    1. Uruchom aplikację po raz pierwszy.
    2. Zaobserwuj obecność monitu o przyznanie uprawnień do powiadomień i dźwięków.
    3. Kliknij przycisk "Zezwól" (interakcja użytkownika odblokowująca `AudioContext`).
    4. Wyzwól alarm w tle.
*   **Oczekiwany rezultat:** Kliknięcie przycisku pomyślnie odblokowuje `AudioContext` i zapisuje flagę `audio_unlocked=true` w `LocalStorage`. Alarm wyzwala się z dźwiękiem bez blokady ze strony przeglądarki.

---

### 7.4. Ograniczenia Tła Przeglądarki (Tab Suspension / Doze Mode)

#### TC-EC-07: Wyzwolenie minutnika w trybie głębokiego uśpienia (Doze Mode / Tab Suspension)
*   **Warunki wstępne:** Minutnik jest uruchomiony na 5 minut. Karta z aplikacją zostaje zminimalizowana, a telefon zablokowany i wprowadzony w stan uśpienia (Doze Mode).
*   **Kroki:**
    1. Zminimalizuj aplikację i zablokuj ekran.
    2. Odczekaj 5 minut, aż czas minutnika dobiegnie końca.
    3. Zaobserwuj zachowanie urządzenia.
*   **Oczekiwany rezultat:** Pomimo dławienia wątku głównego JavaScript przez przeglądarkę, zarejestrowany Service Worker oraz powiadomienie lokalne (Web Notifications API / Notification Triggers) wybudzają urządzenie i wyzwalają pełnoekranowe powiadomienie o najwyższym priorytecie z dźwiękiem i wibracją dokładnie w czasie zakończenia odliczania.

#### TC-EC-08: Synchronizacja stanu po wyjściu z tła (Page Visibility API)
*   **Warunki wstępne:** Stoper jest uruchomiony. Karta aplikacji zostaje zminimalizowana na 2 minuty (wątek główny zostaje zamrożony przez przeglądarkę).
*   **Kroki:**
    1. Zminimalizuj kartę na 2 minuty.
    2. Przywróć kartę jako aktywną (maksymalizacja).
    3. Zaobserwuj zachowanie licznika w pierwszej sekundzie po przywróceniu.
*   **Oczekiwany rezultat:** W momencie zmiany stanu widoczności karty (`visibilitychange` event), aplikacja natychmiast pobiera aktualny czas systemowy, oblicza różnicę i aktualizuje licznik stopera. Brak efektu "zamrożenia" lub skokowego, powolnego nadrabiania czasu w UI.

---

## 8. Matryca Pokrycia Testowego (Traceability Matrix)

Poniższa tabela mapuje wymagania biznesowe (BRD) i techniczne (SDD) na konkretne przypadki testowe zdefiniowane w niniejszym dokumencie, gwarantując 100% pokrycia testowego.

| ID Wymagania (BRD) | Nazwa Wymagania | ID Przypadku Testowego (Test Case ID) | Status Pokrycia |
| :--- | :--- | :--- | :--- |
| **US-1.1** | Autodetekcja strefy | **TC-WC-01**, **TC-WC-02** | **100% Pokryte** |
| **US-1.2** | Obsługa zmian czasu (DST) | **TC-EC-01**, **TC-EC-02** | **100% Pokryte** |
| **US-1.3** | Wyszukiwanie stref | **TC-WC-03** | **100% Pokryte** |
| **US-1.4** | Limit 10 stref | **TC-WC-04** | **100% Pokryte** |
| **US-2.1** | Dokładność stopera (0.01s) | **TC-SW-01** | **100% Pokryte** |
| **US-2.2** | Rejestrowanie międzyczasów | **TC-SW-02** | **100% Pokryte** |
| **US-2.3** | Analityka okrążeń | **TC-SW-02** | **100% Pokryte** |
| **US-2.4** | Ciągłość pomiaru stopera | **TC-SW-03**, **TC-EC-03** | **100% Pokryte** |
| **US-3.1** | Limit 5 minutników | **TC-TM-01**, **TC-TM-02** | **100% Pokryte** |
| **US-3.2** | Szablony minutników | **TC-TM-03** | **100% Pokryte** |
| **US-3.3** | Powiadomienia w tle | **TC-EC-07** | **100% Pokryte** |
| **US-4.1** | Harmonogram alarmów | **TC-AL-01** | **100% Pokryte** |
| **US-4.2** | Mechanizm drzemki | **TC-AL-02** | **100% Pokryte** |
| **US-4.3** | Gradacja głośności (Fade-in) | **TC-AL-03** | **100% Pokryte** |
| **US-4.4** | Tryb dyskretny i konflikty | **TC-EC-05** | **100% Pokryte** |
| **US-4.5** | Niezawodność po restarcie | **TC-EC-04** | **100% Pokryte** |
| **US-5.1** | Tryb Ciemny (AMOLED) | **TC-NFR-01** | **100% Pokryte** |
| **US-5.2** | Tryb Jasny | **TC-NFR-02** | **100% Pokryte** |
| **US-5.3** | Przełącznik motywów | **TC-SET-01** | **100% Pokryte** |
| **US-5.4** | Trwałość danych | **TC-SET-02** | **100% Pokryte** |
| **NFR-01-01** | AMOLED Czysta Czerń | **TC-NFR-01** | **100% Pokryte** |
| **NFR-01-02** | Light Mode | **TC-NFR-02** | **100% Pokryte** |
| **NFR-01-03** | Przełącznik motywów | **TC-SET-01** | **100% Pokryte** |
| **NFR-02-01** | Niezawodność w tle | **TC-EC-04**, **TC-EC-07** | **100% Pokryte** |
| **NFR-02-02** | Architektura stanowa | **TC-SET-01**, **TC-NFR-08** | **100% Pokryte** |
| **NFR-02-03** | Persystencja | **TC-SET-02** | **100% Pokryte** |
| **Edge Case 1** | Zmiana czasu (DST) | **TC-EC-01**, **TC-EC-02** | **100% Pokryte** |
| **Edge Case 2** | Restart urządzenia (Crash) | **TC-EC-03**, **TC-EC-04** | **100% Pokryte** |
| **Edge Case 3** | Konflikt dźwięków | **TC-EC-05**, **TC-EC-06** | **100% Pokryte** |

---
*Dokument zatwierdzony do realizacji testów przez Starszego Inżyniera QA.*
