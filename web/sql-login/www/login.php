<html>
<head>
<title>Login</title>
<style type="text/css">
body {
	background-color: #aaaaaa;
}
.centerDiv {
	border: 2px solid #000000;
	border-radius: 25px;
	background-color: lightblue;
  	text-align: center;
  	padding: 10px;
  	margin: 30px;
  	display: block;
}
#p {
	font-size: 1px;
}
</style>
</head>
<body>
<div class="centerDiv">
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$username = $_POST['name'];
$password  = $_POST['psw'];
$debug = $_POST['debug'];
// Create connection
$con = mysqli_connect("db:3306","db_user","db_password","db_test");

if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  exit();
}
// Perform query
$query = "SELECT * FROM Users WHERE username = '$username' AND password = '$password'";
if ($debug) {
	echo "<p>SQL query performed: ".$query."</p>";
}
$result = mysqli_query($con, $query);
if ($result) {
	if (mysqli_num_rows($result)==1){
		echo "<h1>Login successfull!</h1>";
		echo "<p> KID20{sql_inj3cti0n_i5_alw4ys_fun}</p>";
	}
	else {
		echo "<h1>Login failed</h1>";
		echo "<p>Username and password combination not existing</p>";
	}

}
else {
	echo "<h1>Login failed</h1>";
	echo("Error description: " . mysqli_error($con));
	echo "<p>SQL query: $query</p>";
}
mysqli_close($con);
?>
</div>
</body>
</html>

