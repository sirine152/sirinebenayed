<?php
// Exemple de code PHP vulnérable
// Connexion à la base de données sans gestion d'exception
$host = 'localhost';
$dbname = 'testdb';
$username = 'root';
$password = '';
$conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
// Réception des données de l'utilisateur sans validation
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$username = $_POST['username'];
$password = $_POST['password'];
// Injection SQL possible
$query = "SELECT * FROM users WHERE username = '$username' AND
password = '$password'";
$stmt = $conn->query($query);
if ($stmt->rowCount() > 0) {
echo "Bienvenue, $username!";
} else {
echo "Nom d'utilisateur ou mot de passe incorrect.";
}
}
// Affichage direct des données utilisateur sans encodage
if (isset($_GET['id'])) {
$id = $_GET['id'];
$query = "SELECT * FROM users WHERE id = $id";
foreach ($conn->query($query) as $row) {
echo "Nom : " . $row['name'] . "<br>";
echo "Email : " . $row['email'] . "<br>";
}
}
?>
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Login</title>
</head>
<body>
<h1>Login</h1>
<form method="post" action="">
<label for="username">Nom d'utilisateur :</label>
<input type="text" id="username" name="username"><br><br>
<label for="password">Mot de passe :</label>
<input type="password" id="password" name="password"><br><br>
<button type="submit">Connexion</button>
</form>
</
