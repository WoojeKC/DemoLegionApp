# Raport ze Sparingi Decyzyjnego: Wdrożenie Scoringu AI w Banku Detalicznym

## 1. Podsumowanie Sparingi
Sparing dotyczył wyboru modelu scoringowego opartego na AI dla banku detalicznego (3 mln klientów) z twardym terminem wdrożenia wynoszącym 6 miesięcy. 
* **Krzysztof** bronił pozycji **BLACK-BOX (Maksymalna Skuteczność)**, proponując model LightGBM z silnikiem wyjaśnień post-hoc SHAP.
* **Piotr** bronił pozycji **MODEL WYJAŚNIALNY (Odporność Regulacyjna)**, proponując model GAM / EBM (Explainable Boosting Machine) wdrażany jako kod SQL.

W trakcie sparingu agenci musieli zmierzyć się z **twardym faktem z zewnątrz (Wariant 3)**: model LightGBM odrzucał wnioski określonej grupy demograficznej o 15% częściej niż stary model regułowy, co wywołało kryzys medialny.

---

## 2. Karta Punktowa (Skala 1–5)

| Kryterium | Krzysztof (Black-Box / Treelite) | Piotr (GAM / SQL) |
| :--- | :---: | :---: |
| **1. First Principles** | **5/5** | **4/5** |
| **2. Twarde Liczby** | **5/5** | **3/5** |
| **3. Zderzenie z Rzeczywistością** | **5/5** | **3/5** |
| **4. Idiot Index** (wyższa ocena = lepszy/niższy indeks) | **5/5** | **3/5** |
| **5. Intelektualna Uczciwość** | **4/5** | **3/5** |
| **SUMA** | **24/25** | **16/25** |

---

## 3. Uzasadnienie Punkt po Punkcie

### 1. First Principles (Prawdy pierwsze i ekonomiczne)
* **Krzysztof (5/5):** Genialnie rozbił problem na funkcję matematyczną i ekonomię przetrwania banku. W ostatniej rundzie popisał się głębokim zrozumieniem matematyki debiasingu (Equal Opportunity, Threshold Optimizer) oraz fizyki wdrożenia IT (kompilacja do C++ przez Treelite). Pokazał, że problemem nie jest technologia, ale jakość danych i kalibracja progów.
* **Piotr (4/5):** Dobrze zdefiniował ograniczenia prawne (Art. 105a Prawa Bankowego) i architekturę legacy. Jednak jego fundamentalne założenie, że model GAM nie dyskryminuje, zostało obalone. Model uczący się na skażonych historycznie danych zawsze odtworzy bias, niezależnie od swojej architektury.

### 2. Twarde Liczby (Policzalność i precyzja)
* **Krzysztof (5/5):** Przedstawił bezbłędny rachunek ekonomiczny. Wyliczył, że przy portfelu 4.5 mld PLN i default rate 5%, różnica 9 punktów Gini (0.74 vs 0.65) to aż **40.5 mln PLN rocznie**. Po zastosowaniu filtrów antydyskryminacyjnych jego Gini spada do 0.73, co wciąż daje **9 mln PLN rocznie przewagi** nad Piotrem. Podał też twarde parametry techniczne (predykcja <1ms dzięki Treelite).
* **Piotr (3/5):** Podał liczby (Gini 0.71, 60 dni wdrożenia), ale jego szacunki strat finansowych (5-8 mln PLN przy różnicy Gini) zostały matematycznie zmiażdżone przez Krzysztofa. Piotr drastycznie zaniżył koszt utraconych korzyści, co osłabiło jego argumentację biznesową przed zarządem.

### 3. Zderzenie z Rzeczywistością (Deadline i regulacje)
* **Krzysztof (5/5):** Początkowo jego plan z Dockerem w 4 miesiące na legacy IT był ryzykowny (co Piotr słusznie punktował). Jednak Krzysztof dokonał genialnego zwrotu (fast iteration) i zaproponował kompilację modelu do natywnego kodu C++ (Treelite/ONNX). To całkowicie omija "MLOps Hell", nie wymaga zmian sieciowych i przechodzi audyt bezpieczeństwa w 5 dni. Dodatkowo, matematyczny debiasing (Fairlearn) rozwiązuje kryzys wizerunkowy w sposób akceptowalny dla KNF.
* **Piotr (3/5):** Jego plan wdrożenia GAM jako "prosty SQL" w 14 dni brzmi dobrze tylko na papierze. EBM z interakcjami par wyeksportowany do SQL generuje potwora z setkami tysięcy linii kodu `CASE WHEN`, który zarżnie wydajność bazy danych przy 3 mln klientów. Co gorsza, jego propozycja "ręcznego spłaszczania wykresów suwakami" to arbitralna manipulacja, którą audyt KNF natychmiast odrzuci jako brak rygoru metodologicznego.

### 4. Idiot Index (Marnotrawstwo ponad fundament)
* **Krzysztof (5/5 - Bardzo niski Idiot Index):** Dzięki kompilacji do C++ (Treelite) koszt infrastruktury wynosi 0 PLN, a model przynosi 33.7 mln PLN zysku netto rocznie (po uwzględnieniu debiasingu). Rozwiązanie jest maksymalnie odchudzone i efektywne.
* **Piotr (3/5 - Średni Idiot Index):** Choć koszty wdrożenia SQL to 0 PLN, to ukryty koszt marnotrawstwa (9 mln PLN rocznie utraconych korzyści z tytułu niższego Gini oraz ryzyko zablokowania bazy danych przez niewydajny SQL) drastycznie podnosi ten indeks.

### 5. Intelektualna Uczciwość (Adaptacja do danych vs Ego)
* **Krzysztof (4/5):** Choć w drugiej rundzie zignorował kryzys biasu (za co dostał ostrzeżenie), to w trzeciej rundzie wrócił z potężnym, merytorycznym rozwiązaniem matematycznym (Threshold Optimizer), przyznając, że Gini spadnie z 0.74 do 0.73. Nie bronił ślepo "czystego" LightGBM, tylko zaadaptował model do wymogów regulacyjnych.
* **Piotr (3/5):** Bronił swojej tezy o "bezpiecznym SQL" i niskich stratach Gini, ignorując fakt, że jego model również uczy się na skażonych danych i będzie dyskryminował. Nie potrafił zaproponować systemowego rozwiązania biasu poza "ręcznym klikaniem suwakami", co jest niedopuszczalne w regulowanym banku.

---

## 4. Werdykt Końcowy

* **ZWYCIĘZCA:** **Krzysztof (BLACK-BOX / Treelite)**
* **PRZEGRANY:** **Piotr (MODEL WYJAŚNIALNY / SQL)**

### Dlaczego Krzysztof wygrał?
Krzysztof wygrał, ponieważ przedstawił plan, który jest **matematycznie nadrzędny, ekonomicznie bezkonkurencyjny i technologicznie genialny w swojej prostocie**. 

Zamiast brnąć w skomplikowane i powolne wdrażanie platformy MLOps (co słusznie krytykował Piotr), Krzysztof uprościł wdrożenie do absolutnego minimum: skompilował model LightGBM do natywnej biblioteki C++ (Treelite). To pozwoliło na wdrożenie zaawansowanego modelu w kilka dni bezpośrednio na legacy IT, z czasem predykcji <1ms i przy zerowych kosztach infrastruktury.

Co najważniejsze, Krzysztof nie uciekł przed kryzysem dyskryminacyjnym. Zamiast "ręcznego suwania wykresów" (co zaproponował Piotr, a co KNF uznałby za kryminał), Krzysztof zastosował rygorystyczny, matematyczny debiasing (Threshold Optimizer / Equal Opportunity), który zredukował bias do 0%, zachowując Gini na poziomie 0.73 (o 2 punkty lepiej niż GAM Piotra, co daje bankowi dodatkowe 9 mln PLN rocznie).

### Gdzie przegrał Piotr?
Piotr przegrał na poziomie **zderzenia z rzeczywistością technologiczną i regulacyjną**. Jego "bezpieczny SQL" okazał się wydajnościową bombą zegarową, która przy 3 mln klientów zablokowałaby systemy transakcyjne banku. Dodatkowo, jego propozycja ręcznej modyfikacji wag modelu ("suwaki na mikserze") obnażyła brak rygoru statystycznego – KNF nigdy nie pozwoliłby na to, aby analitycy ręcznie decydowali o scoringu wybranych grup społecznych. Piotr zaniżył również straty finansowe wynikające z niższego Gini, próbując sprzedać zarządowi gorszy model pod płaszczykiem fałszywego bezpieczeństwa.
