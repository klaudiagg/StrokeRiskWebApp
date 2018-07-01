<?php
    session_start();

    DB::connect($dbServer, $dbLogin, $dbHaslo, $dbBaza);
    DB::getConnection() -> query ('SET NAMES utf8');
    DB::getConnection() -> query ('SET CHARACTER_SET utf8_unicode_ci');
?>