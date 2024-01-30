<?php
    session_start();
    if(isset($_SESSION['username']))
    {
        echo "Welcome ".$_SESSION['username']."<br>";
        echo "<a href='logout.php'>Logout</a>";
    }
    else
    {
        header("location:login.php");
    }