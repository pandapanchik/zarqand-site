# Zarqand — landing sahifa

Zarqand restorani uchun bir sahifali sayt. Oddiy HTML/CSS/JS, build kerak emas.

- `index.html` — sahifa
- `css/style.css` — stillar (desktop, planshet ≤1100px, telefon ≤760px)
- `menyu.html` + `css/menu.css` — to‘liq menyu sahifasi (7 kategoriya); taom va narxlar shu faylda tahrirlanadi
- `js/main.js` — mobil menyu, bron formasi, menyu sahifasidagi kategoriya paneli
- `img/` — rasmlar (hozircha AI'da yaratilgan, haqiqiy fotolarga almashtiriladi)
- `fonts/` — Gloock, Mulish, Pinyon Script (Google Fonts, o'zimizda saqlangan)
- `figma-src/`, `docs/`, `assets/` — Figma maketi manbalari, saytga kirmaydi

## To'ldirish kerak

1. `index.html` dagi `<span class="ph">[...]</span>` joylarni haqiqiy ma'lumot bilan almashtiring
   (telefon, manzil, narxlar, reyting, sharhlar va h.k.) va `ph` spanni olib tashlang.
2. `js/main.js` dagi `TELEGRAM_USERNAME` ga restoran Telegram username'ini yozing (`@` siz).
3. `img/` dagi rasmlarni xuddi shu nomlar bilan haqiqiy fotolarga almashtiring
   va `index.html` dagi `AI rasm · almashtiriladi` belgilarini olib tashlang.

## Lokal ko'rish

```bash
python3 -m http.server 4318
```

## Deploy

GitHub'ga `git push` qilinganda Vercel saytni avtomatik yangilaydi.
