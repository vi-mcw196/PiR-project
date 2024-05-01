# README of the PIR development project

## Temat: Electronic flat key

#### Zespół dwuosobowy - Viktor Moldovan, Dominik Tomaszewski
#### Prowadzący labolatorium: Dr inż. Krzysztof Chudzik

## Functional requirements
 - Reading of a card serving as a key through a lock (RFID proximity card reader).
 - Response of the reading device to card application.
 - If a valid card is inserted, the LEDs light up green.
 - In the event of an invalid card being presented, the LEDs turn red and a buzzer sounds.
 - Writing of information about the inserted card in the register (database).
 - Communication between the reading device and the server, involving the transmission of card assignment and card information.
 - Communication between the server and the web application, allowing the presentation of the corresponding results from the database.
 - Possibility of CRUD operations for access cards:
 - Adding a new card.
 - Deleting a card.
 - Changing the name of the card owner.

## Non-functional requirements

Programming languages and technologies used for implementation: Python, SQL.
- Communication between devices: MQTT.
- Reading device: Raspberry Pi (for the lab acting as an electronic lock).
- Peripherals:
  - RFID proximity card reader.
  - Sounder - buzzer.
  - WS2812 line of programmable RGB LEDs.
- Operating systems: Linux Debian.
- Database: SQLite.

## System architecture description
![image](https://user-images.githubusercontent.com/33034120/212048005-457677da-e3c7-4b23-b7c5-06ac969060d4.png)
