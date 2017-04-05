<?php echo "Data Sensor"; ?>
<p>
<?php echo date('Y-m-d H:i:s'); ?>
<p>
<?php
$file = '/sys/bus/w1/devices/28-03167526c6ff/w1_slave';   // Change the id device, you can check it in /sys/bus/w1/devices/
$lines = file($file);
$temp = explode('=', $lines[1]);
$temp = number_format($temp[1] / 1000, 1, '.', '');
echo "Current Temp: ",$temp ,"<BR><p>";
?>


<?php
function showData(){

$serverName = "localhost";
$userName = "root4";
$password = "1234";
$dbname = "tempSensor1";

$db_handle = mysqli_connect($serverName, $userName, $password );
$db_found = mysqli_select_db($db_handle, $dbname);

if ($db_found) {

$SQL = "SELECT * FROM dataSensor1";
$result = mysqli_query($db_handle, $SQL);

while ( $db_field = mysqli_fetch_assoc($result) ) {

print $db_field['tdate'] . "<BR>";
print $db_field['ttime'] . "<BR>";
print $db_field['sensor'] . "<BR>";
print $db_field['temperature'] . "<BR>";
echo "<BR>";
}

}
else {
print "Database NOT Found ";

}

mysqli_close($db_handle);

} //end showData

?>


<?php
 if($_GET['showData']){
        showData();
 }

?>

<html>
  <head>
    <title> Example Show Temp</title>
  </head>
  <body>
    <button id="showData" name="showData" onClick='location.href="?showData=1"'>ShowData</button>
  </body>
</html>

