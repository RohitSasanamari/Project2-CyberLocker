<?php
$server = 'localhost';
$username = 'root';
$password = 'dbconnect';
$dbname = 'cyberlocker';

$conn = mysqli_connect($server,$username,$password,$dbname);

// if(!$conn) {
//     die("Connection failed: ".  mysqli_connect_error());
// }

if(isset($_POST['submit']))
{
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $pass = $_POST['password'];
    $sql = "INSERT INTO users (name, email, phone, password) 
    VALUES ('$name','$email','$phone','$pass')";
    $run = mysqli_query($conn,$sql) or die(mysqli_error());
    if(!$run){
        echo "Form not submitted";
    }
    header("Location: http://localhost/cyberlocker/index.html");
    mysqli_close($conn);
}
?>
<!-- <script type="text/javascript">
    alert("Account Created");
</script> -->
    