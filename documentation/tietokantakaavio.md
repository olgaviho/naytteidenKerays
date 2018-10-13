# Alustava tietokantakaavio

![alt text](https://raw.githubusercontent.com/olgaviho/naytteidenKerays/master/documentation/pictures/tietokantakaavio2.JPG)

Tietokantaan liittyvät _create table_ -lauseet:

```
CREATE TABLE account (
    id INTEGER NOT NULL, 
    date_created DATETIME, 
    date_modified DATETIME, 
    name VARCHAR(144) NOT NULL, 
    username VARCHAR(144) NOT NULL, 
    password VARCHAR(144) NOT NULL, 
    PRIMARY KEY (id)
);
```
```
CREATE TABLE naturesites (
    PRIMARY KEY (id)
);
```
```
CREATE TABLE report (
    PRIMARY KEY (id)
);
```
```
CREATE TABLE comments (
    PRIMARY KEY (id)
);
```

## Tietokannan indeksit <h4>
  
Indeksit nopeuttavat tiedonhakua taulusta. Pääavaimille indeksit on luotu automaattisesti, mutta sille viite-avaimelle, jota käytetään sovelluksen sql-kyselyissä, on luotu myös indeksi Herokun tietokantaan. Indeksi on luotu seuraavalla tavalla:
```
CREATE INDEX idx_account_id_report ON report (account_id);
```

  
## Tietokannan normalisointi <h5>
Normalisoinnin tavoite on vähentää tauluissa esiintyvää toisteista tietoa.
  
Kaikki taulut ovat ensimmäisessä normaalimuodossa, sillä sarakkeissa ei ole listoja, sarakkeiden arvot ovat samaa tyyppiä ja kaksi riviä erottaa toisistaan vähintään id. Ensimmäiselle normaalimuodolle on myös muita vaatimuksia, jotka kaikki täyttyvät: taulun sarakkeet eivät muodosta toistuvia ryhmiä, sarakkeiden nimet ovat uniikkeja taulussaan, sarakkeiden ja rivien järjestys ei vaikuta taulun toimintaan.

Taulut ovat myös toisessa normaalimuodossa, koska se on ensimmäisessä normaalimuodossa ja jokaisella taululla on tasan yksi pääaivain (id) ja muut sarakkeen arvot ovat funktionaalisesti riippuvia siitä.

Taulut ovat myös kolmannessa normaalimuodossa, sillä ne ovat toisessa normaalimuodossa ja sarakkeet eivät ole funktionaalisesti riippuvia toisistaan (paitsi tietenkin pääavaimesta).
