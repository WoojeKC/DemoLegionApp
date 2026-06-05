### 1. Cel, Wizja i Zakres Projektu

#### 1.1. Cel główny
Celem projektu jest zaprojektowanie, rozwój i wdrożenie nowoczesnej, wysoce responsywnej aplikacji webowej typu **SPA (Single Page Application)** służącej do obliczania, interpretacji oraz monitorowania wskaźnika masy ciała (BMI - Body Mass Index). Aplikacja ma działać błyskawicznie, bez przeładowywania strony, dostarczając użytkownikowi natychmiastową wartość informacyjną i angażujące wrażenia wizualne (UX).

#### 1.2. Cele biznesowe i KPI
* **Generowanie leadów i ruchu (Traffic Generation):** Narzędzie ma stanowić element lejka marketingowego, przyciągający użytkowników zainteresowanych zdrowym stylem życia, dietetyką lub fitem.
* **Wysoka konwersja (Engagement):** Intuicyjny interfejs ma zapewnić wskaźnik ukończenia interakcji (wykonania obliczenia) na poziomie minimum 85% użytkowników uruchamiających aplikację.
* **Wiralność (Virality):** Integracja mechanizmów łatwego dzielenia się wynikiem lub samą aplikacją w mediach społecznościowych.
* **Retencja:** Stworzenie fundamentu pod moduł zapisu historii (wersja 2.0), który skłoni użytkowników do regularnych powrotów.

#### 1.3. Grupa docelowa (User Personas)
1.  **Kowalski (Amator zdrowego stylu życia):** Chce szybko i bez rejestracji sprawdzić, czy jego waga mieści się w normie. Oczekuje prostego języka i jasnych wskazówek wizualnych (kolory).
2.  **Świadomy sportowiec / Osoba na diecie:** Regularnie kontroluje parametry ciała. Oczekuje precyzji (miejsca po przecinku), alternatywnych jednostek miar oraz jasnego określenia celów (ile brakuje do normy).
3.  **Użytkownik Mobile-Only:** Korzysta z aplikacji na smartfonie w drodze lub na siłowni. Oczekuje błyskawicznego działania, dużych elementów klikalnych i braku zbędnego tekstu.

---

### 2. Architektura i Kontekst Technologiczny (SPA)

Aplikacja musi zostać zrealizowana w architekturze **Single Page Application (SPA)** przy użyciu nowoczesnego frameworka (np. React, Vue.js lub Angular).

#### Kluczowe założenia architektoniczne:
* **Client-side Rendering (CSR):** Cała logika obliczeniowa oraz renderowanie widoków odbywa się po stronie przeglądarki użytkownika.
* **Brak przeładowań (Zero Page Reloads):** Przejścia pomiędzy wprowadzaniem danych, prezentacją wyniku a ewentualnymi sekcjami informacyjnymi muszą odbywać się płynnie, za pomocą natychmiastowych zmian stanu aplikacji (State Management).
* **Lokalne zarządzanie stanem:** Dane wejściowe i wyniki są przechowywane w pamięci podręcznej aplikacji (lub opcjonalnie w `localStorage` w celu zapamiętania ostatnich parametrów użytkownika).

---

### 3. Wymagania Funkcjonalne (Functional Requirements)

#### 3.1. Moduł Wprowadzania Danych (Formularz Wejściowy)
* **FR-01: Wybór Systemu Miar:** Użytkownik musi mieć możliwość przełączania się pomiędzy systemem metrycznym (kg, cm) a imperialnym (lbs, ft/in). Domyślnym systemem jest system metryczny.
* **FR-02: Wprowadzanie Wzrostu:**
    * System metryczny: pole numeryczne, zakres od 100 do 250 cm, krok co 1 cm.
    * System imperialny: dwa pola (stopy i cale), zakres od 3'3" do 8'2".
* **FR-03: Wprowadzanie Masy Ciała:**
    * System metryczny: pole numeryczne, zakres od 30 do 300 kg, krok co 0.1 kg.
    * System imperialny: pole numeryczne, zakres od 66 do 660 lbs, krok co 0.1 lbs.
* **FR-04: Metadane Personalizacyjne (Opcjonalne):** Suwaki lub pola wyboru dla płci (Kobieta / Mężczyzna) oraz wieku (zakres 2–120 lat) w celu dostosowania komunikatów tekstowych (BMI dzieci i młodzieży rządzi się innymi prawami – siatki centylowe – co w v1.0 zostanie obsłużone komunikatem ostrzegawczym).
* **FR-05: Dynamiczna Walidacja:** System musi na bieżąco (inline) sprawdzać poprawność danych. Przycisk "Oblicz" pozostaje nieaktywny (disabled) lub wyświetla błąd, jeśli wprowadzone wartości wykraczają poza zdefiniowane brzegowe zakresy.

#### 3.2. Moduł Obliczeń i Silnik Matematyczny
* **FR-06: Automatyczne / Półautomatyczne Wyzwalanie:** Obliczenie następuje natychmiast po kliknięciu przycisku "Oblicz BMI" LUB opcjonalnie dynamicznie ("w locie") po wypełnieniu wszystkich wymaganych pól i utracie focusu przez pole edycyjne.
* **FR-07: Przeliczanie Jednostek:** Jeśli użytkownik zmieni system miar po wpisaniu danych, aplikacja automatycznie przeliczy wartości (np. 180 cm zamieni na odpowiednią wartość w stopach i calach), nie czyszcząc formularza.

#### 3.3. Moduł Prezentacji Wyników (Dashboard Wynikowy)
* **FR-08: Prezentacja Liczbowa:** Wyraziste wyświetlenie wyliczonej wartości BMI z dokładnością do jednego miejsca po przecinku (np. **24.2**).
* **FR-09: Wizualizacja Graficzna (Gage/Slider):** Prezentacja wyniku na kolorowym pasku postępu (skali dynamicznej). Wskaźnik (strzałka/suwak) musi płynnie przesunąć się na odpowiedni zakres kolorystyczny:
    * Niebieski/Żółty: Niedowaga
    * Zielony: Waga prawidłowa
    * Pomarańczowy: Nadwaga
    * Czerwony / Ciemnoczerwony: Otyłość (stopnie I, II, III)
* **FR-10: Interpretacja Tekstowa i Rekomendacja:** Dynamiczny opis stanu zdrowia powiązany z wynikiem (np. *"Twój wskaźnik BMI wskazuje na wagę prawidłową. Gratulacje! Dbaj o dotychczasową aktywność fizyczną"*).
* **FR-11: Kontekst Wagowy (Delta):** Aplikacja musi wyliczyć i wyświetlić informację, ile kilogramów użytkownik musiałby zrzucić (lub przybrać), aby znaleźć się w idealnym środku przedziału wagi prawidłowej (BMI = 21.7).

#### 3.4. Dodatkowe Funkcjonalności SPA
* **FR-12: Resetowanie Danych:** Przycisk czyszczący formularz i resetujący widok do stanu początkowego za pomocą płynnej animacji, bez przeładowania karty.
* **FR-13: Udostępnianie Wyniku:** Integracja z systemowym API udostępniania (Web Share API) na urządzeniach mobilnych oraz dedykowane ikony (Facebook, Twitter/X, WhatsApp) generujące unikalny link z parametrami w URL (np. `bmi.app/?w=70&h=175`), umożliwiający natychmiastowe odtworzenie wyniku bez zapisu w bazie danych.

---

### 4. Wymagania Niefunkcjonalne (Non-Functional Requirements)

#### 4.1. Wydajność i Szybkość Działania (Performance)
* **NFR-01: Czas ładowania (LCP):** Wskaźnik *Largest Contentful Paint* na sieci 3G/4G na urządzeniu mobilnym nie może przekraczać **1.5 sekundy**.
* **NFR-02: Czas reakcji interfejsu (FID):** *First Input Delay* na poziomie poniżej **50 ms**. Zmiany stanów, animacje suwaka wyników muszą zachodzić z płynnością 60 klatek na sekundę (60fps).
* **NFR-03: Wielkość paczki (Bundle Size):** Całkowity rozmiar produkcyjny kodu JS/CSS (skompresowany Gzip/Brotli) nie powinien przekraczać **150 KB** przy pierwszym załadowaniu.

#### 4.2. Użyteczność i Design (UX/UI & RWD)
* **NFR-04: Strategia Mobile-First:** Interfejs zaprojektowany w pierwszej kolejności pod ekrany smartfonów (pionowa orientacja, łatwa obsługa kciukiem). Elementy dotykowe (przyciski, switche) o minimalnej wielkości 44x44 piksele.
* **NFR-05: Responsywność:** Płynne skalowanie układu (Fluid Layout) od szerokości ekranu 320px do 2560px. Na ekranach desktopowych formularz i wyniki mogą układać się w dwie kolumny obok siebie.
* **NFR-06: Dostępność (Accessibility - WCAG 2.1):**
    * Pełna zgodność z poziomem **AA**.
    * Współczynnik kontrastu tekstów do tła minimum 4.5:1.
    * Pełna obsługa formularza za pomocą samej klawiatury (tabulacja, enter).
    * Zastosowanie poprawnych atrybutów `aria-*` dla dynamicznie zmieniających się elementów (np. `aria-live="polite"` dla wyniku BMI).

#### 4.3. Bezpieczeństwo i Zgodność Prawna
* **NFR-07: Prywatność z założenia (Privacy by Design):** Wersja 1.0 aplikacji nie przechowuje danych użytkowników na serwerze. Wszystkie obliczenia są ulotne i przetwarzane lokalnie w pamięci RAM przeglądarki. Brak konieczności implementacji ciężkich polityk RODO w zakresie baz danych.
* **NFR-08: Szyfrowanie:** Wymagany certyfikat SSL/TLS (wymuszenie protokołu HTTPS).

---

### 5. Logika Biznesowa i Algorytmy Obliczeniowe

#### 5.1. Wzór Matematyczny
Podstawą działania aplikacji dla systemu metrycznego jest standardowy wzór:

$$BMI = rac{masa\_ciala\_[kg]}{(wzrost\_[m])^2}$$

Dla systemu imperialnego stosowany jest współczynnik korygujący:

$$BMI = rac{masa\_ciala\_[lbs]}{(wzrost\_[in])^2} 	imes 703$$

#### 5.2. Kryteria Klasyfikacji (Zgodnie z WHO)

Aplikacja przypisuje wynik do jednej z poniższych klas, zmieniając kolorystykę komponentu wynikowego:

| Zakres BMI | Klasyfikacja medyczna | Kolorystyka UI | Kod Hex (Sugerowany) |
| :--- | :--- | :--- | :--- |
| **< 16.0** | Wyczerpanie / Wytrenowanie skrajne | Jasnoniebieski | `#3498db` |
| **16.0 – 16.9** | Wychodzenie z normy / Wychudzenie | Niebieski | `#2980b9` |
| **17.0 – 18.4** | Niedowaga | Żółty | `#f1c40f` |
| **18.5 – 24.9** | **Waga prawidłowa** | **Zielony** | `#2ecc71` |
| **25.0 – 29.9** | Nadwaga | Pomarańczowy | `#e67e22` |
| **30.0 – 34.9** | Otyłość I stopnia | Jasnoczerwony | `#e74c3c` |
| **35.0 – 39.9** | Otyłość II stopnia (kliniczna) | Czerwony | `#c0392b` |
| **>= 40.0** | Otyłość III stopnia (skrajna) | Ciemny fiolet/bordowy | `#8e44ad` |

---

### 6. Ryzyka, Ograniczenia i Wyłączenia odpowiedzialności (Disclaimers)

* **R-01: Ograniczenie interpretacji metodologii BMI:** BMI jest wskaźnikiem statystycznym i nie rozróżnia komponentów tkanki tłuszczowej oraz mięśniowej.
    * *Mitygacja:* W widoku prezentacji wyników, bezpośrednio pod wykresem, musi znajdować się stały wpis (Disclaimer):
      > **Ważna informacja:** Wskaźnik BMI ma charakter wyłącznie orientacyjny. Może nie być miarodajny dla sportowców (wysoka masa mięśniowa), kobiet w ciąży oraz dzieci. Wynik ten nie zastępuje indywidualnej porady lekarskiej ani dietetycznej.
* **R-02: Próby wstrzykiwania błędnych danych:** Ryzyko wpisania wartości typu `999999` w pole wagi powodujące zaburzenia layoutu.
    * *Mitygacja:* Zastosowanie restrykcyjnej walidacji po stronie klienta (blokada zatwierdzania formularza, automatyczne formatowanie wpisu do wartości maksymalnej).