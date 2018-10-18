# Tietokantakaavio

![alt text](https://raw.githubusercontent.com/olgaviho/naytteidenKerays/master/documentation/pictures/tietokantakaavio4.png)

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
CREATE TABLE nature_site (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(144), 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```
```
CREATE TABLE report (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	title VARCHAR(144), 
	description VARCHAR(144), 
	account_id INTEGER NOT NULL, 
	naturesite_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(naturesite_id) REFERENCES nature_site (id)
);
```
```
CREATE TABLE comment (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	text VARCHAR(144), 
	account_id INTEGER NOT NULL, 
	report_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(report_id) REFERENCES report (id)
);
CREATE INDEX idx_account_id ON report (account_id);
CREATE INDEX idx_naturesite_id ON report (naturesite_id);

```

## Tietokannan indeksit <h4>
  
Taulujen pääavaimille indeksit on luotu automaattisesti, mutta niille viiteavaimelle, joita käytetään sovelluksen sql-kyselyissä, on luotu myös indeksi Herokun tietokantaan. Indeksi on luotu seuraavalla tavalla:
```
CREATE INDEX idx_account_id ON report (account_id);
CREATE INDEX idx_naturesite_id ON report (naturesite_id);
```

  
## Tietokannan normalisointi <h5>

Kaikki taulut ovat ensimmäisessä normaalimuodossa, sillä sarakkeissa ei ole listoja, sarakkeiden arvot ovat samaa tyyppiä ja kaksi riviä erottaa toisistaan vähintään id. Ensimmäiselle normaalimuodolle on myös muita vaatimuksia, jotka kaikki täyttyvät: taulun sarakkeet eivät muodosta toistuvia ryhmiä, sarakkeiden nimet ovat uniikkeja taulussaan, sarakkeiden ja rivien järjestys ei vaikuta taulun toimintaan.

Taulut ovat myös toisessa normaalimuodossa, koska se on ensimmäisessä normaalimuodossa ja jokaisella taululla on tasan yksi pääaivain (id) ja muut sarakkeen arvot ovat funktionaalisesti riippuvia siitä.

Taulut ovat myös kolmannessa normaalimuodossa, sillä ne ovat toisessa normaalimuodossa ja sarakkeet eivät ole funktionaalisesti riippuvia toisistaan (paitsi tietenkin pääavaimesta).
