# Анализ уязвимостей

## CWE-523: Unprotected Transport of Credentials<br>CWE-598: Use of GET Request Method With Sensitive Query Strings
```php
if( isset( $_GET[ 'Login' ] ) ) {
    $user = $_GET[ 'username' ];
    $pass = $_GET[ 'password' ];
```
**Исправление:** использовать метод POST, чтобы не раскрывать пароль в query string

## CWE-20: Improper Input Validation<br>CWE-790: Improper Filtering of Special Elements
**Исправление:** проверить вводимые данные на спец символы, нейтрализовать эти символы.

## CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
```php
$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
```
**Исправление:** использовать PDO и prepared statements.

## CWE-326: Inadequate Encryption Strength<br>CWE-327: Use of a Broken or Risky Cryptographic Algorithm<br>CWE-328: Use of Weak Hash
```php
$pass = md5( $pass );
```
**Исправление:** использовать более криптостойкий алгоритм хэширования SHA-256.

## CWE-759: Use of a One-Way Hash without a Salt
**Исправление:** использовать соль при хэшировании

## CWE-307: Improper Restriction of Excessive Authentication Attempts<br>CWE-799: Improper Control of Interaction Frequency
**Исправление:** ограничить количество попыток для отправки запросов, поставить капчу или тайм-аут перед следующей попыткой.

## CWE-654: Reliance on a Single Factor in a Security Decision
**Исправление:** добавление двухфакторной аутентификации или введение капчи.
