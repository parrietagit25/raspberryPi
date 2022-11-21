<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHL pro</title>
    <style>
        .centerimg{
            display: block;
            margin: 0px auto;
        }
        #ventana{
            text-align:center;
        }
        .dess{
            transition-property: opacity, left;
            transition-duration: 3s, 5s, 2s, 1s;
        }
    </style>
</head>
<body>
    <img class="centerimg" src="logo.png" alt="" width="300">
    <div id="ventana" style="font-size:400px;">

    </div>
    <script>
        
        var n=0;

        document.addEventListener('keydown', (event) => {
            var keyValue = event.key;
            var codeValue = event.code;

            if (keyValue == 'ArrowUp') {
                if (n >= 18) {
                    
                }else{
                n = n + 1;
                }
                document.querySelector("#ventana").innerHTML = "<img class='dess' src='flecha_arriba.png'> " + n;
                document.querySelector("#ventana").style.color = "#039E39"; 
                setTimeout(()=>{
                    document.querySelector(".dess").style.opacity= 0;
                    fetch('ej.php') 
                    .then();
                },0.5);
                
            }else if(keyValue == 'ArrowDown'){
                if (n <= 0) {
                    
                }else{
                n = n - 1;
                }
                document.querySelector("#ventana").innerHTML = "<img class='dess' src='flecha_abajo.png'> " + n;
                document.querySelector("#ventana").style.color = "#DA0D0D";
                setTimeout(()=>{
                    document.querySelector(".dess").style.opacity= 0;
                    fetch('ej.php') 
                    .then();
                },0.5);
            }
            
            console.log("keyValue: " + keyValue);
            console.log("codeValue: " + codeValue);
        }, false);
    </script>
</body>
</html>
