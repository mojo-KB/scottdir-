#!/usr/bin/perl 
#
# Here's the perl routine to do the same thing 
# 
@monthname = ("Jan","Feb","Mar","Apr","May","Jun",
		"Jul","Aug","Sep","Oct","Nov","Dec");
$|=1;

$oval = $$ + time;  
# more portable this way than to use an exec command.
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = 		gmtime(time); 
$year="2005";
$expires = sprintf "%d-%s-%d %d:%d:%d", 
	$mday,$monthname[$mon],$year,$hour,$min+5,$sec;
print << "HTMLHEAD"; 
Content-type: text/html

<head><META HTTP-EQUIV="Set-Cookie" content="newcookie=$oval; expires=$expires GMT">
<META HTTP-EQUIV="Set-Cookie" content="newcookie2=TST/SCOTT/TEST; expires=$expires GMT">
<META HTTP-EQUIV="Set-Cookie" content="newcookieTST; expires=$expires GMT">
<title>Cookie set</title></head><h1>Cookie Set</h1>
cookie set!
HTMLHEAD

print "<BR>EXPIRES:$expires";
print "<BR>SEC: $sec";
print "<BR>MIN: $min";
print "<BR>HOUR: $hour";
print "<BR>MDAY: $mday";
print "<BR>MON: $mon";
print "<BR>YEAR: $year";
print "<BR>WDAY: $wday";
print "<BR>YDAY $yday";
print "<BR>OVAL $oval";

print " \$\$ = $$";
print "</html>";
