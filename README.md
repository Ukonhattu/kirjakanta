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
  - Kirjojen lisääminen/tarkasteleminen/poisto
  - Käyttäjätietojen muuttaminen ja tilin poisto

  Heroku: [kirjakanta.herokuapp.com]


  User Story:
  - Käyttäjänä voin lisätä kirjoja listaani
  - Käyttäjänä voin liittää genrejä, kirjasarjan ja kirjailijoita kirjaan
  - käyttäjänä voin merkitä lukemani kirjat luetuiksi
  - käyttäjänä voin poistaa lisäämäni kirjat
  - käyttäjänä voin poistaa käyttäjätilini ja samalla lisäämäni kirjat
  - käyttäjänä voin muokata käyttäjätietojani



  Tietokantakaavio:
  ![alt text](documentation/Tietokantakaavio.png)


  Asennusohjeet:

    - Lataa tiedostot githubista
    - Luo python virtuaaliympäristö komennolla
      - python -m venv venv
    - avaa virutaaliympäristö
      - source venv/bin/activate
    - Asenna riipuvuudet
      - pip install -r requirements.txt
    - Käynnistä sovellus
      - python run.py

[Käyttöohje](documentation/kayttoohje.md)
