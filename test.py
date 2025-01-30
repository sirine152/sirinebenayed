import sqlite3
from flask import Flask, request, render_template_string
app = Flask(__name__)
# Connexion à la base de données
conn = sqlite3.connect('testdb.sqlite', check_same_thread=False)
cursor = conn.cursor()
# Création de la table utilisateur
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
password TEXT NOT NULL,
email TEXT
)
''')
conn.commit()
# Remplir la base de données avec un utilisateur de test
cursor.execute("INSERT INTO users (username, password, email) VALUES ('admin',
'password123', 'admin@example.com')")
conn.commit()
# Route pour la page de connexion
@app.route('/', methods=['GET', 'POST'])
def login():
if request.method == 'POST':
username = request.form.get('username')
password = request.form.get('password')
# Requête SQL
query = f"SELECT * FROM users WHERE username = '{username}' AND
password = '{password}'"
result = cursor.execute(query).fetchone()
if result:
return f"Bienvenue, {username}!"
else:
return "Nom d'utilisateur ou mot de passe incorrect."
# Formulaire de connexion
html = '''
<!DOCTYPE html>
<html>
<head>
<title>Login</title>
</head>
<body>
<h1>Login</h1>
<form method="post" action="/">
<label for="username">Nom d'utilisateur :</label>
<input type="text" id="username" name="username"><br><br>
<label for="password">Mot de passe :</label>
<input type="password" id="password" name="password"><br><br>
<button type="submit">Connexion</button>
</form>
</body>
</html>
'''
return render_template_string(html)
# Route pour afficher les informations utilisateur
@app.route('/user/<int:user_id>')
def user_profile(user_id):
# Requête SQL
query = f"SELECT * FROM users WHERE id = {user_id}"
result = cursor.execute(query).fetchone()
if result:
return f"Nom : {result[1]}<br>Email : {result[3]}"
else:
return "Utilisateur introuvable."
if __name__ == '__main__':
app.run(debug=True)
