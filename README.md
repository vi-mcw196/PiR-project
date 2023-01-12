# README z projektu programistycznego PIR

## Temat: Elektroniczny klucz do mieszkania 

#### Zespół dwuosobowy - Viktor Moldovan, Dominik Tomaszewski 
#### Prowadzący labolatorium: Dr inż. Krzysztof Chudzik

## Wymagania funkcjonalne
- Odczyt karty pełniącej rolę klucza przez zamek (czytnik kart zbliżeniowych RFID).
- Reakcja urządzenia odczytującego na przyłożenie karty.
  - W przypadku przyłożenia poprawnej karty, diody zapalają się na kolor zielony.
  - W przypadku przyłożenia niepoprawnej karty, diody zapalają się na kolor czerwony,
oraz włączony zostaje buzzer.
- Zapis informacji o przyłożonej karcie w rejestrze (bazie danych).
- Komunikacja między urządzeniem odczytującym, a serwerem, polegająca na przesłaniu
informacji o przyłożeniu karty i informacji o niej.
- Komunikacja między serwerem, a aplikacją webową, umożliwiająca prezentację
odpowiednich wyników z bazy danych.
- Możliwość operacji CRUD dla kart dostępu:
  - Dodanie nowej karty.
  - Usunięcie karty.
  - Zmiana nazwy właściciela karty.

## Wymagania niefunkcjonalne

Języki i technologie programowania użyte do implementacji: Python, SQL.
- Komunikacja między urządzeniami: MQTT.
- Urządzenie odczytujące: Raspberry Pi (na potrzeby laboratorium działające jako zamek
elektroniczny).
- Peryferia:
  - czytnik kart zbliżeniowych RFID.
  - Sygnalizator dźwiękowy – buzzer.
  - Linijka programowalnych diod LED RGB WS2812 .
- Systemy operacyjne: Linux Debian.
- Baza danych: SQLite.

## Opis architektury systemu
![image](https://user-images.githubusercontent.com/33034120/212048005-457677da-e3c7-4b23-b7c5-06ac969060d4.png)
