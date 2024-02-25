let aktiv = '1. Feladat';
let i = 1;

let adatok = [
    {
        anyag: [
            ['h1', '1. Feladat'],
            ['img', '../images/html_feladat.png'],
            [
                'p',
                'Hozzunk létre egy index.html állományt. A head elemben soroljunk fel minél több meta elemet és írjuk le, hogy mi a feladatuk.',
            ],
        ],
    },
    {
        anyag: [
            ['h1', `${i++}. Lépés`],
            ['img', '../images/kep_013.png', 'kod'],
            ['p', 'A title elem felel a weboldal címéért.'],
            [
                'p',
                'Ez fog megjelenni az index.html-hez tartozó weboldal fülén és a könyvjelzők között is.',
            ],
            ['p', 'Hasznos lehet a SEO folyamán is.'],
        ],
    },
    {
        anyag: [
            ['h1', `${i++}. Lépés`],
            ['img', '../images/kep_014.png', 'kod'],
            ['p', 'Különböző meta elemek.'],
            ['p', 'Hasznosak lehetnek a SEO folyamán is.'],
            [
                'ul',
                [
                    'charset: a karakterkódolásért felel',
                    'viewport: a reszponzivitáshoz kell',
                    'author: az oldal szerzője',
                    'keywords: kulcsszavak az oldal megtalálásához',
                    'description: az oldal tartalmának a leírása',
                ],
            ],
        ],
    },
    {
        anyag: [
            ['h1', `${i++}. Lépés`],
            ['img', '../images/kep_015.png', 'kod'],
            ['p', 'Különböző meta http-equiv elemek.'],
            ['p', 'Hasznosak lehetnek a SEO folyamán is.'],
            [
                'ul',
                [
                    'refresh: az oldal frissítése 5 másodpercenként',
                    'refresh: az oldal azonnali frissítése a url-ben megadott oldalra',
                ],
            ],
        ],
    },
    {
        anyag: [
            ['h1', `${i++}. Lépés`],
            ['img', '../images/kep_016.png', 'kod'],
            ['p', 'Különböző link elemek.'],
            ['p', 'Külső erőforrások (stíluslapok, képek stb.) beimportálása.'],
            [
                'ul',
                [
                    'stylesheet: külső stíluslap beimportálása',
                    'shortcut icon: favicon beimportálása (kis kép a fülön a cím előtt)',
                ],
            ],
        ],
    },
    {
        anyag: [
            ['h1', `${i++}. Lépés`],
            ['img', '../images/kep_017.png', 'kod'],
            ['p', 'Különböző script elemek.'],
            ['p', 'Külső erőforrások (szriptek) beimportálása.'],
        ],
    },
    {
        anyag: [
            ['h1', `${i++}. Lépés`],
            ['img', '../images/kep_018.png', 'kod'],
            ['p', 'Belső stíluslap elemek.'],
        ],
    },
    {
        anyag: [
            ['h1', `${i++}. Lépés`],
            ['img', '../images/kep_019.png', 'kod'],
            ['p', 'A base elemet két dologra használjuk:'],
            [
                'ul',
                [
                    'Az oldalon szereplő hivatkozásokhoz és képekhez egy közös mappa létrehozása (tartalom), és az erre való hivatkozás.',
                    'A hivatkozások új oldalon nyíljanak meg.',
                ],
            ],
        ],
    },
];
