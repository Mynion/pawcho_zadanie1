\# Laboratorium – Programowanie Aplikacji w Chmurze Obliczeniowej



\---



Aplikacja została wykonana w języku Python z wykorzystaniem frameworka Flask.



Funkcjonalność:

\- zapis informacji w logach po uruchomieniu kontenera,

\- wybór miasta i kraju,

\- wyświetlanie aktualnej pogody dla wybranej lokalizacji.



Zastosowano:

\- multi-stage build,

\- obraz python:3.12-alpine,

\- HEALTHCHECK,

\- OCI LABEL.



\---



\# Polecenia Docker



\## Budowanie obrazu



```bash

docker build -t weather-app .

```



\## Uruchomienie kontenera



```bash

docker run -d -p 8080:8080 --name weather weather-app

```



\## Sprawdzenie logów



```bash

docker logs weather

```



\## Sprawdzenie warstw i rozmiaru obrazu



```bash

docker history weather-app

docker images

```



\---



\# Potwierdzenie działania





