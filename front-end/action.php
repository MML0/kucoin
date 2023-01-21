<head>
<?php
  $data = $_GET['data1'];
  $jto  = $_GET['b1'];
  
  $path = 'data.txt';
  if (isset($_GET['data1']) ) {
  $fh = fopen($path,"a+");
  //$string = $_POST['field1'];

  fwrite($fh,$data); // Write information to the file
  fclose($fh); // Close the file

}
?>
<center>
<br><br><br><br><br><br>
<h1>data saved !</h1>
<br><br><br><br><br><br>
<a href=$path>clivk here and reload to see data</a>
</center>
</head>

