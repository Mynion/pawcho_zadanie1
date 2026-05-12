#Laboratorium – Programowanie Aplikacji w Chmurze Obliczeniowej
#Zadanie 1 – część dodatkowa (+80%)

---

#1. Utworzenie buildera buildx

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

#2. Budowanie obrazu multi-platformowego

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t mynion/weather-app:latest --push --builder multi-builder --cache-from=type=registry,ref=mynion/weather-app:cache --cache-to=type=registry,ref=mynion/weather-app:cache,mode=max .
```

W procesie budowania wykorzystano:
- Docker Buildx,
- builder docker-container,
- cache registry,
- platformy linux/amd64 oraz linux/arm64.

---

#3. Weryfikacja manifestu

```bash
docker buildx imagetools inspect mynion/weather-app:latest
```

Potwierdzono obsługę:
- linux/amd64
- linux/arm64

---

#4. Cache build

```bash
docker buildx du
```

W projekcie wykorzystano cache registry w trybie `mode=max`.

---

#5. Dockerfile

W Dockerfile zastosowano rozszerzony frontend BuildKit:

```dockerfile
# syntax=docker/dockerfile:1.7
```

---

#6. Repozytoria

##DockerHub
```text
mynion/weather-app
```

---

# 7. Zrzuty ekranu

