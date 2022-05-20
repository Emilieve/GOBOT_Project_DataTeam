<?php
// put in email adress here -------------------------------<email down here>
$url = 'https://api.seon.io/SeonRestService/email-api/v2.1/mericobi@gmail.com';

//refer to the API key
$headers = array(
  "X-API-KEY: 006c4bc3-4454-4990-8be1-3b0ce6e4df50"
);

//copied from the website
$curl = curl_init($url);

$ch = curl_init();
curl_setopt_array($ch,array(
  CURLOPT_URL => $url,
  CURLOPT_FOLLOWLOCATION => false,
  CURLOPT_HEADER => false,
  CURLOPT_HTTPHEADER => $headers,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_HTTPGET => true,
));

$result = curl_exec($ch);

$err = curl_error($ch);
if (curl_errno($ch) && $err) $res = "CURL ERROR [".curl_errno($ch)."]: ".curl_error($ch);
else $res = $result;

//store the result in yummy and create string out of it so we can take parts of it
$yummy = json_decode($res, true);

// for each key in account details (facebook, linkedin, instagram etc.)
foreach ($yummy['data']['account_details'] as $key => $value) {
    // for each key in facebook instagram linkedin etc. go over all the values > registered, name, town etc.
    foreach ($value as $key => $value){
        //show it
        echo "The value of key '$key' is '$value'", PHP_EOL;
    }
        
}

?>
