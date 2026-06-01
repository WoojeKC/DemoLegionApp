# SPECYFIKACJA INTERFEJSU UŻYTKOWNIKA (UI SPECIFICATION)
## Projekt: ChronosApp — Nowoczesna Aplikacja Zegara i Alertyzacji
**Wersja:** 1.0  
**Status:** Gotowy do weryfikacji  
**Data:** 31 maja 2026 r.  
**Autor:** Starszy Projektant UI / Visual Designer (Senior UI Designer)  
**Dla zespołu:** Product Manager, Architekt Systemowy, Zespół Deweloperski, QA  

---

## Spis Treści
1. [Wprowadzenie i Zasady Projektowe](#1-wprowadzenie-i-zasady-projektowe)
2. [System Tokenów Wizualnych (Design Tokens)](#2-system-tokenów-wizualnych-design-tokens)
3. [Globalny Układ i Nawigacja (Global Layout & Navigation)](#3-globalny-układ-i-nawigacja-global-layout--navigation)
4. [Przepływy Użytkownika (User Flows)](#4-przepływy-użytkownika-user-flows)
5. [Specyfikacja Ekranów i Makiety (ASCII Mockups)](#5-specyfikacja-ekranów-i-makiety-ascii-mockups)
   - [5.1. Czas Światowy (World Clock)](#51-czas-światowy-world-clock)
   - [5.2. Stoper (Stopwatch)](#52-stoper-stopwatch)
   - [5.3. Minutnik (Timer)](#53-minutnik-timer)
   - [5.4. Alarmy (Alarms)](#54-alarmy-alarms)
   - [5.5. Ustawienia (Settings)](#55-ustawienia-settings)
6. [Specyficzne Kontrolki i Komponenty (Custom UI Controls)](#6-specyficzne-kontrolki-i-komponenty-custom-ui-controls)
7. [Zalecenia dotyczące Mikrointerakcji i Animacji](#7-zalecenia-dotyczące-mikrointerakcji-i-animacji)
8. [Dostępność (A11Y) i Standardy WCAG](#8-dostępność-a11y-i-standardy-wcag)

---

## 1. Wprowadzenie i Zasady Projektowe

Niniejszy dokument stanowi kompletną specyfikację interfejsu użytkownika (UI) dla aplikacji **ChronosApp**. Projekt został opracowany w oparciu o zasady **Atomic Design**, wytyczne **Mobile-First** oraz standardy dostępności **WCAG 2.1 AA**.

### Główne Filozofie Projektowe:
1. **Minimalizm i Skupienie (Focus):** Interfejs eliminuje zbędne elementy ozdobne. Czas i kontrolki są najważniejszymi elementami na ekranie.
2. **Brak Drgań Układu (No Layout Jitter):** Wszystkie dynamiczne liczniki czasu (stoper, minutnik, zegary) wykorzystują fonty o stałej szerokości znaków (monospace), co zapobiega przesunięciom układu (Layout Shifts) podczas szybkiego odświeżania cyfr.
3. **Ekstremalna Ergonomia Dotykowa:** Elementy interaktywne na urządzeniach mobilnych mają minimalny obszar klikalny wynoszący `48px x 48px` z odpowiednim marginesem bezpieczeństwa, co ułatwia obsługę jedną ręką (np. podczas biegu czy gotowania).
4. **Zoptymalizowany Ciemny Motyw (AMOLED Black):** W trybie ciemnym tło bazowe to czysta czerń (`#000000`), co pozwala na całkowite wyłączenie pikseli na ekranach OLED/AMOLED, drastycznie redukując zużycie baterii (zgodnie z wymaganiem biznesowym **BR-02**).

---

## 2. System Tokenów Wizualnych (Design Tokens)

### 2.1. Paleta Kolorów (Color Palette)

Aplikacja wspiera dwa motywy kolorystyczne za pomocą atrybutu `data-bs-theme` z Bootstrap 5.3.

| Token | Rola | Motyw Jasny (Light) | Motyw Ciemny (AMOLED Black) | Kontrast (WCAG) |
| :--- | :--- | :--- | :--- | :--- |
| `--color-bg-base` | Główne tło aplikacji | `#F8F9FA` (Złamana biel) | `#000000` (Czysta czerń) | N/A |
| `--color-bg-surface`| Tło kart, paneli, modali | `#FFFFFF` (Biel) | `#121212` (Ciemna szarość) | N/A |
| `--color-text-main` | Tekst główny, nagłówki | `#1A1A1A` (Głęboka czerń) | `#FFFFFF` (Czysta biel) | > 10:1 (AA/AAA) |
| `--color-text-muted`| Tekst pomocniczy, etykiety| `#6C757D` (Szary) | `#A0A0A0` (Jasnoszary) | > 4.5:1 (AA) |
| `--color-primary` | Kolor akcentu, przyciski | `#0D6EFD` (Bootstrap Blue) | `#3B82F6` (Vibrant Blue) | > 4.5:1 (AA) |
| `--color-success` | Najszybsze okrążenie, aktywny| `#198754` (Zielony) | `#2ECC71` (Jasnozielony) | > 4.5:1 (AA) |
| `--color-danger` | Najwolniejsze okrążenie, błąd | `#DC3545` (Czerwony) | `#E74C3C` (Jasnoczerwony) | > 4.5:1 (AA) |
| `--color-border` | Linie podziału, ramki | `#DEE2E6` (Jasnoszary) | `#2D3748` (Ciemnoszary) | N/A |

### 2.2. Typografia (Typography)

*   **Krój pisma podstawowy (Sans-Serif):** `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` (zapewnia natywny wygląd na każdej platformie).
*   **Krój pisma dla liczników (Monospace):** `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace` (zapobiega drganiom cyfr).

#### Hierarchia Typograficzna:
*   **Display 1 (Główny licznik stopera/minutnika):** `font-size: 4.5rem` (~72px), `font-weight: 700`, `font-family: Monospace`.
*   **H1 (Nagłówki sekcji):** `font-size: 2rem` (~32px), `font-weight: 700`.
*   **H2 (Nazwy stref, etykiety kart):** `font-size: 1.25rem` (~20px), `font-weight: 600`.
*   **Body (Tekst podstawowy):** `font-size: 1rem` (~16px), `font-weight: 400`.
*   **Small (Tekst pomocniczy, offsety):** `font-size: 0.875rem` (~14px), `font-weight: 400`.

### 2.3. Odstępy i Siatka (Spacing & Grid)
Zgodnie ze standardem Bootstrap 5.3, stosujemy system odstępów oparty na wielokrotności `0.25rem` (4px):
*   `$spacer-1` (4px), `$spacer-2` (8px), `$spacer-3` (16px), `$spacer-4` (24px), `$spacer-5` (48px).
*   **Siatka responsywna:** `.container` z podziałem na kolumny:
    *   Urządzenia mobilne (<768px): 1 kolumna (`.col-12`).
    *   Tablety (≥768px): 2 kolumny (`.col-md-6`).
    *   Komputery (≥1200px): 3 lub 4 kolumny (`.col-lg-4`, `.col-xl-3`).

---

## 3. Globalny Układ i Nawigacja (Global Layout & Navigation)

Aplikacja posiada spójną strukturę ramową (Shell Layout), która dostosowuje się do rozmiaru ekranu urządzenia.

### 3.1. Układ Mobilny (Mobile Viewport < 768px)
*   **Nagłówek (Header):** Sticky top. Zawiera logo "Chronos" po lewej stronie oraz szybki przełącznik motywu (ikona Słońce/Księżyc) po prawej.
*   **Obszar Treści (Main Content):** Przewijany pionowo, z dolnym marginesem zapobiegającym zasłanianiu przez nawigację.
*   **Nawigacja Dolna (Sticky Bottom Navigation Bar):** Stały pasek na dole ekranu z 5 zakładkami o wysokości `64px`. Każda zakładka ma ikonę oraz etykietę tekstową (touch target min. `48px x 48px`).

### 3.2. Układ Desktopowy (Desktop Viewport ≥ 768px)
*   **Nawigacja Boczna (Sidebar):** Stały panel po lewej stronie o szerokości `240px`. Zawiera logo, pionową listę zakładek z ikonami i tekstem oraz przełącznik motywu na dole.
*   **Obszar Treści (Main Content):** Szeroki panel po prawej stronie z marginesem wewnętrznym `.p-4` (24px), wyświetlający karty w układzie wielokolumnowym (Grid).

### 3.3. Przełącznik Motywów (Theme Switcher)
Przycisk w postaci grupy przycisków (Segmented Control) lub ikony typu toggle:
*   **Stany:** Jasny (Light) | Ciemny (AMOLED) | Systemowy (Auto).
*   **Działanie:** Zmiana motywu odbywa się bez przeładowania strony (manipulacja atrybutem `data-bs-theme` na elemencie `<html>` oraz klasą `.amoled-black` na `<body>`). Stan sesji (np. działający stoper) jest w pełni zachowany.

---

## 4. Przepływy Użytkownika (User Flows)

Poniższe diagramy tekstowe przedstawiają logiczne ścieżki poruszania się użytkownika po aplikacji.

### 4.1. Przepływ: Dodawanie Strefy Czasowej (World Clock Flow)
```
[Ekran World Clock] 
       │
       ▼ (Kliknięcie przycisku "+ Dodaj strefę" - Touch Target 48px)
[Modal: Dodaj Strefę Czasową]
       │
       ├─► [Pole wyszukiwania] ──► (Wpisanie "Tok") ──► [Lista autouzupełniania: "Asia/Tokyo"]
       │                                                          │
       ▼                                                          ▼ (Kliknięcie pozycji)
[Zablokowanie przycisku "+" jeśli limit 10 stref] ◄──────── [Dodanie strefy do listy głównej]
       │
       ▼ (Automatyczne zamknięcie modala i odświeżenie listy)
[Ekran World Clock z nową strefą na dole]
```

### 4.2. Przepływ: Obsługa Stopera (Stopwatch Flow)
```
[Ekran Stoper (Stan: Idle 00:00.00)]
       │
       ├─► [Przycisk "Start" (Zielony)] ──► [Stoper Uruchomiony (Running)]
       │                                              │
       │       ┌──────────────────────────────────────┴──────────────────────────────────────┐
       │       ▼ (Kliknięcie "Okrążenie")                                                    ▼ (Kliknięcie "Pauza")
       │  [Zapis okrążenia do listy]                                                    [Stoper Zapauzowany]
       │  [Dynamiczne wyróżnienie ekstremów (min. 3 okr.)]                                   │
       │       │                                                                             ├─► [Przycisk "Wznów"] ──► (Powrót do Running)
       │       └───────────────────────◄─────────────────────────────────────────────────────├─► [Przycisk "Reset"]
       │                                                                                     │         │
       ▼                                                                                     ▼         ▼
[Zachowanie stanu przy minimalizacji/restarcie] ◄────────────────────────────────────────────┴─── [Powrót do stanu Idle]
```

### 4.3. Przepływ: Konfiguracja i Wyzwolenie Alarmu (Alarms Flow)
```
[Ekran Alarmy]
       │
       ▼ (Kliknięcie "+ Dodaj alarm" lub edycja istniejącego)
[Modal / Ekran Edycji Alarmu]
       │
       ├─► [Wybór godziny i minuty] (Duży selektor kołowy lub klawiatura)
       ├─► [Wybór dni tygodnia] (Siedem okrągłych przycisków P-N, wielokrotny wybór)
       ├─► [Suwak drzemki] (Włącz/Wyłącz + czas trwania + limit powtórzeń)
       ├─► [Profil dźwiękowy] (Dropdown: Tylko wibracje | Łagodny | Standardowy)
       │
       ▼ (Kliknięcie "Zapisz")
[Zapis do IndexedDB i rejestracja w Service Workerze]
       │
       ▼ (Nadejście czasu alarmu w tle / uśpieniu)
[Pełnoekranowy Ekran Alarmu (Overlay)] ──► [Liniowe pogłaśnianie Fade-in (15s)]
       │
       ├─► [Przycisk "Drzemka" (Snooze)] ──► [Wyciszenie i zaplanowanie kolejnego za X min]
       │                                      (Zablokowany po osiągnięciu limitu drzemek)
       ▼
[Przycisk "Wyłącz" (Dismiss)] ──► [Zatrzymanie dźwięku/wibracji i powrót do stanu uśpienia]
```

---

## 5. Specyfikacja Ekranów i Makiety (ASCII Mockups)

### 5.1. Czas Światowy (World Clock)

#### Opis i Hierarchia:
Ekran wyświetla aktualny czas lokalny w postaci dużej, centralnej sekcji na górze, a poniżej listę maksymalnie 10 wybranych stref czasowych w postaci kart (`.card`). Każda karta strefy zawiera nazwę miasta/strefy, różnicę czasu względem lokalnego (offset) oraz aktualną godzinę i datę w tej strefie.

#### Komponenty Bootstrap 5.3:
*   `.card` z klasami `.border-0`, `.shadow-sm` dla czystego wyglądu.
*   `.btn-primary` z ikoną plusa do dodawania stref.
*   `.modal` do wyszukiwania stref z autouzupełnianiem.
*   `.badge` do wyświetlania offsetu czasu (np. `+6h`, `-2h`).

#### Makieta ASCII — Motyw Jasny (Light Mode)
```text
+-------------------------------------------------------------------------+
|  CHRONOS                                                        [ (o) ] | <-- Header (Logo & Theme Toggle)
+-------------------------------------------------------------------------+
|                                                                         |
|  LOKALNY CZAS                                                           |
|  +-------------------------------------------------------------------+  |
|  |  Warszawa, Polska (CET)                                           |  |
|  |  [H1] 14:35:22                                                    |  |
|  |  Piątek, 31 maja 2026 r.                                          |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  MOJE STREFY (3 z 10)                                                   |
|  +-------------------------------------------------------------------+  |
|  |  Londyn, Wielka Brytania (GMT)                  13:35:22          |  |
|  |  [Badge: -1h] Dzisiaj                           31.05.2026        |  |
|  +-------------------------------------------------------------------+  |
|  |  Nowy Jork, USA (EST)                           08:35:22          |  |
|  |  [Badge: -6h] Dzisiaj                           31.05.2026        |  |
|  +-------------------------------------------------------------------+  |
|  |  Tokio, Japonia (JST)                           21:35:22          |  |
|  |  [Badge: +7h] Dzisiaj                           31.05.2026        |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  [ + Dodaj nową strefę ] <-- Przycisk (Wysokość 48px, pełna szerokość)  |
|                                                                         |
+-------------------------------------------------------------------------+
|  [Zegar]      [Stoper]      [Minutnik]      [Alarmy]      [Ustawienia]  | <-- Bottom Nav
+-------------------------------------------------------------------------+
```

#### Makieta ASCII — Motyw Ciemny (AMOLED Black — `#000000`)
```text
+-------------------------------------------------------------------------+
|  CHRONOS                                                        [ (*) ] | <-- Tło: #000000, Tekst: #FFFFFF
+-------------------------------------------------------------------------+
|                                                                         |
|  LOKALNY CZAS                                                           |
|  +-------------------------------------------------------------------+  |
|  |  Warszawa, Polska (CET)                                           |  | <-- Karta tło: #121212
|  |  [H1] 14:35:22                                                    |  | <-- Tekst: #FFFFFF (Monospace)
|  |  Piątek, 31 maja 2026 r.                                          |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  MOJE STREFY (3 z 10)                                                   |
|  +-------------------------------------------------------------------+  |
|  |  Londyn, Wielka Brytania (GMT)                  13:35:22          |  | <-- Karta tło: #121212
|  |  [Badge: -1h] Dzisiaj                           31.05.2026        |  | <-- Badge tło: #2D3748
|  +-------------------------------------------------------------------+  |
|  |  Nowy Jork, USA (EST)                           08:35:22          |  |
|  |  [Badge: -6h] Dzisiaj                           31.05.2026        |  |
|  +-------------------------------------------------------------------+  |
|  |  Tokio, Japonia (JST)                           21:35:22          |  |
|  |  [Badge: +7h] Dzisiaj                           31.05.2026        |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  [ + Dodaj nową strefę ] <-- Przycisk tło: #3B82F6, Tekst: #FFFFFF      |
|                                                                         |
+-------------------------------------------------------------------------+
|  [Zegar]      [Stoper]      [Minutnik]      [Alarmy]      [Ustawienia]  | <-- Aktywna zakładka: [Zegar] (#3B82F6)
+-------------------------------------------------------------------------+
```

#### Stany i Warianty:
*   **Default:** Lista stref wczytana z bazy danych.
*   **Hover/Active (Karty stref):** Delikatne podświetlenie obramowania (`--color-primary`) na desktopie. Na mobile brak efektu hover (zapobieganie "lepkim" stanom dotykowym).
*   **Disabled:** Przycisk "[ + Dodaj nową strefę ]" staje się nieaktywny (szary, `opacity: 0.5`, `pointer-events: none`), gdy na liście znajduje się dokładnie 10 stref.
*   **Loading (Szkielet / Skeleton):** Zamiast kart wyświetlane są pulsujące szare bloki o tych samych wymiarach (efekt `.placeholder` z Bootstrap).

---

### 5.2. Stoper (Stopwatch)

#### Opis i Hierarchia:
Głównym elementem jest gigantyczny, precyzyjny cyfrowy licznik czasu na środku ekranu. Poniżej znajdują się dwa duże, okrągłe przyciski akcji (Start/Pauza oraz Okrążenie/Reset) umieszczone obok siebie, zoptymalizowane pod kątem szybkiego klikania kciukiem. Pod przyciskami znajduje się przewijana pionowo lista zarejestrowanych okrążeń z automatycznym wyróżnianiem ekstremów.

#### Komponenty Bootstrap 5.3:
*   `.display-1` dla głównego licznika (z klasą `.font-monospace`).
*   `.btn-lg` z klasami `.rounded-circle` (okrągłe przyciski o średnicy `72px` dla maksymalnej ergonomii).
*   `.list-group` z klasą `.list-group-flush` dla listy okrążeń.

#### Makieta ASCII — Motyw Jasny (Light Mode)
```text
+-------------------------------------------------------------------------+
|  CHRONOS                                                        [ (o) ] |
+-------------------------------------------------------------------------+
|                                                                         |
|                               STOPER                                    |
|                                                                         |
|                        [Display 1] 02:14.56                             | <-- Monospace, wysoka czytelność
|                                                                         |
|                  ( Okrążenie )           ((  Start  ))                  | <-- Okrągłe przyciski (72x72px)
|                  [Szary/Disabled]        [Zielony/Sukces]               |
|                                                                         |
|  OKRĄŻENIA                                                              |
|  +-------------------------------------------------------------------+  |
|  | Okrążenie 3                  00:12.40                  02:14.56   |  |
|  | [Zielony tekst - Najszybsze]                                      |  | <-- Ekstremum (Najszybsze)
|  +-------------------------------------------------------------------+  |
|  | Okrążenie 2                  01:15.10                  02:02.16   |  |
|  | [Czerwony tekst - Najwolniejsze]                                  |  | <-- Ekstremum (Najwolniejsze)
|  +-------------------------------------------------------------------+  |
|  | Okrążenie 1                  00:47.06                  00:47.06   |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
+-------------------------------------------------------------------------+
|  [Zegar]      [Stoper]      [Minutnik]      [Alarmy]      [Ustawienia]  |
+-------------------------------------------------------------------------+
```

#### Makieta ASCII — Motyw Ciemny (AMOLED Black — `#000000`)
```text
+-------------------------------------------------------------------------+
|  CHRONOS                                                        [ (*) ] |
+-------------------------------------------------------------------------+
|                                                                         |
|                               STOPER                                    |
|                                                                         |
|                        [Display 1] 02:14.56                             | <-- Tekst: #FFFFFF
|                                                                         |
|                  ( Okrążenie )           ((  Start  ))                  | <-- Start: tło #2ECC71, tekst #000000
|                  [Tło: #121212]                                         | <-- Okrążenie: tło #121212, tekst #FFFFFF
|                                                                         |
|  OKRĄŻENIA                                                              |
|  +-------------------------------------------------------------------+  |
|  | Okrążenie 3                  00:12.40                  02:14.56   |  | <-- Tekst: #2ECC71 (Jasnozielony)
|  +-------------------------------------------------------------------+  |
|  | Okrążenie 2                  01:15.10                  02:02.16   |  | <-- Tekst: #E74C3C (Jasnoczerwony)
|  +-------------------------------------------------------------------+  |
|  | Okrążenie 1                  00:47.06                  00:47.06   |  | <-- Tekst: #FFFFFF
|  +-------------------------------------------------------------------+  |
|                                                                         |
+-------------------------------------------------------------------------+
|  [Zegar]      [Stoper]      [Minutnik]      [Alarmy]      [Ustawienia]  |
+-------------------------------------------------------------------------+
```

#### Stany i Warianty:
*   **Stan: Idle (Zresetowany):** Licznik pokazuje `00:00.00`. Przycisk "Okrążenie" jest nieaktywny (disabled). Przycisk "Start" ma kolor zielony.
*   **Stan: Running (W biegu):** Licznik odlicza czas. Przycisk "Start" zmienia się w czerwony przycisk "Pauza". Przycisk "Okrążenie" staje się aktywny.
*   **Stan: Paused (Zapauzowany):** Licznik jest zatrzymany. Przycisk "Pauza" zmienia się w zielony przycisk "Wznów". Przycisk "Okrążenie" zmienia się w szary przycisk "Reset".

---

### 5.3. Minutnik (Timer)

#### Opis i Hierarchia:
Ekran podzielony jest na dwie sekcje: górną (konfigurator nowego minutnika z szybkimi szablonami/presetami) oraz dolną (lista maksymalnie 5 jednocześnie działających minutników). Każdy aktywny minutnik wyświetlany jest jako karta z nazwą, dużym odliczaniem wstecz, paskiem postępu (Progress Bar) oraz przyciskami kontrolnymi (Pauza/Wznów, Usuń).

#### Komponenty Bootstrap 5.3:
*   `.progress` i `.progress-bar` z klasą `.progress-bar-striped` i `.progress-bar-animated` dla wizualizacji upływu czasu.
*   `.form-control` i `.form-select` do konfiguracji czasu i etykiety.
*   `.btn-group` do szybkiego wyboru presetów.

#### Makieta ASCII — Motyw Jasny (Light Mode)
```text
+-------------------------------------------------------------------------+
|  CHRONOS                                                        [ (o) ] |
+-------------------------------------------------------------------------+
|                                                                         |
|  NOWY MINUTNIK                                                          |
|  [ 00 ] godz.   [ 05 ] min.   [ 00 ] sek.   Etykieta: [ Jajka miękkie ] | <-- Pola formularza
|                                                                         |
|  SZYBKI WYBÓR (PRESETS)                                                 |
|  [ 3 min ]  [ 5 min ]  [ 10 min ]  [ 15 min ]  [ 25 min ]  [ 45 min ]   | <-- Przyciski presetów
|                                                                         |
|  [ Uruchom minutnik ] <-- Przycisk (Wysokość 48px, pełna szerokość)     |
|                                                                         |
|  AKTYWNE MINUTNIKI (2 z 5)                                              |
|  +-------------------------------------------------------------------+  |
|  |  Jajka miękkie                                                    |  |
|  |  [H2] 02:45                                                       |  | <-- Monospace
|  |  [=========================>..........................] 55%       |  | <-- Pasek postępu (Progress)
|  |  [ Pauza ]  [ Usuń ]                                              |  | <-- Przyciski kontrolne
|  +-------------------------------------------------------------------+  |
|  |  Pieczenie ciasta                                                 |  |
|  |  [H2] 38:12                                                       |  |
|  |  [===================================================>.] 98%       |  |
|  |  [ Pauza ]  [ Usuń ]                                              |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
+-------------------------------------------------------------------------+
|  [Zegar]      [Stoper]      [Minutnik]      [Alarmy]      [Ustawienia]  |
+-------------------------------------------------------------------------+
```

#### Makieta ASCII — Motyw Ciemny (AMOLED Black — `#000000`)
```text
+-------------------------------------------------------------------------+
|  CHRONOS                                                        [ (*) ] |
+-------------------------------------------------------------------------+
|                                                                         |
|  NOWY MINUTNIK                                                          |
|  [ 00 ] godz.   [ 05 ] min.   [ 00 ] sek.   Etykieta: [ Jajka miękkie ] | <-- Inputy tło: #121212, ramka: #2D3748
|                                                                         |
|  SZYBKI WYBÓR (PRESETS)                                                 |
|  [ 3 min ]  [ 5 min ]  [ 10 min ]  [ 15 min ]  [ 25 min ]  [ 45 min ]   | <-- Presety tło: #121212, tekst: #FFFFFF
|                                                                         |
|  [ Uruchom minutnik ] <-- Przycisk tło: #3B82F6, Tekst: #FFFFFF      |
|                                                                         |
|  AKTYWNE MINUTNIKI (2 z 5)                                              |
|  +-------------------------------------------------------------------+  |
|  |  Jajka miękkie                                                    |  | <-- Karta tło: #121212
|  |  [H2] 02:45                                                       |  | <-- Tekst: #FFFFFF
|  |  [=========================>..........................] 55%       |  | <-- Pasek postępu: #3B82F6
|  |  [ Pauza ]  [ Usuń ]                                              |  | <-- Przyciski tło: #2D3748
|  +-------------------------------------------------------------------+  |
|  |  Pieczenie ciasta                                                 |  |
|  |  [H2] 38:12                                                       |  |
|  |  [===================================================>.] 98%       |  |
|  |  [ Pauza ]  [ Usuń ]                                              |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
+-------------------------------------------------------------------------+
|  [Zegar]      [Stoper]      [Minutnik]      [Alarmy]      [Ustawienia]  |
+-------------------------------------------------------------------------+
```

#### Stany i Warianty:
*   **Default (Uruchomiony):** Pasek postępu płynnie się kurczy, czas odlicza w dół. Przycisk "Pauza" jest aktywny.
*   **Zapauzowany:** Pasek postępu przestaje się animować i zmienia kolor na szary. Przycisk "Pauza" zmienia się na "Wznów".
*   **Zakończony (Completed):** Karta minutnika pulsuje czerwonym obramowaniem, pasek postępu ma 100% szerokości i kolor czerwony. Wyświetla się przycisk "Wyłącz" (Dismiss) oraz odtwarzany jest dźwięk/wibracja.
*   **Disabled:** Przycisk "[ Uruchom minutnik ]" oraz presety stają się nieaktywne, gdy działa dokładnie 5 minutników (zgodnie z regułą **BR-02**).

---

### 5.4. Alarmy (Alarms)

#### Opis i Hierarchia:
Ekran wyświetla listę skonfigurowanych alarmów w postaci dużych kart. Każda karta zawiera czas alarmu (duży font), etykietę, wybrane dni tygodnia (skróty literowe z wyróżnieniem aktywnych) oraz przełącznik (Switch) do szybkiego włączania/wyłączania alarmu. Na dole ekranu znajduje się pływający przycisk dodawania nowego alarmu (Floating Action Button - FAB) lub duży przycisk na dole.

#### Komponenty Bootstrap 5.3:
*   `.form-switch` dla przełącznika aktywności alarmu.
*   `.btn-group` lub niestandardowe okrągłe przyciski dla dni tygodnia.
*   `.modal` do konfiguracji i edycji parametrów alarmu.

#### Makieta ASCII — Motyw Jasny (Light Mode)
```text
+-------------------------------------------------------------------------+
|  CHRONOS                                                        [ (o) ] |
+-------------------------------------------------------------------------+
|                                                                         |
|  ALARMY                                                                 |
|  +-------------------------------------------------------------------+  |
|  |  [H1] 07:00                                      ( o ) Switch ON  |  | <-- Przełącznik aktywności
|  |  Pobudka Praca                                                    |  |
|  |  Powtarzaj: [Pn] [Wt] [Śr] [Cz] [Pt]  So  Nd                      |  | <-- Aktywne dni w nawiasach []
|  |  Drzemka: 9 min (max 3) | Profil: Standardowy                     |  |
|  +-------------------------------------------------------------------+  |
|  |  [H1] 09:30                                      ( . ) Switch OFF |  | <-- Alarm wyłączony (poszarzały)
|  |  Weekendowy relaks                                                |  |
|  |  Powtarzaj:  Pn   Wt   Śr   Cz   Pt  [So] [Nd]                    |  |
|  |  Drzemka: Wyłączona | Profil: Łagodny                             |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  [ + Dodaj nowy alarm ] <-- Przycisk (Wysokość 48px, pełna szerokość)   |
|                                                                         |
+-------------------------------------------------------------------------+
|  [Zegar]      [Stoper]      [Minutnik]      [Alarmy]      [Ustawienia]  |
+-------------------------------------------------------------------------+
```

#### Makieta ASCII — Motyw Ciemny (AMOLED Black — `#000000`)
```text
+-------------------------------------------------------------------------+
|  CHRONOS                                                        [ (*) ] |
+-------------------------------------------------------------------------+
|                                                                         |
|  ALARMY                                                                 |
|  +-------------------------------------------------------------------+  |
|  |  [H1] 07:00                                      ( o ) Switch ON  |  | <-- Karta tło: #121212, Switch: #3B82F6
|  |  Pobudka Praca                                                    |  |
|  |  Powtarzaj: [Pn] [Wt] [Śr] [Cz] [Pt]  So  Nd                      |  | <-- Aktywne dni: tekst #3B82F6
|  |  Drzemka: 9 min (max 3) | Profil: Standardowy                     |  |
|  +-------------------------------------------------------------------+  |
|  |  [H1] 09:30                                      ( . ) Switch OFF |  | <-- Karta tło: #121212, opacity: 0.5
|  |  Weekendowy relaks                                                |  |
|  |  Powtarzaj:  Pn   Wt   Śr   Cz   Pt  [So] [Nd]                    |  |
|  |  Drzemka: Wyłączona | Profil: Łagodny                             |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  [ + Dodaj nowy alarm ] <-- Przycisk tło: #3B82F6, Tekst: #FFFFFF      |
|                                                                         |
+-------------------------------------------------------------------------+
|  [Zegar]      [Stoper]      [Minutnik]      [Alarmy]      [Ustawienia]  |
+-------------------------------------------------------------------------+
```

#### Stany i Warianty:
*   **Alarm Aktywny (Switch ON):** Karta ma pełną widoczność, tekst jest jasny, przełącznik ma kolor akcentu (`--color-primary`).
*   **Alarm Nieaktywny (Switch OFF):** Karta ma zmniejszoną przezroczystość (`opacity: 0.5`), co wizualnie odróżnia ją od aktywnych alarmów.
*   **Tryb Edycji (Modal):** Wyświetla się po kliknięciu w dowolne miejsce karty alarmu (poza przełącznikiem).

---

### 5.5. Ustawienia (Settings)

#### Opis i Hierarchia:
Ekran zawiera listę opcji konfiguracyjnych pogrupowanych w logiczne sekcje (Wygląd, Dźwięki i Powiadomienia, System). Każda opcja ma jasną etykietę, opis pomocniczy oraz odpowiednią kontrolkę (Select, Switch, Button).

#### Komponenty Bootstrap 5.3:
*   `.list-group` z klasą `.list-group-flush` dla czystego podziału opcji.
*   `.form-select` do wyboru motywu i formatu czasu.
*   `.btn-outline-danger` do resetowania danych.

#### Makieta ASCII — Motyw Jasny (Light Mode)
```text
+-------------------------------------------------------------------------+
|  CHRONOS                                                        [ (o) ] |
+-------------------------------------------------------------------------+
|                                                                         |
|  USTAWIENIA                                                             |
|                                                                         |
|  WYGLĄD                                                                 |
|  +-------------------------------------------------------------------+  |
|  |  Motyw aplikacji                                                  |  |
|  |  [ Wybór: Jasny / Ciemny / Zgodnie z systemem ]                   |  | <-- Form Select
|  +-------------------------------------------------------------------+  |
|  |  Format czasu                                                     |  |
|  |  (o) 24-godzinny (14:35)      ( ) 12-godzinny (2:35 PM)           |  | <-- Radio Buttons
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  DŹWIĘKI I POWIADOMIENIA                                                |
|  +-------------------------------------------------------------------+  |
|  |  Domyślny czas drzemki                                            |  |
|  |  [ Wybór: 5 minut / 9 minut / 10 minut / 15 minut ]               |  |
|  +-------------------------------------------------------------------+  |
|  |  Zezwolenie na powiadomienia                                      |  |
|  |  Status: [ Przyznano ]  [ Przetestuj powiadomienie ]              |  | <-- Przycisk testowy
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  SYSTEM                                                                 |
|  +-------------------------------------------------------------------+  |
|  |  [ Resetuj wszystkie dane aplikacji ] <-- Przycisk czerwony       |  | <-- Wyczyszczenie bazy danych
|  +-------------------------------------------------------------------+  |
|                                                                         |
+-------------------------------------------------------------------------+
|  [Zegar]      [Stoper]      [Minutnik]      [Alarmy]      [Ustawienia]  |
+-------------------------------------------------------------------------+
```

#### Makieta ASCII — Motyw Ciemny (AMOLED Black — `#000000`)
```text
+-------------------------------------------------------------------------+
|  CHRONOS                                                        [ (*) ] |
+-------------------------------------------------------------------------+
|                                                                         |
|  USTAWIENIA                                                             |
|                                                                         |
|  WYGLĄD                                                                 |
|  +-------------------------------------------------------------------+  |
|  |  Motyw aplikacji                                                  |  |
|  |  [ Wybór: Jasny / Ciemny / Zgodnie z systemem ]                   |  | <-- Select tło: #121212, tekst: #FFFFFF
|  +-------------------------------------------------------------------+  |
|  |  Format czasu                                                     |  |
|  |  (o) 24-godzinny (14:35)      ( ) 12-godzinny (2:35 PM)           |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  DŹWIĘKI I POWIADOMIENIA                                                |
|  +-------------------------------------------------------------------+  |
|  |  Domyślny czas drzemki                                            |  |
|  |  [ Wybór: 5 minut / 9 minut / 10 minut / 15 minut ]               |  |
|  +-------------------------------------------------------------------+  |
|  |  Zezwolenie na powiadomienia                                      |  |
|  |  Status: [ Przyznano ]  [ Przetestuj powiadomienie ]              |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  SYSTEM                                                                 |
|  +-------------------------------------------------------------------+  |
|  |  [ Resetuj wszystkie dane aplikacji ] <-- Przycisk czerwony       |  | <-- Border: #E74C3C, Tekst: #E74C3C
|  +-------------------------------------------------------------------+  |
|                                                                         |
+-------------------------------------------------------------------------+
|  [Zegar]      [Stoper]      [Minutnik]      [Alarmy]      [Ustawienia]  |
+-------------------------------------------------------------------------+
```

---

## 6. Specyficzne Kontrolki i Komponenty (Custom UI Controls)

W celu zapewnienia najwyższej użyteczności (UX) zaprojektowano dedykowane, intuicyjne kontrolki dla kluczowych funkcji aplikacji.

### 6.1. Wyszukiwanie Stref z Autouzupełnianiem (Zone Search Autocomplete)
Kontrolka umieszczona w modalu dodawania strefy czasowej.

```text
+-----------------------------------------------------------------------+
|  Dodaj strefę czasową                                             (X) | <-- Nagłówek modala
+-----------------------------------------------------------------------+
|  [ Ikona lupy ] [ Wpisz miasto lub strefę... (np. Tok)            [x] | <-- Pole tekstowe z przyciskiem czyszczenia [x]
+-----------------------------------------------------------------------+
|  WYNIKI WYSZUKIWANIA                                                  |
|  > Asia/Tokyo (Tokio, Japonia)                      [ + Dodaj ]       | <-- Pozycja aktywna/wybrana (podświetlona)
|    Asia/Tomsk (Tomsk, Rosja)                        [ + Dodaj ]       |
|    Pacific/Tongatapu (Tongatapu, Tonga)             [ + Dodaj ]       |
+-----------------------------------------------------------------------+
```
*   **Interakcja:** 
    *   Wpisanie min. 1 znaku uruchamia filtrowanie listy w czasie rzeczywistym.
    *   Przycisk `[x]` po prawej stronie pola tekstowego natychmiast czyści wpisany tekst i przywraca stan początkowy.
    *   Nawigacja strzałkami góra/dół na klawiaturze pozwala na poruszanie się po wynikach, a klawisz `Enter` zatwierdza wybór i dodaje strefę.

### 6.2. Lista Okrążeń z Wyróżnieniem Ekstremów (Lap List with Extremes)
Tabela lub lista w module stopera, która dynamicznie analizuje czasy po dodaniu każdego nowego okrążenia (wymagane min. 3 okrążenia).

```text
+-----------------------------------------------------------------------+
|  Okrążenie 4          00:10.15 [Najszybsze]               02:24.71    | <-- Kolor zielony (#2ECC71 / #198754)
|  Okrążenie 3          00:12.40                            02:14.56    | <-- Kolor standardowy
|  Okrążenie 2          01:15.10 [Najwolniejsze]            02:02.16    | <-- Kolor czerwony (#E74C3C / #DC3545)
|  Okrążenie 1          00:47.06                            00:47.06    | <-- Kolor standardowy
+-----------------------------------------------------------------------+
```
*   **Logika wizualna:** Zielone i czerwone wyróżnienie jest aplikowane wyłącznie do tekstu czasu okrążenia (lub jako subtelna plakietka/badge obok numeru okrążenia), aby uniknąć zbyt agresywnego kolorowania całego wiersza, co mogłoby obniżyć czytelność w trybie ciemnym.

### 6.3. Konfigurator Dni Tygodnia w Alarmach (Weekday Picker)
Kontrolka w postaci 7 okrągłych przycisków reprezentujących dni tygodnia.

```text
Powtarzaj w dni:
( Pn )   ( Wt )   ( Śr )   ( Cz )   ( Pt )   [ So ]   [ Nd ]
```
*   **Zasada działania:**
    *   Dni aktywne (wybrane) mają pełne tło w kolorze akcentu (`--color-primary`) i biały tekst.
    *   Dni nieaktywne mają tylko obramowanie (`border`) i standardowy kolor tekstu.
    *   **A11Y:** Każdy przycisk posiada atrybut `aria-pressed="true/false"` oraz pełną etykietę dla czytników ekranu (np. `aria-label="Poniedziałek, zaznaczone"`).

### 6.4. Suwak i Limit Drzemki (Snooze Slider & Limit)
Intuicyjna sekcja konfiguracji drzemki w modalu edycji alarmu.

```text
[x] Włącz drzemkę (Switch)
Czas trwania drzemki:
<---[=======o======================]--->  9 minut (Suwak / Range Input)

Maksymalna liczba drzemek:
( ) Bez limitu   (o) Limit: [ 3 ] powtórzenia (Stepper: - / +)
```
*   **Interakcja:**
    *   Wyłączenie drzemki za pomocą głównego przełącznika (Switch) automatycznie poszarza (`opacity: 0.5`, `pointer-events: none`) suwak czasu oraz konfigurator limitu drzemek.
    *   Stepper limitu drzemek posiada przyciski `-` oraz `+` o rozmiarze `40px x 40px` dla łatwej regulacji.

---

## 7. Zalecenia dotyczące Mikrointerakcji i Animacji

Płynne animacje i przejścia (Transitions) podnoszą jakość UX, nadając aplikacji nowoczesny charakter i ułatwiając zrozumienie zmian stanów.

### 7.1. Parametry Animacji (Timing & Easing)
Wszystkie animacje w aplikacji muszą być zgodne z poniższymi wytycznymi wydajnościowymi (zapobieganie Layout Shifts, płynność 60 FPS):
*   **Czas trwania (Duration):**
    *   Szybkie przejścia (np. hover na przyciskach, zmiana stanu switcha): `150ms`.
    *   Średnie animacje (np. otwieranie modali, wysuwanie toastów): `250ms`.
    *   Długie animacje (np. usuwanie karty z listy): `350ms`.
*   **Krzywa przejścia (Easing):**
    *   Wejście elementu: `cubic-bezier(0, 0, 0.2, 1)` (Decelerate - szybki start, łagodne zatrzymanie).
    *   Wyjście elementu: `cubic-bezier(0.4, 0, 1, 1)` (Accelerate - powolny start, szybkie wyjście).
    *   Ruch wewnątrz ekranu: `cubic-bezier(0.4, 0, 0.2, 1)` (Standard - naturalny ruch).

### 7.2. Specyficzne Mikrointerakcje:
1.  **Pasek Postępu Minutnika (Timer Progress Bar):** Pasek postępu musi zmniejszać się płynnie za pomocą przejścia CSS na właściwości `width`: `transition: width 1s linear`. Zapobiega to skokowemu zmniejszaniu się paska co sekundę.
2.  **Dodawanie Okrążenia (Lap Insertion):** Nowo dodane okrążenie na liście stopera powinno pojawiać się na samej górze za pomocą animacji wysunięcia z góry (Slide-down) z jednoczesnym rozjaśnieniem (Fade-in):
    ```css
    @keyframes lapInsert {
      from { opacity: 0; transform: translateY(-20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    ```
3.  **Pulsowanie Aktywnego Alarmu (Alarm Trigger Overlay):** Gdy alarm ulega wyzwoleniu, tło ekranu alarmu powinno łagodnie pulsować (efekt "oddychania") w rytm dźwięku, przechodząc od czerni do bardzo ciemnej czerwieni (`#1A0000`), co sygnalizuje stan alarmowy bez wywoływania nagłego oślepienia użytkownika w ciemnym pokoju.
4.  **Przełącznik Motywów (Theme Toggle Animation):** Podczas kliknięcia ikony motywu, ikona Słońca powinna płynnie obrócić się o 360 stopni i przekształcić w ikonę Księżyca (wykorzystanie transformacji SVG).

---

## 8. Dostępność (A11Y) i Standardy WCAG

Aplikacja ChronosApp została zaprojektowana z myślą o pełnej inkluzywności, spełniając wymagania **WCAG 2.1 AA**.

### 8.1. Kontrast i Czytelność (Contrast)
*   Wszystkie teksty główne w motywie jasnym i ciemnym posiadają współczynnik kontrastu do tła przekraczający **7:1** (spełniając nawet rygorystyczny standard WCAG AAA).
*   Teksty pomocnicze i ikony posiadają kontrast minimum **4.5:1**.
*   Elementy akcentujące (zielone najszybsze okrążenie, czerwone najwolniejsze okrążenie) zostały dobrane tak, aby były doskonale widoczne również dla osób z zaburzeniami rozpoznawania barw (deuteranopia, protanopia).

### 8.2. Nawigacja Klawiaturą (Keyboard Navigation)
*   **Focus Ring:** Każdy element interaktywny (przycisk, input, zakładka) posiada wyraźną, kontrastową ramkę skupienia (`:focus-visible`) w kolorze `--color-primary` o szerokości `3px` z przesunięciem `2px` (`outline-offset`).
*   **Kolejność Tabulacji (Tab Order):** Nawigacja klawiszem `Tab` odbywa się w sposób logiczny, od góry do dołu, od lewej do prawej.
*   **Skróty Klawiszowe (Keyboard Shortcuts):**
    *   `Spacja` — Start / Pauza stopera oraz aktywnego minutnika (gdy element sterujący ma focus).
    *   `Escape` — Zamknięcie aktywnego modala lub wyciszenie dzwoniącego alarmu.

### 8.3. Atrybuty ARIA i Wsparcie dla Czytników Ekranu (Screen Readers)
*   **Dynamiczne Liczniki:** Wyświetlacze czasu stopera i minutnika posiadają atrybut `aria-live="polite"`, co pozwala czytnikom ekranu na odczytywanie aktualnego stanu na żądanie użytkownika, bez ciągłego, uciążliwego odczytywania setnych części sekundy.
*   **Etykiety Pomocnicze:** Wszystkie przyciski oparte wyłącznie na ikonach (np. przycisk usuwania strefy z ikoną kosza) posiadają tekstową etykietę `aria-label` (np. `aria-label="Usuń strefę Londyn"`).
*   **Stany Kontrolek:** Przełączniki alarmów posiadają atrybut `role="switch"` oraz `aria-checked="true/false"`.

### 8.4. Obszary Dotykowe (Touch Targets)
*   Minimalny rozmiar każdego elementu klikalnego na urządzeniach mobilnych wynosi **`48px x 48px`** (zgodnie z wytycznymi Apple HIG i Google Material Design).
*   Odległość między sąsiadującymi przyciskami wynosi minimum **`8px`**, co zapobiega przypadkowym kliknięciom (np. kliknięciu "Reset" zamiast "Okrążenie").

---
*Dokument specyfikacji UI zatwierdzony do wdrożenia i przekazany zespołowi deweloperskiemu.*
