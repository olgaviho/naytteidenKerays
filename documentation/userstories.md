# Käyttötapaukset

Tässä tapaukset, jotka kuuluvat sovellukselle:

## Käyttäjä, joka ei ole kirjautunut

- Käyttäjä, joka ei ole kirjautunut, pystyy rekisteröitymään sovellukseen.
- Käyttäjä, joka ei ole kirjautunut, pystyy rekisteröitymisen jälkeen kirjautumaan sovellukseen.
- Käyttäjä, joka ei ole kirjautunut, pystyy katsomaan luotuja luontokohteita kuvauksineen.
- Käyttäjä, joka ei ole kirjautunut, pystyy katsomaan yhteenvetoa luoduista raporteista. 

Kirjautumattomat käyttäjät näkevät kahden sql-kyselyn tulokset. Ensimmäinen kertoo, kuinka monta raporttia kukin käyttäjä on luonut järjestelmään.

```
"SELECT Account.name, COUNT(Report.id) FROM Account"
                    " LEFT JOIN Report ON Report.account_id = Account.id"
                    " GROUP BY Account.id") 
```

Toinen kysely kertoo, millaisia raportteja järjestelmään on luotu. Raporteista tulee ilmi niiden otsikko, itse kuvaus, luontokohde ja kirjoittaja. 

```
SELECT Report.title, Account.name, Report.description, Nature_site.name FROM Report"
                    " LEFT JOIN Account ON Report.account_id = Account.id"
                    " LEFT JOIN Nature_site ON Report.naturesite_id = Nature_site.id") 
```


## Kirjautunut käyttäjä

- Kirjautunut käyttäjä voi lisätä uusia luontokohteita.
- Kirjautunut käyttäjä voi muokata luotujen luontokohteiden kuvausta.
- Kirjautunut käyttäjä voi lisätä raportin luontokohteelle.
- Kirjautunut käyttäjä voi muokata lisäämäänsä raporttia.
- Kirjautunut käyttäjä voi poistaa luomansa raportin.
- Kirjautunut käyttäjä voi kirjautua ulos sovelluksesta.
- Kirjautunut käyttäjä voi kirjoittaa kommentin raporttiin.
- Kirjautunut käyttäjä voi muokata kommenttiaan.
- Kirjautunut käyttäjä voi poistaa kommenttinsa.

