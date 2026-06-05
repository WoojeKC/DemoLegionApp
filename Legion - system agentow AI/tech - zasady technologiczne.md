# STOS TECHNOLOGICZNY i WYTYCZNE ARCHITEKTONICZNE (SPA)

Budujesz aplikację w architekturze **Local-First Single-Page Application (SPA)**. Cała logika biznesowa, renderowanie oraz zarządzanie stanem muszą być wykonywane wyłącznie po stronie klienta (w przeglądarce), bez dedykowanej warstwy backendowej.

### 1. Architektura i Zarządzanie Stanem

* **Struktura:** Aplikacja musi być zawarta w jednym pliku HTML (lub logicznie podzielona na komponenty webowe na etapie deweloperskim, ale kompilowana do jednego punktu wejścia), zapewniając natychmiastowe działanie bez przeładowywania strony.
* **Trwałość Danych (Persistence):** * Do przechowywania stanu aplikacji użyj **IndexedDB** (zalecane poprzez lekką bibliotekę-wrapper, np. *Dexie.js* lub *localForage*) zamiast czystego `LocalStorage`. Powód: IndexedDB jest asynchroniczne, nie blokuje wątku głównego (UI thread) i pozwala na bezpieczne operowanie na większych wolumenach danych.
* `LocalStorage` dopuszcza się wyłącznie do prostych flag konfiguracyjnych (np. `theme=dark`).


### 2. Warstwa Wizualna i UX (Bootstrap 5.3+)

* **Framework CSS:** Użyj najnowszej stabilnej wersji **Bootstrap 5.3+** (wersja w pełni pozbawiona jQuery, oparta na natywnym JavaScript).
* **Wsparcie dla Dark Mode:** Wykorzystaj natywną funkcjonalność Bootstrap 5.3 dotyczącą motywów (`data-bs-theme="dark"` / `data-bs-theme="light"`). Interfejs musi automatycznie reagować na ustawienia systemowe użytkownika lub oferować płynny przełącznik (Toggle) w UI.
* **UX i Responsywność:**
* Projektuj zgodnie z zasadą **Mobile-First** przy użyciu systemu siatki (Flexbox/Grid zintegrowany w Bootstrap).
* Zastosuj nowoczesne komponenty Bootstrap (np. *Modals, Toasts* do powiadomień, *Spinners* dla stanów ładowania), aby zapewnić użytkownikowi natychmiastowy, asynchroniczny feedback na jego akcje.



### 3. Logika i Standardy Kodowania (Clean Code)

* **JavaScript:** Pisz w czystym, nowoczesnym standardzie **ES6+**. Architektura kodu musi być modularna (podział na moduły odpowiedzialne za UI, stan i warstwę danych).
* **Dostępność (A11Y):** Każdy komponent Bootstrap musi zachować poprawne atrybuty `aria-*`, semantyczne tagi HTML5 (`<main>`, `<nav>`, `<section>`), oraz pełną obsługę nawigacji klawiaturą.
* **Wydajność UX:** Wszystkie operacje zapisu/odczytu z pamięci przeglądarki muszą być asynchroniczne (`async/await`), aby uniknąć mikro-zamrożeń interfejsu (Layout Shifts i Input Lag).

