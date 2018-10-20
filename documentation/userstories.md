# Käyttötapaukset

Tässä tapaukset, jotka kuuluvat sovellukselle:

## Käyttäjä, joka ei ole kirjautunut

- Käyttäjä, joka ei ole kirjautunut, pystyy rekisteröitymään sovellukseen.

```
INSERT INTO account (date_created, date_modified, name, username, password) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Olga', 'olgaviho', 'pipapo')
```

- Käyttäjä, joka ei ole kirjautunut, pystyy rekisteröitymisen jälkeen kirjautumaan sovellukseen.

```
SELECT account.id AS account_id, account.date_created AS account_date_created,
account.date_modified AS account_date_modified, account.name AS account_name, 
account.username AS account_username, account.password AS account_password
FROM account WHERE account.password = 'pipapo' AND account.username = 'olgaviho'
```


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
                    " LEFT JOIN Comment ON Comment.report_id = report.id"
                    " GROUP BY Report.id, Account.username, Nature_site.name"
```


## Kirjautunut käyttäjä

- Kirjautunut käyttäjä voi lisätä uusia luontokohteita.
```
INSERT INTO nature_site (date_created, date_modified, name, description, account_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Vanhankaupunginlahti', 'Lahti Helsingissä', 1)
```

- Kirjautunut käyttäjä voi muokata luotujen luontokohteiden kuvausta.
```
 UPDATE nature_site SET date_modified=CURRENT_TIMESTAMP, description='Lahteen laskee Vantaanjoki', 
 WHERE nature_site.id = 1
```
- Kirjautunut käyttäjä voi lisätä raportin luontokohteelle.

```
INSERT INTO report (date_created, date_modified, title, description, account_id, naturesite_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'lintuhavaintoja 8.10.',
'Valkoposkihanhet lähdössä muuttomatkalla etelään', 1, 1)
```

- Kirjautunut käyttäjä voi muokata lisäämäänsä raporttia.

```
UPDATE report SET date_modified=CURRENT_TIMESTAMP, 
description='Hanhet valmistelemassa muuttomatkaa etelään' WHERE report.id = 18

```
- Kirjautunut käyttäjä voi poistaa luomansa raportin.
```
 DELETE FROM report WHERE report.id = 18
```

- Kirjautunut käyttäjä voi kirjoittaa kommentin raporttiin.
```
INSERT INTO comment (date_created, date_modified, text, account_id, report_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'Hanhien seassa oli myös muita vesilintuja', 1, 18)
```

- Kirjautunut käyttäjä voi muokata kommenttiaan.
```
UPDATE comment SET date_modified=CURRENT_TIMESTAMP, text='Hanhien seassa oli sinisorsia' 
WHERE comment.id = 26

```

- Kirjautunut käyttäjä voi poistaa kommenttinsa.
```
DELETE FROM comment WHERE comment.id = 26
```
