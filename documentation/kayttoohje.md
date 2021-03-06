# Asennusohje
Lataa git-repositorio zippinä tietokoneellesi klikkaamalla etusivulla painiketta _clone or download_. Pura paketti sopivaan kohtaan koneellesi. 

## Ohjelman käynnistäminen
Ennen käynnistystä pitää aktivoida venvin virtuaaliympäristö ja päivittää riippuvuudet komennolla:
```
pip install -r requirements.txt
```

Ohjelma käynnistetään komennolla:
```
python3 run.py
```

# Käyttöohje
  
## Aloitussivu
 
Aloitussivulle pääsee aina klikkaamalla yläpalkissa kohtaa _Nature sites and reports_. Aloitussivulla on lueteltu sovelluksen käyttäjät ja heidän luomat raportit.

## Kirjautuminen
Kirjautuminen onnistuu valitsemalla oikeasta yläkulmasta vaihtoehdon _login_. Ylempään syötekenttään kirjoitetaan käyttäjätunnus ja alempaan syötekenttään salasana.
Jos käyttäjän luonti onnistuu, siirrytään aloitussivulle. Uloskirjatuminen onnistuu klikkamalla ylhäältä painiketta _log out_.

## Uuden käyttäjän luominen
Uuden käyttäjän pääsee luomaan klikkaamalla _Create user_. Uusi käyttäjä luodaan syöttämällä pyydetyt tiedot syötekenttiin ja painamalla _Add a new user_. Jos käyttäjän luonti onnistuu, siirrytään aloitussivulle.

## Luontokohteiden selaaminen
Luontokohteita pääsee selaamaan, vaikka ei olisi kirjautunut sisään järjestelmään. Valitsemalla ylhäältä _List nature sites_ näkee kaikki tämän hetkiset luontokohteet.

## Raporttien selaaminen
Raportteja pääsee selaamaan, vaikka ei olisi kirjautunut sisään järjestelmään. Valitsemalla ylhäältä _All reports_ näkee kaikki luodut raportit.

# Seuraavat toiminnot ovat vain kirjatuneille käyttäjille:

## Luontokohteen luominen
Uuden luontokohteen voi luoda valitsemalla ylhäällä olevasta valikosta _Add a nature site_. Luontokohteelle pitää antaa nimi sekä kuvaus ja sen jälkeen klikata painiketta _Add a new nature site_. Kahdella luontokohteella ei voi olla samaa nimeä.

## Luontokohteen raporttien selaaminen
Luontokohteita selatessa voi klikata haluamansa luontokohteen nimeä, josta pääsee katsomaan kyseiselle luontokohteelle luotuja raportteja.

## Luontokohteen kuvauksen muuttaminen
Luontokohteita selatessa voi klikata luontokohteen nimen kohdalla olevaa linkkiä, josta pääsee katsomaan luotokohdetta tarkemmin Painamlla linkkia _edit nature site_ pääsee muokkaamaan kuvausta. Vain alkuperäisen luontokohteen luoja voi muuttaa kuvausta. Mikäli, yrittää muokata toisen luomaa luontokohdetta, päätyy kirjautumissivulle. Luontokohteen kuvausta voi muuttaa kirjoittamalla kohtaan _Write new description_ uuden kuvauksen ja painamalla painiketta _Change description_.

## Raportin luominen
Kenen tahansa luomaan luontokohteeseen voi luoda uuden raportin. Uuden raportin voi luoda valitsemalla _Create a new report_. Raportille pitää antaa otsikko sekä kuvaus ja sen jälkeen klikata painiketta _Add a new report_. Kuvaukseen voi kirjoittaa esimerkiksi mitä lintulajeja on havainnut vieraillessaan luontokohteella.

## Raportin muokkaaminen ja poistaminen
Raportteja selatessa voi klikata kohtaa _edit report_, josta pääsee raportin muokkaussivulle. Kohtaan _New description_ voi kirjoittaa uuden kuvauksen ja, kun painaa painiketta _Change description_, muuttuu raportin kuvaus. Raportin voi poistaa raportin muokkaussivulta painamalla painiketta _Delete_. Vain omia raportteja voi muokata tai poistaa. Mikäli, yrittää muokata tai poistaa toisen luomaa raporttia, päätyy kirjautumissivulle.

## Kommenttien katsominen
Raportin kommentteja voi katsoa klikkamalla kohtaa _comments_.

## Kommentin luominen
Kenen tahansa luomaan raporttiin voi luoda uuden kommentin kirjoittamalla sen kohtaan _write a new comment_. Kommentin kirjoittamisen jälkeen pitää klikata painiketta _Add a new comment_.

## Kommentin muokkaaminen ja poistaminen
Kommentteja selatessa voi kommenttia muokata painamalla linkkiä _Edit_, josta pääsee kommentin muokkaussivulle. Uuden tekstin voi kirjoittaa kohtaan _Write new text_ ja painamalla painiketta _Change text_, muuttuu kommentin sisältö. Kommentin voi poistaa muokkaussivulla painamalla painiketta _Delete_. Vain omia kommentteja voi muokata tai poistaa. Mikäli, yrittää muokata tai poistaa toisen luomaa kommenttia, päätyy kirjautumissivulle. Kuitenkin, jos raportin kirjoittaja päättää poistaa oman raporttinsa, poistuvat myös siihen liittyvät kommentit.


# Sovellukseen jääneet puutteet

Sovellukseen on jäänyt muutamia puutteita, esimerkiksi seuraavia asioita voisi vielä parantaa:

- Koodissa on jonkun verran copypastea _error_ -sivulle viemisen osalta
- Sivutus ei ole käytössä

# Oma kokemukseni tietokantasovelluksen teosta

Opin valtavasti web-sovelluksen teosta, html:stä ja pythonista. Nämä eivät olleet minulle tuttuja etukäteen. Itse sovelluksen toiminnallisuuksien tekemiseen meni minulta valtavasti aikaa, joka aiheutti sen, ettei lopulta ollut tarpeeksi aikaa keskittyä esimerkiksi ulkoasun hiomiseen bootstrapin avulla tai sivutukseen. Kuitenkin lopputulos oli parempi, mitä osasin aluksi odottaa.
