# INSTRUKCJA UŻYTKOWNIKA (USER MANUAL)
## ChronosApp — Nowoczesna Aplikacja Zegara i Alertyzacji
**Wersja dokumentu:** 1.0  
**Status:** Gotowy do weryfikacji  
**Data publikacji:** 31 maja 2026 r.  
**Zgodność z wersją aplikacji:** v1.0.0  

---

## Witamy w ChronosApp!
Dziękujemy za wybór **ChronosApp** – zaawansowanego, a zarazem minimalistycznego narzędzia do zarządzania czasem. Aplikacja została zaprojektowana z myślą o maksymalnej niezawodności, wyjątkowej ergonomii (UX) oraz optymalizacji zużycia energii (AMOLED Black). 

Niniejsza instrukcja przeprowadzi Cię przez wszystkie funkcje aplikacji, pomagając w pełni wykorzystać jej potencjał w codziennym życiu, pracy oraz treningach.

---

## Spis Treści
1. [Pierwsze Uruchomienie i Konfiguracja Początkowa](#1-pierwsze-uruchomienie-i-konfiguracja-początkowa)
   - [Automatyczne wykrywanie strefy czasowej](#automatyczne-wykrywanie-strefy-czasowej)
   - [Odblokowanie dźwięku (Baner Autoplay)](#odblokowanie-dźwięku-baner-autoplay)
   - [Uprawnienia systemowe (Powiadomienia i praca w tle)](#uprawnienia-systemowe-powiadomienia-i-praca-w-tle)
2. [Moduł 1: Czas Światowy (World Clock)](#moduł-1-czas-światowy-world-clock)
   - [Dodawanie nowej strefy czasowej](#dodawanie-nowej-strefy-czasowej)
   - [Zarządzanie listą „Moje Strefy”](#zarządzanie-listą-moje-strefy)
   - [Automatyczna obsługa czasu letniego/zimowego (DST)](#automatyczna-obsługa-czasu-letniegozimowego-dst)
3. [Moduł 2: Precyzyjny Stoper (Stopwatch)](#moduł-2-precyzyjny-stoper-stopwatch)
   - [Podstawowy pomiar czasu](#podstawowy-pomiar-czasu)
   - [Zapisywanie międzyczasów (Okrążenia / Laps)](#zapisywanie-międzyczasów-okrążenia--laps)
   - [Automatyczna analityka okrążeń (Ekstrema)](#automatyczna-analityka-okrążeń-ekstrema)
   - [Ciągłość pomiaru w tle i po restarcie](#ciągłość-pomiaru-w-tle-i-po-restarcie)
4. [Moduł 3: Wielowątkowy Minutnik (Timer)](#moduł-3-wielowątkowy-minutnik-timer)
   - [Uruchamianie wielu minutników jednocześnie](#uruchamianie-wielu-minutników-jednocześnie)
   - [Zarządzanie szablonami szybkiego wyboru (Presets)](#zarządzanie-szablonami-szybkiego-wyboru-presets)
   - [Niezależna kontrola i usuwanie minutników](#niezależna-kontrola-i-usuwanie-minutników)
5. [Moduł 4: Inteligentny System Alarmów (Alarms)](#moduł-4-inteligentny-system-alarmów-alarms)
   - [Tworzenie i edycja alarmów](#tworzenie-i-edycja-alarmów)
   - [Harmonogram powtarzalności (Dni tygodnia)](#harmonogram-powtarzalności-dni-tygodnia)
   - [Mechanizm drzemki (Snooze) i limity powtórzeń](#mechanizm-drzemki-snooze-i-limity-powtórzeń)
   - [Łagodne wybudzanie (Fade-in) i profile dźwiękowe](#łagodne-wybudzanie-fade-in-i-profile-dźwiękowe)
   - [Obsługa połączeń telefonicznych (Tryb dyskretny)](#obsługa-połączeń-telefonicznych-tryb-dyskretny)
6. [Ekran Ustawień (Settings) i Personalizacja](#ekran-ustawień-settings-i-personalizacja)
   - [Przełączanie motywów (Jasny, Ciemny, Systemowy)](#przełączanie-motywów-jasny-ciemny-systemowy)
   - [Oszczędzanie energii (AMOLED Black)](#oszczędzanie-energii-amoled-black)
7. [Działanie w Tle i Rozwiązywanie Problemów (Troubleshooting)](#działanie-w-tle-i-rozwiązywanie-problemów-troubleshooting)
   - [Service Worker i powiadomienia systemowe](#service-worker-i-powiadomienia-systemowe)
   - [Optymalizacja baterii (Doze Mode / Autostart)](#optymalizacja-baterii-doze-mode--autostart)
   - [Co zrobić, gdy nie słychać alarmu?](#co-zrobić-gdy-nie-słychać-alarmu)

---

## 1. Pierwsze Uruchomienie i Konfiguracja Początkowa

### Automatyczne wykrywanie strefy czasowej
Przy pierwszym uruchomieniu ChronosApp automatycznie wykrywa Twoją lokalizację oraz strefę czasową skonfigurowaną w systemie operacyjnym urządzenia. 
*   **Jak to działa:** Aplikacja odczytuje ustawienia regionalne i ustawia Twoją strefę domową jako główny punkt odniesienia na ekranie czasu światowego.
*   **Brak uprawnień:** Jeśli zablokujesz dostęp do lokalizacji, aplikacja bezpiecznie pobierze strefę czasową bezpośrednio z zegara systemowego (np. `Europe/Warsaw`).

### Odblokowanie dźwięku (Baner Autoplay)
Ze względu na rygorystyczne polityki bezpieczeństwa nowoczesnych przeglądarek internetowych oraz systemów operacyjnych (tzw. *Autoplay Policy*), odtwarzanie dźwięków bez wcześniejszej interakcji użytkownika z ekranem jest blokowane.
*   **Baner odblokowania:** Przy pierwszym uruchomieniu aplikacji (lub po jej zresetowaniu) na górze ekranu pojawi się dyskretny baner informacyjny:  
    `🔔 Aby zapewnić poprawne działanie alarmów i minutników, kliknij tutaj, aby odblokować dźwięki.`
*   **Co należy zrobić:** Kliknij baner. Spowoduje to jednorazowe udzielenie aplikacji zgody na odtwarzanie sygnałów dźwiękowych w tle. Po kliknięciu baner zniknie, a system audio zostanie w pełni aktywowany.

### Uprawnienia systemowe (Powiadomienia i praca w tle)
Aby ChronosApp mogła niezawodnie powiadamiać Cię o alarmach i zakończeniu odliczania minutników, podczas pierwszego uruchomienia zostaniesz poproszony o:
1.  **Zgodę na wysyłanie powiadomień push/lokalnych:** Kliknij „Zezwól” w oknie systemowym. Bez tego powiadomienia o alarmach nie będą wyświetlać się na zablokowanym ekranie.
2.  **Zgodę na działanie w tle (Ignorowanie optymalizacji baterii):** Na urządzeniach z systemem Android zalecamy wyłączenie optymalizacji zużycia energii dla ChronosApp (szczegóły w sekcji [Troubleshooting](#optymalizacja-baterii-doze-mode--autostart)).

---

## 2. Moduł 1: Czas Światowy (World Clock)

Moduł Czasu Światowego pozwala na jednoczesne monitorowanie czasu w różnych zakątkach globu. Jest to idealne rozwiązanie dla osób pracujących w międzynarodowych zespołach, podróżników oraz inwestorów giełdowych.

```
+--------------------------------------------------+
| WORLD CLOCK                               [ + ]  |
+--------------------------------------------------+
| Warszawa (Lokalny)                      14:35:02 |
| Środa, 31 maja 2026                              |
+--------------------------------------------------+
| New York (EST) -6h                      08:35:02 |
| Środa, 31 maja 2026                              |
+--------------------------------------------------+
| Tokyo (JST) +7h                         21:35:02 |
| Środa, 31 maja 2026                              |
+--------------------------------------------------+
```

### Dodawanie nowej strefy czasowej
1.  Przejdź do zakładki **Czas Światowy** (ikona globu w dolnym menu).
2.  Kliknij przycisk **Dodaj [ + ]** w prawym górnym rogu ekranu.
3.  W polu wyszukiwania zacznij wpisywać:
    *   **Nazwę miasta** (np. `Londyn`, `Nowy Jork`, `Tokio`),
    *   **Nazwę kraju** (np. `Wielka Brytania`, `Japonia`),
    *   **Skrót strefy** (np. `GMT`, `EST`, `CET`, `JST`).
4.  Wyszukiwarka działa w trybie autouzupełniania – pasujące wyniki pojawią się natychmiast po wpisaniu pierwszego znaku.
5.  Kliknij wybraną strefę na liście wyników, aby dodać ją do ekranu głównego.

### Zarządzanie listą „Moje Strefy”
*   **Limit stref:** Możesz dodać maksymalnie **10 aktywnych stref czasowych** jednocześnie. Po osiągnięciu tego limitu przycisk dodawania zostanie zablokowany.
*   **Usuwanie strefy:** Aby usunąć strefę z listy, przesuń palcem po jej nazwie w lewo (gest *swipe-to-delete*) lub kliknij przycisk **Edytuj**, a następnie ikonę czerwonego kosza przy wybranej strefie.
*   **Różnica czasu:** Pod nazwą każdej dodanej strefy wyświetla się informacja o przesunięciu czasowym względem Twojej lokalizacji domowej (np. `-6 godzin` lub `+7 godzin`).

### Automatyczna obsługa czasu letniego/zimowego (DST)
Nie musisz martwić się o ręczne przestawianie zegarków. ChronosApp korzysta z globalnej, na bieżąco aktualizowanej bazy danych stref czasowych **IANA (tz database)**. Przejścia na czas letni (DST) i zimowy odbywają się w pełni automatycznie i niezauważalnie dla użytkownika, gwarantując poprawność wskazań co do sekundy.

---

## 3. Moduł 2: Precyzyjny Stoper (Stopwatch)

Stoper w ChronosApp to profesjonalne narzędzie pomiarowe o wysokiej dokładności, wyposażone w inteligentną analitykę wyników.

```
+--------------------------------------------------+
| STOPWATCH                                        |
+--------------------------------------------------+
|                   01:24.58                       |
+--------------------------------------------------+
|   [ Okrążenie ]                    [ Pauza ]     |
+--------------------------------------------------+
| Okrążenie 3        00:12.15 (Najszybsze)         |
| Okrążenie 2        00:45.20 (Najwolniejsze)      |
| Okrążenie 1        00:27.23                      |
+--------------------------------------------------+
```

### Podstawowy pomiar czasu
*   **Start:** Kliknij zielony przycisk **Start**, aby rozpocząć odliczanie. Czas mierzony jest z dokładnością do **0.01 sekundy** (setne części sekundy).
*   **Pauza:** Kliknij czerwony przycisk **Pauza**, aby wstrzymać pomiar. Licznik zatrzyma się, a przycisk zmieni nazwę na **Wznów**.
*   **Reset:** Gdy stoper jest zapauzowany, kliknij przycisk **Reset**, aby wyzerować licznik (`00:00.00`) i wyczyścić listę międzyczasów.

### Zapisywanie międzyczasów (Okrążenia / Laps)
Podczas gdy stoper działa, kliknięcie przycisku **Okrążenie** (Lap) powoduje zapisanie bieżącego stanu licznika na liście poniżej, bez zatrzymywania głównego pomiaru. Licznik bieżącego okrążenia automatycznie startuje od zera, umożliwiając precyzyjny pomiar kolejnego etapu.

### Automatyczna analityka okrążeń (Ekstrema)
Gdy zarejestrujesz **minimum 3 okrążenia**, ChronosApp automatycznie przeanalizuje Twoje wyniki i wyróżni je kolorystycznie na liście:
*   🟢 **Kolor zielony:** Oznacza Twoje **najszybsze okrążenie** (najkrótszy czas).
*   🔴 **Kolor czerwony:** Oznacza Twoje **najwolniejsze okrążenie** (najdłuższy czas).

Analityka działa dynamicznie – jeśli kolejne okrążenie pobije dotychczasowy rekord, kolory automatycznie dostosują się do nowych wyników.

### Ciągłość pomiaru w tle i po restarcie
Stoper w ChronosApp jest odporny na zakłócenia zewnętrzne:
*   Możesz zminimalizować aplikację, zablokować telefon lub pisać wiadomości – stoper działa nieprzerwanie w tle.
*   Nawet jeśli Twój telefon nagle się rozładuje lub system zamknie aplikację, po ponownym uruchomieniu ChronosApp stoper odtworzy swój stan i precyzyjnie przeliczy czas, który upłynął (na podstawie bezpiecznego czasu serwerów NTP), nie gubiąc ani setnej sekundy.

---

## 4. Moduł 3: Wielowątkowy Minutnik (Timer)

Moduł Minutnika umożliwia jednoczesne śledzenie wielu niezależnych procesów odliczania wstecznego.

```
+--------------------------------------------------+
| TIMERS                                     [ + ] |
+--------------------------------------------------+
| Makarony (Aktywny)                      00:04:12 |
| [|| Pauza] [x Usuń]                              |
+--------------------------------------------------+
| Pieczenie ciasta (Zapauzowany)          00:35:00 |
| [> Wznów] [x Usuń]                               |
+--------------------------------------------------+
| Szybki wybór (Presets):                          |
| [ 3 min ]  [ 5 min ]  [ 15 min ]  [ 45 min ]     |
+--------------------------------------------------+
```

### Uruchamianie wielu minutników jednocześnie
ChronosApp pozwala na jednoczesne uruchomienie do **5 niezależnych minutników**.
1.  Przejdź do zakładki **Minutnik**.
2.  Kliknij przycisk **Dodaj [ + ]**.
3.  Za pomocą bębnów wyboru ustaw czas (godziny, minuty, sekundy).
4.  Wpisz **Etykietę** dla minutnika (np. `Makarony`, `Pranie`, `Trening`), aby łatwo go zidentyfikować.
5.  Kliknij **Start**.

### Zarządzanie szablonami szybkiego wyboru (Presets)
Jeśli często korzystasz z tych samych czasów odliczania, możesz zapisać je jako szablony:
*   **Tworzenie szablonu:** Podczas ustawiania nowego minutnika kliknij przycisk **Zapisz jako szablon**. Szablon pojawi się w sekcji „Szybki wybór” na dole ekranu.
*   **Uruchamianie z szablonu:** Kliknij na kafelek wybranego szablonu (np. `3 min` lub `45 min`), a minutnik zostanie natychmiast utworzony i uruchomiony.
*   **Usuwanie szablonu:** Przytrzymaj dłużej kafelek szablonu i kliknij ikonę kosza, aby go usunąć.

### Niezależna kontrola i usuwanie minutników
Każdy minutnik na liście posiada własny zestaw przycisków kontrolnych:
*   **Pauza / Wznów:** Wstrzymuje lub wznawia odliczanie konkretnego minutnika.
*   **Reset:** Przywraca początkowy czas odliczania.
*   **Usuń (X):** Całkowicie kasuje minutnik z listy, zwalniając miejsce na nowy (pamiętaj o limicie 5 aktywnych minutników).

Po zakończeniu odliczania minutnika usłyszysz wyraźny sygnał dźwiękowy, a na ekranie pojawi się powiadomienie z nazwą etykiety.

---

## 5. Moduł 4: Inteligentny System Alarmów (Alarms)

Moduł Alarmów został zaprojektowany tak, aby zagwarantować Ci niezawodne wybudzenie przy jednoczesnym zachowaniu maksymalnego komfortu i braku porannego stresu.

```
+--------------------------------------------------+
| ALARMS                                     [ + ] |
+--------------------------------------------------+
| 07:00                                            |
| Pon, Wt, Śr, Czw, Pt                 [ Włączony ]|
| Dźwięk: Standard, Drzemka: 9 min                 |
+--------------------------------------------------+
| 09:30                                            |
| Sob, Niedz                           [ Wyłączony]|
| Dźwięk: Tylko wibracje                           |
+--------------------------------------------------+
```

### Tworzenie i edycja alarmów
1.  Przejdź do zakładki **Alarmy**.
2.  Kliknij przycisk **Dodaj [ + ]** lub kliknij na istniejący alarm, aby go edytować.
3.  Ustaw pożądaną godzinę i minutę.

### Harmonogram powtarzalności (Dni tygodnia)
Możesz precyzyjnie określić, w które dni alarm ma być aktywny:
*   W sekcji **Powtarzaj** zaznacz wybrane dni tygodnia (np. od poniedziałku do piątku dla pracy, lub tylko weekendy).
*   **Alarmy jednorazowe:** Jeśli nie zaznaczysz żadnego dnia, alarm zadzwoni tylko raz (najbliższego dnia o ustawionej godzinie), a po wyzwoleniu automatycznie się wyłączy.

### Mechanizm drzemki (Snooze) i limity powtórzeń
Dostosuj zachowanie alarmu, gdy potrzebujesz jeszcze kilku minut snu:
*   **Czas drzemki:** Wybierz długość drzemki (domyślnie **9 minut**, dostępne opcje: `5`, `10`, `15 minut`).
*   **Limit drzemek:** Możesz ustawić maksymalną liczbę dozwolonych drzemek (np. maksymalnie **3 drzemki**). Po osiągnięciu tego limitu przycisk „Drzemka” zniknie z ekranu wyzwolonego alarmu, zmuszając Cię do wstania i całkowitego wyłączenia budzika.

### Łagodne wybudzanie (Fade-in) i profile dźwiękowe
*   **Liniowe pogłaśnianie (Fade-in):** Aby zapobiec nagłemu wybudzeniu ze stresu, dźwięk alarmu rozpoczyna się od bardzo cichego poziomu (**10% głośności**) i liniowo, łagodnie wzrasta do **100% w ciągu 15 sekund**.
*   **Profile dźwiękowe:** W ustawieniach alarmu możesz wybrać jeden z dwóch profili:
    1.  **Dźwięk i Wibracje:** Standardowy, pełny tryb alarmu.
    2.  **Tylko wibracje (Tryb dyskretny):** Urządzenie nie wyda żadnego dźwięku, a jedynie uruchomi intensywne, cykliczne wibracje. Idealne rozwiązanie, gdy nie chcesz budzić partnera lub śpisz w podróży.

### Obsługa połączeń telefonicznych (Tryb dyskretny)
Jeśli alarm wyzwoli się w trakcie, gdy prowadzisz aktywną rozmowę telefoniczną, ChronosApp automatycznie dostosuje się, aby nie uszkodzić Twojego słuchu:
*   Głośnik zewnętrzny pozostanie wyciszony.
*   W słuchawce usłyszysz łagodny, cichy sygnał powiadomienia (beeping).
*   Telefon uruchomi intensywne wibracje, a na ekranie pojawi się standardowy panel wyłączenia alarmu.

---

## 6. Ekran Ustawień (Settings) i Personalizacja

Ekran Ustawień (dostępny po kliknięciu ikony koła zębatego) pozwala dostosować wygląd i zachowanie aplikacji do Twoich indywidualnych preferencji.

### Przełączanie motywów (Jasny, Ciemny, Systemowy)
ChronosApp oferuje trzy tryby wyświetlania interfejsu:
1.  **Jasny (Light Mode):** Oparty na eleganckich odcieniach złamanej bieli i jasnej szarości (zakres kolorów `#F8F9FA` do `#EDF2F7`). Zapewnia doskonałą czytelność w pełnym słońcu i spełnia rygorystyczne normy kontrastu WCAG 2.1 AA (kontrast minimum 4.5:1).
2.  **Ciemny (Dark Mode - Pure Black):** Dedykowany tryb nocny oparty o głęboką, czystą czerń (HEX `#000000`).
3.  **Zgodnie z systemem:** Aplikacja automatycznie dostosuje swój wygląd do globalnych ustawień Twojego urządzenia (np. włączy tryb ciemny po zachodzie słońca).

*Przełączanie motywów odbywa się całkowicie płynnie – bez restartowania aplikacji i bez ryzyka utraty jakichkolwiek danych sesyjnych (np. działającego stopera).*

### Oszczędzanie energii (AMOLED Black)
Jeśli posiadasz urządzenie z ekranem typu **OLED** lub **AMOLED** (większość nowoczesnych smartfonów), korzystanie z motywu **Ciemnego (Pure Black)** pozwala na realne oszczędzanie energii baterii. 
*   **Jak to działa:** W technologii AMOLED wyświetlenie koloru czysto czarnego (`#000000`) polega na całkowitym wyłączeniu poszczególnych pikseli ekranu. Dzięki temu ekran zużywa do **15-20% mniej energii** w porównaniu do standardowych motywów ciemnoszarych.

---

## 7. Działanie w Tle i Rozwiązywanie Problemów (Troubleshooting)

### Service Worker i powiadomienia systemowe
W wersji webowej (PWA) ChronosApp wykorzystuje zaawansowany mechanizm **Service Worker**. Działa on jako niezależny proces w tle Twojej przeglądarki. Dzięki temu, nawet jeśli zamkniesz kartę z aplikacją, Service Worker dba o to, aby Twoje minutniki i alarmy zostały wyzwolone dokładnie o czasie, wysyłając systemowe powiadomienie push.

### Optymalizacja baterii (Doze Mode / Autostart)
Nowoczesne systemy operacyjne (szczególnie Android) posiadają agresywne mechanizmy oszczędzania baterii, które potrafią „ubić” procesy w tle lub opóźnić powiadomienia. Aby zapewnić 100% niezawodności ChronosApp, wykonaj poniższe kroki:

#### Dla systemu Android:
1.  Wejdź w **Ustawienia** telefonu -> **Aplikacje** -> **ChronosApp**.
2.  Wybierz sekcję **Bateria** lub **Zużycie energii**.
3.  Zmień ustawienie na **Nieograniczone** (lub wyłącz opcję „Optymalizuj zużycie baterii”).
4.  Upewnij się, że opcja **Autostart / Uruchamianie w tle** jest włączona.

#### Dla systemu iOS:
1.  Wejdź w **Ustawienia** -> **ChronosApp**.
2.  Upewnij się, że opcja **Odświeżanie w tle** (Background App Refresh) jest włączona.

### Co zrobić, gdy nie słychać alarmu?
Jeśli alarmy wyzwalają się wizualnie, ale nie słyszysz dźwięku, sprawdź poniższe punkty:
1.  **Czy odblokowano dźwięk?** Upewnij się, że po uruchomieniu aplikacji kliknięto baner odblokowania dźwięku (patrz sekcja [Odblokowanie dźwięku](#odblokowanie-dźwięku-baner-autoplay)).
2.  **Głośność multimediów/alarmów:** Sprawdź fizycznymi przyciskami głośności na boku telefonu, czy głośność alarmów lub multimediów nie jest wyciszona do zera.
3.  **Tryb Nie Przeszkadzać (Do Not Disturb):** Upewnij się, że Twój telefon nie ma włączonego trybu „Nie przeszkadzać”, który blokuje dźwięki powiadomień (chyba że w ustawieniach systemu dodałeś ChronosApp jako wyjątek o wysokim priorytecie).

---
*ChronosApp — Twój czas pod pełną kontrolą. W razie dalszych pytań skontaktuj się z naszym działem wsparcia technicznego.*
