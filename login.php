<!DOCTYPE html>
<html lang="en">
<head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<nav class="navbar navbar-expand-sm navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="login.php">NIS</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="mynavbar">
            <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a class="nav-link" href="https://www.google.com.tw">Google</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://ctf.hackme.quest/scoreboard/">HackMe - CTF</a>
                </li>
            </ul>
            <form class="d-flex" method="post">
                <input class="form-control me-2" type="text" placeholder="Account" name="user">
                <input class="form-control me-2" type="password" placeholder="Password" name="password">
                <button class="btn btn-primary" type="submit" name="button">Login</button>
            </form>
        </div>
    </div>
</nav>

<div class="container-fluid mt-3">
    <h3 >
        <?php
        if (isset($_POST['button'])) {
            $db = new mysqli("localhost", "root", "", "nis");
            $q = sprintf("SELECT * FROM account WHERE user='%s' AND password = '%s'", $_POST['user'], $_POST['password']);
            $result = $db->query($q);
            if ($result->num_rows > 0) {
                $row = $result->fetch_assoc();
                printf("歡迎 %s" . PHP_EOL, $row['name']);
            }
        }
        ?>
    </h3>
<!--    <p>You can also include forms inside the navigation bar.</p>-->
</div>

</body>
</html>