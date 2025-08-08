HOLYSIMPLICITY - první projekt
Jednoduchá webová aplikace pro prezentaci firmy a příjem poptávek.

Co projekt umí
Statický web s informacemi o firmě HOLYSIMPLICITY s.r.o.
Kontaktní formulář, který odesílá zprávy na backend
Backend napsaný v Django, který přijímá poptávky přes API
Odesílání poptávek e-mailem na zadanou adresu

Použité technologie
Frontend: HTML, CSS, JavaScript
Backend: Django, Django REST Framework
Hosting: Netlify (frontend), Render (backend)
E-mailový server: SMTP Seznam.cz

Jak spustit projekt lokálně
Naklonuj repozitář:
git clone https://github.com/eNesibleed/holysimplicity.git
Nastav prostředí a nainstaluj závislosti:
pip install -r requirements.txt
Nastav .env soubor s potřebnými proměnnými (např. SECRET_KEY, DATABASE_URL, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
Spusť migrace databáze:
python manage.py migrate
Spusť backend server:
python manage.py runserver
Otevři frontend (statické soubory) ve webovém prohlížeči

Poznámka
REST API pro správu poptávek není veřejně přístupné v nasazené verzi projektu.
