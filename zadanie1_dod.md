# Laboratorium – Programowanie Aplikacji w Chmurze Obliczeniowej
# Zadanie 1 – część dodatkowa (+80%)

---

# 1. Utworzenie buildera buildx

```bash
docker buildx create --name multi-builder --driver docker-container --use
```

```bash
docker buildx inspect --bootstrap
```

```bash
docker buildx ls
```

---

# 2. Budowanie obrazu multi-platformowego

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t mynion/weather-app:latest --push --builder multi-builder --cache-from=type=registry,ref=mynion/weather-app:cache --cache-to=type=registry,ref=mynion/weather-app:cache,mode=max .
```

W procesie budowania wykorzystano:
- Docker Buildx,
- builder docker-container,
- cache registry,
- platformy linux/amd64 oraz linux/arm64.

---

# 3. Weryfikacja manifestu

```bash
docker buildx imagetools inspect mynion/weather-app:latest
```

Potwierdzono obsługę:
- linux/amd64
- linux/arm64

---

# 4. Cache build

```bash
docker buildx build --progress=plain .
```

W projekcie wykorzystano cache registry w trybie `mode=max`.

---

# 5. Dockerfile

W Dockerfile zastosowano rozszerzony frontend BuildKit:

```dockerfile
# syntax=docker/dockerfile:1.7
```

---

# 6. Repozytoria

##DockerHub
```text
mynion/weather-app
```

---

# 7. Zrzuty ekranu
<img width="1637" height="97" alt="Zrzut ekranu 2026-05-12 151940" src="https://github.com/user-attachments/assets/82cdd3a4-a997-4d6b-a130-1a276662a734" />
<img width="1877" height="885" alt="image" src="https://github.com/user-attachments/assets/4cc241c9-4f6f-4a4e-8136-7602c9ed6f81" />
<img width="1541" height="627" alt="Zrzut ekranu 2026-05-12 152254" src="https://github.com/user-attachments/assets/6754c8a9-002c-4490-bc03-e48cd891df20" />
<img width="1901" height="926" alt="Zrzut ekranu 2026-05-12 152346" src="https://github.com/user-attachments/assets/96e3f37a-5ec3-49d8-a159-d0dc74d01ee8" />

