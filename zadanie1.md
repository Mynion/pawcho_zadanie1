# Laboratorium – Programowanie Aplikacji w Chmurze Obliczeniowej

---

Aplikacja została wykonana w języku Python z wykorzystaniem frameworka Flask.

Funkcjonalność:
- zapis informacji w logach po uruchomieniu kontenera,
- wybór miasta i kraju,
- wyświetlanie aktualnej pogody dla wybranej lokalizacji.

Zastosowano:
- multi-stage build,
- obraz python:3.12-alpine,
- HEALTHCHECK,
- OCI LABEL.

---

# Polecenia Docker

## Budowanie obrazu

```bash
docker build -t weather-app .
```

## Uruchomienie kontenera

```bash
docker run -d -p 8080:8080 --name weather weather-app
```

## Sprawdzenie logów

```bash
docker logs weather
```
<img width="1440" height="346" alt="image" src="https://github.com/user-attachments/assets/a9aa09f2-28ab-49e2-93f5-fbc0b88b1fe4" />

## Sprawdzenie warstw i rozmiaru obrazu

```bash
docker history weather-app
docker images
```
<img width="942" height="317" alt="image" src="https://github.com/user-attachments/assets/5e339db1-4702-4685-afa7-4896cfefcfb9" />

<img width="902" height="96" alt="image" src="https://github.com/user-attachments/assets/9088e2f5-1ceb-445e-9c91-ecbf96969651" />

---

# Potwierdzenie działania
<img width="545" height="513" alt="image" src="https://github.com/user-attachments/assets/11892bfd-30b1-4f63-b873-e1036130b5e6" />

<img width="1866" height="60" alt="image" src="https://github.com/user-attachments/assets/d38a2324-c140-482c-a4e3-cd67cbf1ccb2" />



