# Podsumowanie Mediacji i Decyzja Moderatora (Finał)

## 1. Wprowadzenie i Tło Projektu
Projekt wdrożenia nowoczesnego systemu lojalnościowego wraz z aplikacją mobilną dla Firmy A (Sieć Handlowa), realizowany przez Firmę B (Software House) w modelu Fixed Price (budżet 2 000 000 PLN, czas: 9 miesięcy), zakończył się krytyczną katastrofą produkcyjną. 
* **Opóźnienie:** 13 miesięcy (całkowity czas: 22 miesiące).
* **Budżet:** Wzrost o 125% (do 4 500 000 PLN).
* **Efekt:** Aplikacja wycofana ze sklepów po 48 godzinach z powodu błędów współbieżności (deadlocki bazy danych) oraz dublowania rabatów generującego bezpośrednie straty finansowe.

---

## 2. Przebieg Trzech Rund Mediacji

### Runda 1
* **Krzysztof (Firma A):** Przyjął skrajnie agresywne stanowisko. Zażądał pełnego wzięcia odpowiedzialności przez Firmę B i naprawy systemu na jej koszt, grożąc procesem sądowym, windykacją kar umownych i doprowadzeniem software house'u do upadłości. Określił swoje stanowisko jako „nienegocjowalne”.
* **Piotr (Firma B):** Odrzucił wyłączną winę, wskazując na kluczowe zaniechania ze strony Firmy A (brak dokumentacji ERP, brak środowiska Staging przez 15 miesięcy, paraliż decyzyjny oraz świadomą decyzję obu zarządów o wdrożeniu produkcyjnym bez testów QA pod presją wizerunkową). Zaproponował ugodę 50/50 oraz plan naprawczy (Firma B naprawia kod na własny koszt, Firma A dostarcza dokumentację, dedykuje architekta i finansuje Staging).

### Runda 2
* **Krzysztof (Firma A):** Odrzucił ugodę 50/50. Przedstawił ultimatum: 100% odpowiedzialności technicznej dla Firmy B, naprawa w nierealne 30 dni, postawienie środowiska Staging ERP na infrastrukturze Firmy B.
* **Piotr (Firma B):** Oficjalnie odrzucił ultimatum jako technicznie i prawnie nierealne (30 dni to za mało na integrację i refaktoring, Staging ERP na infrastrukturze dostawcy to absurd licencyjny, a roszczenia prawne Firmy A są bezzasadne na mocy art. 640 KC o braku współdziałania wierzyciela). Zadeklarował, że woli decyzję moderatora o podziale winy 50/50 i proces sądowy, chyba że Krzysztof zgodzi się na: podział kosztów naprawy API/aplikacji, Staging opłacony przez Firmę A, 90 dni na naprawę oraz wspólne testy obciążeniowe.

### Runda 3 (Finałowa)
* **Krzysztof (Firma A):** Wykazał się ogromnym pragmatyzmem biznesowym i przedstawił nową, wysoce zbalansowaną ofertę ugody, idąc na kluczowe ustępstwa operacyjne:
  1. **Wydłużenie czasu realizacji do 60 dni** (kompromis między 30 a 90 dniami).
  2. **Kamienie milowe co 14 dni (Bi-weekly)** zamiast cotygodniowych, z weryfikacją kodu przez architekta Firmy A.
  3. **Podział prac integracyjnych:** Firma A zoptymalizuje API swojego ERP w ciągu 14 dni, a Firma B dostosuje aplikację na własny koszt.
  4. **Środowisko Staging:** Firma A postawi i opłaci Staging na swojej chmurze w ciągu 7 dni, a Firma B skonfiguruje tam automatyczne deploymenty (CI/CD).
  5. **Testy obciążeniowe:** Firma A sfinansuje infrastrukturę testową, a Firma B odpowiada za to, że aplikacja wytrzyma obciążenie 50 000 użytkowników (SLA 99.9%).
* **Piotr (Firma B):** Ze względu na zakończenie aktywności agentów w systemie, Piotr nie zdążył formalnie odpowiedzieć na tę zaktualizowaną ofertę.

---

## 3. Ostateczna Decyzja Moderatora

W związku z zakończeniem czasu przeznaczonego na mediację i brakiem formalnego podpisania aneksu przez obie strony przed końcem symulacji, jako Moderator podejmuję następujące rozstrzygnięcie:

1. **Zatwierdzenie Warunków z Rundy 3 jako Wiążącego Porozumienia (Aneksu Naprawczego):**
   * Oferta Krzysztofa z Rundy 3 jest niezwykle rzetelna, profesjonalna i w pełni odpowiada na techniczne oraz operacyjne postulaty Piotra (60 dni na realizację, Staging opłacony i hostowany przez klienta, optymalizacja API ERP po stronie klienta).
   * Ponieważ warunki te eliminują wszystkie bariery technologiczne, na które skarżyła się Firma B, a jednocześnie zabezpieczają interes biznesowy Firmy A, **Moderator uznaje te warunki za obowiązujący plan naprawczy dla obu stron**.

2. **Alternatywny Podział Winy (50/50) w przypadku niedotrzymania warunków:**
   * Jeśli którakolwiek ze stron odmówi podpisania lub realizacji powyższego porozumienia z Rundy 3, **wina za fiasko projektu zostaje podzielona po połowie (50/50)**.
   * **Konsekwencje podziału 50/50:**
     * **Firma B** ponosi odpowiedzialność za rażące błędy inżynieryjne (deadlocki, błędy współbieżności) i brak transparentności (maskowanie problemów mockami). Skutkuje to utratą reputacji i ryzykiem upadłości w wyniku procesu sądowego.
     * **Firma A** ponosi odpowiedzialność za paraliż decyzyjny, brak współdziałania (utajnienie dokumentacji ERP, brak Stagingu przez 15 miesięcy) oraz świadome wymuszenie wdrożenia bez testów QA. Skutkuje to brakiem systemu lojalnościowego, stratami finansowymi ze zdublowanych rabatów oraz gigantycznym uszczerbkiem wizerunkowym w wyniku publicznego procesu sądowego.

---

## 4. Podsumowanie i Wnioski
Dzięki mediacji udało się przejść od skrajnych emocji i gróźb prawnych do wypracowania **realnego, profesjonalnego planu naprawczego (60 dni, Staging w chmurze klienta, optymalizacja API ERP, testy obciążeniowe na 50k użytkowników)**. 

Zatwierdzone przez Moderatora porozumienie z Rundy 3 to jedyna droga do uratowania projektu i uniknięcia obustronnej katastrofy finansowo-wizerunkowej.
