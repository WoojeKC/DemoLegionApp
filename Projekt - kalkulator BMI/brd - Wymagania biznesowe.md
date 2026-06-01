# DOKUMENT WYMAGAŃ BIZNESOWYCH (BRD)
## Projekt: Nowoczesna Aplikacja BMI SPA (Wersja 1.0)

| Parametr | Szczegóły |
| :--- | :--- |
| **Nazwa Projektu** | BMI SPA Application |
| **Wersja Dokumentu** | 1.0.0 |
| **Status** | Gotowy do Przeglądu (Ready for Review) |
| **Autor** | Starszy Analityk Biznesowy (Senior Business Analyst) |
| **Rola Odbiorcy** | Product Manager, Zespół Deweloperski, QA |
| **Data Utworzenia** | Październik 2023 |

---

## 1. Wstęp i Podsumowanie Menedżerskie (Executive Summary)

### 1.1. Wizja i Cel Główny
Projekt zakłada stworzenie nowoczesnej, wysoce responsywnej aplikacji webowej typu **Single Page Application (SPA)** służącej do szybkiego obliczania, interpretacji oraz monitorowania wskaźnika masy ciała (BMI - Body Mass Index). Aplikacja ma działać błyskawicznie, bez przeładowywania strony, dostarczając użytkownikowi natychmiastową wartość informacyjną i angażujące wrażenia wizualne (UX).

Głównym celem biznesowym jest stworzenie skutecznego narzędzia wizerunkowo-marketingowego, które przyciągnie użytkowników zainteresowanych zdrowym stylem życia, dietetyką oraz aktywnością fizyczną, stanowiąc kluczowy element lejka marketingowego (generowanie leadów i ruchu).

### 1.2. Cele Biznesowe i Wskaźniki KPI
Wdrożenie aplikacji ma na celu realizację następujących celów biznesowych:
1. **Generowanie leadów i ruchu (Traffic Generation):** Pozyskanie nowego, organicznego ruchu na stronach powiązanych z marką poprzez wiralny charakter narzędzia.
2. **Wysoka konwersja (Engagement):** Intuicyjny interfejs ma zapewnić wskaźnik ukończenia interakcji (wykonania pełnego obliczenia) na poziomie **minimum 85%** użytkowników uruchamiających aplikację.
3. **Wiralność (Virality):** Ułatwienie użytkownikom dzielenia się swoimi wynikami lub samą aplikacją w mediach społecznościowych, co obniży koszt pozyskania użytkownika (CAC).
4. **Retencja (Retention):** Przygotowanie solidnego fundamentu architektonicznego pod moduł zapisu historii (planowany w wersji 2.0), który skłoni użytkowników do regularnych powrotów.

---

## 2. Grupa Docelowa i Persony (User Personas)

Aplikacja została zaprojektowana z myślą o trzech głównych typach użytkowników:

### Persona 1: Jan Kowalski – Amator Zdrowego Stylu Życia
* **Profil:** Chce szybko i bez rejestracji sprawdzić, czy jego waga mieści się w normie.
* **Potrzeby:** Prosty język (brak skomplikowanego żargonu medycznego), jasne wskazówki wizualne (kolory, intuicyjny suwak), brak konieczności zakładania konta.
* **Kluczowe wymaganie:** Natychmiastowy wynik po wpisaniu podstawowych danych.

### Persona 2: Anna Nowak – Świadoma Sportowiec / Osoba na Diecie
* **Profil:** Regularnie kontroluje parametry swojego ciała, dba o szczegóły.
* **Potrzeby:** Wysoka precyzja obliczeń (miejsca po przecinku), obsługa alternatywnych jednostek miar (np. imperialnych podczas korzystania z zagranicznych planów treningowych), jasne określenie celów (dokładna informacja, ile kilogramów brakuje do wagi idealnej).
* **Kluczowe wymaganie:** Precyzyjny moduł "Delty Wagowej" oraz bezbłędne przeliczanie jednostek.

### Persona 3: Tomasz Wiśniewski – Użytkownik Mobile-Only
* **Profil:** Korzysta z aplikacji wyłącznie na smartfonie, często w drodze, na siłowni lub podczas zakupów.
* **Potrzeby:** Błyskawiczne ładowanie strony, duże i łatwo klikalne elementy interfejsu (obsługa jednym kciukiem), brak zbędnych bloków tekstu rozpraszających uwagę.
* **Kluczowe wymaganie:** Pełna responsywność (RWD), zgodność z zasadami Mobile-First, wysoka wydajność na łączach mobilnych (3G/4G).

---

## 3. Architektura i Kontekst Technologiczny (SPA)

Aplikacja musi zostać zrealizowana w architekturze **Single Page Application (SPA)** przy użyciu nowoczesnego frameworka frontendowego (np. React, Vue.js lub Angular).

### Kluczowe Założenia Architektoniczne:
1. **Client-side Rendering (CSR):** Cała logika obliczeniowa oraz renderowanie widoków odbywa się po stronie przeglądarki użytkownika. Serwer dostarcza jedynie statyczne pliki (HTML, JS, CSS, zasoby graficzne).
2. **Brak Przeładowań Strony (Zero Page Reloads):** Przejścia pomiędzy wprowadzaniem danych, prezentacją wyniku a sekcjami informacyjnymi muszą odbywać się płynnie, za pomocą natychmiastowych zmian stanu aplikacji (State Management).
3. **Lokalne Zarządzanie Stanem:** Dane wejściowe i wyniki są przechowywane w pamięci podręcznej aplikacji. W celu poprawy UX, aplikacja powinna opcjonalnie zapisywać ostatnio wprowadzone parametry w `localStorage` przeglądarki, aby użytkownik nie musiał wpisywać ich ponownie przy kolejnej wizycie.

---

## 4. Dekompozycja Wymagań na Epiki i User Stories

### EPIC 1: Konfiguracja i Wprowadzanie Danych (Data Input & Configuration)

#### US-1.1: Wybór Systemu Miar (FR-01)
* **Jako:** Użytkownik aplikacji (zarówno preferujący system metryczny, jak i imperialny)
* **Chcę:** Mieć możliwość łatwego przełączania się pomiędzy systemem metrycznym (kg, cm) a imperialnym (lbs, ft/in)
* **Aby:** Wprowadzać dane w jednostkach, które są dla mnie najbardziej naturalne i zrozumiałe.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Domyślny stan:** Po pierwszym uruchomieniu aplikacji domyślnie wybrany jest system metryczny (metry, centymetry, kilogramy).
  2. **Element UI:** Przełącznik systemów miar (np. Segmented Control lub Switch) jest widoczny na samej górze formularza wejściowego.
  3. **Wielkość elementu:** Przełącznik spełnia wymóg minimalnej wielkości dotykowej (minimum 44x44 px).
  4. **Zmiana etykiet:** Przełączenie systemu natychmiastowo zmienia etykiety i jednostki przy polach formularza (cm/kg na ft, in/lbs) bez przeładowania strony.

#### US-1.2: Wprowadzanie Wzrostu (FR-02)
* **Jako:** Użytkownik aplikacji
* **Chcę:** Wprowadzić swój wzrost w wybranym systemie miar
* **Aby:** System mógł użyć tej wartości do obliczenia wskaźnika BMI.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **System Metryczny:**
     * Widoczne jest jedno pole numeryczne oznaczone jako "Wzrost".
     * Jednostka: `cm`.
     * Dozwolony zakres wartości: od `100` do `250` cm włącznie.
     * Krok walidacji (step): `1` cm (tylko liczby całkowite).
  2. **System Imperialny:**
     * Widoczne są dwa osobne pola numeryczne: "Stopy" (`ft`) oraz "Cale" (`in`).
     * Dozwolony zakres łączny: od `3'3"` (3 stopy, 3 cale) do `8'2"` (8 stóp, 2 cale) włącznie.
     * Przelicznik zakresu imperialnego na metryczny: 3'3" = ok. 99 cm, 8'2" = ok. 249 cm.
  3. **Wprowadzanie danych:** Pola numeryczne na urządzeniach mobilnych automatycznie wywołują klawiaturę numeryczną (atrybut `inputmode="numeric"` lub `type="number"`).

#### US-1.3: Wprowadzanie Masy Ciała (FR-03)
* **Jako:** Użytkownik aplikacji
* **Chcę:** Wprowadzić swoją aktualną wagę w wybranym systemie miar
* **Aby:** System mógł precyzyjnie obliczyć mój wskaźnik BMI.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **System Metryczny:**
     * Widoczne jest pole numeryczne oznaczone jako "Masa ciała" lub "Waga".
     * Jednostka: `kg`.
     * Dozwolony zakres wartości: od `30.0` do `300.0` kg włącznie.
     * Krok walidacji (step): `0.1` kg (obsługa liczb zmiennoprzecinkowych).
  2. **System Imperialny:**
     * Widoczne jest pole numeryczne oznaczone jako "Masa ciała" lub "Waga".
     * Jednostka: `lbs`.
     * Dozwolony zakres wartości: od `66.0` do `660.0` lbs włącznie.
     * Krok walidacji (step): `0.1` lbs.

#### US-1.4: Metadane Personalizacyjne i Ostrzeżenie dla Wieku (FR-04)
* **Jako:** Użytkownik (w tym rodzic sprawdzający BMI dziecka)
* **Chcę:** Opcjonalnie podać swoją płeć oraz wiek
* **Aby:** Otrzymać bardziej spersonalizowany komunikat lub dowiedzieć się o ograniczeniach interpretacji wyniku dla dzieci.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Opcjonalność:** Pola płci i wieku są wyraźnie oznaczone jako "Opcjonalne". Brak ich wypełnienia nie blokuje możliwości obliczenia BMI.
  2. **Wybór Płci:** Dostępne opcje to "Kobieta" i "Mężczyzna" (np. w formie czytelnych kafelków lub przełącznika).
  3. **Wprowadzanie Wieku:** Pole numeryczne lub suwak w zakresie od `2` do `120` lat.
  4. **Ostrzeżenie dla Wieku Dziecięcego (Siatki Centylowe):**
     * Jeśli wprowadzony wiek wynosi **poniżej 18 lat** (zakres 2–17 lat), system natychmiast wyświetla pod polem wieku wyraźne, żółte ostrzeżenie (inline alert):
       > **Uwaga:** Interpretacja BMI dla dzieci i młodzieży (poniżej 18 roku życia) wymaga zastosowania siatek centylowych. Standardowa klasyfikacja dla dorosłych może być niemiarodajna.
     * Alert pojawia się dynamicznie w locie (on change) i znika, gdy wiek zostanie zmieniony na >= 18 lat.

#### US-1.5: Dynamiczna Walidacja Formularza (FR-05)
* **Jako:** Użytkownik aplikacji
* **Chcę:** Widzieć natychmiastowe błędy walidacji, jeśli wpiszę niepoprawne dane
* **Aby:** Uniknąć wysyłania błędnych formularzy i wiedzieć, jak poprawić wpisane wartości.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Walidacja w locie (Inline Validation):** Walidacja następuje przy każdej zmianie wartości (on change) lub przy opuszczeniu pola (on blur).
  2. **Komunikaty o błędach:** Jeśli wartość wykracza poza zakres określony w US-1.2 lub US-1.3, pod danym polem pojawia się czerwony, czytelny komunikat (np. *"Wprowadź wzrost w zakresie 100 - 250 cm"*).
  3. **Stan przycisku "Oblicz":** Przycisk "Oblicz BMI" staje się nieaktywny (`disabled`), dopóki wszystkie wymagane i wypełnione pola nie przejdą pomyślnie walidacji.
  4. **Zabezpieczenie przed ekstremalnymi wartościami (R-02):** System uniemożliwia wpisanie wartości dłuższych niż dopuszczalne (np. max 6 znaków) i automatycznie ogranicza wpis do wartości maksymalnej z zakresu, jeśli użytkownik spróbuje wkleić ekstremalną liczbę.

#### US-1.6: Automatyczna Konwersja Jednostek (FR-07)
* **Jako:** Użytkownik, który wprowadził już dane do formularza
* **Chcę:** Aby po przełączeniu systemu miar moje dane zostały automatycznie przeliczone
* **Aby:** Nie tracić wpisanych informacji i zobaczyć ich odpowiedniki w drugim systemie.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Wyzwalacz:** Kliknięcie przełącznika systemu miar (US-1.1) przy niepustych polach wzrostu/wagi.
  2. **Przeliczenie Wzrostu:**
     * Z metrycznego na imperialny: `cm` przeliczane na stopy i cale (np. 180 cm -> 5 stóp, 11 cali). Zaokrąglenie do najbliższego cala.
     * Z imperialnego na metryczny: stopy i cale przeliczane na `cm` (np. 5'11" -> 180 cm). Zaokrąglenie do najbliższej liczby całkowitej.
  3. **Przeliczenie Wagi:**
     * Z metrycznego na imperialny: `kg` przeliczane na `lbs` (mnożnik `2.20462`). Zaokrąglenie do 1 miejsca po przecinku.
     * Z imperialnego na metryczny: `lbs` przeliczane na `kg` (mnożnik `0.453592`). Zaokrąglenie do 1 miejsca po przecinku.
  4. **Zachowanie stanu:** Formularz nie jest czyszczony, a nowo przeliczone wartości są od razu widoczne w polach wejściowych.

---

### EPIC 2: Silnik Obliczeniowy i Logika Biznesowa (Calculation Engine & Business Logic)

#### US-2.1: Obliczanie Wskaźnika BMI (FR-06, FR-08)
* **Jako:** Użytkownik aplikacji
* **Chcę:** Aby system obliczył mój wskaźnik BMI na podstawie wprowadzonych danych
* **Aby:** Poznać swój wynik liczbowy.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Wyzwalanie obliczeń:** Obliczenie następuje natychmiast po kliknięciu przycisku "Oblicz BMI" LUB automatycznie "w locie" po poprawnym wypełnieniu wszystkich wymaganych pól i utracie focusu (on blur) przez ostatnie edytowane pole.
  2. **Wzór Metryczny:**
     $$BMI = \frac{masa\_ciala\_[kg]}{(wzrost\_[m])^2}$$
     *Uwaga:* Wzrost w formularzu podawany jest w `cm`, więc przed podstawieniem do wzoru musi zostać podzielony przez 100.
  3. **Wzór Imperialny:**
     $$BMI = \frac{masa\_ciala\_[lbs]}{(wzrost\_[in])^2} \times 703$$
     *Uwaga:* Wzrost w stopach (`ft`) i calach (`in`) musi zostać sprowadzony do łącznej liczby cali: $wzrost\_[in] = (ft \times 12) + in$.
  4. **Precyzja wyniku:** Wynik końcowy BMI musi być zaokrąglony i wyświetlony z dokładnością do **jednego miejsca po przecinku** (np. `24.2`).

#### US-2.2: Klasyfikacja Wyniku i Przypisanie Kolorystyki (Kryteria WHO)
* **Jako:** Użytkownik aplikacji
* **Chcę:** Aby mój wynik został przyporządkowany do odpowiedniej kategorii medycznej i oznaczony kolorem
* **Aby:** Szybko zinterpretować, czy mój wynik jest prawidłowy.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Klasyfikacja:** System przypisuje wyliczone BMI do jednej z 8 klas zgodnie z poniższą tabelą:

| Zakres BMI | Klasyfikacja medyczna | Kolorystyka UI | Kod Hex |
| :--- | :--- | :--- | :--- |
| **< 16.0** | Wyczerpanie / Wytrenowanie skrajne | Jasnoniebieski | `#3498db` |
| **16.0 – 16.9** | Wychodzenie z normy / Wychudzenie | Niebieski | `#2980b9` |
| **17.0 – 18.4** | Niedowaga | Żółty | `#f1c40f` |
| **18.5 – 24.9** | **Waga prawidłowa** | **Zielony** | `#2ecc71` |
| **25.0 – 29.9** | Nadwaga | Pomarańczowy | `#e67e22` |
| **30.0 – 34.9** | Otyłość I stopnia | Jasnoczerwony | `#e74c3c` |
| **35.0 – 39.9** | Otyłość II stopnia (kliniczna) | Czerwony | `#c0392b` |
| **>= 40.0** | Otyłość III stopnia (skrajna) | Ciemny fiolet/bordowy | `#8e44ad` |

  2. **Zastosowanie kolorystyki:** Kolor powiązany z klasą musi zostać dynamicznie zaaplikowany do elementów wizualnych (tekst wyniku, tło alertu rekomendacji, wskaźnik na suwaku).

#### US-2.3: Kalkulacja Delty Wagowej do Wagi Idealnej (FR-11)
* **Jako:** Użytkownik z nadwagą, niedowagą lub wagą prawidłową
* **Chcę:** Dowiedzieć się, ile dokładnie kilogramów (lub funtów) muszę zrzucić lub przybrać, aby osiągnąć idealny środek przedziału wagi prawidłowej
* **Aby:** Mieć jasny, mierzalny cel zdrowotny.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Punkt odniesienia:** Idealny środek przedziału wagi prawidłowej jest zdefiniowany jako **BMI = 21.7**.
  2. **Wzór na wagę idealną ($W_{idealna}$):**
     * System metryczny: $W_{idealna} = 21.7 \times (wzrost\_[m])^2$ (wynik w kg).
     * System imperialny: $W_{idealna} = \frac{21.7 \times (wzrost\_[in])^2}{703}$ (wynik w lbs).
  3. **Kalkulacja Delty ($\Delta$):**
     $$\Delta = Masa\_aktualna - W_{idealna}$$
  4. **Prezentacja Wyniku (3 scenariusze):**
     * **Scenariusz A (Niedowaga - BMI < 18.5):** System wyświetla komunikat: *"Aby osiągnąć idealną masę ciała (BMI = 21.7), powinieneś przybrać na wadze **X kg** (lub **Y lbs**)"*.
     * **Scenariusz B (Nadwaga/Otyłość - BMI >= 25.0):** System wyświetla komunikat: *"Aby osiągnąć idealną masę ciała (BMI = 21.7), powinieneś zrzucić **X kg** (lub **Y lbs**)"*.
     * **Scenariusz C (Waga prawidłowa - 18.5 <= BMI < 25.0):** System wyświetla komunikat gratulacyjny: *"Twoja waga jest idealna! Utrzymuj obecną masę ciała. Twój idealny środek przedziału to **W_idealna kg/lbs** (różnica wynosi zaledwie **X kg/lbs**)"*.
  5. **Precyzja:** Wartości delty oraz wagi idealnej są zaokrąglane do 1 miejsca po przecinku.

---

### EPIC 3: Prezentacja Wyników i Interakcja (Results Presentation & Interaction)

#### US-3.1: Liczbowy i Tekstowy Dashboard Wynikowy (FR-08, FR-10)
* **Jako:** Użytkownik aplikacji
* **Chcę:** Zobaczyć swój wynik BMI w postaci czytelnego podsumowania liczbowego i tekstowego
* **Aby:** Łatwo zrozumieć interpretację mojego wyniku.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Prezentacja Liczbowa:** Wynik BMI (np. **24.2**) jest wyświetlany bardzo dużą, pogrubioną czcionką w centralnej części sekcji wyników.
  2. **Etykieta Klasyfikacji:** Bezpośrednio pod liczbą wyświetlana jest nazwa klasyfikacji medycznej (np. "WAGA PRAWIDŁOWA") w kolorze odpowiadającym danej klasie (zgodnie z tabelą z US-2.2).
  3. **Dynamiczna Rekomendacja:** Wyświetlany jest spersonalizowany opis tekstowy, zależny od wyniku oraz opcjonalnie od płci (jeśli została podana).
     * *Przykład dla wagi prawidłowej:* "Twój wskaźnik BMI wskazuje na wagę prawidłową. Gratulacje! Dbaj o dotychczasową aktywność fizyczną i zbilansowaną dietę."
     * *Przykład dla nadwagi:* "Twój wskaźnik BMI wskazuje na nadwagę. Zalecamy zwiększenie aktywności fizycznej oraz konsultację z dietetykiem w celu optymalizacji nawyków żywieniowych."
  4. **Dostępność:** Kontener z wynikami posiada atrybut `aria-live="polite"`, aby czytniki ekranu odczytały wynik natychmiast po jego wygenerowaniu.

#### US-3.2: Wizualizacja Graficzna (Gage/Slider) (FR-09)
* **Jako:** Użytkownik (szczególnie wzrokowiec)
* **Chcę:** Zobaczyć swój wynik na kolorowej, graficznej skali (suwaku)
* **Aby:** Wizualnie ocenić, jak daleko znajduję się od innych przedziałów wagowych.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Skala Kolorystyczna:** Komponent wizualny przedstawia ciągły lub segmentowy pasek odzwierciedlający pełen zakres BMI (od <16 do >=40) z zachowaniem kolorów z tabeli WHO.
  2. **Dynamiczny Wskaźnik (Marker):** Strzałka lub pionowa linia wskazuje precyzyjnie wyliczoną wartość na skali.
  3. **Płynna Animacja:** Po kliknięciu "Oblicz", wskaźnik przesuwa się płynnie od lewej krawędzi (lub od poprzedniego wyniku) do aktualnego punktu docelowego. Animacja musi działać w 60 klatkach na sekundę (60fps).
  4. **Responsywność:** Pasek skali dopasowuje swoją szerokość do ekranu urządzenia (RWD), nie powodując przewijania poziomego.

#### US-3.3: Resetowanie Danych i Powrót do Stanu Początkowego (FR-12)
* **Jako:** Użytkownik aplikacji
* **Chcę:** Mieć możliwość szybkiego wyczyszczenia formularza i wyników jednym kliknięciem
* **Aby:** Wprowadzić dane innej osoby lub zacząć od nowa bez konieczności odświeżania strony.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Przycisk Reset:** Widoczny w sekcji wyników lub bezpośrednio pod formularzem jako przycisk "Resetuj" lub "Oblicz ponownie".
  2. **Brak przeładowania:** Reset następuje natychmiastowo w pamięci aplikacji, bez przeładowania karty przeglądarki (zachowanie SPA).
  3. **Czyszczenie stanu:** Wszystkie pola formularza (wzrost, waga, wiek, płeć) zostają przywrócone do wartości domyślnych/pustych. Sekcja wyników zostaje płynnie ukryta (np. za pomocą animacji fade-out).
  4. **Focus:** Po zresetowaniu, focus klawiatury automatycznie wraca do pierwszego pola formularza (Wybór systemu miar lub Wzrost).

#### US-3.4: Wyłączenie Odpowiedzialności (Disclaimer) (R-01)
* **Jako:** Użytkownik aplikacji / Właściciel biznesowy
* **Chcę:** Widzieć stałą informację o ograniczeniach wskaźnika BMI
* **Aby:** Zrozumieć kontekst medyczny i uchronić markę przed odpowiedzialnością prawną za błędną samodiagnozę.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Widoczność:** Tekst wyłączenia odpowiedzialności (Disclaimer) jest stale widoczny w widoku prezentacji wyników, bezpośrednio pod wykresem/suwakiem.
  2. **Treść komunikatu:**
     > **Ważna informacja:** Wskaźnik BMI ma charakter wyłącznie orientacyjny. Może nie być miarodajny dla sportowców (wysoka masa mięśniowa), kobiet w ciąży oraz dzieci. Wynik ten nie zastępuje indywidualnej porady lekarskiej ani dietetycznej.
  3. **Stylistyka:** Tekst napisany mniejszą czcionką (np. `font-size: 0.85rem`), w stonowanym kolorze (np. szarym), zapewniającym jednak minimalny kontrast WCAG AA (4.5:1).

---

### EPIC 4: Wiralność i Udostępnianie (Virality & Sharing)

#### US-4.1: Udostępnianie Wyniku przez Web Share API i Social Media (FR-13)
* **Jako:** Użytkownik zadowolony ze swojego wyniku
* **Chcę:** Łatwo udostępnić informację o aplikacji lub moim wyniku znajomym
* **Aby:** Pochwalić się osiągnięciem lub polecić przydatne narzędzie.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Web Share API (Urządzenia Mobilne):**
     * Na urządzeniach wspierających Web Share API (głównie smartfony) kliknięcie głównego przycisku "Udostępnij" wywołuje systemowe menu udostępniania systemu Android/iOS.
     * Przesyłana treść: *"Sprawdź swój wskaźnik BMI w nowoczesnej aplikacji! Mój wynik to [Wartość BMI] ([Klasyfikacja]). Oblicz swoje BMI tutaj: [Unikalny Link]"*.
  2. **Ikony Social Media (Fallback & Desktop):**
     * Na urządzeniach desktopowych lub jako alternatywa widoczne są dedykowane, łatwo klikalne ikony: Facebook, Twitter/X, WhatsApp.
     * Kliknięcie ikony otwiera nowe okno (pop-up) z gotowym do opublikowania postem zawierającym unikalny link i krótki tekst zachęcający.
  3. **Wymiary:** Ikony społecznościowe mają rozmiar minimum 44x44 px (strefa kliknięcia).

#### US-4.2: Odtwarzanie Wyniku z Parametrów URL (FR-13)
* **Jako:** Odbiorca udostępnionego linku
* **Chcę:** Po kliknięciu w link zobaczyć od razu wyliczony wynik nadawcy bez konieczności ponownego wpisywania danych
* **Aby:** Szybko zrozumieć, czym podzielił się ze mną znajomy.
* **Kryteria Akceptacji (Acceptance Criteria):**
  1. **Struktura Linku:** Link generowany podczas udostępniania (US-4.1) zawiera parametry zapytania (Query Parameters) kodujące wprowadzone dane, np.:
     * System metryczny: `https://bmi.app/?sys=m&w=70&h=175&g=f&a=25` (gdzie `sys` = system, `w` = waga w kg, `h` = wzrost w cm, `g` = płeć, `a` = wiek).
     * System imperialny: `https://bmi.app/?sys=i&w=154&h_ft=5&h_in=9&g=m&a=30`.
  2. **Obsługa wejścia (Routing/Parsing):** Przy załadowaniu aplikacji, skrypt sprawdza obecność parametrów w URL.
  3. **Automatyczne renderowanie:** Jeśli parametry są obecne i poprawne (przechodzą walidację zakresów), aplikacja automatycznie wypełnia formularz tymi danymi, wykonuje obliczenie i prezentuje Dashboard Wynikowy od razu po załadowaniu strony.
  4. **Brak zapisu w bazie:** Cały proces odbywa się po stronie klienta (CSR) na podstawie parsowania URL, bez odpytywania jakiejkolwiek bazy danych.

---

## 5. Wymagania Niefunkcjonalne (Non-Functional Requirements)

### 5.1. Wydajność i Szybkość Działania (Performance)
* **NFR-01: Czas ładowania (LCP):** Wskaźnik *Largest Contentful Paint* mierzony na urządzeniu mobilnym przy symulacji sieci 3G/4G (np. w Lighthouse) nie może przekraczać **1.5 sekundy**.
* **NFR-02: Czas reakcji interfejsu (FID):** *First Input Delay* musi wynosić poniżej **50 ms**. Wszystkie przejścia stanów, animacje suwaka i renderowanie wyników muszą zachodzić z płynnością **60 klatek na sekundę (60fps)**.
* **NFR-03: Wielkość paczki (Bundle Size):** Całkowity rozmiar produkcyjny kodu JavaScript i CSS (po minifikacji i kompresji Gzip lub Brotli) nie może przekraczać **150 KB** przy pierwszym załadowaniu strony.

### 5.2. Użyteczność i Design (UX/UI & RWD)
* **NFR-04: Strategia Mobile-First:** Interfejs musi być zaprojektowany w pierwszej kolejności pod ekrany smartfonów (pionowa orientacja, łatwa obsługa kciukiem). Wszystkie elementy dotykowe (przyciski, przełączniki, pola wyboru) muszą mieć minimalną wielkość **44x44 piksele**, aby zapobiec przypadkowym kliknięciom.
* **NFR-05: Responsywność (RWD):** Płynne skalowanie układu (Fluid Layout) od szerokości ekranu **320px** (starsze smartfony) do **2560px** (monitory desktopowe). Na ekranach desktopowych (szerokość >= 1024px) formularz wejściowy i dashboard wynikowy powinny układać się w układ dwukolumnowy (obok siebie), aby optymalnie zagospodarować przestrzeń.
* **NFR-06: Dostępność (Accessibility - WCAG 2.1 AA):**
  * **Kontrast:** Współczynnik kontrastu tekstów do tła musi wynosić minimum **4.5:1** (dotyczy również tekstów pomocniczych i disclaimera).
  * **Nawigacja klawiaturą:** Pełna możliwość obsługi całego formularza i akcji za pomocą klawiatury (klawisze Tab, Enter, Spacja).
  * **Atrybuty ARIA:** Zastosowanie poprawnych atrybutów `aria-*` dla dynamicznie zmieniających się elementów (np. `aria-live="polite"` dla kontenera z wynikami, `aria-invalid` dla błędów walidacji).

### 5.3. Bezpieczeństwo i Zgodność Prawna
* **NFR-07: Prywatność z założenia (Privacy by Design):** Wersja 1.0 aplikacji nie przechowuje żadnych danych osobowych ani medycznych użytkowników na serwerze. Wszystkie obliczenia są ulotne i przetwarzane lokalnie w pamięci RAM przeglądarki. Dzięki temu aplikacja nie wymaga wdrażania skomplikowanych polityk RODO/GDPR w zakresie baz danych.
* **NFR-08: Szyfrowanie:** Całość komunikacji musi być zabezpieczona certyfikatem SSL/TLS (wymuszenie protokołu HTTPS).

---

## 6. Reguły Biznesowe i Algorytmy

### 6.1. Algorytm Konwersji Jednostek
W celu zapewnienia spójności danych podczas przełączania systemów miar (US-1.6), system stosuje następujące stałe matematyczne:
* $1\text{ cal (in)} = 2.54\text{ cm}$
* $1\text{ stopa (ft)} = 12\text{ cali (in)} = 30.48\text{ cm}$
* $1\text{ funt (lbs)} = 0.45359237\text{ kg}$
* $1\text{ kg} = 2.20462262\text{ lbs}$

### 6.2. Algorytm Obliczania Delty Wagowej
Punktem docelowym jest zawsze $BMI_{docelowe} = 21.7$.
* **Dla systemu metrycznego:**
  $$W_{idealna} = 21.7 \times \left(\frac{Wzrost\_cm}{100}\right)^2$$
  $$\Delta_{kg} = Masa\_kg - W_{idealna}$$
* **Dla systemu imperialnego:**
  $$Wzrost\_in = (Wzrost\_ft \times 12) + Wzrost\_in\_reszta$$
  $$W_{idealna} = \frac{21.7 \times (Wzrost\_in)^2}{703}$$
  $$\Delta_{lbs} = Masa\_lbs - W_{idealna}$$

---

## 7. Ryzyka i Mitygacja

| ID Ryzyka | Opis Ryzyka | Wpływ | Prawdopodobieństwo | Strategia Mitygacji |
| :--- | :--- | :--- | :--- | :--- |
| **R-01** | **Ograniczenie metodologii BMI:** Użytkownicy o wysokiej masie mięśniowej (sportowcy) lub kobiety w ciąży mogą błędnie zinterpretować wynik jako nadwagę/otyłość. | Wysoki | Wysokie | Stałe wyświetlanie widocznego wyłączenia odpowiedzialności (Disclaimer) bezpośrednio pod wynikami (US-3.4). |
| **R-02** | **Próby wstrzykiwania skrajnych danych:** Wpisywanie wartości typu `999999` w pola formularza, co mogłoby rozbić layout lub zawiesić silnik JS. | Średni | Średnie | Restrykcyjna walidacja po stronie klienta (US-1.5). Blokada wpisywania znaków niebędących cyframi, automatyczne przycinanie wartości do limitów brzegowych. |
| **R-03** | **Niska wydajność na urządzeniach mobilnych:** Wolne ładowanie aplikacji na słabszych telefonach (wysoki wskaźnik LCP). | Wysoki | Średnie | Optymalizacja wielkości paczki (NFR-03), rezygnacja z ciężkich bibliotek zewnętrznych, leniwe ładowanie (lazy loading) zasobów graficznych. |

---

## 8. Wyłączenia z Zakresu (Out of Scope - v2.0+)

Następujące funkcjonalności zostały zidentyfikowane jako pożądane w przyszłości, ale są **całkowicie wyłączone** z zakresu wersji 1.0 (MVP):
1. **Konta użytkowników i logowanie:** Brak rejestracji, uwierzytelniania i profili użytkowników.
2. **Zapisywanie historii wyników w chmurze:** Brak bazy danych po stronie serwera.
3. **Wykresy historyczne zmian wagi:** Wizualizacja trendu w czasie zostanie wdrożona w v2.0 (wymaga lokalnej bazy danych np. IndexedDB lub kont użytkowników).
4. **Siatki centylowe dla dzieci:** Pełna, automatyczna interpretacja BMI dla dzieci na podstawie siatek centylowych WHO (w v1.0 stosujemy jedynie ostrzeżenie tekstowe).
5. **Integracja z zewnętrznymi API fitness:** Brak połączenia z Apple Health, Google Fit czy Strava.

---

## 9. Otwarte Pytania do Biznesu (Open Questions)

Podczas analizy zidentyfikowano następujące kwestie wymagające ostatecznego potwierdzenia przez Product Managera / Biznes:
1. **Czy w wersji 1.0 chcemy zapamiętywać ostatnie wyniki w `localStorage`?**
   * *Rekomendacja BA:* Tak, to znacznie poprawia retencję (KPI) i UX bez konieczności tworzenia bazy danych. Przy ponownym wejściu użytkownik widzi swoje ostatnie dane.
2. **Czy format udostępniania wyniku w social media powinien zawierać dokładną wagę i wzrost użytkownika, czy tylko sam wynik BMI i klasyfikację?**
   * *Rekomendacja BA:* Ze względów prywatności (część osób wstydzi się swojej wagi), domyślny tekst udostępniania powinien zawierać jedynie wskaźnik BMI i klasyfikację (np. "Mój wskaźnik BMI to 22.0 - Waga prawidłowa!"), natomiast parametry w URL (do odtworzenia wyniku) powinny być opcjonalne lub zakodowane w sposób nieczytelny na pierwszy rzut oka (np. Base64), aby nie zniechęcać użytkowników do dzielenia się linkiem.
