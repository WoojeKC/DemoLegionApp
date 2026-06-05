# PLAN TESTÓW (TEST PLAN)
## Projekt: Nowoczesna Aplikacja BMI SPA (Wersja 1.0)

| Parametr | Szczegóły |
| :--- | :--- |
| **Nazwa Projektu** | BMI SPA Application |
| **Wersja Dokumentu** | 1.0.0 |
| **Status** | Gotowy do Realizacji |
| **Autor** | Starszy Inżynier QA / QA Lead (Senior Quality Assurance Engineer) |
| **Rola Odbiorcy** | Product Manager, Zespół Deweloperski, QA Team |
| **Data Utworzenia** | Październik 2023 |

---

## 1. Wstęp i Cel Dokumentu

Niniejszy dokument stanowi kompleksowy Plan Testów dla aplikacji **BMI SPA (Single Page Application) w wersji 1.0**. Celem dokumentu jest zdefiniowanie strategii testów, zakresu prac, środowiska testowego, narzędzi oraz szczegółowych przypadków testowych (funkcjonalnych i niefunkcjonalnych). 

Plan testów został opracowany na podstawie Dokumentu Wymagań Biznesowych (BRD), Dokumentu Projektu Systemowego (SDD) oraz Specyfikacji Interfejsu Użytkownika (UI Spec). Głównym celem procesu QA jest zapewnienie, że aplikacja działa bezbłędnie, jest wysoce wydajna, dostępna (zgodna z WCAG 2.1 AA) oraz odporna na błędy i próby manipulacji danymi.

---

## 2. Zakres Testów (Test Scope)

### 2.1. W zakresie testów (In Scope)
* **Testy Funkcjonalne (FR-01 do FR-13):**
  * Wybór i przełączanie systemów miar (metryczny vs imperialny).
  * Walidacja pól wejściowych (wzrost, waga, wiek, płeć) z uwzględnieniem wartości brzegowych i ekstremalnych.
  * Silnik obliczeniowy BMI (wzory matematyczne dla obu systemów, precyzja do 1 miejsca po przecinku).
  * Klasyfikacja WHO i dynamiczne przypisywanie kolorystyki oraz rekomendacji.
  * Kalkulacja delty wagowej do wagi idealnej (BMI = 21.7).
  * Automatyczna konwersja jednostek "w locie" bez czyszczenia formularza.
  * Resetowanie danych i powrót do stanu początkowego.
  * Udostępnianie wyników (Web Share API, fallback dla social media).
  * Odtwarzanie wyników z parametrów URL-Safe Base64 (dekodowanie, walidacja, obsługa błędów).
* **Testy Trwałości Danych (Persistence):**
  * Zapis i odczyt historii z IndexedDB (Dexie.js).
  * Obsługa LocalStorage (motyw, ID ostatniej kalkulacji).
  * Mechanizm fallback w przypadku zablokowanego IndexedDB (tryb incognito).
* **Testy Niefunkcjonalne:**
  * Responsywność (RWD) od 320px do 2560px (Mobile-First).
  * Wydajność (LCP < 1.5s, FID < 50ms, płynność animacji 60fps, rozmiar paczki < 150 KB).
  * Dostępność (WCAG 2.1 AA, czytniki ekranu, nawigacja klawiaturą, kontrasty).
  * Przełączanie motywów (Light/Dark Mode) i integracja z preferencjami systemowymi.
* **Testy Bezpieczeństwa:**
  * Zabezpieczenie przed atakami XSS przez parametry URL.
  * Odporność na manipulację parametrami URL (tampering).

### 2.2. Poza zakresem testów (Out of Scope)
* Konta użytkowników, rejestracja i logowanie (funkcjonalność planowana w v2.0).
* Zapisywanie historii wyników w chmurze / na serwerze (brak backendu w v1.0).
* Automatyczna interpretacja BMI dzieci na podstawie siatek centylowych (w v1.0 tylko ostrzeżenie tekstowe).
* Integracja z zewnętrznymi API fitness (Apple Health, Google Fit).

---

## 3. Strategia i Podejście do Testów (Testing Strategy)

### 3.1. Poziomy Testów
1. **Testy Jednostkowe (Unit Tests):** Skupione na module `calculator.js` (czyste funkcje matematyczne, konwersje jednostek, obliczenia delty) oraz `storage.js` (walidacja parametrów).
2. **Testy Integracyjne (Integration Tests):** Weryfikacja współpracy między `state.js`, `storage.js` (IndexedDB) oraz `app.js` (routing i parsowanie URL).
3. **Testy Systemowe (E2E / System Tests):** Kompleksowe testy przepływu użytkownika (User Flows) od wprowadzenia danych, przez obliczenie, po prezentację wyników i udostępnienie.
4. **Testy Niefunkcjonalne (Non-functional Tests):** Testy wydajnościowe (Lighthouse), dostępności (axe-core, czytniki ekranu) oraz RWD.

### 3.2. Środowisko Testowe
* **Urządzenia Mobilne (Fizyczne i Emulatory):**
  * iPhone 13/14 (iOS, Safari, Chrome)
  * Samsung Galaxy S21/S22 (Android, Chrome, Samsung Internet)
  * Emulacja w Chrome DevTools: Moto G Power, iPhone SE (szerokość 320px)
* **Urządzenia Desktopowe:**
  * Windows 11 (Chrome, Firefox, Edge)
  * macOS (Safari, Chrome)
* **Sieć:** Symulacja wolnego połączenia mobilnego (Fast 3G / Slow 4G) w celu weryfikacji budżetu wydajnościowego.

### 3.3. Narzędzia Testowe
* **Automatyzacja E2E / Integracyjna:** Playwright lub Cypress (do testów UI, IndexedDB, URL parsing).
* **Testy Jednostkowe:** Jest lub Vitest.
* **Wydajność:** Lighthouse, WebPageTest.
* **Dostępność (A11Y):** WAVE Extension, Axe DevTools, czytnik ekranu NVDA (Windows) / VoiceOver (macOS/iOS).
* **Bezpieczeństwo:** OWASP ZAP (podstawowy skan), ręczna manipulacja payloadem Base64.

---

## 4. Macierz Pokrycia Testowego (Test Coverage Matrix)

| ID Wymagania | Obszar Funkcjonalny | Typ Testu | Priorytet | Status Pokrycia |
| :--- | :--- | :--- | :--- | :--- |
| **FR-01** | Wybór Systemu Miar | Funkcjonalny / UI | Krytyczny (P1) | Pokryte (TC-01, TC-02) |
| **FR-02** | Wprowadzanie Wzrostu | Funkcjonalny / Walidacja | Krytyczny (P1) | Pokryte (TC-03, TC-04, TC-05) |
| **FR-03** | Wprowadzanie Masy Ciała | Funkcjonalny / Walidacja | Krytyczny (P1) | Pokryte (TC-06, TC-07, TC-08) |
| **FR-04** | Metadane Personalizacyjne | Funkcjonalny / UI | Wysoki (P2) | Pokryte (TC-09, TC-10) |
| **FR-05** | Dynamiczna Walidacja | Funkcjonalny / UI | Krytyczny (P1) | Pokryte (TC-11, TC-12) |
| **FR-06** | Wyzwalanie Obliczeń | Funkcjonalny / Integracyjny | Krytyczny (P1) | Pokryte (TC-13, TC-14) |
| **FR-07** | Przeliczanie Jednostek | Funkcjonalny / Logika | Wysoki (P2) | Pokryte (TC-15, TC-16) |
| **FR-08** | Prezentacja Liczbowa BMI | Funkcjonalny / UI | Krytyczny (P1) | Pokryte (TC-17) |
| **FR-09** | Wizualizacja Graficzna (SVG) | UI / Animacja | Średni (P3) | Pokryte (TC-18, TC-19) |
| **FR-10** | Interpretacja i Rekomendacja | Funkcjonalny / Logika | Wysoki (P2) | Pokryte (TC-20) |
| **FR-11** | Kontekst Wagowy (Delta) | Funkcjonalny / Logika | Wysoki (P2) | Pokryte (TC-21, TC-22, TC-23) |
| **FR-12** | Resetowanie Danych | Funkcjonalny / UI | Wysoki (P2) | Pokryte (TC-24) |
| **FR-13** | Udostępnianie i URL Base64 | Integracyjny / Bezpieczeństwo | Krytyczny (P1) | Pokryte (TC-25, TC-26, TC-27, TC-28) |
| **NFR-01-03**| Wydajność (LCP, FID, Bundle) | Niefunkcjonalny | Wysoki (P2) | Pokryte (TC-33) |
| **NFR-04-05**| RWD i Mobile-First | Niefunkcjonalny / UI | Krytyczny (P1) | Pokryte (TC-31, TC-32) |
| **NFR-06** | Dostępność (WCAG 2.1 AA) | Niefunkcjonalny / A11Y | Wysoki (P2) | Pokryte (TC-34, TC-35) |
| **NFR-07-08**| Bezpieczeństwo i Szyfrowanie | Niefunkcjonalny / Bezp. | Wysoki (P2) | Pokryte (TC-29, TC-30) |
| **SDD-2.1** | Trwałość IndexedDB & Fallback | Integracyjny / Systemowy | Wysoki (P2) | Pokryte (TC-36, TC-37) |
| **SDD-5.2** | Przełączanie Motywów | UI / UX | Średni (P3) | Pokryte (TC-38, TC-39) |

---

## 5. Szczegółowe Scenariusze i Przypadki Testowe

### Grupa 1: Moduł Wprowadzania Danych i Walidacji (FR-01 - FR-05)

#### TC-01: Domyślny stan formularza po pierwszym uruchomieniu
* **ID:** TC-01
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Czysta sesja przeglądarki (brak danych w `LocalStorage` i `IndexedDB`). Aplikacja uruchomiona pod adresem głównym.
* **Kroki:**
  1. Załaduj aplikację w przeglądarce.
  2. Zweryfikuj, który system miar jest zaznaczony.
  3. Zweryfikuj stan pól: Wzrost, Masa ciała, Płeć, Wiek.
  4. Zweryfikuj stan przycisku "Oblicz BMI".
  5. Zweryfikuj widoczność sekcji wyników.
* **Oczekiwany rezultat:**
  * Domyślnie wybrany jest system metryczny.
  * Pola Wzrost, Masa ciała są puste. Płeć nie jest zaznaczona. Suwak wieku ustawiony na wartość domyślną (lub pole puste).
  * Przycisk "Oblicz BMI" jest nieaktywny (`disabled`).
  * Sekcja wyników jest niewidoczna (na mobile) lub wyświetla stan pusty/placeholder (na desktopie).

#### TC-02: Przełączanie systemów miar (Etykiety i Jednostki)
* **ID:** TC-02
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Aplikacja uruchomiona, formularz pusty.
* **Kroki:**
  1. Kliknij segment "Imperialny (ft, lbs)" na przełączniku systemów miar.
  2. Zweryfikuj etykiety i jednostki dla pól wzrostu i wagi.
  3. Kliknij segment "Metryczny (cm, kg)".
  4. Zweryfikuj etykiety i jednostki ponownie.
* **Oczekiwany rezultat:**
  * Po przełączeniu na system imperialny: etykieta wzrostu zmienia się na "Stopy" i "Cale" (dwa osobne pola z jednostkami `ft` i `in`), a etykieta wagi na "Masa ciała" z jednostką `lbs`.
  * Po powrocie na system metryczny: widoczne jest jedno pole wzrostu z jednostką `cm` oraz jedno pole wagi z jednostką `kg`.
  * Przejście następuje natychmiastowo, bez przeładowania strony.

#### TC-03: Walidacja wartości brzegowych wzrostu - System Metryczny (Dolna i Górna Granica)
* **ID:** TC-03
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Wybrany system metryczny.
* **Kroki:**
  1. Wprowadź w pole Wzrost wartość `99` (poniżej minimum). Zweryfikuj komunikat i stan przycisku "Oblicz".
  2. Wprowadź w pole Wzrost wartość `100` (dokładnie minimum). Zweryfikuj brak błędu.
  3. Wprowadź w pole Wzrost wartość `250` (dokładnie maksimum). Zweryfikuj brak błędu.
  4. Wprowadź w pole Wzrost wartość `251` (powyżej maksimum). Zweryfikuj komunikat i stan przycisku "Oblicz".
* **Oczekiwany rezultat:**
  * Dla `99` cm: Wyświetla się czerwony komunikat inline: *"Wprowadź wzrost w zakresie 100 - 250 cm"*. Przycisk "Oblicz BMI" jest zablokowany. Pole ma `aria-invalid="true"`.
  * Dla `100` cm i `250` cm: Brak komunikatu o błędzie. Pole jest poprawne.
  * Dla `251` cm: Wyświetla się czerwony komunikat inline: *"Wprowadź wzrost w zakresie 100 - 250 cm"*. Przycisk "Oblicz BMI" jest zablokowany.

#### TC-04: Walidacja wartości brzegowych wzrostu - System Imperialny (Dolna i Górna Granica)
* **ID:** TC-04
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Wybrany system imperialny. Zakres dopuszczalny: 3'3" do 8'2" (łączna liczba cali: 39 do 98).
* **Kroki:**
  1. Wprowadź wzrost: Stopy = `3`, Cale = `2` (łącznie 38 cali - poniżej minimum). Zweryfikuj błąd.
  2. Wprowadź wzrost: Stopy = `3`, Cale = `3` (łącznie 39 cali - dokładnie minimum). Zweryfikuj brak błędu.
  3. Wprowadź wzrost: Stopy = `8`, Cale = `2` (łącznie 98 cali - dokładnie maksimum). Zweryfikuj brak błędu.
  4. Wprowadź wzrost: Stopy = `8`, Cale = `3` (łącznie 99 cali - powyżej maksimum). Zweryfikuj błąd.
  5. Wprowadź w pole Cale wartość `12` (niepoprawna wartość dla cali, powinna być < 12). Zweryfikuj reakcję systemu.
* **Oczekiwany rezultat:**
  * Dla 3'2" (38 in) oraz 8'3" (99 in): Wyświetla się czerwony komunikat o błędzie: *"Wprowadź wzrost w zakresie 3'3" - 8'2""*. Przycisk "Oblicz" jest zablokowany.
  * Dla 3'3" (39 in) oraz 8'2" (98 in): Brak błędów walidacji.
  * Dla Cale = `12`: System powinien automatycznie przeliczyć to na +1 stopę i 0 cali LUB wyświetlić błąd walidacji pola cali (zakres 0-11).

#### TC-05: Walidacja typów danych w polu Wzrost (Znaki niepoprawne)
* **ID:** TC-05
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Wybrany system metryczny.
* **Kroki:**
  1. Spróbuj wpisać w pole Wzrost litery `abc`.
  2. Spróbuj wpisać znaki specjalne `@#$`.
  3. Spróbuj wpisać wartość zmiennoprzecinkową `175.5` (krok dla systemu metrycznego to 1 cm).
  4. Spróbuj wkleić (Ctrl+V) ciąg `180abc`.
* **Oczekiwany rezultat:**
  * System blokuje wpisywanie znaków niebędących cyframi (pole typu `number` lub `inputmode="numeric"`).
  * Wpisanie `175.5` powoduje błąd walidacji (oczekiwana liczba całkowita) lub automatyczne zaokrąglenie do `176` (zgodnie z krokiem `step="1"`).
  * Wklejenie `180abc` skutkuje odfiltrowaniem liter i pozostawieniem samej liczby `180` lub wywołaniem błędu walidacji.

#### TC-06: Walidacja wartości brzegowych masy ciała - System Metryczny
* **ID:** TC-06
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Wybrany system metryczny. Zakres dopuszczalny: 30.0 do 300.0 kg. Krok: 0.1 kg.
* **Kroki:**
  1. Wprowadź wagę `29.9` kg. Zweryfikuj błąd.
  2. Wprowadź wagę `30.0` kg. Zweryfikuj brak błędu.
  3. Wprowadź wagę `300.0` kg. Zweryfikuj brak błędu.
  4. Wprowadź wagę `300.1` kg. Zweryfikuj błąd.
  5. Wprowadź wagę `70.55` kg (dwie liczby po przecinku). Zweryfikuj zaokrąglenie lub błąd.
* **Oczekiwany rezultat:**
  * Dla `29.9` kg i `300.1` kg: Wyświetla się czerwony komunikat: *"Wprowadź wagę w zakresie 30.0 - 300.0 kg"*. Przycisk "Oblicz" zablokowany.
  * Dla `30.0` kg i `300.0` kg: Brak błędów.
  * Dla `70.55` kg: System zaokrągla wartość do `70.6` kg (zgodnie z krokiem 0.1) lub akceptuje ją, ale silnik obliczeniowy zaokrągla ją wewnętrznie.

#### TC-07: Walidacja wartości brzegowych masy ciała - System Imperialny
* **ID:** TC-07
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Wybrany system imperialny. Zakres dopuszczalny: 66.0 do 660.0 lbs. Krok: 0.1 lbs.
* **Kroki:**
  1. Wprowadź wagę `65.9` lbs. Zweryfikuj błąd.
  2. Wprowadź wagę `66.0` lbs. Zweryfikuj brak błędu.
  3. Wprowadź wagę `660.0` lbs. Zweryfikuj brak błędu.
  4. Wprowadź wagę `660.1` lbs. Zweryfikuj błąd.
* **Oczekiwany rezultat:**
  * Dla `65.9` lbs i `660.1` lbs: Wyświetla się czerwony komunikat: *"Wprowadź wagę w zakresie 66.0 - 660.0 lbs"*. Przycisk "Oblicz" zablokowany.
  * Dla `66.0` lbs i `660.0` lbs: Brak błędów.

#### TC-08: Zabezpieczenie przed ekstremalnymi wartościami (R-02)
* **ID:** TC-08
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Wybrany system metryczny.
* **Kroki:**
  1. Spróbuj wkleić w pole wagi wartość `999999999999`.
  2. Zweryfikuj, czy pole ogranicza liczbę znaków (np. max 6 znaków).
  3. Zweryfikuj, czy layout formularza nie uległ rozbiciu.
* **Oczekiwany rezultat:**
  * System automatycznie przycina wpis do wartości maksymalnej (`300.0` kg) lub blokuje wprowadzanie tak długiego ciągu znaków.
  * Layout pozostaje nienaruszony, brak błędów w konsoli JS.

#### TC-09: Walidacja pola Wiek (Opcjonalne, zakres 2 - 120 lat)
* **ID:** TC-09
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Aplikacja uruchomiona.
* **Kroki:**
  1. Pozostaw pole Wiek puste. Wprowadź poprawny wzrost i wagę. Zweryfikuj, czy przycisk "Oblicz" jest aktywny.
  2. Wprowadź wiek `1` (poniżej minimum). Zweryfikuj błąd.
  3. Wprowadź wiek `2` (dokładnie minimum). Zweryfikuj brak błędu.
  4. Wprowadź wiek `120` (dokładnie maksimum). Zweryfikuj brak błędu.
  5. Wprowadź wiek `121` (powyżej maksimum). Zweryfikuj błąd.
* **Oczekiwany rezultat:**
  * Pole jest opcjonalne – puste pole nie blokuje obliczeń.
  * Dla wieku `1` i `121` lat: Wyświetla się błąd walidacji: *"Wprowadź wiek w zakresie 2 - 120 lat"*. Przycisk "Oblicz" zablokowany.
  * Dla wieku `2` i `120` lat: Brak błędów.

#### TC-10: Ostrzeżenie dla wieku dziecięcego (Siatki Centylowe)
* **ID:** TC-10
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Aplikacja uruchomiona.
* **Kroki:**
  1. Wprowadź w pole Wiek wartość `17`.
  2. Zweryfikuj, czy pod polem wieku pojawił się żółty alert ostrzegawczy.
  3. Zmień wartość wieku na `18`.
  4. Zweryfikuj, czy alert zniknął.
  5. Zmień wartość wieku na `2`.
  6. Zweryfikuj, czy alert pojawił się ponownie.
* **Oczekiwany rezultat:**
  * Dla wieku z zakresu `2 - 17` lat dynamicznie (on change) pojawia się żółty alert: *"Uwaga: Interpretacja BMI dla dzieci i młodzieży (poniżej 18 roku życia) wymaga zastosowania siatek centylowych..."*.
  * Dla wieku `>= 18` lat alert natychmiast znika.

#### TC-11: Dynamiczna walidacja przycisku "Oblicz BMI"
* **ID:** TC-11
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Aplikacja uruchomiona.
* **Kroki:**
  1. Otwórz stronę (pola puste) -> Sprawdź stan przycisku "Oblicz".
  2. Wpisz poprawny wzrost, pozostaw wagę pustą -> Sprawdź stan przycisku.
  3. Wpisz poprawną wagę, ale wprowadź niepoprawny wzrost (np. `50` cm) -> Sprawdź stan przycisku.
  4. Wpisz poprawny wzrost i poprawną wagę -> Sprawdź stan przycisku.
* **Oczekiwany rezultat:**
  * Przycisk "Oblicz BMI" posiada atrybut `disabled` w krokach 1, 2, 3.
  * Przycisk staje się aktywny (atrybut `disabled` usunięty) natychmiast po poprawnym wypełnieniu obu wymaganych pól (krok 4).

#### TC-12: Walidacja pola Płeć (Opcjonalne)
* **ID:** TC-12
* **Priorytet:** Średni (P3)
* **Warunki wstępne:** Aplikacja uruchomiona.
* **Kroki:**
  1. Pozostaw płeć niewybraną. Wykonaj obliczenie. Zweryfikuj sukces.
  2. Kliknij kafelek "Kobieta". Zweryfikuj stan wizualny.
  3. Kliknij kafelek "Mężczyzna". Zweryfikuj, czy stan "Kobieta" został odznaczony.
* **Oczekiwany rezultat:**
  * Wybór płci jest opcjonalny.
  * Kafelki działają jak przyciski radiowe (wybór jest wzajemnie wykluczający się). Wybrany kafelek ma wyraźne obramowanie i tło `--color-primary`.

---

### Grupa 2: Silnik Matematyczny i Obliczenia (FR-06, FR-08, FR-10, FR-11)

#### TC-13: Obliczenie BMI dla systemu metrycznego (Weryfikacja dokładności)
* **ID:** TC-13
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Wybrany system metryczny.
* **Kroki:**
  1. Wprowadź Wzrost = `180` cm, Masa = `75` kg. Kliknij "Oblicz BMI".
  2. Oblicz ręcznie: $BMI = 75 / (1.8)^2 = 75 / 3.24 = 23.148...$
  3. Zweryfikuj wyświetloną wartość w Dashboardzie.
* **Oczekiwany rezultat:**
  * Wyświetlona wartość to dokładnie `23.1` (zaokrąglenie do jednego miejsca po przecinku).

#### TC-14: Obliczenie BMI dla systemu imperialnego (Weryfikacja dokładności)
* **ID:** TC-14
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Wybrany system imperialny.
* **Kroki:**
  1. Wprowadź Wzrost: Stopy = `5`, Cale = `11` (łącznie 71 cali). Masa = `165.3` lbs. Kliknij "Oblicz BMI".
  2. Oblicz ręcznie: $BMI = (165.3 / (71)^2) \times 703 = (165.3 / 5041) \times 703 = 0.03279... \times 703 = 23.05...$
  3. Zweryfikuj wyświetloną wartość w Dashboardzie.
* **Oczekiwany rezultat:**
  * Wyświetlona wartość to dokładnie `23.1` (zaokrąglenie do jednego miejsca po przecinku).

#### TC-15: Wyzwalanie obliczeń onBlur (Semi-automatic trigger)
* **ID:** TC-15
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Aplikacja uruchomiona.
* **Kroki:**
  1. Wprowadź Wzrost = `170` cm.
  2. Wprowadź Masa = `60` kg.
  3. Kliknij myszką poza formularz (utrata focusu przez pole wagi).
  4. Zweryfikuj, czy obliczenie zostało wywołane automatycznie bez klikania przycisku "Oblicz".
* **Oczekiwany rezultat:**
  * Obliczenie zostaje wyzwolone automatycznie po utracie focusu (on blur) przez ostatnie wymagane pole, pod warunkiem, że wszystkie dane są poprawne. Dashboard Wynikowy staje się widoczny.

---

### Grupa 3: Automatyczna Konwersja Jednostek (FR-07)

#### TC-16: Konwersja z systemu metrycznego na imperialny
* **ID:** TC-16
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Wprowadzone dane w systemie metrycznym: Wzrost = `180` cm, Masa = `75.0` kg. Wynik BMI wyliczony (`23.1`).
* **Kroki:**
  1. Kliknij przełącznik "System Imperialny".
  2. Zweryfikuj wartości w polach Wzrost (Stopy, Cale) oraz Masa (Funty).
  3. Zweryfikuj, czy wynik BMI uległ zmianie lub zresetowaniu.
* **Oczekiwany rezultat:**
  * Wzrost `180` cm zostaje przeliczony na `5` ft i `11` in (180 / 30.48 = 5.905 ft -> 5 ft i 11 in).
  * Masa `75.0` kg zostaje przeliczona na `165.3` lbs (75 * 2.20462 = 165.346 -> zaokrąglone do 165.3).
  * Wynik BMI pozostaje bez zmian (`23.1`). Formularz nie został wyczyszczony.

#### TC-17: Konwersja z systemu imperialnego na metryczny
* **ID:** TC-17
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Wprowadzone dane w systemie imperialnym: Wzrost: Stopy = `5`, Cale = `11`, Masa = `165.3` lbs.
* **Kroki:**
  1. Kliknij przełącznik "System Metryczny".
  2. Zweryfikuj wartości w polach Wzrost (cm) oraz Masa (kg).
* **Oczekiwany rezultat:**
  * Wzrost zostaje przeliczony na `180` cm (5 * 30.48 + 11 * 2.54 = 152.4 + 27.94 = 180.34 -> zaokrąglone do 180).
  * Masa zostaje przeliczona na `75.0` kg (165.3 * 0.453592 = 74.978 -> zaokrąglone do 75.0).
  * Wynik BMI pozostaje stabilny.

---

### Grupa 4: Prezentacja Wyników i Interakcja (FR-09, FR-12)

#### TC-18: Klasyfikacja WHO i kolorystyka UI (Weryfikacja wszystkich 8 klas)
* **ID:** TC-18
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** System metryczny. Wzrost stały = `100` cm (ułatwia dobór wagi do BMI, bo $BMI = Masa / 1^2 = Masa$).
* **Kroki:**
  1. Wprowadź wagę `15.5` kg (BMI = 15.5). Oblicz. Zweryfikuj klasę i kolor.
  2. Wprowadź wagę `16.5` kg (BMI = 16.5). Oblicz. Zweryfikuj klasę i kolor.
  3. Wprowadź wagę `18.0` kg (BMI = 18.0). Oblicz. Zweryfikuj klasę i kolor.
  4. Wprowadź wagę `22.0` kg (BMI = 22.0). Oblicz. Zweryfikuj klasę i kolor.
  5. Wprowadź wagę `27.0` kg (BMI = 27.0). Oblicz. Zweryfikuj klasę i kolor.
  6. Wprowadź wagę `32.0` kg (BMI = 32.0). Oblicz. Zweryfikuj klasę i kolor.
  7. Wprowadź wagę `37.0` kg (BMI = 37.0). Oblicz. Zweryfikuj klasę i kolor.
  8. Wprowadź wagę `42.0` kg (BMI = 42.0). Oblicz. Zweryfikuj klasę i kolor.
* **Oczekiwany rezultat:**
  * **BMI 15.5:** "Wyczerpanie / Wytrenowanie skrajne", kolor Jasnoniebieski (`#3498db`).
  * **BMI 16.5:** "Wychodzenie z normy / Wychudzenie", kolor Niebieski (`#2980b9`).
  * **BMI 18.0:** "Niedowaga", kolor Żółty (`#f1c40f`).
  * **BMI 22.0:** "Waga prawidłowa", kolor Zielony (`#2ecc71`).
  * **BMI 27.0:** "Nadwaga", kolor Pomarańczowy (`#e67e22`).
  * **BMI 32.0:** "Otyłość I stopnia", kolor Jasnoczerwony (`#e74c3c`).
  * **BMI 37.0:** "Otyłość II stopnia (kliniczna)", kolor Czerwony (`#c0392b`).
  * **BMI 42.0:** "Otyłość III stopnia (skrajna)", kolor Ciemny fiolet (`#8e44ad`).
  * Kolorystyka jest aplikowana do tekstu klasyfikacji oraz tła alertu rekomendacji.

#### TC-19: Pozycjonowanie i animacja markera na suwaku SVG
* **ID:** TC-19
* **Priorytet:** Średni (P3)
* **Warunki wstępne:** Aplikacja uruchomiona.
* **Kroki:**
  1. Wprowadź dane dające BMI = `15.0` (skrajna lewa granica skali). Oblicz. Zweryfikuj pozycję markera.
  2. Wprowadź dane dające BMI = `30.0` (środek skali). Oblicz. Zweryfikuj pozycję markera.
  3. Wprowadź dane dające BMI = `45.0` (skrajna prawa granica skali). Oblicz. Zweryfikuj pozycję markera.
  4. Zweryfikuj płynność ruchu markera (brak szarpania, płynne przejście CSS).
* **Oczekiwany rezultat:**
  * Dla BMI = 15.0: Marker znajduje się na pozycji X = 0 (lub blisko lewej krawędzi).
  * Dla BMI = 30.0: Marker znajduje się dokładnie w połowie szerokości paska SVG (X = 500).
  * Dla BMI = 45.0: Marker znajduje się na pozycji X = 1000 (prawa krawędź).
  * Ruch markera jest płynny, animacja trwa ok. 0.8s z efektem ease-out (cubic-bezier).

#### TC-20: Kalkulacja Delty Wagowej - Scenariusz A (Niedowaga)
* **ID:** TC-20
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Wybrany system metryczny. Wzrost = `180` cm, Masa = `55` kg (BMI = 17.0 - Niedowaga).
* **Kroki:**
  1. Kliknij "Oblicz BMI".
  2. Zweryfikuj treść komunikatu o delcie wagowej.
  3. Oblicz ręcznie: Waga idealna (BMI = 21.7) dla 180 cm to: $21.7 \times (1.8)^2 = 21.7 \times 3.24 = 70.308$ kg. Delta: $55 - 70.3 = -15.3$ kg.
* **Oczekiwany rezultat:**
  * Wyświetla się komunikat: *"Aby osiągnąć idealną masę ciała (BMI = 21.7), powinieneś przybrać na wadze 15.3 kg"* (wartość bezwzględna z delty). Waga idealna wskazana jako `70.3` kg.

#### TC-21: Kalkulacja Delty Wagowej - Scenariusz B (Nadwaga)
* **ID:** TC-21
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Wybrany system metryczny. Wzrost = `180` cm, Masa = `90` kg (BMI = 27.8 - Nadwaga).
* **Kroki:**
  1. Kliknij "Oblicz BMI".
  2. Zweryfikuj treść komunikatu o delcie wagowej.
  3. Oblicz ręcznie: Waga idealna = `70.3` kg. Delta: $90 - 70.3 = 19.7$ kg.
* **Oczekiwany rezultat:**
  * Wyświetla się komunikat: *"Aby osiągnąć idealną masę ciała (BMI = 21.7), powinieneś zrzucić 19.7 kg"*.

#### TC-22: Kalkulacja Delty Wagowej - Scenariusz C (Waga prawidłowa)
* **ID:** TC-22
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Wybrany system metryczny. Wzrost = `180` cm, Masa = `72` kg (BMI = 22.2 - Waga prawidłowa).
* **Kroki:**
  1. Kliknij "Oblicz BMI".
  2. Zweryfikuj treść komunikatu o delcie wagowej.
  3. Oblicz ręcznie: Waga idealna = `70.3` kg. Różnica: $72 - 70.3 = 1.7$ kg.
* **Oczekiwany rezultat:**
  * Wyświetla się komunikat gratulacyjny: *"Twoja waga jest idealna! Utrzymuj obecną masę ciała. Twój idealny środek przedziału to 70.3 kg (różnica wynosi zaledwie 1.7 kg)"*.

#### TC-23: Resetowanie danych (Przycisk "Oblicz ponownie")
* **ID:** TC-23
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Wyświetlony wynik BMI dla wprowadzonych danych.
* **Kroki:**
  1. Kliknij przyciski "Oblicz ponownie" lub "Resetuj".
  2. Zweryfikuj stan pól formularza.
  3. Zweryfikuj widoczność sekcji wyników.
  4. Zweryfikuj, gdzie znajduje się focus klawiatury.
* **Oczekiwany rezultat:**
  * Wszystkie pola formularza zostają wyczyszczone do wartości domyślnych (puste).
  * Sekcja wyników zostaje płynnie ukryta (animacja fade-out).
  * Strona nie przeładowuje się (brak odświeżenia karty).
  * Focus klawiatury zostaje automatycznie przeniesiony na pierwsze pole formularza (Wzrost).

---

### Grupa 5: Dekodowanie i Walidacja Parametrów URL-Safe Base64 (FR-13 / US-4.2)

#### TC-24: Generowanie poprawnego linku udostępniania
* **ID:** TC-24
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Wprowadzone dane: System metryczny, Wzrost = `178` cm, Masa = `72.5` kg, Płeć = Mężczyzna (`m`), Wiek = `28` lat. Wynik obliczony.
* **Kroki:**
  1. Kliknij przycisk "Udostępnij Wynik".
  2. Skopiuj wygenerowany link ze schowka lub modala fallback.
  3. Zweryfikuj strukturę parametru `?data=` w URL.
  4. Zdekoduj ręcznie parametr Base64 i sprawdź strukturę JSON.
* **Oczekiwany rezultat:**
  * Link ma postać: `https://[domena]/?data=[URL_SAFE_BASE64]`.
  * Zdekodowany JSON ma strukturę: `{"sys":"m","w":72.5,"h":178,"g":"m","a":28}`.
  * W ciągu Base64 nie występują znaki `+`, `/` ani `=` (zastąpione odpowiednio przez `-`, `_` i usunięte dopełnienie).

#### TC-25: Odtworzenie poprawnego wyniku z linku URL-Safe Base64
* **ID:** TC-25
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Czysta sesja przeglądarki. Przygotowany link: `https://bmi.app/?data=eyJzeXMiOiJtIiwidyI6NzIuNSwiaCI6MTc4LCJnIjoibSIsImEiOjI4fQ` (zakodowany JSON z TC-24).
* **Kroki:**
  1. Wklej link w pasek adresu przeglądarki i zatwierdź.
  2. Zweryfikuj, czy formularz został automatycznie wypełniony.
  3. Zweryfikuj, czy Dashboard Wynikowy wyświetlił się automatycznie bez klikania "Oblicz".
  4. Zweryfikuj obecność powiadomienia Toast o wczytaniu danych.
* **Oczekiwany rezultat:**
  * Formularz wypełniony: System metryczny, Wzrost = 178 cm, Waga = 72.5 kg, Płeć = Mężczyzna, Wiek = 28 lat.
  * Dashboard wyświetla się natychmiast po załadowaniu strony z wynikiem BMI = `22.9`.
  * Wyświetla się Toast: *"Wczytano wynik z udostępnionego linku!"*.

#### TC-26: Obsługa uszkodzonego/niepoprawnego ciągu Base64 w URL
* **ID:** TC-26
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Przygotowany uszkodzony link (np. ucięty Base64): `https://bmi.app/?data=eyJzeXMiOiJtIiwidyI6NzIuNSwiaCI6MTc4LCJnIjoibSIsImEiOjI4` (brak końcówki).
* **Kroki:**
  1. Załaduj uszkodzony link w przeglądarce.
  2. Zweryfikuj zachowanie aplikacji (czy nie wystąpił "White Screen of Death").
  3. Zweryfikuj stan formularza i obecność komunikatu ostrzegawczego.
* **Oczekiwany rezultat:**
  * Aplikacja ładuje się poprawnie w stanie domyślnym (pusty formularz metryczny).
  * W konsoli nie ma nieobsłużonych błędów blokujących działanie aplikacji.
  * Wyświetla się Toast ostrzegawczy: *"Nie udało się odtworzyć wyniku z linku – parametry są niepoprawne."*

#### TC-27: Próba wstrzyknięcia niepoprawnych zakresów danych przez URL (Tampering)
* **ID:** TC-27
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Przygotowany zmodyfikowany JSON z wartościami poza zakresem: `{"sys":"m","w":9999,"h":178,"g":"m","a":28}`. Zakodowany do URL-Safe Base64: `eyJzeXMiOiJtIiwidyI6OTk5OSwiaCI6MTc4LCJnIjoibSIsImEiOjI4fQ`.
* **Kroki:**
  1. Załaduj link `https://bmi.app/?data=eyJzeXMiOiJtIiwidyI6OTk5OSwiaCI6MTc4LCJnIjoibSIsImEiOjI4fQ` w przeglądarce.
  2. Zweryfikuj, czy aplikacja odrzuciła te dane.
* **Oczekiwany rezultat:**
  * Funkcja `validateDecodedParams` wykrywa, że waga `9999` kg wykracza poza dopuszczalny zakres (30-300 kg).
  * Dane z URL są ignorowane. Aplikacja uruchamia się w stanie domyślnym (pusty formularz).
  * Wyświetla się Toast ostrzegawczy o niepoprawnych parametrach.

#### TC-28: Próba ataku XSS przez parametry URL (Security Test)
* **ID:** TC-28
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Przygotowany złośliwy JSON próbujący wstrzyknąć skrypt do pola tekstowego (np. płeć): `{"sys":"m","w":70,"h":170,"g":"<script>alert('XSS')</script>","a":25}`. Zakodowany do Base64.
* **Kroki:**
  1. Załaduj wygenerowany link w przeglądarce.
  2. Zweryfikuj, czy skrypt JS został wykonany (czy pojawił się alert).
  3. Zweryfikuj, czy złośliwy kod został wyrenderowany w DOM jako kod HTML, czy jako bezpieczny tekst.
* **Oczekiwany rezultat:**
  * Skrypt NIE uruchamia się.
  * Walidacja `validateDecodedParams` odrzuca obiekt, ponieważ wartość pola `g` nie jest równa `"m"` ani `"f"`.
  * Nawet w przypadku braku walidacji, moduł `ui.js` używa wyłącznie `textContent` / `innerText`, co uniemożliwia wykonanie wstrzykniętego kodu HTML/JS.

---

### Grupa 6: Trwałość Danych (IndexedDB, LocalStorage) oraz Fallback (Tryb Incognito)

#### TC-29: Zapis kalkulacji do IndexedDB i odczyt przy ponownym wejściu
* **ID:** TC-29
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Czysta baza danych.
* **Kroki:**
  1. Wprowadź dane: Wzrost = `175` cm, Masa = `70` kg. Kliknij "Oblicz BMI".
  2. Zamknij kartę przeglądarki.
  3. Otwórz ponownie aplikację pod adresem głównym (bez parametrów URL).
  4. Zweryfikuj, czy aplikacja automatycznie wczytała ostatnie obliczenie.
  5. Otwórz DevTools -> Application -> IndexedDB -> `BMISpaDB` -> `calculations` i sprawdź obecność rekordu.
* **Oczekiwany rezultat:**
  * Po ponownym wejściu aplikacja odczytuje `bmi_last_calc_id` z `LocalStorage`, pobiera rekord z `IndexedDB` i automatycznie wypełnia formularz oraz prezentuje wyniki.
  * W bazie danych `BMISpaDB` znajduje się dokładnie jeden rekord z poprawnym znacznikiem czasu i parametrami.

#### TC-30: Fallback w trybie Incognito (Zablokowane IndexedDB)
* **ID:** TC-30
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Przeglądarka uruchomiona w trybie prywatnym / incognito (gdzie IndexedDB rzuca błąd zapisu/odczytu).
* **Kroki:**
  1. Otwórz aplikację w oknie Incognito.
  2. Wprowadź poprawne dane i kliknij "Oblicz BMI".
  3. Zweryfikuj, czy obliczenie zakończyło się sukcesem.
  4. Zweryfikuj obecność powiadomienia Toast o trybie prywatnym.
  5. Zweryfikuj, czy w konsoli nie ma krytycznych błędów blokujących UI.
* **Oczekiwany rezultat:**
  * Aplikacja działa poprawnie w trybie in-memory. Obliczenie zostaje wykonane, Dashboard Wynikowy wyświetla się prawidłowo.
  * Wyświetla się Toast: *"Działasz w trybie prywatnym. Historia obliczeń nie zostanie zapisana po zamknięciu karty."*
  * Brak błędów typu `Uncaught (in promise) DOMException` w konsoli.

---

### Grupa 7: Testy Niefunkcjonalne (RWD, Wydajność, Dostępność, Motywy)

#### TC-31: Responsywność (RWD) - Układ Mobilny vs Desktopowy
* **ID:** TC-31
* **Priorytet:** Krytyczny (P1)
* **Warunki wstępne:** Aplikacja uruchomiona.
* **Kroki:**
  1. Zmniejsz szerokość okna do `320px` (np. iPhone SE). Zweryfikuj układ (powinien być jednokolumnowy, sekcja wyników ukryta przed obliczeniem).
  2. Wykonaj obliczenie na mobile. Zweryfikuj, czy strona płynnie przewija się do wyników.
  3. Zwiększ szerokość okna do `1024px` (Desktop). Zweryfikuj układ (dwukolumnowy, formularz po lewej, wyniki po prawej).
  4. Zweryfikuj, czy nie pojawia się poziomy pasek przewijania (horizontal scrollbar) na żadnej rozdzielczości.
* **Oczekiwany rezultat:**
  * Pełna responsywność. Na szerokości < 992px układ jest pionowy (jednokolumnowy). Na >= 992px dwukolumnowy.
  * Brak błędów typu overflow (teksty mieszczą się w kontenerach, suwak SVG skaluje się płynnie).

#### TC-32: Wielkość elementów dotykowych (Touch Targets)
* **ID:** TC-32
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Urządzenie mobilne.
* **Kroki:**
  1. Zweryfikuj wielkość przycisków przełącznika systemów miar, kafelków płci, przycisku "Oblicz" oraz ikon social media.
* **Oczekiwany rezultat:**
  * Wszystkie elementy interaktywne mają minimalną strefę kliknięcia wynoszącą **48x48 pikseli** (zgodnie z NFR-04 i standardem WCAG).

#### TC-33: Wydajność i Budżet Wydajnościowy (Lighthouse)
* **ID:** TC-33
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Wersja produkcyjna aplikacji (zminifikowany kod, kompresja Gzip/Brotli).
* **Kroki:**
  1. Uruchom audyt Lighthouse w trybie "Mobile" z profilowaniem sieci (Moto G4 na wolnym 3G/4G).
  2. Zweryfikuj wskaźnik LCP (Largest Contentful Paint).
  3. Zweryfikuj wskaźnik FID (First Input Delay) / TBT (Total Blocking Time).
  4. Zweryfikuj całkowity rozmiar pobieranych zasobów (Bundle Size).
* **Oczekiwany rezultat:**
  * LCP < 1.5 sekundy (cel: < 1.0s).
  * FID < 50 ms (TBT < 150ms).
  * Całkowity rozmiar paczki JS/CSS przy pierwszym załadowaniu < 150 KB (skompresowany).
  * Wynik Performance w Lighthouse >= 95.

#### TC-34: Dostępność (WCAG 2.1 AA) - Kontrasty i Semantyka
* **ID:** TC-34
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Aplikacja uruchomiona. Zainstalowane narzędzie Axe DevTools.
* **Kroki:**
  1. Uruchom automatyczny skan dostępności za pomocą Axe DevTools dla trybu jasnego i ciemnego.
  2. Zweryfikuj współczynnik kontrastu tekstów (szczególnie disclaimera i tekstów pomocniczych).
  3. Zweryfikuj obecność atrybutów `alt` dla grafik oraz powiązań `<label>` z `<input>`.
* **Oczekiwany rezultat:**
  * Zero krytycznych błędów dostępności.
  * Współczynnik kontrastu dla wszystkich tekstów wynosi minimum 4.5:1 (dla dużych tekstów min. 3:1).
  * Wszystkie pola formularza są poprawnie powiązane z etykietami za pomocą atrybutu `for`.

#### TC-35: Nawigacja klawiaturą i czytniki ekranu (A11Y)
* **ID:** TC-35
* **Priorytet:** Wysoki (P2)
* **Warunki wstępne:** Uruchomiony czytnik ekranu (np. NVDA lub VoiceOver). Myszka odłączona.
* **Kroki:**
  1. Użyj klawisza `Tab`, aby przejść przez cały formularz. Zweryfikuj widoczność wskaźnika focusu (focus ring).
  2. Użyj klawisza `Space` / `Enter`, aby przełączyć system miar oraz wybrać płeć.
  3. Użyj strzałek `Left` / `Right`, aby zmienić wiek na suwaku.
  4. Wypełnij dane, przejdź do przycisku "Oblicz BMI" i kliknij `Enter`.
  5. Zweryfikuj, czy czytnik ekranu automatycznie odczytał wygenerowany wynik (dzięki `aria-live="polite"`).
* **Oczekiwany rezultat:**
  * Każdy element interaktywny posiada wyraźny, widoczny focus ring.
  * Możliwe jest pełne obsłużenie aplikacji za pomocą samej klawiatury.
  * Po obliczeniu, czytnik ekranu natychmiast anonsuje wynik, np.: *"Twój wynik to 23.1, Waga prawidłowa"*.

#### TC-36: Przełączanie motywów (Light/Dark Mode)
* **ID:** TC-36
* **Priorytet:** Średni (P3)
* **Warunki wstępne:** Aplikacja uruchomiona.
* **Kroki:**
  1. Kliknij przycisk przełącznika motywu w nagłówku.
  2. Zweryfikuj, czy atrybut `data-bs-theme` na elemencie `<html>` zmienił się na `dark`.
  3. Zweryfikuj, czy kolory tła i tekstów zmieniły się zgodnie ze specyfikacją UI (sekcja 2.1).
  4. Odśwież stronę. Zweryfikuj, czy wybrany motyw został zapamiętany.
* **Oczekiwany rezultat:**
  * Kliknięcie przełącza motyw natychmiastowo.
  * Wybrany motyw (`light` lub `dark`) jest zapisywany w `LocalStorage` pod kluczem `bmi_theme` i poprawnie odtwarzany po odświeżeniu strony.

#### TC-37: Integracja motywu z preferencjami systemowymi
* **ID:** TC-37
* **Priorytet:** Średni (P3)
* **Warunki wstępne:** Brak zapisanego motywu w `LocalStorage` (czysta sesja).
* **Kroki:**
  1. Ustaw motyw systemu operacyjnego / przeglądarki na Ciemny (Dark).
  2. Załaduj aplikację. Zweryfikuj motyw.
  3. Zmień motyw systemu na Jasny (Light).
  4. Zweryfikuj, czy aplikacja automatycznie dostosowała motyw w locie.
* **Oczekiwany rezultat:**
  * Aplikacja poprawnie reaguje na zapytanie mediów `(prefers-color-scheme: dark)` i automatycznie dostosowuje motyw, jeśli użytkownik nie dokonał wcześniej ręcznego wyboru.

---

## 6. Zarządzanie Defektami i Raportowanie

### 6.1. Szablon Raportu o Błędzie (Bug Report Template)

W przypadku wykrycia błędu podczas testów, należy zarejestrować zgłoszenie według poniższego szablonu:

```markdown
### [BUG] Krótki, jednoznaczny tytuł (Co, Gdzie, W jakich warunkach)
**ID błędu:** BUG-XXX
**Priorytet:** [Krytyczny (P1) / Wysoki (P2) / Średni (P3) / Niski (P4)]
**Dotkliwość (Severity):** [Blocker / Critical / Major / Minor / Trivial]
**Środowisko:** [np. Chrome v118, Windows 11 / Safari, iOS 17]

#### Opis błędu:
[Krótki opis problemu i jego wpływu na użytkownika/system]

#### Kroki do reprodukcji:
1. Wejdź na stronę główną aplikacji.
2. Przełącz system miar na Imperialny.
3. Wprowadź wzrost: Stopy = 5, Cale = 11.
4. Wprowadź wagę: 165.3 lbs.
5. Kliknij przycisk "Oblicz BMI".

#### Rezultat faktyczny (Actual Result):
[Co się stało? np. Wynik BMI wynosi 24.5 zamiast 23.1, w konsoli pojawia się błąd NaN]

#### Rezultat oczekiwany (Expected Result):
[Co powinno się stać? np. Wynik BMI powinien wynosić dokładnie 23.1]

#### Załączniki / Logi:
- [Zrzut ekranu / Nagranie wideo]
- [Logi z konsoli przeglądarki]
```

### 6.2. Klasyfikacja Defektów (Severity vs Priority)

* **Krytyczny (P1) / Blocker:** Błędy uniemożliwiające korzystanie z głównej funkcjonalności aplikacji (np. silnik obliczeniowy zwraca błędne wyniki, aplikacja zawiesza się, błędy bezpieczeństwa XSS, brak możliwości obliczenia BMI).
* **Wysoki (P2) / Major:** Błędy znacznie utrudniające korzystanie z aplikacji lub naruszające kluczowe wymagania niefunkcjonalne (np. brak walidacji pól, niedziałająca konwersja jednostek, niedziałający zapis w IndexedDB, rażące naruszenie kontrastów WCAG).
* **Średni (P3) / Minor:** Błędy o mniejszym znaczeniu funkcjonalnym, usterki UI/UX (np. drobne przesunięcia layoutu, niepłynna animacja suwaka SVG, brak zapamiętywania motywu).
* **Niski (P4) / Trivial:** Literówki w tekstach, drobne sugestie kosmetyczne niebędące błędami technicznymi.
