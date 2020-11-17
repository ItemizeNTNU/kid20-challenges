# sql-login:
## Description:
On this web page we are presented with only a login terminal and the text.
---

###Welcome to my first web page!
####Only administrators are allowed to see the secrets of this web page

---

The name of this task hints towards SQL injection so we will start by checking if the web page is vulnerable to SQL injections. By typing ``'";`` in the username field and pressing enter we get the following error code: 
```
Uncaught mysqli_sql_exception: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '"; ' AND password = 'dwd'' at line 1 in /var/www/html/login.php:41 Stack trace: #0 /var/www/html/login.php(41): mysqli_query(Object(mysqli), 'SELECT * FROM U...') #1 {main} thrown in /var/www/html/login.php on line 41
``` 

We now know SQL injection is possible and want to try to login. 
Since we are given the information that only administrators are allowed to see the secrets of the page we have to try and login as an administrator. Knowing the username of the administrator is not always easy, however guessing *admin* is a good place to begin. Since we do not know the password we need to somehow make the SQL query ignore the password field. This can be done in many ways, but by commenting out everthing after the username is a simple solution. We therefore type in the following:
```
username: admin' -- 
password: whatever
```
(make sure to have a space after the last *-* in the username)
Which will result in the following SQL query:
```sql 
SELECT * FROM Users WHERE username = 'admin' --  AND password = 'whatever'
```

And we will end up with the flag displayed on the web page
```
KID20{sql_inj3cti0n_i5_alw4ys_fun}
```