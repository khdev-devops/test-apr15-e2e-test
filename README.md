# Systemtest med Playwright (Python)

I denna övning får du:
- Förstå vad ett **systemtest** (E2E-test) innebär
- Lära dig grunderna i **Playwright för Python**
- Skriva test som simulerar en **verklig användare i en webbläsare**
- Reflektera över när systemtest är värdefulla – och vad som kan göra dem sköra

---

## Förberedelser

### 1. Skapa en virtuell miljö (rekommenderas)

```bash
python -m venv venv
source venv/bin/activate  # eller .\venv\Scripts\activate på Windows
```

### 2. Installera dependencies

```bash
pip install -r requirements.txt
```


### 3. Installera Playwright och relaterade verktyg

```bash
pip install pytest playwright
playwright install
```

---

## Övning 1: Läsbart exempeltest

Du börjar med att titta på ett [färdigt exempeltest](./tests/system/test_example.py) som:
- kör mot en lokal app (http://127.0.0.1/horizontal_slider)
- visar struktur och syntax
- följer best practices från [BetterStack](https://betterstack.com/community/guides/testing/playwright-best-practices/), bl.a.:
  - Använd stabila selektorer (`get_by_role()` hellre än element-ID / path)
  - Ha fokuserade och isolerade tester
  - Skriv assertions ur användarens perspektiv
  - Använd tydliga namn på test och steg

### Din uppgift

1. Starta appen (`python app/app.py`) i en terminalsession
2. Starta en ny terminalsession (och aktivera din virtuella pythonmiljö, om du har använder en sådan)
2. Kör testet (`pytest`) och se att det går igenom
3. Kör testet med [olika webbläsare]((https://playwright.dev/python/docs/browsers))
4. Reflektera:
   - Vad testas – och vad inte?
   - Vad händer om UI ändras? Blir testet instabilt?

## Övning 2: Skriv ett eget test för en annan webbsida

Du ska nu testa en webbsida med dynamiskt laddat innehåll. Sidan visar en laddningsindikator och döljer ett meddelande tills innehållet är klart.

### Din uppgift
1. Starta appen (`python app/app.py`)
2. Testa webbsidan manuellt: http://12.0.0.1/dynamic_loading
    - Vad händer? I vilken sekvens?
3. Fundera: Vad vill du verifiera? Vad kan gå fel?
4. Skriv ett test med Playwright
5. Kör testet och få det att gå igenom
6. Reflektera:
   - Vilka ändringar i webbsidan skulle få testet att fallera?
   - Är testet robust?

Tips:
- Läs dokumentationen om [vänta på element](https://playwright.dev/python/docs/wait-for)
- Använd `expect(...)` istället för `assert` när du testar UI

## Länkar

- [Playwright för Python – Officiell dokumentation](https://playwright.dev/python/)
- [9 Playwright Best Practices (BetterStack)](https://betterstack.com/community/guides/testing/playwright-best-practices/)
- [Playwright Inspector (Debugging)](https://playwright.dev/python/docs/debug)
- [Testa med olika webbläsare](https://playwright.dev/python/docs/browsers)

---

## Klar?

- Prova köra dina test i `headless=False` och prova med olika värden på parametern `slow_mo`
- Lägg till fler steg i flödet
- Diskutera med en kompis: vad testas – vad inte?
