Анализ уязвимостей

CWE-20: Improper Input Validation - вводимые пользователем данные не проверяются на безопасность их использования
CWE-790: Improper Filtering of Special Elements
Исправление: проверять вводимые данные на спец символы, нейтрализовать эти символы.

CWE-89 : Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
Исправление: использовать PDO и prepared statements.

CWE-523: Unprotected Transport of Credentials
CWE-598: Use of GET Request Method With Sensitive Query Strings
Исправление: использовать метод POST, чтобы не раскрывать пароль в query string

CWE-326: Inadequate Encryption Strength
CWE-327: Use of a Broken or Risky Cryptographic Algorithm
CWE-328: Use of Weak Hash
Исправление: использовать более криптостойкий алгоритм хэширования SHA-256.

CWE-759: Use of a One-Way Hash without a Salt
Исправление: использовать соль при хэшировании

CWE-307: Improper Restriction of Excessive Authentication Attempts
CWE-799: Improper Control of Interaction Frequency
Исправление: ограничить количество попыток для отправки запросов, поставить капчу или тайм-аут перед следующей попыткой.

CWE-654: Reliance on a Single Factor in a Security Decision
Исправление: добавление двухфакторной аутентификации или введение капчи.