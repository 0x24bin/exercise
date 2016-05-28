<?php
# the str you wanna crack
$str="abcdefghijklmnopqrstuvwxyz./{_=23";
#here is the output
$cae=$str;
#the key
$key=0;
$k=strlen($str);
while($key<26){
	$i=0;
	while($i<$k){
		switch($str[$i]){
			case 'a':
				$num=1;
				break;
			case 'b':
				$num=2;
				break;
			case 'c':
				$num=3;
				break;
			case 'd':
				$num=4;
				break;
			case 'e':
				$num=5;
				break;
			case 'f':
				$num=6;
				break;
			case 'g':
				$num=7;
				break;
			case 'h':
				$num=8;
				break;
			case 'i':
				$num=9;
				break;
			case 'j':
				$num=10;
				break;
			case 'k':
				$num=11;
				break;
			case 'l':
				$num=12;
				break;
			case 'm':
				$num=13;
				break;
			case 'n':
				$num=14;
				break;
			case 'o':
				$num=15;
				break;
			case 'p':
				$num=16;
				break;
			case 'q':
				$num=17;
				break;
			case 'r':
				$num=18;
				break;
			case 's':
				$num=19;
				break;
			case 't':
				$num=20;
				break;
			case 'u':
				$num=21;
				break;
			case 'v':
				$num=22;
				break;
			case 'w':
				$num=23;
				break;
			case 'x':
				$num=24;
				break;
			case 'y':
				$num=25;
				break;
			case 'z':
				$num=26;
				break;
			default:
				$num=100;
				break;
		}

		switch($num+$key){
			case 1:
				$cae[$i]='a';
				break;
			case 2:
				$cae[$i]='b';
				break;
			case 3:
				$cae[$i]='c';
				break;
			case 4:
				$cae[$i]='d';
				break;
			case 5:
				$cae[$i]='e';
				break;
			case 6:
				$cae[$i]='f';
				break;
			case 7:
				$cae[$i]='g';
				break;
			case 8:
				$cae[$i]='h';
				break;
			case 9:
				$cae[$i]='i';
				break;
			case 10:
				$cae[$i]='j';
				break;
			case 11:
				$cae[$i]='k';
				break;
			case 12:
				$cae[$i]='l';
				break;
			case 13:
				$cae[$i]='m';
				break;
			case 14:
				$cae[$i]='n';
				break;
			case 15:
				$cae[$i]='o';
				break;
			case 16:
				$cae[$i]='p';
				break;
			case 17:
				$cae[$i]='q';
				break;
			case 18:
				$cae[$i]='r';
				break;
			case 19:
				$cae[$i]='s';
				break;
			case 20:
				$cae[$i]='t';
				break;
			case 21:
				$cae[$i]='u';
				break;
			case 22:
				$cae[$i]='v';
				break;
			case 23:
				$cae[$i]='w';
				break;
			case 24:
				$cae[$i]='x';
				break;
			case 25:
				$cae[$i]='y';
				break;
			case 26:
				$cae[$i]='z';
				break;
			case 27:
				$cae[$i]='a';
				break;
			case 28:
				$cae[$i]='b';
				break;
			case 29:
				$cae[$i]='c';
				break;
			case 30:
				$cae[$i]='d';
				break;
			case 31:
				$cae[$i]='e';
				break;
			case 32:
				$cae[$i]='f';
				break;
			case 33:
				$cae[$i]='g';
				break;
			case 34:
				$cae[$i]='h';
				break;
			case 35:
				$cae[$i]='i';
				break;
			case 36:
				$cae[$i]='j';
				break;
			case 37:
				$cae[$i]='k';
				break;
			case 38:
				$cae[$i]='l';
				break;
			case 39:
				$cae[$i]='m';
				break;
			case 40:
				$cae[$i]='n';
				break;
			case 41:
				$cae[$i]='o';
				break;
			case 42:
				$cae[$i]='p';
				break;
			case 43:
				$cae[$i]='q';
				break;
			case 44:
				$cae[$i]='r';
				break;
			case 45:
				$cae[$i]='s';
				break;
			case 46:
				$cae[$i]='t';
				break;
			case 47:
				$cae[$i]='u';
				break;
			case 48:
				$cae[$i]='v';
				break;
			case 49:
				$cae[$i]='w';
				break;
			case 50:
				$cae[$i]='x';
				break;
			case 51:
				$cae[$i]='y';
				break;
			case 52:
				$cae[$i]='z';
				break;
			default:
				
				break;
		}
		
		
		if($k-$i==1){
			echo $cae;
			echo "\n";
		}
		$i++;
	}
	
	$key++;

}
?>
