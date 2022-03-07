#!/usr/bin/perl 
#
# Here's the perl routine to do the same thing 
# 
@monthname = ("Jan","Feb","Mar","Apr","May","Jun",
		"Jul","Aug","Sep","Oct","Nov","Dec");
$|=1;

$oval = $$ + time;  




# ****************************************
# $year is the number of years since 1900.
# ## http://perldoc.perl.org/functions/gmtime.html
# ****************************************

# more portable this way than to use an exec command.
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime(time); 
# ****************************************
$year="2020";
$expires = sprintf "%d-%s-%d %d:%d:%d", 
	$mday,$monthname[$mon],$year,$hour,$min+5,$sec;
$mytmp="newcookie=$oval";
print << "HTMLHEAD"; 
Content-type: text/html

<head><META HTTP-EQUIV="Set-Cookie" content="$mytmp; expires=$expires GMT">
<head><META HTTP-EQUIV="Set-Cookie" content="newcookie2=SCOTT; expires=$expires GMT">
<head><META HTTP-EQUIV="Set-Cookie" content="newcookie3; expires=$expires GMT">
<title>Cookie set</title></head><h1>Cookie Set</h1>
cookie set!
</head></html> 
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
