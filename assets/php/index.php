<?php
include("config.php");
if(isset($_POST['submit']))
{
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $pass = $_POST['password'];
    $check = "Select * from users where email='$email'";
    $check2 = "Select * from users where phone='$phone'";
    $res = mysqli_query($conn,$check);
    $res2 = mysqli_query($conn, $check2);
    if (mysqli_num_rows($res) > 0) {
        echo '<script>alert("Email already exists !! Try again.")</script>';
        exit();
    }
    if(mysqli_num_rows($res2) > 0) {
        echo '<script>alert("Phone number already exists !! Try again.")</script>';
    }
    else{     
        $sql = "INSERT INTO users (name, email, phone, password) 
        VALUES ('$name','$email','$phone','$pass')";
        $run = mysqli_query($conn,$sql);
        mysqli_close($conn);
        echo '<script type="text/javascript">
        var r = confirm("You are sucessfully registered. Press OK to get your Cloud Credentials. NOTE IT DOWN. ");
        if(r == true){
            window.location.assign("http://localhost/cyberlocker/assets/php/showCred.php"); 
        }
        </script>';
    }
}
?>

    