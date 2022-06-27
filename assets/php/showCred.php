<html>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        Your Credentials
    </title>
    <style>
    body{
        background-image: url('http://localhost/cyberlocker/assets/img/intro-bg.jpg');
    }
    
    .animate-charcter
    {
        margin-top: 250px;
        background-image: linear-gradient(
        -225deg,
        #231557 0%,
        #44107a 29%,
        #ff1361 67%,
        #fff800 100%
        );

        background-size: auto auto;
        background-clip: border-box;
        background-size: 200% auto;
        color: #fff;
        background-clip: text;
        text-fill-color: transparent;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textclip 2s linear infinite;
        display: inline-block;
        font-size: 20px;
    }

    @keyframes textclip {
        to {
            background-position: 200% center;
        }
    }
    </style>
    <script type="text/javascript">
        function checkEvt(){
            var evTypep=window.performance.getEntriesByType("navigation")[0].type;
                if (evTypep=='reload'){
                    window.location.replace("http://localhost/cyberlocker/index.html");
                }
            }
            checkEvt();
    </script>
    </head>
    <body>
        <?php
            $file = fopen("count.txt", "r") or die("Unable to open file!");
            $temp = fgets($file);
            $count = $temp + 1;
            fclose($file);
            $file = fopen("count.txt", "w") or die("Unable to open file!");
            fwrite($file,$count);
            fclose($file);
            $lines = file("users.txt");
            $user = $lines[$temp]; 
            echo "<div class='container'>
                    <div class='row'>
                        <div class='col-md-12 text-center'>
                            <center> <h5 class='animate-charcter'> $user </h5> </center>
                        </div>
                        <center> <h4> *KINDLY NOTE DOWN YOUR CREDENTIALS.</h4> </center>
                        <center> <h4> This credentials are displayed only once. You will be able to change your password when you log into your cloud for the first time. </h4> </center>
                        <center> <h4> *Refresh to go to Homepage. </h4> </center>
                    </div>
                </div>";
        ?>
    </body>
</html>

