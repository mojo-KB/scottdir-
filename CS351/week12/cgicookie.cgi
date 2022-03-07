#!/usr/bin/perl
# Author:       Robert Eger
# Date:         3/27/14
# Class:        CS351
# Location:     ~EGERR/www/CS351/hw7.cgi


print "Content-type: text/html\n\n";
use CGI qw/:standard/;
use CGI::Cookie;


print "Hello<br>\n";


if ($ENV{'CONTENT_LENGTH'} == 0) {
	$content{'linenumber'} = 0;
	$content{'file'}="Homework3.txt";
	$content{'oldfile'}="Homework4.txt";
    $content{'dir'}="forward";
    $content{'olddir'}="forward";
	@files = (
		"Homework3.txt",
		"Homework4.txt",
		"Homework5a.txt");
	}
else{
	read(STDIN,$buffer,$ENV{'CONTENT_LENGTH'});
	foreach $pair (split(/&/,$buffer)){
	    ($vari,$value)=split(/=/,$pair);
		if($vari eq "files"){
			push(@files, $value)
		}else{
	        $content{$vari}=$value;}
        }
}

$cookies = CGI::Cookie->fetch;
if($cookies{'linenumber'} != $content{'linenumber'}){
	print "yay not null";
	print $cookies{'linenumber'};
	$content{'linenumber'} = $cookies{'linenumber'};
	$content{'file'} = $cookies{'file'};
	$content{'dir'} = $cookies{'dir'};
}



$cookie1 = CGI::Cookie->new(-name=>'status'
			-value=>{ line => $content{'linenumber'},
				file=>$content{'file'},
				dir=> $content{'dir'} });
print $cookie1;
#$cookie1 ->bake;
$linenum = $cookie1{'linenumber'};
print $linenum;
