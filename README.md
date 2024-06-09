# Fairoulette

Realisiert: 
- Simple GUI mit Knopfen und Wette
- sqlite: create_user, create_bet; models
- Funktionen in server.py
- Zusammenhang python mit c++
- random(0,36)

## Contributors

- Daniil (CTO): Datentypen, dokumentation
- Felix (CEO): Tests, Exceptions, Fehlerbehebung
- Mohammed (CUO - Chief UML Officer):UML 

## Credits
- Sir Tim Berners-Lee: Thanks for the Internet
- Felix Boes: Dessen Vorlesungen die Grundlage für dieses Projekt bilden.

## Setup for Server/Client
```shell
cmake -S . -B build/ &&
cmake --build build/ &&
cmake --install build
```

### Run Server
`python3 server/extra/server.py`


### Run Client
`python3 client/src/server.py`




