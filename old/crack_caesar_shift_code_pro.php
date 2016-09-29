<?php
#the string you wanna crack
$str="abcdefghijklmnopqrstuvwxyz}/,=_23";
$cas=$str;
$letter=array('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z');
#the key
$key=0;
$len=strlen($str);
while ($key<26) {
	$i=0;
	while($i<$len){
		if (in_array($str[$i],$letter)) {
			$num=array_search($str[$i], $letter);
			if(($num+$key)<26) {
				$cas[$i]=$letter[$num+$key];
			}
			else if(($num+$key)>=26){
				$cas[$i]=$letter[$num+$key-26];
			}
		}
		
		$i++;
	}
	echo $cas;
	echo "\n";
	$key++;
}
?>
