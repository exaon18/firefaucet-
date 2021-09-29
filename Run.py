
yggl<?php

$Color_Off="\033[0m";      

$Black="\033[0;30m";      

$Red= "\033[0;31m";         

$Green="\033[0;32m";      

$Yellow="\033[0;33m";       

$Blue="\033[0;34m";         

$Purple="\033[0;35m";      

$Cyan="\033[0;36m";       

$White="\033[0;37m";       

$IYellow="\033[0;93m";      

$IRed="\033[0;91m";         

$BIRed="\033[1;91m";   

$On_Cyan="\033[46m";

$BIWhite="\033[1;97m";     

$BIBlue="\033[1;94m";      

$BICyan="\033[1;96m";       

$BIBlack="\033[1;90m";     

$BBlack="\033[1;30m";

$IBlack="\033[0;90m";  

$On_White="\033[47m";     

$BIBlue="\033[1;94m";

$On_IRed="\033[0;101m";

$On_Red="\033[41m";   

$On_Blue="\033[44m";

$On_Green="\033[42m";  

$IGreen="\033[0;92m";   

//red to yellow shade ↓

$r3="\033[01;38;5;196m";

$r2="\033[01;38;5;202m";

$r1="\033[01;38;5;208m";

$ry="\033[01;38;5;214m";

$y1="\033[01;38;5;220m";

$y2="\033[01;38;5;226m";

$y3="\033[01;38;5;228m";

$date = exec("date\n");

system('clear');

sleep(1);

error_reporting(0);

echo$r3."                 \n";
echo$r2."                      \n";
echo$r1."           on tech  

        _____,    _..-=-=-=-=-====--,

     _.'a   /  .-',___,..=--=--==-'`

    ( _     \ /  //___/-=---=----'

     ` `\    /  //---/--==----=-'

  ,-.    | / \_//-_.'==-==---='

 (.-.`\  | |'../-'=-=-=-=--'

  (' `\`\| //_|-\.`;-~````~,        _

       \ | \_,_,_\.'        \     .'_`\

        `\            ,    , \    || `\\

          \    /   _.--\    \ '._.'/  / |

          /  /`---'   \ \   |`'---'   \/

         / /'          \ ;-. \

   __/ /           __) \ ) `|

    ((='--;)         (,___/(,_/ITS EXAON          \n";
echo$ry."                   n";
echo$y1."                  \n";
echo$y2."                 \n';
echo$y3."                                                                  \n";

echo"

";

echo $IGreen."[ ".$date." ]".$Color_Off."\n";

sleep(1);

echo"_____________________________________________________________________________\n";

echo" ____  _   ___   ____      ____   __    _     __    ____ _____ 

| |_  | | | |_) | |_      | |_   / /\  | | | / /`  | |_   | |  

|_|   |_| |_| \ |_|__     |_|   /_/--\ \_\_/ \_\_, |_|__  |_|

";

echo"_____________________________________________________________________________\n";

exec("xdg-open \"https://youtube.com/channel/UCf_tfuMFBEmeyUEhRkwTH3A\" > /dev/null 2>&1 &");

echo"

";

echo$BIWhite.$On_Blue."Like",$Color_Off."👍 | ";

sleep(1);

echo$BIWhite.$On_Green."Share",$Color_Off."🍻 | ";

sleep(1);

echo$BIWhite.$On_Red."subscribe",$Color_Off."🔔 \n👆        👆         👆";

echo$Color_Off." \n";

echo " \n";

function password (){

  $IRed="\033[0;91m";

  $IGreen="\033[0;92m";

$ch1 = curl_init();

curl_setopt($ch1, CURLOPT_URL , "https://controlc.com/9d47fe67");

curl_setopt($ch1, CURLOPT_FOLLOWLOCATION , true);

curl_setopt($ch1, CURLOPT_RETURNTRANSFER , 1);

$resultraw = curl_exec($ch1);

#echo$resultraw;

$startfull = explode("<iframe frameborder='0' id='pasteFrame' src=\"", $resultraw)[1];

$fullscrnlink = explode('"', $startfull)[0];

#echo$fullscrnlink;

$ch1 = curl_init();

curl_setopt($ch1, CURLOPT_URL , $fullscrnlink);

curl_setopt($ch1, CURLOPT_FOLLOWLOCATION , true);

curl_setopt($ch1, CURLOPT_RETURNTRANSFER , 1);

$resultfull = curl_exec($ch1);

#echo$resultfull;

$startmsg = explode('class="prettyprint">', $resultfull)[1];

$msg = explode('</pre>', $startmsg)[0];

#echo$msg."\n";

$ch1 = curl_init();

curl_setopt($ch1, CURLOPT_URL , "https://controlc.com/04400cbd");

curl_setopt($ch1, CURLOPT_FOLLOWLOCATION , true);

curl_setopt($ch1, CURLOPT_RETURNTRANSFER , 1);

$resultrawpass = curl_exec($ch1);

$startfull = explode("<iframe frameborder='0' id='pasteFrame' src=\"", $resultrawpass)[1];

$fullscrnlink = explode('"', $startfull)[0];

#echo$fullscrnlink;

$ch1 = curl_init();

curl_setopt($ch1, CURLOPT_URL , $fullscrnlink);

curl_setopt($ch1, CURLOPT_FOLLOWLOCATION , true);

curl_setopt($ch1, CURLOPT_RETURNTRANSFER , 1);

$resultpass = curl_exec($ch1);

#echo$resultpass;

$content= explode('class="prettyprint">Links :- ',$resultpass)[1];

$content1= explode('Password :- ',$resultpass)[1];

$link= explode('Password',$content)[0];

$pass= explode('</pre>',$content1)[0];

$check = file_exists("password.txt");

if($check!=true){

  #echo$pass;

  echo$msg."\n";

  echo"\n"."\n";

$file = fopen("password.txt", "w");

$input= readline("Links: ↓"."\n\n".$link."\n"."\n"."Enter password: ");

$file1 = fopen("password.txt", "w");

fwrite($file1,$input);

fclose($file1);

if($input!=$pass)

{

  echo$IRed."password wrong (×)\n";

  sleep(1);

  exit;

}

else{

  echo$IGreen."password success (✓)\n"; 

  sleep(1);

  system ("clear");

}

}

else{

$file = fopen("password.txt", "r");

$saved = fgets($file);

fclose($file);

if($saved != $pass)

{

  echo$msg."\n";

  echo"\n"."\n";

$input= readline("Links: ↓"."\n\n".$link."\n"."Enter password: ");

$file1 = fopen("password.txt", "w");

fwrite($file1,$input);

fclose($file1);

if($input!=$pass)

{

  echo$IRed."password wrong (×)\n";

  sleep(1);

  exit;

}

else{

  echo$IGreen."password success (✓)\n";

  sleep(1);

  system ("clear");

}

}

}

}

password ();

system ("clear");

echo$r3."           \n";
echo$r2."          \n";
echo$r1."    on tech  
        _____,    _..-=-=-=-=-====--,
     _.'a   /  .-',___,..=--=--==-'`
    ( _     \ /  //___/-=---=----'
     ` `\    /  //---/--==----=-'
  ,-.    | / \_//-_.'==-==---='
 (.-.`\  | |'../-'=-=-=-=--'
  (' `\`\| //_|-\.`;-~````~,        _
       \ | \_,_,_\.'        \     .'_`\
        `\            ,    , \    || `\\
          \    /   _.--\    \ '._.'/  / |
          /  /`---'   \ \   |`'---'   \/
         / /'          \ ;-. \
   __/ /           __) \ ) `|
    ((='--;)         (,___/(,_/ITS EXAON       \n";
echo$ry."          \n";
echo$y1."           \n";
echo$y2.'                    \n";
echo$y3."                                 |
\n";

echo"

";

echo $IGreen."[ ".$date." ]".$Color_Off."\n";

echo"_____________________________________________________________________________\n";

echo" ____  _   ___   ____      ____   __    _     __    ____ _____ 

| |_  | | | |_) | |_      | |_   / /\  | | | / /`  | |_   | |  

|_|   |_| |_| \ |_|__     |_|   /_/--\ \_\_/ \_\_, |_|__  |_|

";

echo"_____________________________________________________________________________\n";

echo"

";

echo$BIWhite.$On_Blue."Like",$Color_Off."👍 | ";

echo$BIWhite.$On_Green."Share",$Color_Off."🍻 | ";

echo$BIWhite.$On_Red."subscribe",$Color_Off."🔔 \n👆        👆         👆";

echo$Color_Off." \n";

echo " \n";

while(true){

$ua = array(

  include ("cfg.php"),

  "user-agent: ".$uag,

  include ("cfg.php"),

  "cookie: ".$cookie

  

  );

$ch = curl_init();

curl_setopt($ch ,CURLOPT_URL , "https://firefaucet.win/internal-api/payout/" );

curl_setopt($ch ,CURLOPT_FOLLOWLOCATION ,true );

curl_setopt($ch ,CURLOPT_RETURNTRANSFER ,1);

curl_setopt($ch ,CURLOPT_HTTPHEADER , $ua);

curl_setopt($ch ,CURLOPT_SSL_VERIFYPEER , 1 );

curl_setopt($ch ,CURLOPT_COOKIEJAR , "cookie.txt" );

curl_setopt($ch ,CURLOPT_COOKIEFILE , "cookie.txt" );

$result = curl_exec($ch);

#echo$result."\n";

$check = explode('success":',$result)[1];

$check = explode(',',$check)[0];

$coins = explode('"logs":{',$result)[1];

$coins = explode('}',$coins)[0];

$balance = explode('{"balance":',$result)[1];

$balance = explode(',',$balance)[0];

$time = explode('"time_left":"',$result)[1];

$time = explode('"}',$time)[0];

if($check=="true"){

  echo$IGreen."[✓] ".$White.$On_Green."Successfully claimed ".$coins.$Color_Off."\n";

  echo$White."Auto claims Remaining: ".$Black.$On_White.$balance.$Color_Off."\n";

  echo$White."Time until Faucet Stops :".$Black.$On_White.$time.$Color_Off."\n";

  echo$IGreen."——————————————————————————————————————————————————————\n";

  echo"——————————————————————————————————————————————————————".$Color_Off."\n";

}else{

  echo$IRed."[×] ".$Black.$On_Red."Error! Not Claimed (time over or Cookies expired).".$Color_Off."\n";

  echo$IRed."------------------------------------------------------".$Color_Off."\n";

}

for ($i=60;$i>-1;$i--){

echo "\r                                                   \r";

echo"["."⏳"."] "."Please Wait ".$i." Seconds";

        if($i<=60){echo$r3." •";}

			  if($i<=54){echo$r2."•";}

			  if($i<=48){echo$r1."•";}

			  if($i<=42){echo$ry."•";}

			  if($i<=36){echo$y1."•";}

			  if($i<=30){echo$y2."•";}

			  if($i<=24){echo$y3."•";}

			  if($i<=18){echo$Yellow."•";}

			  if($i<=12){echo$Green."•";}

			  if($i<=6){echo$IGreen."•";}

sleep(1);

echo "\r                                                   \r";

}

}
