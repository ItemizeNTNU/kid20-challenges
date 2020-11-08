### Flaggformat:
`KID20{*}`\
`*` kan være mer eller mindre hva som helst. Ungå gjerne mellomrom, og kan godt hive på l33t speak. E.g.:
`KID20{th1s_i5_my_l33t_fl4g}`

### Språk:
Husk å holde alle oppgavene på engelsk.

## Stuktur
Se `/web/guessy-as-fork` for eksempel på oppgave og struktur.

Mappestruktur:
```
├── README.md
├── crypto
│   └── ...
├── misc
│   └── ...
├── rev
│   └── ...
├── stego
│   └── ...
└── web
    └── guessy-as-fork
        ├── Dockerfile
        ├── app
        │   ├── app.js
        │   ├── package-lock.json
        │   ├── package.json
        │   └── speeding.png
        ├── description.md
        └── docker-compose.yml
```

Alle oppgaver skal inneholde en `description.md`. 
Denne skal inneholde navn på oppgavelager, flagg + beskrivelse av oppgaven, har støtte for markdown format. E.g.:
```markdown
author: null
flag: KID20{tOlD_Y0u_n0t_6U3zzy}

--

You can go buser your way all you want, but you'll never find my secret! Even if you try 10,000 times to guess your way in, you'll never find it!

{url}

_I swear, totally not guessy chall..._
```

`{url}` vil bli byttet ut med URL til oppgaven. Alt blir lastet opp manuelt, så format er ikke super farlig.

`author` kan man velge hva man vil bruke, men anbefaler discord navn slik at en blir letter å kjenne igjen på discord serveren hvis noen har spørsmål til din oppgave.


## Docker:
Alle oppgaver som skal kjøres (e.g. web server, pwn eller lignende) skal det lages docker container for. Alle oppgaver som kjører i Docker skal ha en `docker-compose.yml` fil. Det er bare å ta kontakt om man trenger hjelp til å sette opp dette.

### docker-compose.yml tips:
Kjekke tips til docker-compose.
* Forsiktig med volumes:
	* Volumes er veldig greit for utvikling, men husk at ting blir lagret i volumet hvis deltagere har mulighet til å skrive til oppgaven. Bruk gjerne `:ro` for read-only om man bruker volumes.
* `restart: always`
	* Denne bør alle inkludere, sier at containeren skal alltid restarte hvis den crasher
* `stop_signal: SIGKILL`
	* Greit for python oppgaver, da python ikke alltid har lyst til å avslutte. Sier basically at vi ikke bryr oss om at containeren avslutter "skikkelig", men heller bare stopp ASAP. Ettersom containerene skal være "imutable" så har ikke dette så mye å si.
* Port nummer:
	* Bare å velge noe random, men ikke ta noe som allerede er tatt. Velg gjerne et tilfeldig tall mellom 10,000 og 65,000 så burde nok dette gå fint.
	Eventuelt generer et tall [her](https://duckduckgo.com/?q=random+number+between+10000+and+65000).

### Filer:
Har man filer som skal lastes opp, lag en mappe med navn `files` og legg filer i denne.

# Ekstra:
Ikke vær redd for å pushe til egen branch, er fin måte å få tilbakemelding på, og andre kan se over og kommentere. Ikke vær redd for å gjør feil eller ødelegg ting. Ting blir sett over før det merges inn i #main.
