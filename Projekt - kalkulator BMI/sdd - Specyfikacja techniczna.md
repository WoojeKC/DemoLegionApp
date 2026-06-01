# DOKUMENT PROJEKTU SYSTEMOWEGO (SDD)
## Projekt: Nowoczesna Aplikacja BMI SPA (Wersja 1.0)

| Parametr | Szczegóły |
| :--- | :--- |
| **Nazwa Projektu** | BMI SPA Application |
| **Wersja Dokumentu** | 1.0.0 |
| **Status** | Gotowy do Implementacji |
| **Autor** | Starszy Analityk Systemowy (Senior Systems Analyst) |
| **Rola Odbiorcy** | Zespół Deweloperski, Product Manager, QA |
| **Data Utworzenia** | Październik 2023 |

---

## 1. Architektura i Przepływ Systemowy (Architectural Overview)

Aplikacja zostanie zrealizowana w architekturze **Local-First Single-Page Application (SPA)**. Całość logiki biznesowej, obliczeniowej, walidacyjnej oraz prezentacyjnej jest wykonywana po stronie klienta (Client-Side Rendering - CSR) w przeglądarce użytkownika. Aplikacja nie posiada dedykowanego backendu bazodanowego ani aplikacyjnego – jest wdrażana jako zestaw statycznych plików (HTML, JS, CSS) na serwerze WWW / CDN.

### 1.1. Schemat Blokowy Architektury (Component Diagram)

Poniższy diagram przedstawia architekturę modułową aplikacji uruchamianej w piaskownicy przeglądarki internetowej:

```
+---------------------------------------------------------------------------------+
|                               PRZEGLĄDARKA KLIENTA                              |
|                                                                                 |
|  +---------------------------------------------------------------------------+  |
|  |                           WARSTWA PREZENTACJI (UI)                        |  |
|  |  [ HTML5 / Bootstrap 5.3 ] <---> [ Moduł UI (ui.js) ]                     |  |
|  +-------------------------------------+-------------------------------------+  |
|                                        | (Zdarzenia / Aktualizacja DOM)      |
|                                        v                                        |
|  +---------------------------------------------------------------------------+  |
|  |                         WARSTWA KONTROLI I STANU                          |  |
|  |  [ Moduł Aplikacji (app.js) ] <---> [ Zarządca Stanu (state.js) ]         |  |
|  +-------------------------------------+-------------------------------------+  |
|                                        |                                        |
|                    +-------------------+-------------------+                    |
|                    | (Dane wejściowe)                      | (Zapis/Odczyt)     |
|                    v                                       v                    |
|  +-----------------------------------+   +-----------------------------------+  |
|  |     SILNIK OBLICZENIOWY           |   |       WARSTWA DANYCH (STORAGE)    |  |
|  |     (calculator.js)               |   |       (storage.js)                |  |
|  |  - Obliczanie BMI                 |   |  - Wrapper Dexie.js (IndexedDB)   |  |
|  |  - Klasyfikacja WHO               |   |  - Obsługa LocalStorage           |  |
|  |  - Delta wagowa                   |   +-----------------+-----------------+  |
|  |  - Konwersja jednostek            |                     |                    |
|  +-----------------------------------+                     |                    |
|                                                            v                    |
|                                          +-----------------+-----------------+  |
|                                          |        PAMIĘĆ PRZEGLĄDARKI        |  |
|                                          |  [ IndexedDB ]   [ LocalStorage ] |  |
|                                          +-----------------------------------+  |
+---------------------------------------------------------------------------------+
```

### 1.2. Przepływ Procesu Obliczeniowego (Sequence Diagram)

Poniższy diagram sekwencji przedstawia interakcję między modułami podczas wprowadzania danych przez użytkownika, walidacji, zapisu oraz prezentacji wyników.

```mermaid
sequenceDiagram
    autonumber
    actor Uzytkownik as Użytkownik
    participant UI as Moduł UI (ui.js)
    participant State as Zarządca Stanu (state.js)
    participant Calc as Silnik Obliczeniowy (calculator.js)
    participant Store as Warstwa Danych (storage.js)
    database IDB as IndexedDB

    Uzytkownik->>UI: Wprowadzenie danych (Wzrost, Waga, Wiek, Płeć)
    activate UI
    UI->>UI: Walidacja pól formularza (w locie)
    alt Dane niepoprawne
        UI->>Uzytkownik: Wyświetlenie czerwonych komunikatów, zablokowanie "Oblicz"
    else Dane poprawne
        UI->>UI: Odblokowanie przycisku "Oblicz"
        Uzytkownik->>UI: Kliknięcie "Oblicz BMI" (lub onBlur ostatniego pola)
        UI->>State: Aktualizacja stanu wejściowego (updateInputState)
        activate State
        State->>Calc: Wywołanie obliczeń (calculateBMI, getClassification, getDelta)
        activate Calc
        Calc-->>State: Zwrócenie wyników (BMI, Klasa WHO, Delta, Waga Idealna)
        deactivate Calc
        State->>Store: Zapisz kalkulację (saveCalculation)
        activate Store
        Store->>IDB: Asynchroniczny zapis rekordu (Dexie.js)
        activate IDB
        IDB-->>Store: Potwierdzenie zapisu (ID rekordu)
        deactivate IDB
        Store-->>State: Zwrócenie ID rekordu
        deactivate Store
        State->>Store: Zapisz ID jako ostatnią kalkulację (LocalStorage)
        State-->>UI: Powiadomienie o zmianie stanu (State Change Event)
        deactivate State
        UI->>UI: Renderowanie Dashboardu Wynikowego
        UI->>UI: Animacja suwaka skali BMI (60fps)
        UI->>Uzytkownik: Prezentacja wyników, delty i rekomendacji
    end
    deactivate UI
```

---

## 2. Model Danych i Trwałość (Data Model & Persistence)

Zgodnie z wytycznymi technologicznymi, do przechowywania historii obliczeń oraz parametrów użytkownika wykorzystywana jest baza danych **IndexedDB** za pośrednictwem lekkiej biblioteki-wrappera **Dexie.js** (ładowanej przez CDN). `LocalStorage` jest używany wyłącznie do przechowywania prostych flag konfiguracyjnych.

### 2.1. Schemat Bazy Danych IndexedDB (`BMISpaDB`)

Baza danych o nazwie `BMISpaDB` posiada jedną tabelę (Object Store) o nazwie `calculations`.

#### Tabela: `calculations`
* **Klucz główny:** `id` (Auto-increment)
* **Indeksy:** `[id, timestamp]` (umożliwiające szybkie sortowanie po czasie)

| Nazwa Pola | Typ Danych | Walidacja / Zakres | Opis |
| :--- | :--- | :--- | :--- |
| `id` | `Integer` | Autoincrement | Unikalny identyfikator rekordu (Klucz główny). |
| `timestamp` | `Integer` | Wartość > 0 | Znacznik czasu Unix (w milisekundach) wykonania obliczenia. |
| `system` | `String` | `"metric"` \| `"imperial"` | Wybrany system miar podczas wprowadzania danych. |
| `height` | `Number` | Metryczny: `100 - 250` (cm)<br>Imperialny: `39 - 98` (cale) | Wzrost użytkownika zapisany w jednostce wejściowej. |
| `weight` | `Number` | Metryczny: `30.0 - 300.0` (kg)<br>Imperialny: `66.0 - 660.0` (lbs) | Masa ciała użytkownika zapisana w jednostce wejściowej. |
| `gender` | `String` \| `null` | `"male"` \| `"female"` \| `null` | Płeć użytkownika (opcjonalna). |
| `age` | `Integer` \| `null` | `2 - 120` \| `null` | Wiek użytkownika w latach (opcjonalny). |
| `bmi` | `Number` | `10.0 - 100.0` (zaokr. do 1 m.p.p.) | Wyliczony wskaźnik BMI. |
| `classification` | `String` | Słownik klasyfikacji WHO (patrz sekcja 2.3) | Klasyfikacja medyczna wyniku. |
| `delta` | `Number` | Dowolna wartość zmiennoprzecinkowa | Różnica do wagi idealnej (dodatnia dla nadwagi, ujemna dla niedowagi, bliska 0 dla normy). |
| `idealWeight` | `Number` | Wartość zmiennoprzecinkowa | Wyliczona idealna masa ciała dla podanego wzrostu (BMI = 21.7). |

### 2.2. Schemat LocalStorage

`LocalStorage` jest używany synchronicznie wyłącznie do przechowywania nieczułych danych konfiguracyjnych aplikacji.

| Klucz | Typ Danych | Dopuszczalne Wartości | Opis |
| :--- | :--- | :--- | :--- |
| `bmi_theme` | `String` | `"light"` \| `"dark"` | Wybrany motyw kolorystyczny interfejsu. |
| `bmi_last_calc_id` | `Integer` | Dowolny ID z IndexedDB | Identyfikator ostatniej kalkulacji w celu odtworzenia stanu przy ponownym uruchomieniu aplikacji (gdy brak parametrów URL). |

### 2.3. Słowniki i Stałe Systemowe

#### Słownik Klasyfikacji WHO (`WHO_CLASSIFICATIONS`)
Aplikacja definiuje 8 klasyfikacji medycznych na podstawie wartości BMI:

```javascript
const WHO_CLASSIFICATIONS = {
  SEVERE_THINNESS: { min: 0, max: 15.99, label: "Wyczerpanie / Wytrenowanie skrajne", color: "#3498db", alertClass: "alert-info" },
  MODERATE_THINNESS: { min: 16.0, max: 16.99, label: "Wychodzenie z normy / Wychudzenie", color: "#2980b9", alertClass: "alert-info" },
  MILD_THINNESS: { min: 17.0, max: 18.49, label: "Niedowaga", color: "#f1c40f", alertClass: "alert-warning" },
  NORMAL: { min: 18.5, max: 24.99, label: "Waga prawidłowa", color: "#2ecc71", alertClass: "alert-success" },
  OVERWEIGHT: { min: 25.0, max: 29.99, label: "Nadwaga", color: "#e67e22", alertClass: "alert-warning" },
  OBESITY_CLASS_1: { min: 30.0, max: 34.99, label: "Otyłość I stopnia", color: "#e74c3c", alertClass: "alert-danger" },
  OBESITY_CLASS_2: { min: 35.0, max: 39.99, label: "Otyłość II stopnia (kliniczna)", color: "#c0392b", alertClass: "alert-danger" },
  OBESITY_CLASS_3: { min: 40.0, max: Infinity, label: "Otyłość III stopnia (skrajna)", color: "#8e44ad", alertClass: "alert-danger" }
};
```

---

## 3. Struktura Modułowa Kodu (Modular JS Structure)

Kod JavaScript zostanie podzielony na logiczne moduły ES6. W wersji produkcyjnej moduły te mogą być spakowane do jednego pliku za pomocą bundlera (np. Vite, Webpack) lub ładowane bezpośrednio w przeglądarce jako `<script type="module">`.

### 3.1. Podział na Moduły

```
/src
├── index.html          # Główny i jedyny plik HTML aplikacji
├── css/
│   └── custom.css      # Dedykowane style (nadpisanie Bootstrap, animacje suwaka)
└── js/
    ├── app.js          # Główny koordynator (Orchestrator) i router URL
    ├── state.js        # Zarządzanie stanem aplikacji (State Management)
    ├── storage.js      # Warstwa integracji z IndexedDB (Dexie.js) i LocalStorage
    ├── calculator.js   # Czyste funkcje matematyczne i konwersje
    └── ui.js           # Manipulacja DOM, obsługa zdarzeń, animacje i wykresy
```

### 3.2. Specyfikacja Interfejsów Modułów (API wewnętrzne)

#### Moduł `calculator.js`
Zawiera wyłącznie czyste funkcje (pure functions), łatwe do testowania jednostkowego.

```javascript
/**
 * Oblicza BMI na podstawie wagi i wzrostu w systemie metrycznym.
 * @param {number} weightKg - Waga w kg
 * @param {number} heightCm - Wzrost w cm
 * @returns {number} BMI zaokrąglone do 1 miejsca po przecinku
 */
export function calculateMetricBMI(weightKg, heightCm) { ... }

/**
 * Oblicza BMI na podstawie wagi i wzrostu w systemie imperialnym.
 * @param {number} weightLbs - Waga w lbs
 * @param {number} heightInches - Wzrost w calach
 * @returns {number} BMI zaokrąglone do 1 miejsca po przecinku
 */
export function calculateImperialBMI(weightLbs, heightInches) { ... }

/**
 * Zwraca obiekt klasyfikacji WHO dla danej wartości BMI.
 * @param {number} bmi 
 * @returns {object} Element z WHO_CLASSIFICATIONS
 */
export function getClassification(bmi) { ... }

/**
 * Oblicza wagę idealną (BMI = 21.7) i różnicę (deltę) do wagi aktualnej.
 * @param {number} height - Wzrost (cm lub cale)
 * @param {number} currentWeight - Aktualna waga (kg lub lbs)
 * @param {string} system - 'metric' | 'imperial'
 * @returns {object} { idealWeight, delta }
 */
export function calculateWeightDelta(height, currentWeight, system) { ... }

/**
 * Konwertuje cm na stopy i cale.
 * @param {number} cm 
 * @returns {object} { ft, in }
 */
export function cmToFeetInches(cm) { ... }

/**
 * Konwertuje stopy i cale na cm.
 * @param {number} ft 
 * @param {number} inches 
 * @returns {number} cm (zaokrąglone do liczby całkowitej)
 */
export function feetInchesToCm(ft, inches) { ... }
```

#### Moduł `storage.js`
Odpowiada za asynchroniczną komunikację z IndexedDB oraz synchroniczną z LocalStorage.

```javascript
import Dexie from 'https://unpkg.com/dexie@3.2.4/dist/dexie.mjs';

const db = new Dexie('BMISpaDB');
db.version(1).stores({
  calculations: '++id, timestamp, bmi, classification'
});

export async function saveCalculation(calcData) {
  try {
    const id = await db.calculations.add({
      timestamp: Date.now(),
      ...calcData
    });
    localStorage.setItem('bmi_last_calc_id', id);
    return id;
  } catch (error) {
    console.error("Błąd zapisu do IndexedDB:", error);
    throw error;
  }
}

export async function getCalculationById(id) {
  return await db.calculations.get(Number(id));
}

export async function getHistory() {
  return await db.calculations.orderBy('timestamp').reverse().toArray();
}

export async function clearHistory() {
  await db.calculations.clear();
  localStorage.removeItem('bmi_last_calc_id');
}
```

#### Moduł `state.js`
Zarządza reaktywnym stanem aplikacji. Implementuje wzorzec Obserwatora (Observer Pattern) do powiadamiania modułu UI o zmianach.

```javascript
class StateManager {
  constructor() {
    this.state = {
      system: 'metric', // 'metric' | 'imperial'
      inputs: { height: null, weight: null, age: null, gender: null },
      results: null,    // { bmi, classification, delta, idealWeight }
      history: []
    };
    this.listeners = [];
  }

  subscribe(listener) {
    this.listeners.push(listener);
  }

  notify() {
    this.listeners.forEach(listener => listener(this.state));
  }

  setState(newState) {
    this.state = { ...this.state, ...newState };
    this.notify();
  }
}
export const stateManager = new StateManager();
```

---

## 4. Routing i Parsowanie URL (Privacy-Preserving Sharing)

Aby zapewnić maksymalną prywatność użytkowników przy jednoczesnym zachowaniu funkcji udostępniania wyników (US-4.1, US-4.2), parametry wejściowe są kodowane w formacie **Base64** i przekazywane w jednym parametrze URL o nazwie `data`.

### 4.1. Struktura Obiektu Danych (JSON)

Przed zakodowaniem do Base64, parametry wejściowe są serializowane do minimalnego obiektu JSON w celu zaoszczędzenia miejsca w adresie URL:

```json
{
  "sys": "m",
  "w": 72.5,
  "h": 178,
  "g": "m",
  "a": 28
}
```

*Skróty kluczy:*
* `sys`: System miar (`"m"` = metryczny, `"i"` = imperialny)
* `w`: Masa ciała (zawsze liczba zmiennoprzecinkowa, w kg dla `"m"`, w lbs dla `"i"`)
* `h`: Wzrost (dla `"m"` liczba całkowita w cm; dla `"i"` łączna liczba cali jako liczba całkowita, np. 5'11" = 71 cali)
* `g`: Płeć (`"m"` = mężczyzna, `"f"` = kobieta, `null` = nie podano)
* `a`: Wiek (liczba całkowita `2 - 120`, `null` = nie podano)

### 4.2. Algorytm Kodowania i Dekodowania URL-Safe Base64

Standardowe Base64 zawiera znaki `+`, `/` oraz `=`, które wymagają kodowania procentowego w adresach URL. Aby linki były czyste i czytelne, zastosowany zostanie standard **URL-Safe Base64** (zgodny z RFC 4648):

```javascript
/**
 * Koduje obiekt parametrów do bezpiecznego ciągu Base64 dla URL.
 * @param {object} obj 
 * @returns {string} URL-safe Base64 string
 */
export function encodeParams(obj) {
  const jsonStr = JSON.stringify(obj);
  // Standardowe kodowanie Base64 z obsługą znaków UTF-8
  const base64 = btoa(encodeURIComponent(jsonStr).replace(/%([0-9A-F]{2})/g, (match, p1) => {
    return String.fromCharCode(parseInt(p1, 16));
  }));
  // Zamiana znaków na bezpieczne dla URL i usunięcie dopełnienia '='
  return base64
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=+$/, '');
}

/**
 * Dekoduje ciąg URL-safe Base64 z powrotem do obiektu.
 * @param {string} safeBase64 
 * @returns {object|null} Zdekodowany obiekt lub null w przypadku błędu
 */
export function decodeParams(safeBase64) {
  try {
    // Przywrócenie standardowych znaków Base64 i dopełnienia '='
    let base64 = safeBase64.replace(/-/g, '+').replace(/_/g, '/');
    while (base64.length % 4) {
      base64 += '=';
    }
    const jsonStr = decodeURIComponent(atob(base64).split('').map(c => {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    
    const parsed = JSON.parse(jsonStr);
    return validateDecodedParams(parsed) ? parsed : null;
  } catch (e) {
    console.error("Błąd dekodowania parametrów URL:", e);
    return null;
  }
}
```

### 4.3. Walidacja Zdekodowanych Danych (Zabezpieczenie przed XSS i Tamperingiem)

Przed zaaplikowaniem zdekodowanych danych do stanu aplikacji, moduł `app.js` musi przeprowadzić rygorystyczną walidację typów i zakresów:

```javascript
function validateDecodedParams(data) {
  if (typeof data !== 'object' || data === null) return false;
  
  // Walidacja systemu miar
  if (data.sys !== 'm' && data.sys !== 'i') return false;
  
  // Walidacja wagi
  if (typeof data.w !== 'number' || isNaN(data.w)) return false;
  if (data.sys === 'm' && (data.w < 30.0 || data.w > 300.0)) return false;
  if (data.sys === 'i' && (data.w < 66.0 || data.w > 660.0)) return false;
  
  // Walidacja wzrostu
  if (typeof data.h !== 'number' || !Number.isInteger(data.h)) return false;
  if (data.sys === 'm' && (data.h < 100 || data.h > 250)) return false;
  if (data.sys === 'i' && (data.h < 39 || data.h > 98)) return false;
  
  // Walidacja płci (opcjonalna)
  if (data.g !== undefined && data.g !== null && data.g !== 'm' && data.g !== 'f') return false;
  
  // Walidacja wieku (opcjonalna)
  if (data.a !== undefined && data.a !== null) {
    if (!Number.isInteger(data.a) || data.a < 2 || data.a > 120) return false;
  }
  
  return true;
}
```

---

## 5. Projekt UI/UX i Integracja z Bootstrap 5.3

Interfejs użytkownika zostanie zbudowany w oparciu o **Bootstrap 5.3+** bez użycia jQuery. Wykorzystane zostaną natywne mechanizmy Bootstrap do obsługi motywów (Dark Mode) oraz komponenty RWD.

### 5.1. Struktura Układu (Grid & Responsywność)

Zastosowany zostanie dwukolumnowy układ na dużych ekranach (Desktop) oraz jednokolumnowy na urządzeniach mobilnych (Mobile-First).

* **Siatka Bootstrap:**
  * Kontener główny: `<div class="container py-4">`
  * Wiersz główny: `<div class="row g-4">`
  * Kolumna formularza (lewa): `<div class="col-12 col-lg-6">`
  * Kolumna wyników (prawa): `<div class="col-12 col-lg-6 d-none d-lg-block" id="results-column">` (dynamicznie pokazywana na mobile po kliknięciu "Oblicz").

### 5.2. Implementacja Dark Mode (Natywny Bootstrap 5.3)

Przełączanie motywów odbywa się poprzez modyfikację atrybutu `data-bs-theme` na elemencie `<html>`.

```javascript
// ui.js - Zarządzanie motywem
export function initTheme() {
  const savedTheme = localStorage.getItem('bmi_theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const activeTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
  
  setTheme(activeTheme);
  
  // Nasłuchiwanie zmian systemowych
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    if (!localStorage.getItem('bmi_theme')) {
      setTheme(e.matches ? 'dark' : 'light');
    }
  });
}

export function setTheme(theme) {
  document.documentElement.setAttribute('data-bs-theme', theme);
  localStorage.setItem('bmi_theme', theme);
  updateThemeToggleUI(theme);
}
```

### 5.3. Wizualizacja Graficzna (Suwak BMI - 60fps CSS Transition)

Wizualizacja wyniku BMI zostanie zrealizowana za pomocą responsywnego paska SVG z dynamicznym markerem (strzałką). Użycie SVG gwarantuje idealną ostrość na ekranach Retina oraz pełną responsywność.

#### Kod HTML/SVG Komponentu:
```html
<div class="bmi-gauge-container my-4">
  <svg viewBox="0 0 1000 60" width="100%" height="60" class="rounded shadow-sm">
    <!-- Definicje gradientów lub segmentów kolorystycznych -->
    <g id="gauge-segments">
      <!-- Wyczerpanie <16.0 -->
      <rect x="0" y="10" width="120" height="30" fill="#3498db" />
      <!-- Wychudzenie 16.0-17.0 -->
      <rect x="120" y="10" width="50" height="30" fill="#2980b9" />
      <!-- Niedowaga 17.0-18.5 -->
      <rect x="170" y="10" width="75" height="30" fill="#f1c40f" />
      <!-- Norma 18.5-25.0 -->
      <rect x="245" y="10" width="325" height="30" fill="#2ecc71" />
      <!-- Nadwaga 25.0-30.0 -->
      <rect x="570" y="10" width="125" height="30" fill="#e67e22" />
      <!-- Otyłość I 30.0-35.0 -->
      <rect x="695" y="10" width="125" height="30" fill="#e74c3c" />
      <!-- Otyłość II 35.0-40.0 -->
      <rect x="820" y="10" width="125" height="30" fill="#c0392b" />
      <!-- Otyłość III >=40.0 -->
      <rect x="945" y="10" width="55" height="30" fill="#8e44ad" />
    </g>
    
    <!-- Teksty pomocnicze (zakresy) -->
    <g font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle" y="52">
      <text x="120">16.0</text>
      <text x="170">17.0</text>
      <text x="245">18.5</text>
      <text x="570">25.0</text>
      <text x="695">30.0</text>
      <text x="820">35.0</text>
      <text x="945">40.0</text>
    </g>
    
    <!-- Dynamiczny wskaźnik (Marker) -->
    <g id="bmi-marker" style="transition: transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);">
      <polygon points="0,0 -10,-10 10,-10" fill="currentColor" transform="translate(0, 10)" />
      <line x1="0" y1="10" x2="0" y2="40" stroke="currentColor" stroke-width="3" />
    </g>
  </svg>
</div>
```

#### Logika Pozycjonowania Markera (`ui.js`):
Wartość BMI od 15.0 do 45.0 jest mapowana liniowo na współrzędną X od 0 do 1000 pikseli na osi SVG.

```javascript
export function updateMarkerPosition(bmi) {
  const marker = document.getElementById('bmi-marker');
  const minBmi = 15.0;
  const maxBmi = 45.0;
  
  // Ograniczenie wartości do zakresu skali
  const clampedBmi = Math.max(minBmi, Math.min(maxBmi, bmi));
  
  // Obliczenie procentowej pozycji na skali
  const percentage = (clampedBmi - minBmi) / (maxBmi - minBmi);
  const xPosition = percentage * 1000; // Szerokość viewBox to 1000
  
  // Zastosowanie transformacji sprzętowej (GPU) dla płynności 60fps
  marker.style.transform = `translateX(${xPosition}px)`;
}
```

### 5.4. Dostępność (A11Y) i Standardy WCAG 2.1 AA

Aplikacja musi w pełni wspierać standardy dostępności:
1. **Kontrast:** Wszystkie kolory tekstów i tła (w tym w trybie ciemnym) muszą spełniać wymóg kontrastu minimum **4.5:1**. Dla tekstów na kolorowych tłach alertów (np. klasyfikacja WHO) zastosowane zostaną natywne klasy Bootstrap `.alert-*` z odpowiednio dobranymi kolorami tekstu.
2. **Nawigacja Klawiaturą:**
   * Wszystkie pola formularza posiadają logiczną kolejność tabulacji (`tabindex`).
   * Przełącznik systemów miar (metryczny/imperialny) oraz kafelki płci są w pełni obsługiwane za pomocą klawiszy `Space` / `Enter`.
3. **Atrybuty ARIA:**
   * Kontener wyników posiada atrybut `aria-live="polite"`, co powoduje automatyczne odczytanie wyniku przez czytniki ekranu po jego wyliczeniu.
   * Pola z błędami walidacji dynamicznie otrzymują atrybut `aria-invalid="true"` oraz `aria-describedby="[ID_KOMUNIKATU_O_BŁĘDZIE]"`.

---

## 6. Integracje i Udostępnianie (API & Sharing Contracts)

Moduł udostępniania (US-4.1) integruje się z systemowym API przeglądarki (Web Share API) lub stosuje bezpieczny fallback.

### 6.1. Kontrakt Integracyjny Web Share API

Przed wywołaniem API systemowego następuje sprawdzenie jego dostępności w przeglądarce użytkownika.

```javascript
/**
 * Obsługuje proces udostępniania wyniku.
 * @param {number} bmi - Wyliczone BMI
 * @param {string} classification - Tekstowa klasyfikacja WHO
 * @param {string} shareUrl - Unikalny link z zakodowanymi parametrami Base64
 */
export async function shareResult(bmi, classification, shareUrl) {
  const shareData = {
    title: 'Mój Wynik BMI',
    text: `Mój wskaźnik BMI wynosi ${bmi} (${classification}). Sprawdź swoje BMI w nowoczesnej aplikacji SPA!`,
    url: shareUrl
  };

  if (navigator.share && navigator.canShare && navigator.canShare(shareData)) {
    try {
      await navigator.share(shareData);
      showToast("Pomyślnie udostępniono wynik!", "success");
    } catch (err) {
      if (err.name !== 'AbortError') {
        console.error("Błąd Web Share API:", err);
        fallbackShare(shareData);
      }
    }
  } else {
    // Fallback dla przeglądarek desktopowych / niekompatybilnych
    fallbackShare(shareData);
  }
}
```

### 6.2. Fallback dla Mediów Społecznościowych (Desktop)

W przypadku braku wsparcia dla `navigator.share`, aplikacja wyświetla modal/popover z dedykowanymi linkami do serwisów społecznościowych oraz przyciskiem "Kopiuj link do schowka".

#### Szablony Linków Fallback:
* **Facebook:**
  `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(shareUrl)}`
* **Twitter / X:**
  `https://twitter.com/intent/tweet?text=${encodeURIComponent(shareData.text)}&url=${encodeURIComponent(shareUrl)}`
* **WhatsApp:**
  `https://api.whatsapp.com/send?text=${encodeURIComponent(shareData.text + ' ' + shareUrl)}`

#### Kopiowanie do Schowka (Clipboard API):
```javascript
export async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
    showToast("Link został skopiowany do schowka!", "success");
  } catch (err) {
    console.error("Błąd kopiowania do schowka:", err);
    // Ostateczny fallback dla starych przeglądarek
    const textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
    showToast("Link został skopiowany do schowka!", "success");
  }
}
```

---

## 7. Obsługa Sytuacji Wyjątkowych i Bezpieczeństwo

Jako aplikacja typu Local-First, system musi być odporny na błędy środowiskowe po stronie klienta.

### 7.1. Obsługa Błędów IndexedDB (np. Tryb Prywatny / Brak Miejsca)

W niektórych przeglądarkach (np. w trybie incognito Safari/Firefox) dostęp do `IndexedDB` może być zablokowany lub ograniczony.

* **Strategia Mitygacji:**
  * Każda operacja zapisu/odczytu z modułu `storage.js` jest otoczona blokiem `try-catch`.
  * W przypadku rzucenia błędu przez Dexie.js (np. `SecurityError` lub `QuotaExceededError`), aplikacja automatycznie przełącza się w **tryb in-memory (ulotny)**.
  * Użytkownik jest informowany nieinwazyjnym komunikatem (Toast): *"Działasz w trybie prywatnym. Historia obliczeń nie zostanie zapisana po zamknięciu karty."*
  * Logika obliczeniowa działa bez zakłóceń, pomijając jedynie krok zapisu do bazy.

### 7.2. Zabezpieczenie przed Atakami XSS (Cross-Site Scripting)

Ponieważ aplikacja parsuje parametry z URL (`?data=...`), istnieje ryzyko próby wstrzyknięcia złośliwego kodu JS (XSS) poprzez zmodyfikowany link Base64.

* **Strategia Mitygacji:**
  1. **Rygorystyczna Walidacja Typów:** Funkcja `validateDecodedParams` (sekcja 4.3) odrzuca wszelkie dane, które nie są czystymi liczbami lub predefiniowanymi ciągami znaków (`"m"`, `"i"`, `"f"`).
  2. **Bezpieczne Renderowanie DOM:** W module `ui.js` zabrania się używania właściwości `innerHTML` do wstrzykiwania wartości pochodzących z URL lub formularza. Wszystkie dynamiczne wartości liczbowe i tekstowe muszą być wprowadzane do DOM za pomocą bezpiecznej właściwości `textContent` lub `innerText`.

### 7.3. Obsługa Błędnych / Uszkodzonych Linków URL

Jeśli użytkownik wejdzie na stronę z uszkodzonym parametrem `?data=` (np. ucięty ciąg Base64):
* Funkcja `decodeParams` przechwyci błąd parsowania w bloku `try-catch` i zwróci `null`.
* Aplikacja zignoruje uszkodzony parametr, załaduje się w stanie domyślnym (pusty formularz metryczny) i wyświetli Toast ostrzegawczy: *"Nie udało się odtworzyć wyniku z linku – parametry są niepoprawne."*

---

## 8. Wymagania Niefunkcjonalne i Metryki Wydajnościowe

### 8.1. Budżet Wydajnościowy (Performance Budget)

Aplikacja musi osiągać najwyższe wyniki wydajnościowe (Lighthouse Performance Score >= 95).

| Metryka | Cel (Target) | Sposób Realizacji |
| :--- | :--- | :--- |
| **LCP (Largest Contentful Paint)** | `< 1.0s` (sieć 4G) | Brak ciężkich frameworków JS, asynchroniczne ładowanie Bootstrap i Dexie.js przez szybkie CDN (Cloudflare/jsDelivr). |
| **FID (First Input Delay)** | `< 50ms` | Całość logiki UI i obliczeń jest nieblokująca. Operacje I/O (IndexedDB) są asynchroniczne. |
| **CLS (Cumulative Layout Shift)** | `0.0` | Sztywne rezerwowanie wysokości dla kontenerów (np. min-height dla sekcji wyników), aby uniknąć przesuwania layoutu podczas renderowania. |
| **Rozmiar Paczki (Bundle Size)** | `< 100 KB` | Minifikacja własnego kodu JS/CSS. Wykorzystanie wersji produkcyjnych bibliotek zewnętrznych. |

### 8.2. Bezpieczeństwo i Hosting

1. **Wymuszenie HTTPS:** Serwer hostingowy (np. Cloudflare Pages) musi mieć włączoną regułę *Always Use HTTPS* oraz nagłówek *Strict-Transport-Security (HSTS)*.
2. **Content Security Policy (CSP):** Wdrożenie restrykcyjnych nagłówków CSP zezwalających na wykonywanie skryptów wyłącznie z zaufanych źródeł CDN (Bootstrap, Dexie.js) oraz blokujących inline-scripts (`unsafe-inline` dozwolone tylko dla krytycznych stylów CSS, jeśli niezbędne).
