<?php 
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
fwrite($myfile, $_GET['hi']);

?>