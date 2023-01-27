# Installation du projet DevDuel

### 1) Cloner le dépôt git: https://github.com/TheoROB/dd-api

### 2) cd dd-api/

### 3) python -m venv venv

### 4) pip install -r requirements.txt

### 5) Télécharger Postgresql 14.6 et lancer PgAdmin en locale

### 6) Créer une base de données "DDEV accéssible sur le port 5432

### 7) (Si il n'y a pas de migration) Créer une nouvelle migration avec la commande: python manager.py makemigrations

### 8) Appliquer la nouvelle migration avec la commande: python manager.py migrate

### 9) Vérifier que les tables sont bien crées dans la base de données

### 10) Lancer le server avec la commande: python manage.py runserver

## Le server est prêt à recevoir des requetes !

### Pour exploiter l'API, rendez vous sur PostMan

### Pour visualiser les routes disponibles 
#### GET: http://127.0.0.1:8000/api/

### Pour récupérer tous les joueurs 
#### GET: http://127.0.0.1:8000/api/players/

### Pour récupérer un joueur avec son ID
#### GET: http://127.0.0.1:8000/api/player/
#### body: { "id" : int }

### Pour récupérer les joueurs en fonction de leur elo
#### GET: http://127.0.0.1:8000/api/players/elo

### Pour créer un nouveau joueur
#### POST: http://127.0.0.1:8000/api/player/new
#### body: { "pseudo": string, "image": string, "elo": int, "attack": int, "creator_id": int }

### Pour créer un nouveau user
#### POST: http://127.0.0.1:8000/api/user/new
#### body: { "name": string, "password": string }

### Pour créer un nouveau résultat de combat
#### POST: http://127.0.0.1:8000/api/result/new
#### body: { "player1_id": string, "player2_id": string, "winner_id": string }

### Pour modifier les informations d'un player
#### PUT: http://127.0.0.1:8000/api/player/update
#### body: { "pseudo": string, "image": string, "elo": int, "attack": int, "creator_id": int }

### Pour supprimer un player
#### DELETE: http://127.0.0.1:8000/api/player/delete
#### body: { "id": id }

### Pour supprimer un user
#### DELETE: http://127.0.0.1:8000/api/user/delete
#### body: { "id": id }
