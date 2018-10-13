# Asennusohje <h1>  
Lataa git-repositorio zippinä tietokoneellesi klikkaamalla etusivulla painiketta _clone or download_. Pura paketti sopivaan kohtaan koneellesi. 

## Ohjelman käynnistäminen <h2>
(Ennen käynnistystä pitää aktivoida venvin virtuaaliympäristö?) Ohjelma käynnistetään komennolla:
```
python3 run.py
```

# Käyttöohje <h3>

## Kirjautuminen <h4>
Sovellus käynnistyy näkymään: 
Kirjautuminen onnistuu valitsemalla oikeasta yläkulmasta vaihtoehto _login_. Ylempään syötekenttään kirjoitetaan käyttäjätunnus ja alempaan syötekenttään salasana.
Jos käyttäjän luonti onnistuu, siirrytään sivulle, jossa näkyy, kuinka monta raporttia kukin käyttäjä on luonut. Uloskirjatuminen onnistuu klikkamalla ylhäältä painiketta _log out_.

## Uuden käyttäjän luominen <h5>
Aloitussivulta pääsee luomaan uuden käyttäjän klikkaamalla _Create user_. Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla _Add a new user_. Uuden käyttäjän luomisen jälkeen sovellukseen pitää kirjautua sisälle.
Jos käyttäjän luonti onnistuu, siirrytään sivulle, jossa on kaikki tällä hetkellä järjestelmään luodut luontokohteet kuvauksineen.

## Luontokohteiden selaaminen <h6> 
Luontokohteita pääsee selaamaan, vaikka ei olisi kirjautunut sisään järjestelmään. Valitsemalla ylhäältä _List nature sites_ näkee kaikki tämän hetkiset luontokohteet.

## Raporttien selaaminen <h7> 
Raportteja pääsee selaamaan, vaikka ei olisi kirjautunut sisään järjestelmään. Valitsemalla ylhäältä _All reports_ näkee kaikki luodut raportit..

## Seuraavat toiminnot ovat vain kirjatuneille käyttäjille: <h8>

## Luontokohteen luominen <h9>
Uuden luontokohteen voi luoda valitsemalla ylhäällä olevasta valikosta _Add a nature site_. Luontokohteelle pitää antaa nimi sekä kuvaus ja sen jälkeen klikata painiketta _Add a new nature site_.

## Luontokohteen kuvauksen muuttaminen <h10>
Luontokohteita selatessa voi klikata luontokohteen linkkiä, josta pääsee muokkaamaan kuvausta. Luontokohteen kuvausta voi muuttaa kirjoittamalla kohtaan _Edit description_ uuden kuvauksen ja painamalla painiketta _Change description_.

## Luontokohteen raporttien selaaminen <h11>
Luontokohteita selatessa voi klikata kyseistä luontokohdetta, josta pääsee katsomaan kyseiselle luontokohteelle luotuja raportteja.

## Raportin luominen <h12>
Kenen tahansa luomaan luontokohteeseen voi luoda uuden raportin. Uuden raportin voi luoda valitsemalla alhaalta. _Create new report_. Raportille pitää antaa otsikko sekä kuvaus ja sen jälkeen klikata painiketta _Add a new report_.

## Raportin muokkaaminen ja poistaminen <h13>
Raportteja selatessa voi klikata painiketta _edit_ ja sen jälkeen kirjoittaa kohtaan _Change description_ uusi kuvays ja painaa painiketta _Change description_. Raportin voi poistaa painamalla painiketta _Delete_. Vain omia raportteja voi muokata tai poistaa. Mikäli, yrittää muokata tai poistaa toisen luomaa raporttia, päätyy kirjautumissivulle.

## Kommenttien katsominen <h14>
Raportin kommentteja voi katsoa klikkamalla kohtaa _comments_.

## Kommentin luominen <h15>
Kenen tahansa luomaan raporttiin voi luoda uuden kommentin. Kommentin kirjoittamisen jälkeen pitää klikata painiketta _Add a new comment_.

## Kommentin muokkaaminen ja poistaminen <h16>
Kommentteja selatessa voi kommenttia muokata kirjoittamalla kohtaan _Edit_ uuden kuvauksen ja painamalla painiketta _Change text_. Kommentin voi poistaa painamalla painiketta _Delete_. Vain omia kommentteja voi muokata tai poistaa. Mikäli, yrittää muokata tai poistaa toisen luomaa kommenttia, päätyy kirjautumissivulle.


# Sovellukseen jääneet puutteet <h17>

Sovellukseen on jäänyt muutamia puutteita, esimerkiksi seuraavia asioita voisi vielä parantaa:

- Kun kommenttia muokatessa laittaa esimerkiksi liian lyhyen tekstin kommentiksi, tulee virheilmoitus sekä virheellinen teksti kaikkiin kommenttibokseihin, mikä ei ollut tarkoitus. Tätä toiminnallisuutta, olisi voinut hioa vielä lisää.
- Osa kielletyistä toiminnoista ei ole käyttäjältä piilossa. Esimerkiksi jokaista kommenttia voi yrittää poistaa, mutta vain omat kommentit poistuvat. Delete-nappulan voisi siis piilottaa, mikäli kommentti ei ole nykyisen käyttäjän kirjoittama.
- Kielletyn toiminnan tekeminen, vie aina kirjautumissivulle, mikä ei ole kaikkein tyylikkäin ratkaisu kaikissa tilanteissa
- Sivutus ei ole käytössä

# Oma kokemukseni tietokantasovelluksen teosta <h18>

Opin valtavasti web-sovelluksen teosta, html:stä ja pythonista. Nämä eivät olleet minulle tuttuja etukäteen. Itse sovelluksen toiminnallisuuksien tekemiseen meni minulta valtavasti aikaa, joka aiheutti sen, ettei lopulta ollut tarpeeksi aikaa keskittyä esimerkiksi ulkoasun hiomiseen bootstrapin avulla. Viime tingassa tuli myös lisättyä tietokantaan indeksi ja error.html, jonne pitäisi päätyä aina kun polussa on virheellinen indeksi. En myöskään ehtinyt perehtyä lainkaan sivutukseen. Sovelluksen aihe mahdollisesti levisi minulle liian laajaksi.
