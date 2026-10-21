"""Zarqand menu content, in the order a dasturxon is laid.

Dish names and descriptions are sample content; every price is a sample and must be confirmed by the restaurant.
Each item: (name, description, price). A price may carry its portion: "4 dona · 44 000".
"""

SALATLAR = [
    ("Salatlar", [
        ("Achchiq-chuchuk", "Pomidor, piyoz, achchiq qalampir va rayhon", "22 000"),
        ("Toshkent salati", "Mol go‘shti, turp, tuxum va qovurilgan piyoz", "38 000"),
        ("Suzmali ko‘kat", "Suzma, bodring, ukrop va yalpiz", "26 000"),
        ("Zarqand salati", "Qo‘y tili, anor donasi, yong‘oq va ko‘katlar", "46 000"),
    ]),
    ("Gazaklar", [
        ("Qazi va norin likopchasi", "Uy qazisi, qarta va yupqa norin", "85 000"),
        ("Tuzlama", "Bodring, pomidor, karam va sarimsoq", "28 000"),
        ("Pishloq va mevalar", "Uch xil pishloq, uzum, asal va yong‘oq", "64 000"),
    ]),
    ("Non", [
        ("Samarqand noni", "Tandirda, kunjut va sedana bilan", "12 000"),
        ("Patir", "Qaymoqli qatlama xamir", "15 000"),
        ("Jizzali non", "Tandir noni, jizza bilan", "14 000"),
    ]),
]

SHORVALAR = [
    ("Qo‘y sho‘rva", "Qo‘y go‘shti, no‘xat, sabzi va kartoshka", "42 000"),
    ("Mastava", "Guruch, mol go‘shti va suzma", "36 000"),
    ("Moshxo‘rda", "Mosh, guruch va qatiq", "34 000"),
    ("Chuchvara sho‘rva", "Mayda chuchvara, ko‘katlar bilan", "38 000"),
    ("Lag‘mon sho‘rva", "Qo‘lda cho‘zilgan lag‘mon va sabzavotlar", "40 000"),
    ("Ko‘za sho‘rva", "Sopol ko‘zada, tandirda dimlangan", "52 000"),
]

ASOSIY = [
    ("Osh", [
        ("Samarqand oshi", "Qo‘y go‘shti, sariq sabzi, qazi va bedana tuxumi", "68 000"),
        ("To‘y oshi", "Mol go‘shti, no‘xat va mayiz", "62 000"),
        ("Choyxona oshi", "Qazi, kishmish va kuzgi sabzi", "72 000"),
    ]),
    ("Qozon taomlari", [
        ("Qozon kabob", "Qo‘y go‘shti va kartoshka, o‘z yog‘ida", "78 000"),
        ("Dimlama", "Go‘sht, karam va sabzavotlar, bug‘da", "58 000"),
        ("Lag‘mon", "Qo‘lda cho‘zilgan, qovurma yoki suyuq", "48 000"),
        ("Norin", "Ot go‘shti va yupqa xamir, sovuq holda", "56 000"),
        ("Jiz", "Qo‘y go‘shti va dumba, qozonda qovurilgan", "74 000"),
        ("Tandir go‘sht", "Qo‘y go‘shti, tandirda sekin pishgan", "0,5 kg · 120 000"),
    ]),
]

XAMIR = [
    ("Manti", "Qo‘y go‘shti va dumba, suzma bilan", "4 dona · 44 000"),
    ("Qovoqli manti", "Qovoq va piyoz, qaymoq bilan", "4 dona · 38 000"),
    ("Chuchvara", "Qo‘lda tugilgan, qatiq bilan", "40 000"),
    ("Tandir somsa", "Qatlama xamir, go‘sht va kunjut", "1 dona · 16 000"),
    ("Ko‘k somsa", "Bahorgi ko‘katlar bilan", "1 dona · 12 000"),
    ("Xonim", "Go‘sht va kartoshka, bug‘da o‘ralgan", "42 000"),
    ("Qutob", "Yupqa xamir, ko‘kat yoki go‘sht bilan", "2 dona · 24 000"),
]

KABOB = [
    ("Kabob · 1 six", [
        ("Qo‘y go‘shti", "Bo‘lak go‘sht, dumba bilan", "32 000"),
        ("Mol go‘shti", "Yumshoq bo‘laklar", "34 000"),
        ("Lula kabob", "Qiyma va ziravorlar", "28 000"),
        ("Jigar kabob", "Qo‘y jigari va dumba", "26 000"),
        ("Tovuq kabob", "Marinadlangan son go‘shti", "24 000"),
        ("Bedana", "Butun bedana, cho‘g‘da", "34 000"),
        ("Assorti", "Olti xil kabob, 2–3 kishiga", "180 000"),
    ]),
    ("Kabobga qo‘shimcha", [
        ("Shakarob", "Pomidor, piyoz va rayhon", "18 000"),
        ("Qovurilgan kartoshka", "Ko‘kat va sarimsoq bilan", "20 000"),
    ]),
]

SHIRINLIK = [
    ("Zarqand qandi", "Zafaronli navvot, choy bilan", "34 000"),
    ("Chak-chak", "Asalli xamir va yong‘oq", "28 000"),
    ("Paxlava", "Yong‘oq va asal qatlamlari", "32 000"),
    ("Oq halva", "Kunjutli, uy usulida", "24 000"),
    ("Navvot va quruq mevalar", "Mayiz, o‘rik va yong‘oq", "30 000"),
    ("Pashmak", "Ipak qand, choy bilan", "22 000"),
    ("Qovun va muzqaymoq", "Mavsumiy qovun, vanilli muzqaymoq", "36 000"),
    ("Holvaytar", "Issiq, un va sariyog‘dan", "26 000"),
]

ICHIMLIK = [
    ("Choy va qahva", [
        ("Ko‘k choy, choynak", "12 000"),
        ("Qora choy, choynak", "12 000"),
        ("Limonli choy", "18 000"),
        ("Na’matak choyi", "22 000"),
        ("Zafaronli choy", "28 000"),
        ("Turkcha qahva", "22 000"),
        ("Kapuchino", "24 000"),
    ]),
    ("Sovuq ichimliklar", [
        ("Uy kompoti, 1 l", "28 000"),
        ("Ayron", "14 000"),
        ("Tarxunli limonad", "26 000"),
        ("Rayhonli limonad", "26 000"),
        ("Muzli choy", "20 000"),
    ]),
    ("Sharbatlar", [
        ("Anor", "32 000"),
        ("Apelsin", "28 000"),
        ("Olma va sabzi", "24 000"),
        ("Qovun, mavsumiy", "26 000"),
    ]),
    ("Suv", [
        ("Gazsiz suv, 0,5 l", "8 000"),
        ("Gazli suv, 0,5 l", "10 000"),
        ("Gazsiz suv, 1,5 l", "14 000"),
        ("Mineral suv, 0,33 l", "16 000"),
    ]),
]

# Navigation labels, in page order.
CATEGORIES = [
    ("salatlar", "Salatlar"),
    ("shorvalar", "Sho‘rvalar"),
    ("asosiy", "Asosiy taomlar"),
    ("xamir", "Xamir taomlar"),
    ("kabob", "Kabob"),
    ("shirinlik", "Shirinliklar"),
    ("ichimlik", "Ichimliklar"),
]
