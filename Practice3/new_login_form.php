<?php

function is_valid($fieldName)
{
   if (!isset($_POST[$fieldName])
       return false;

   $disallowedSymbols = array('\'', '"', ';', '--');

   foreach ($disallowedSymbols as &$symbol)
	   if (strpos($_POST[$fieldName], $symbol)) return false;

   return true;
}

function is_blocked($username)
{
   $attemptsBeforeBlocking = 3;
   $timeOut = 60;

   $res = $db->query('SELECT loginTime, failsCount FROM users WHERE user = ' . $username);
   $data = $res->fetch_assoc();
 
   if ($data['failsCount'] >= $attemptsBeforeBlocking)
      if (time() - strtotime($data['loginTime']) < $timeOut)
          return true

   return false;
}

function succeed()
{
    $res = $db->query('UPDATE users SET failsCount = 0, loginTime = ' . time() . ' WHERE user = ' . $username); 
    $row = $res->fetch_assoc()

    $user = $row['user']; 
    $avatar = $row['avatar'];

    echo "<p>Welcome to the password protected area {$user}</p>";  
    echo "<img src=\"{$avatar}\" />";   
}

function fail()
{
    $res = $db->query('UPDATE users SET failsCount = failsCount + 1 WHERE user = ' . $username);

    echo "<pre><br />Username and/or password incorrect.</pre>";
}


if(isset($_POST[ 'Login' ])) {
    if (!is_valid('username') || !is_valid('password'))      
    return;                                               

    $user = $_POST['username'];
    // $salt = sha256("")
    $password = crypt($_POST['password'], $salt);

    $prepared = $db->prepare('SELECT * FROM users WHERE user = (:username) AND password = (:password) LIMIT 1;');
    $prepared->bindParam(':username', $username, PDO::PARAM_STR);
    $prepared->bindParam(':password', $password, PDO::PARAM_STR);
    $res = $prepared->execute($data);

    $is_blocked = is_blocked($username);
    if (!$is_blocked)
        succeed();
    else
        fail();    
}

?>