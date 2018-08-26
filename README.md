Aiheen kuvaus

Luodaan sovellus jonka avulla käyttäjä voi pitää kirjaa lukemistaan kirjoista ja niistä kirjoista jotka haluaa lukea.
Kirjat voi jakaa kategorioihin niiden genren sekä kirjasarjan perusteella. Oletuksena jokainen käyttäjä voi nähdä vain oman listansa.

Testitunnukset:
Username: hello
Password: world

Tunnettuja haavoittuuvuuksia ja muita ongelmia:
  - Kirjoja voi poistaa tai ne merkitä luetuiksi id:n perusteella vaikka ei olisi oma kirja
  - Plaintext pw
    - "But how could we check if the password is right if it is crypted?" -Yahoo

Toimintoja:
  - Kirjautuminen
  - Genren lisääminen/tarkasteleminen/poisto
  - Kirjasarjan lisääminen/tarkasteleminen/poisto
  - Kirjojen lisääminen/tarkasteleminen/poisto
    - Kirjojen tarkasteleminen eri kriiterien perusteella kuten genre tai luettu/lukematta
  - Jos aikaa jää niin useampien listojen tekeminen, joita voisi myös jakaa

  Heroku: [kirjakanta.herokuapp.com]


  User Story:
  - Käyttäjänä voin lisätä kirjoja listaani -- Tehty
  - Käyttäjänä voin lisätä genrejä sekä kirjasarjoja "alaotsikoiksi" helpottamaan lajittelua -- Kirjoihin on liitetty genret, tekijät sekä kirjsarja
  - käyttäjänä voin listata kirjoja genren tai kirjasarjan perusteella -- ei tehty
  - käyttäjänä voin merkitä lukemani kirjat luetuiksi -- tehty
  - käyttäjänä voin määrittää onko listani julkinen vai ei -- ei tehty
  - käyttäjänä voin selata muiden käyttäjien julkisia listoja -- ei tehty


  - ylläpitäjänä voin tarkastella käyttäjiä sekä heidän lisäämiään kirjojaan ja genrejä -- ei tehty

  Tietokantakaavio:
  ![alt text](documentation/Tietokantakaavio.png)


  Asennusohjeet:
    Ovat hieman myöhässä. Tässä pikaisesti laaditut

    - Lataa tiedostot githubista
    - Luo python virtuaaliympäristö komennolla
      - python -m venv venv
    - avaa virutaaliympäristö
      - source venv/bin/activate
    - Asenna riipuvuudet
      - pip install -r requirements.txt
    - Käynnistä sovellus
      - python run.py
