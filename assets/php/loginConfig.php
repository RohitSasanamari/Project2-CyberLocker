<?php 
include("config.php");

if(isset($_POST['submit']))
{
$email = $_POST['email'];
$password = $_POST['password'];
$sql = "Select * from users where email='$email' and password='$password'";
$res = mysqli_query($conn,$sql);
$result=mysqli_fetch_array($res);
if($result)
{
	echo '<script>alert("Successfully logged in.")</script>';
	header("Location: http://localhost:5000/");  
}
else
{
	echo '<script>alert("Incorrect Email or Password !! Try again.")</script>';
}
}  
?>