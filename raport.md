# 1. Automat biletowy MPK
## Opis zadania 

- Automat przechowuje informacje o monetach/banknotach znajdujących się w nim (1, 2, 5, 10, 20, 50gr, 1, 2, 5, 10, 20, 50zł) [dziedziczenie: można napisać uniwersalną klasę PrzechowywaczMonet po której dziedziczyć będzie automat]
- Okno z listą biletów w różnych cenach (jako przyciski). Wymagane bilety: 20-minutowy, 40-minutowy, 60-minutowy w wariantach normalnym i ulgowym.
- Możliwość wybrania więcej niż jednego rodzaju biletu. Możliwość wprowadzenia liczby biletów.
- Po wybraniu biletu pojawia się okno z listą monet (przyciski) oraz możliwością dodania kolejnego biletu lub liczby biletów
- Interfejs ma dodatkowo zawierać pole na wybór liczby wrzucanych monet (domyślnie jedna).
- Po wrzuceniu monet, których wartość jest większa lub równa cenie wybranych biletów, automat sprawdza czy może wydać resztę.
    - Brak reszty/może wydać: wyskakuje okienko z informacją o zakupach, wydaje resztę (dolicza wrzucone monety, odlicza wydane jako reszta), wraca do wyboru biletów.
    - Nie może wydać: wyskakuje okienko z napisem "Tylko odliczona kwota" oraz zwraca włożone monety. 
    
## Github
https://github.com/KarolBochenek/AutomatBiletowyMPK-PK.git


## Klasy, istotne metody i moduły


### Klasa [PrzechowywaczMonet](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/PrzechowywaczMonet.py#L8)
Klasa odpowiadająca za przechowywanie listy monet aktualnie wrzuconych do automatu wraz z ich wartościami.

#### Metoda [addCoin](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/PrzechowywaczMonet.py#L15)
Metoda odpowiadająca za dodanie danego biletu lub kilku biletów do listy biletów aktualnie przechowywanych w automacie.

#### Metoda [potwierdzIlosc](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/PrzechowywaczMonet.py#L25)
Metoda odpowiedzialna za sprawdzenie poprawności wrzuconej ilości - tzn. czy nie jest ujemna lub niecałkowita.


### Klasa [Automat](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/23527f9af7c86dc97d5791002f59bf73e4a155b3/src/Automat.py)
Klasa zajmująca się obsługą ceny, wydawania reszty. Dziedziczy ona po klasie PrzechowywaczMonet.

#### Metoda [remainderCalculator](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Automat.py#L29)
Metoda zajmująca się obliczaniem reszty w zależności od wrzuconej kwoty.



### Moduł [Interfejs](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Interfejs.py)
Odpowiada za wszystko, co wyświetla się na ekranie, osługę przycisków, odpowiedzi do działań użytkownika.

#### Klasa [StartPage](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Interfejs.py#L25)
Odpowiada za wstępną inicjalizację, wczytanie początkowych monet dostępnych w automacie oraz przejście do ekranu wyboru biletów.

#### Klasa [PageOne](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Interfejs.py#L42)
Wyświetla pierwszą ramkę, w której użytkownik dokonuje wyboru biletu wraz z ilością. Posiada metodę ticketsAdder, która iteruje w poszukiwaniu biletów oraz odpowiada za sprawdzenie poprawności wprowadzanej ilości biletów.

#### Klasa [PageTwo](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Interfejs.py#L125)
Wyświetla ramkę do płatności monetami. Posiada metodę finishTransaction, która wydaje ewentualną resztę.



### Moduł [exception](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/tree/main/exception)
Moduł odpowiedzialny za obsługę wyjątków.

#### Klasa [BrakMonetDoWydania](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/exception/BrakMonetDoWydania.py#L1)
Wyjątek wyrzucany w momencie, kiedy w automacie nie ma monet do wydania reszty.

#### Klasa [BrakWybranegoBiletu](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/exception/BrakWybranegoBiletu.py#L1)
Wyjątek wyrzucany, gdy nie wybierzemy żadnego biletu (wybierzemy ilość 0)

#### Klasa [NiewlasciwaIloscBiletow](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/exception/NiewlasciwaIloscBiletow.py#L1)
Wyjątek wyrzucany, gdy wprowadzona ilość biletów jest nieprawidłowa - ujemna bądź niecałkowita.

#### Klasa [NiewlasciwaIloscMonet](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/exception/NiewlasciwaIloscMonet.py#L1)
Wyjątek wyrzucany, gdy wprowadzona ilość monet jest nieprawdiłowa - ujemna bądź niecałkowita.



### Moduł [Test](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Test.py)

#### Metoda [test_shouldRetunrNoRemainder](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Test.py#L13)
Bilet kupiony za odliczoną kwotę. Oczekiwany brak reszty.

#### Metoda [test_shouldReturnRemainder](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Test.py#L28)
Bilet kupiony za kwotę wyższą, niż cena biletu. Oczekiwana reszta.

#### Metoda [test_shouldReturnCantReturnRemainder](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Test.py#L49)
Bilet kupiony za kwotę wyższą, niż cena biletu ale automat nie ma reszty - oczekiwany komunikat o błędzie i oddanie wrzuconych monet.

#### Metoda [test_shouldCorrectlySumCoins](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Test.py#L66)
Bilet kupiony wrzucając po 1gr. Oczekiwany brak błędów i odpowiednie zsumowanie.

#### Metoda [test_shouldSumTicketsPriceCorrectly](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Test.py#L82)
Zakup dwóch biletów na raz, cena jest sumą.

#### Metoda [test_shouldNotResetCoinsListAfterAddingTicket](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Test.py#L99)
Wybranie biletu, wrzucenie kilku monet, wybranie kolejnego biletu i wrzucenie pozostałych monet za odliczoną kwotę - oczekiwany brak reszty.

#### Metoda [test_shouldRaiseIncorrectValueErrorWhenAmountIsNotInteger](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Test.py#L122)
Próba wrzucenia niecałkowitej liczby monet.

#### Metoda [test_shouldRaiseIncorrectValueErrorWhenAmountIsNegative](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/8b771da09da3f79f4ac7218483b3b444706ce1e3/src/Test.py#L134)
Próba wrzucenia ujemnej liczny monet.


## Istotne fragmenty kodu

### Wyrażenia lambda

1. [Link 1](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/src/Interfejs.py#L139)
2. [Link 2](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/src/Interfejs.py#L152)
3. [Link 3](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/src/Interfejs.py#L155)

### List/dictionary comprehensions

1. [Link 1](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/src/Interfejs.py#L167)
2. [Link 2](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/src/Interfejs.py#L170)
3. [Link 3]()

### Klasy

1. [Link 1](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/src/PrzechowywaczMonet.py)
2. [Link 2](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/src/Automat.py)
3. [Link 3](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/src/Interfejs.py#L25)

### Wyjątki

1. [Link 1](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/exception/NiewlasciwaIloscMonet.py)
2. [Link 2](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/exception/BrakWybranegoBiletu.py)
3. [Link 3](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/exception/BrakMonetDoWydania.py)

### Moduły

1. [Link 1](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/src/Interfejs.py)
2. [Link 2](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/src/Automat.py)
3. [Link 3](https://github.com/KarolBochenek/AutomatBiletowyMPK-PK/blob/1fe9eaac1e94ca16dd07649c6ba74f9dd5aa82a9/exception)


