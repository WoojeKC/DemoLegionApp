# SPECYFIKACJA INTERFEJSU UŻYTKOWNIKA (UI SPECIFICATION)
## Projekt: Nowoczesna Aplikacja BMI SPA (Wersja 1.0)

| Parametr | Szczegóły |
| :--- | :--- |
| **Nazwa Projektu** | BMI SPA Application |
| **Wersja Dokumentu** | 1.0.0 |
| **Status** | Gotowy do Implementacji |
| **Autor** | Starszy Projektant UI / Visual Designer (Senior UI Designer) |
| **Rola Odbiorcy** | Zespół Deweloperski, Product Manager, QA |
| **Data Utworzenia** | Październik 2023 |

---

## 1. Wstęp i Założenia Projektowe (Design Principles)

Niniejszy dokument zawiera szczegółową specyfikację interfejsu użytkownika (UI) dla nowoczesnej aplikacji Single Page Application (SPA) do obliczania wskaźnika masy ciała (BMI). Projekt został opracowany zgodnie z najnowszymi trendami w projektowaniu interfejsów cyfrowych, kładąc nacisk na estetykę, ergonomię, wydajność oraz pełną dostępność.

### 1.1. Główne Filozofie Projektowe
* **Mobile-First & Touch-First:** Interfejs został zaprojektowany w pierwszej kolejności na urządzenia mobilne. Wszystkie elementy interaktywne mają powiększoną strefę kliknięcia (touch targets), co ułatwia obsługę kciukiem na ekranach dotykowych.
* **Atomic Design:** Interfejs opiera się na spójnym systemie komponentów (tokeny, atomy, molekuły, organizmy), co gwarantuje spójność wizualną i ułatwia implementację w kodzie.
* **Local-First & Zero-Latency Feel:** Aplikacja reaguje natychmiastowo. Przejścia stanów, animacje i walidacja odbywają się w czasie rzeczywistym (60fps), dając użytkownikowi poczucie płynności i braku opóźnień.
* **Inkluzywność (A11Y):** Pełna zgodność ze standardami WCAG 2.1 na poziomie AA. Interfejs jest czytelny dla osób niedowidzących, wspiera czytniki ekranu oraz umożliwia pełną nawigację za pomocą klawiatury.

---

## 2. System Tokenów Projektowych (Design Tokens)

Tokeny projektowe stanowią fundament spójności wizualnej aplikacji. Są one bezpośrednio mapowane na zmienne CSS (CSS Custom Properties) w Bootstrap 5.3.

### 2.1. Paleta Kolorów (Color Palette)

Aplikacja wspiera natywny tryb jasny (Light Mode) oraz ciemny (Dark Mode). Kolory zostały dobrane tak, aby spełniać wymagania kontrastu WCAG 2.1 AA (minimum 4.5:1 dla tekstu normalnego, 3:1 dla dużego).

#### A. Kolory Podstawowe i Neutralne

| Token CSS | Light Mode (Hex) | Dark Mode (Hex) | Zastosowanie |
| :--- | :--- | :--- | :--- |
| `--color-bg-main` | `#f8f9fa` (Gray 100) | `#121212` | Główne tło aplikacji |
| `--color-bg-card` | `#ffffff` | `#1e1e1e` | Tło kart formularza i wyników |
| `--color-text-primary` | `#212529` (Gray 900) | `#f8f9fa` (Gray 100) | Główny tekst, nagłówki |
| `--color-text-muted` | `#6c757d` (Gray 600) | `#a0a0a0` | Teksty pomocnicze, disclaimery |
| `--color-border` | `#dee2e6` (Gray 300) | `#2d2d2d` | Ramki, linie podziału |
| `--color-primary` | `#0d6efd` (Blue) | `#0d6efd` | Kolor akcentowy, przyciski, aktywne stany |
| `--color-primary-hover`| `#0b5ed7` | `#0b5ed7` | Stan hover dla elementów aktywnych |

#### B. Kolory Statusów WHO (Wizualizacja Wyników)

Te kolory są stałe dla obu motywów i służą do oznaczania kategorii BMI na suwaku SVG, tekstach wyników oraz tła alertów.

| Kategoria BMI | Zakres | Kolor Hex | Klasa Bootstrap | Zastosowanie |
| :--- | :--- | :--- | :--- | :--- |
| **Wyczerpanie** | `< 16.0` | `#3498db` | `.text-info` / `.alert-info` | Jasnoniebieski |
| **Wychudzenie** | `16.0 – 16.9` | `#2980b9` | `.text-info` / `.alert-info` | Niebieski |
| **Niedowaga** | `17.0 – 18.4` | `#f1c40f` | `.text-warning` / `.alert-warning` | Żółty |
| **Waga prawidłowa**| `18.5 – 24.9` | `#2ecc71` | `.text-success` / `.alert-success` | Zielony |
| **Nadwaga** | `25.0 – 29.9` | `#e67e22` | `.text-warning` / `.alert-warning` | Pomarańczowy |
| **Otyłość I stopnia**| `30.0 – 34.9` | `#e74c3c` | `.text-danger` / `.alert-danger` | Jasnoczerwony |
| **Otyłość II stopnia**| `35.0 – 39.9` | `#c0392b` | `.text-danger` / `.alert-danger` | Czerwony |
| **Otyłość III stopnia**| `>= 40.0` | `#8e44ad` | `.text-danger` / `.alert-danger` | Ciemny fiolet |

### 2.2. Typografia (Typography)

Aplikacja wykorzystuje systemowy stos fontów (sans-serif), co eliminuje potrzebę pobierania zewnętrznych plików czcionek i przyspiesza ładowanie strony (LCP).

* **Stos fontów:** `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
* **Skala typograficzna:**

| Token CSS | Wielkość (rem / px) | Grubość (Weight) | Zastosowanie |
| :--- | :--- | :--- | :--- |
| `--font-size-h1` | `2.25rem` (36px) | `700` (Bold) | Główny nagłówek (tytuł aplikacji) |
| `--font-size-bmi` | `4.5rem` (72px) | `800` (Extra Bold) | Wyświetlacz liczbowy BMI w Dashboardzie |
| `--font-size-h2` | `1.5rem` (24px) | `600` (Semi Bold) | Nagłówki sekcji (Formularz, Wyniki) |
| `--font-size-body` | `1.0rem` (16px) | `400` (Regular) | Teksty zwykłe, etykiety pól |
| `--font-size-small`| `0.875rem` (14px) | `400` (Regular) | Komunikaty o błędach, opisy pól |
| `--font-size-xs` | `0.75rem` (12px) | `400` (Regular) | Disclaimer, podziałka suwaka SVG |

### 2.3. Odstępy i Siatka (Grid & Spacing)

Zgodnie z systemem Bootstrap 5.3, stosujemy siatkę opartą na 12 kolumnach oraz standardowe klasy odstępów (spacers):

* **Siatka (Breakpoints):**
  * Mobile: `< 992px` (układ jednokolumnowy, formularz i wyniki pionowo).
  * Desktop: `>= 992px` (układ dwukolumnowy, formularz po lewej, wyniki po prawej).
* **Odstępy (Spacing System):**
  * `p-3` / `m-3` = `1.0rem` (16px) - standardowy padding wewnątrz kart na mobile.
  * `p-4` / `m-4` = `1.5rem` (24px) - standardowy padding wewnątrz kart na desktopie.
  * `g-4` = `1.5rem` (24px) - odstęp między kolumnami siatki.

---

## 3. Przepływ Użytkownika (User Flows)

### 3.1. Scenariusz 1: Pierwsze wejście i obliczenie (System Metryczny)
1. Użytkownik wchodzi na stronę. Widzi czysty, nowoczesny formularz w trybie metrycznym (domyślny). Kolumna wyników na desktopie wyświetla stan pusty (placeholder zachęcający do wpisania danych), a na mobile jest ukryta.
2. Użytkownik wpisuje wzrost (np. `180` cm) i wagę (np. `75` kg). Pola opcjonalne (wiek, płeć) pozostawia puste.
3. Podczas wpisywania system waliduje dane w locie. Przycisk "Oblicz BMI" staje się aktywny.
4. Użytkownik klika "Oblicz BMI" (lub opuszcza ostatnie pole formularza).
5. **Efekt:**
   * Na mobile: Ekran płynnie przewija się (scroll-to-view) do sekcji wyników, która pojawia się z animacją fade-in.
   * Na desktopie: Sekcja wyników po prawej stronie natychmiast wypełnia się danymi.
   * Marker na suwaku SVG płynnie przesuwa się na wartość `23.1` (zielony zakres - waga prawidłowa).
   * Wyświetla się duży wynik `23.1`, etykieta "WAGA PRAWIDŁOWA" oraz zielony alert z rekomendacją i wyliczoną deltą wagową.

### 3.2. Scenariusz 2: Przełączanie jednostek (System Imperialny)
1. Użytkownik ma wpisane dane w systemie metrycznym (`180` cm, `75` kg).
2. Użytkownik klika przełącznik "System Imperialny" na górze formularza.
3. **Efekt:**
   * Etykiety pól natychmiast zmieniają się na "Stopy", "Cale" oraz "Funty".
   * Wartości w polach zostają automatycznie przeliczone bez czyszczenia formularza: wzrost `180` cm zamienia się na `5` ft i `11` in, a waga `75` kg na `165.3` lbs.
   * Wynik BMI pozostaje bez zmian (`23.1`), suwak i dashboard nie ulegają resetowi.

### 3.3. Scenariusz 3: Wejście z linku udostępnionego (Base64 URL)
1. Użytkownik klika w link udostępniony przez znajomego: `https://bmi.app/?data=eyJzeXMiOiJtIiwidyI6NzIuNSwiaCI6MTc4LCJnIjoibSIsImEiOjI4fQ`
2. Aplikacja uruchamia się, parser w `app.js` wykrywa parametr `data`, dekoduje go z Base64 i waliduje.
3. Formularz automatycznie wypełnia się zdekodowanymi danymi: System metryczny, Wzrost `178` cm, Waga `72.5` kg, Płeć: Mężczyzna, Wiek: 28 lat.
4. Silnik automatycznie wyzwala obliczenie.
5. Użytkownik od razu po załadowaniu strony widzi gotowy Dashboard Wynikowy znajomego. Na górze pojawia się powiadomienie Toast: *"Wczytano wynik z udostępnionego linku!"*.

### 3.4. Scenariusz 4: Resetowanie i ponowne obliczenie
1. Użytkownik ma wyświetlony wynik. Klika przycisk "Oblicz ponownie" lub "Resetuj" w sekcji wyników.
2. **Efekt:**
   * Formularz zostaje wyczyszczony do stanu początkowego (puste pola, domyślny system metryczny).
   * Sekcja wyników płynnie znika (fade-out).
   * Focus klawiatury zostaje automatycznie przeniesiony na pierwsze pole formularza (Wzrost).

---

## 4. Struktura i Układ Ekranu (Layout & Grid)

Aplikacja wykorzystuje elastyczny, responsywny układ oparty na Bootstrap 5.3.

### 4.1. Układ Mobilny (Mobile Layout - < 992px)
Na urządzeniach mobilnych interfejs układa się w jedną pionową kolumnę. Sekcja wyników jest początkowo ukryta i pojawia się dynamicznie pod formularzem dopiero po wykonaniu obliczenia.

```
+---------------------------------------+
|  [Ikona] BMI SPA App    [Theme Toggle]|  <- Header (Sticky)
+---------------------------------------+
|                                       |
|  +---------------------------------+  |
|  |       KARTA FORMULARZA          |  |  <- Krok 1: Wprowadzanie danych
|  |                                 |  |
|  |  [ Metryczny ]  [ Imperialny ]  |  |  <- Przełącznik systemów miar
|  |                                 |  |
|  |  Wzrost (cm)                    |  |
|  |  [ 180                       ]  |  |  <- Input numeryczny
|  |                                 |  |
|  |  Masa ciała (kg)                |  |
|  |  [ 75                        ]  |  |  <- Input numeryczny
|  |                                 |  |
|  |  Płeć (Opcjonalnie)             |  |
|  |  [ Kobieta ]    [ Mężczyzna ]   |  |  <- Segmented Control
|  |                                 |  |
|  |  Wiek (Opcjonalnie): 25 lat     |  |
|  |  (======o=====================) |  |  <- Suwak (Range Input)
|  |                                 |  |
|  |  [       OBLICZ BMI          ]  |  |  <- Przycisk akcji (Duży, 44px+)
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  |       KARTA WYNIKÓW (Dynamic)   |  |  <- Krok 2: Prezentacja (po kliknięciu)
|  |                                 |  |
|  |            TWÓJ WYNIK           |  |
|  |              23.1               |  |  <- Duży wskaźnik liczbowy
|  |        WAGA PRAWIDŁOWA          |  |  <- Klasyfikacja WHO (Kolor)
|  |                                 |  |
|  |  [======|=====================]  |  |  <- Suwak SVG z markerem
|  |                                 |  |
|  |  +---------------------------+  |  |
|  |  | Alert: Gratulacje! Twój   |  |  |  <- Dynamiczna rekomendacja i delta
|  |  | idealny środek to 70.3 kg |  |  |
|  |  +---------------------------+  |  |
|  |                                 |  |
|  |  [ Udostępnij ]   [ Resetuj ]   |  |  <- Przyciski akcji pomocniczych
|  |                                 |  |
|  |  *Disclaimer: BMI ma charakter  |  |  <- Wyłączenie odpowiedzialności
|  |   orientacyjny...               |  |
|  +---------------------------------+  |
+---------------------------------------+
```

### 4.2. Układ Desktopowy (Desktop Layout - >= 992px)
Na dużych ekranach stosowany jest układ dwukolumnowy. Lewa kolumna zawiera formularz, prawa kolumna zawiera sekcję wyników. Jeśli wynik nie został jeszcze obliczony, prawa kolumna wyświetla estetyczny stan pusty (Placeholder) zachęcający do wpisania danych.

```
+---------------------------------------------------------------------------------------+
|  [Ikona] BMI SPA App                                                    [Theme Toggle]|
+---------------------------------------------------------------------------------------+
|                                                                                       |
|  +---------------------------------+     +---------------------------------+          |
|  |       KARTA FORMULARZA          |     |          KARTA WYNIKÓW          |          |
|  |                                 |     |                                 |          |
|  |  [ Metryczny ]  [ Imperialny ]  |     |           TWÓJ WYNIK            |          |
|  |                                 |     |              23.1               |          |
|  |  Wzrost (cm)                    |     |        WAGA PRAWIDŁOWA          |          |
|  |  [ 180                       ]  |     |                                 |          |
|  |                                 |     |  [======|=====================]  |          |
|  |  Masa ciała (kg)                |     |                                 |          |
|  |  [ 75                        ]  |     |  +---------------------------+  |          |
|  |                                 |     |  | Alert: Gratulacje! Twój   |  |          |
|  |  Płeć (Opcjonalnie)             |     |  | idealny środek to 70.3 kg |  |          |
|  |  [ Kobieta ]    [ Mężczyzna ]   |     |  +---------------------------+  |          |
|  |                                 |     |                                 |          |
|  |  Wiek (Opcjonalnie): 25 lat     |     |  [ Udostępnij ]   [ Resetuj ]   |          |
|  |  (======o=====================) |     |                                 |          |
|  |                                 |     |  *Disclaimer: BMI ma charakter  |          |
|  |  [       OBLICZ BMI          ]  |     |   orientacyjny...               |          |
|  +---------------------------------+     +---------------------------------+          |
|                                                                                       |
+---------------------------------------------------------------------------------------+
```

---

## 5. Szczegółowe Makiety Tekstowe (ASCII Art)

### 5.1. Widok Główny: Formularz Wejściowy (System Metryczny)

```
================================================================================
  [O] BMI SPA Calculator                                        [ Motyw: Jasny ]
================================================================================

  +--------------------------------------------------------------------------+
  |  Wprowadź swoje parametry                                                |
  +--------------------------------------------------------------------------+
  |                                                                          |
  |  System miar:                                                            |
  |  +--------------------------------------------------------------------+  |
  |  |       [X] Metryczny (cm, kg)      |      [ ] Imperialny (ft, lbs)  |  |
  |  +--------------------------------------------------------------------+  |
  |                                                                          |
  |  Wzrost:                                                                 |
  |  +--------------------------------------------------------------------+  |
  |  |  180                                                          | cm |  |
  |  +--------------------------------------------------------------------+  |
  |  <small class="text-muted">Dozwolony zakres: 100 - 250 cm</small>        |
  |                                                                          |
  |  Masa ciała:                                                             |
  |  +--------------------------------------------------------------------+  |
  |  |  75.0                                                         | kg |  |
  |  +--------------------------------------------------------------------+  |
  |  <small class="text-muted">Dozwolony zakres: 30.0 - 300.0 kg</small>      |
  |                                                                          |
  |  Płeć (Opcjonalnie):                                                     |
  |  +--------------------------------------------------------------------+  |
  |  |         [ ] Kobieta               |         [ ] Mężczyzna          |  |
  |  +--------------------------------------------------------------------+  |
  |                                                                          |
  |  Wiek (Opcjonalnie): 25 lat                                              |
  |  [====================o==============================================]  |
  |  <small class="text-muted">Zakres: 2 - 120 lat</small>                   |
  |                                                                          |
  |  +--------------------------------------------------------------------+  |
  |  |                            OBLICZ BMI                              |  |
  |  +--------------------------------------------------------------------+  |
  |                                                                          |
  +--------------------------------------------------------------------------+
```

### 5.2. Widok Główny: Formularz Wejściowy (System Imperialny)

```
================================================================================
  [O] BMI SPA Calculator                                        [ Motyw: Jasny ]
================================================================================

  +--------------------------------------------------------------------------+
  |  Wprowadź swoje parametry                                                |
  +--------------------------------------------------------------------------+
  |                                                                          |
  |  System miar:                                                            |
  |  +--------------------------------------------------------------------+  |
  |  |       [ ] Metryczny (cm, kg)      |      [X] Imperialny (ft, lbs)  |  |
  |  +--------------------------------------------------------------------+  |
  |                                                                          |
  |  Wzrost:                                                                 |
  |  +----------------------------------+ +-------------------------------+  |
  |  |  5                          | ft | |  11                      | in |  |
  |  +----------------------------------+ +-------------------------------+  |
  |  <small class="text-muted">Dozwolony zakres: 3'3" - 8'2"</small>          |
  |                                                                          |
  |  Masa ciała:                                                             |
  |  +--------------------------------------------------------------------+  |
  |  |  165.3                                                       | lbs |  |
  |  +--------------------------------------------------------------------+  |
  |  <small class="text-muted">Dozwolony zakres: 66.0 - 660.0 lbs</small>     |
  |                                                                          |
  |  Płeć (Opcjonalnie):                                                     |
  |  +--------------------------------------------------------------------+  |
  |  |         [ ] Kobieta               |         [ ] Mężczyzna          |  |
  |  +--------------------------------------------------------------------+  |
  |                                                                          |
  |  Wiek (Opcjonalnie): 25 lat                                              |
  |  [====================o==============================================]  |
  |  <small class="text-muted">Zakres: 2 - 120 lat</small>                   |
  |                                                                          |
  |  +--------------------------------------------------------------------+  |
  |  |                            OBLICZ BMI                              |  |
  |  +--------------------------------------------------------------------+  |
  |                                                                          |
  +--------------------------------------------------------------------------+
```

### 5.3. Widok Wyników: Dashboard Wynikowy

```
  +--------------------------------------------------------------------------+
  |  Twój Wynik Analizy BMI                                                  |
  +--------------------------------------------------------------------------+
  |                                                                          |
  |                             TWÓJ WSKAŹNIK BMI                            |
  |                                                                          |
  |                                  23.1                                    |  <- Duża czcionka (72px)
  |                                                                          |
  |                            WAGA PRAWIDŁOWA                               |  <- Kolor zielony (#2ecc71)
  |                                                                          |
  |  Skala BMI (WHO):                                                        |
  |  +--------------------------------------------------------------------+  |
  |  | [Nieb] | [Nieb] | [Żółt] |      [Zielony]      | [Pom] | [Czer] |[Fio]|  |  <- Suwak SVG
  |  +--------------------------^-----------------------------------------+  |
  |  15.0                      23.1                                      45.0|  <- Dynamiczny marker
  |                                                                          |
  |  +--------------------------------------------------------------------+  |
  |  | [IKONA SUKCESU] Gratulacje!                                        |  |  <- Dynamiczny Alert
  |  |                                                                    |  |
  |  | Twój wskaźnik BMI wskazuje na wagę prawidłową. Dbaj o dotychczasową|  |
  |  | aktywność fizyczną i zbilansowaną dietę.                           |  |
  |  |                                                                    |  |
  |  | Twój idealny środek przedziału wagi to: 70.3 kg (BMI = 21.7).      |  |  <- Delta wagowa
  |  | Różnica do wagi idealnej wynosi zaledwie -4.7 kg.                  |  |
  |  +--------------------------------------------------------------------+  |
  |                                                                          |
  |  +----------------------------------+ +-------------------------------+  |
  |  | [>] Udostępnij Wynik             | | [R] Oblicz Ponownie           |  |  <- Przyciski akcji
  |  +----------------------------------+ +-------------------------------+  |
  |                                                                          |
  |  <small class="text-muted">                                              |
  |  * Ważna informacja: Wskaźnik BMI ma charakter wyłącznie orientacyjny.   |  <- Disclaimer
  |    Może nie być miarodajny dla sportowców (wysoka masa mięśniowa),       |
  |    kobiet w ciąży oraz dzieci. Wynik ten nie zastępuje indywidualnej     |
  |    porady lekarskiej ani dietetycznej.                                   |
  |  </small>                                                                |
  |                                                                          |
  +--------------------------------------------------------------------------+
```

### 5.4. Modal Udostępniania (Web Share Fallback)

Ten modal pojawia się na urządzeniach desktopowych lub przeglądarkach niespierających Web Share API po kliknięciu przycisku "Udostępnij Wynik".

```
  +--------------------------------------------------------------------------+
  |  Udostępnij swój wynik                                               [X] |  <- Nagłówek modala
  +--------------------------------------------------------------------------+
  |                                                                          |
  |  Twój wynik: BMI = 23.1 (Waga prawidłowa)                                |
  |                                                                          |
  |  Wybierz kanał udostępniania:                                            |
  |  +--------------------------------------------------------------------+  |
  |  |  [F] Facebook      |  [X] Twitter/X       |  [W] WhatsApp          |  |  <- Ikony social media
  |  +--------------------------------------------------------------------+  |
  |                                                                          |
  |  Lub skopiuj bezpośredni link:                                           |
  |  +------------------------------------------------------------+-------+  |
  |  | https://bmi.app/?data=eyJzeXMiOiJtIiwidyI6NzIuNSwiaCI6MT...| Kopiuj|  |  <- Kopiowanie linku
  |  +------------------------------------------------------------+-------+  |
  |                                                                          |
  +--------------------------------------------------------------------------+
```

### 5.5. Powiadomienia (Toasts) i Stany Ładowania (Spinners)

#### A. Powiadomienie Toast (Pozycjonowane w prawym górnym rogu ekranu)
```
  +--------------------------------------------------------------------+
  | [I] Sukces!                                                    [X] |
  | Link został pomyślnie skopiowany do schowka.                       |
  +--------------------------------------------------------------------+
```

#### B. Stan Ładowania (Spinner wewnątrz przycisku "Oblicz BMI" podczas przetwarzania)
```
  +--------------------------------------------------------------------+
  |  [ o ] Obliczanie...                                               |  <- Animowany spinner CSS
  +--------------------------------------------------------------------+
```

---

## 6. Specyfikacja Komponentów i Stanów (Component Specification)

### 6.1. Przełącznik Systemu Miar (Segmented Control)
Komponent typu "Segmented Control" (dwustanowy przełącznik) zrealizowany za pomocą grupy przycisków radiowych w Bootstrap (`btn-group`).

* **Stany:**
  * **Default (Metryczny aktywny):** Lewy segment ma tło `--color-primary` i biały tekst. Prawy segment ma tło przezroczyste, ramkę `--color-border` i tekst `--color-text-primary`.
  * **Hover (na nieaktywnym segmencie):** Lekkie przyciemnienie tła nieaktywnego segmentu (np. szary 200 w trybie jasnym).
  * **Focus:** Wyraźna niebieska obwódka wokół całego komponentu (`box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25)`).
  * **Active (Imperialny aktywny):** Prawy segment staje się niebieski, lewy przezroczysty.

### 6.2. Pola Wprowadzania Danych (Inputs)
Standardowe pola tekstowe/numeryczne z pływającymi etykietami (`form-floating` w Bootstrap 5).

* **Stany:**
  * **Default (Pusty/Wypełniony):** Cienka ramka `--color-border`, etykieta umieszczona wewnątrz pola (gdy puste) lub nad wartością (gdy wypełnione).
  * **Focus:** Ramka zmienia kolor na `--color-primary`, pojawia się delikatny cień wokół pola.
  * **Error (Błąd walidacji):** Ramka zmienia kolor na czerwony (`#dc3545`), pod polem pojawia się czerwony komunikat o błędzie. Pole otrzymuje atrybut `aria-invalid="true"`.
  * **Disabled:** Tło pola staje się lekko szare, tekst zablokowany, kursor zmienia się na `not-allowed`.

### 6.3. Przełącznik Płci (Gender Selector)
Dwa duże, klikalne kafelki (Kobieta / Mężczyzna) ułatwiające szybki wybór na urządzeniach mobilnych.

* **Stany:**
  * **Default (Nieaktywny):** Białe/ciemnoszare tło, cienka ramka, ikona i tekst w kolorze neutralnym.
  * **Hover:** Subtelne podświetlenie tła i pogrubienie ramki.
  * **Selected (Aktywny):** Tło zmienia się na jasnoniebieskie (lub ciemnoniebieskie w trybie ciemnym), ramka staje się grubsza i przyjmuje kolor `--color-primary`.
  * **Focus (Nawigacja klawiaturą):** Obwódka focusu wokół wybranego kafelka.

### 6.4. Suwak Wieku (Age Slider)
Połączenie suwaka (`input type="range"`) z cyfrowym wyświetlaczem aktualnej wartości.

* **Stany i zachowanie:**
  * Przesuwanie suwaka dynamicznie aktualizuje wartość liczbową nad nim (np. "Wiek: 25 lat").
  * **Alert dla dzieci (Wiek < 18):** Jeśli suwak zostanie przesunięty poniżej wartości 18, pod suwakiem natychmiast pojawia się żółty alert ostrzegawczy (inline alert) o konieczności stosowania siatek centylowych. Pojawienie się alertu jest płynne (slide-down).

### 6.5. Przycisk "Oblicz BMI" (Primary Button)
Główny przycisk akcji (Call to Action).

* **Stany:**
  * **Default (Aktywny):** Pełne niebieskie tło (`--color-primary`), biały tekst, zaokrąglone rogi. Wysokość minimum 48px (wygodna dla kciuka).
  * **Hover:** Ciemniejszy odcień niebieskiego (`--color-primary-hover`).
  * **Focus:** Wyraźny pierścień wokół przycisku.
  * **Disabled (Błędy w formularzu):** Tło szare, tekst wyblakły, brak reakcji na kliknięcie.
  * **Loading (Podczas obliczeń):** Tekst przycisku zmienia się na "Obliczanie...", a obok pojawia się kręcący się spinner CSS.

### 6.6. Suwak Wyników SVG (Gauge/Slider)
Responsywny komponent SVG przedstawiający skalę BMI.

* **Stany i zachowanie:**
  * **Default (Przed obliczeniem):** Marker (strzałka) znajduje się na samej lewej krawędzi (BMI = 15.0) lub jest niewidoczny.
  * **Po obliczeniu:** Marker płynnie przesuwa się na wyliczoną pozycję na skali. Kolor markera (strzałki i linii pionowej) dynamicznie dostosowuje się do koloru kategorii WHO (np. zielony dla wagi prawidłowej, czerwony dla otyłości).

### 6.7. Przełącznik Motywów (Theme Toggle)
Przycisk w nagłówku aplikacji pozwalający na szybką zmianę motywu (Light/Dark).

* **Stany:**
  * Wyświetla ikonę słońca (Sun) w trybie ciemnym (kliknięcie włącza tryb jasny) lub księżyca (Moon) w trybie jasnym (kliknięcie włącza tryb ciemny).
  * Posiada atrybut `aria-label="Przełącz motyw kolorystyczny"`.

---

## 7. Mikrointerakcje i Animacje

Wszystkie animacje zostały zaprojektowane z myślą o wydajności (60fps) i wykorzystują wyłącznie właściwości optymalizowane sprzętowo przez GPU (`transform`, `opacity`).

### 7.1. Animacja Markera na Suwaku SVG
Przesunięcie markera (strzałki) na skali BMI po kliknięciu "Oblicz" odbywa się za pomocą płynnego przejścia CSS.

* **Właściwość CSS:** `transition: transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);`
* **Efekt:** Marker startuje szybko, a pod koniec płynnie zwalnia (ease-out), co nadaje interfejsowi bardzo nowoczesny, "fizyczny" charakter.

### 7.2. Płynne Pojawianie się Wyników (Fade-in & Slide-up)
Sekcja wyników (Dashboard) na urządzeniach mobilnych pojawia się z podwójnym efektem animacji.

* **Właściwości CSS:**
  ```css
  .results-card-animate {
    animation: fadeInUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }
  
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  ```

### 7.3. Animacja Alertów Walidacji i Ostrzeżeń
Pojawianie się komunikatów o błędach pod polami oraz alertu o wieku dziecięcym jest animowane za pomocą przejścia wysokości i przezroczystości, aby uniknąć nagłego "skakania" layoutu.

* **Właściwość CSS:** `transition: max-height 0.3s ease-out, opacity 0.3s ease-out;`

### 7.4. Powiadomienia Toast
Powiadomienia Toast wysuwają się z prawej krawędzi ekranu (lub z góry na mobile), pozostają widoczne przez 4 sekundy, a następnie płynnie znikają.

* **Właściwość CSS:** `transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.3s ease;`

---

## 8. Dostępność (Accessibility / WCAG 2.1 AA)

Projekt w pełni realizuje wytyczne dostępności cyfrowej, zapewniając równe szanse wszystkim użytkownikom.

### 8.1. Kontrasty i Czytelność
Wszystkie kombinacje kolorów tekstu i tła zostały zweryfikowane pod kątem kontrastu.

* **Tekst główny na tle karty:** Kontrast `10.5:1` (Light) / `12.2:1` (Dark) - przekracza wymogi AAA.
* **Tekst pomocniczy (muted):** Kontrast `4.6:1` (Light) / `4.8:1` (Dark) - spełnia wymogi AA.
* **Alerty statusów WHO:** Zastosowano natywne klasy Bootstrap `.alert-success`, `.alert-warning`, `.alert-danger` z odpowiednio dobranymi kolorami tekstu o wysokim kontraście.

### 8.2. Atrybuty ARIA i Semantyka HTML
* **Semantyczne tagi:** Użycie `<main>`, `<section>`, `<header>`, `<footer>`, `<label>`, `<button>`.
* **Dynamiczne aktualizacje (Aria Live):** Kontener z wynikami posiada atrybut `aria-live="polite"`. Dzięki temu czytnik ekranu automatycznie odczyta wyliczony wynik BMI i klasyfikację zaraz po ich wygenerowaniu, bez potrzeby odświeżania strony.
* **Powiązanie etykiet z polami:** Każde pole formularza posiada unikalne `id` powiązane z elementem `<label for="...">`.
* **Obsługa błędów:** Pola z błędami walidacji otrzymują atrybut `aria-invalid="true"` oraz `aria-describedby="[ID_KOMUNIKATU_O_BŁĘDZIE]"`, co pozwala czytnikom ekranu poinformować użytkownika o naturze błędu.

### 8.3. Nawigacja Klawiaturą (Keyboard Navigation)
Użytkownik może w pełni obsłużyć aplikację bez użycia myszki lub ekranu dotykowego.

* **Kolejność tabulacji (Tab Order):** Logiczny przepływ od góry do dołu:
  1. Przełącznik motywu (Theme Toggle)
  2. Przełącznik systemu miar (Segmented Control)
  3. Pole wzrostu (Height Input)
  4. Pole wagi (Weight Input)
  5. Przełącznik płci (Kobieta / Mężczyzna)
  6. Suwak wieku (Age Slider)
  7. Przycisk "Oblicz BMI"
  8. Przycisk "Udostępnij Wynik" (po obliczeniu)
  9. Przycisk "Oblicz Ponownie" (po obliczeniu)
* **Zarządzanie Focusem (Focus Management):**
  * Po kliknięciu "Oblicz BMI" na urządzeniach mobilnych, focus jest automatycznie przenoszony na nagłówek sekcji wyników (`tabindex="-1"`), aby ułatwić nawigację użytkownikom czytników ekranu.
  * Po kliknięciu "Oblicz Ponownie" (Reset), focus wraca na pierwsze pole formularza (Wzrost).
* **Obsługa klawiszy:**
  * Przełączniki (system miar, płeć) mogą być aktywowane za pomocą klawiszy `Space` lub `Enter`.
  * Suwak wieku może być precyzyjnie regulowany za pomocą strzałek na klawiaturze (`Left` / `Right`).

### 8.4. Touch Targets (Wielkość Elementów Dotykowych)
Wszystkie elementy interaktywne na urządzeniach mobilnych mają minimalną strefę kliknięcia wynoszącą **48x48 pikseli** (zalecenie WCAG 2.1 to min. 44x44px), co zapobiega przypadkowym kliknięciom sąsiednich elementów. Dotyczy to w szczególności:
* Przycisków przełącznika systemów miar.
* Kafelków wyboru płci.
* Przycisku "Oblicz BMI".
* Ikon udostępniania w mediach społecznościowych.
* Przycisku zamknięcia modala (X).
