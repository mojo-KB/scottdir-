#!/usr/bin/perl 
#
# Here's the perl routine to do the same thing 
# 
@monthname = ("Jan","Feb","Mar","Apr","May","Jun",
		"Jul","Aug","Sep","Oct","Nov","Dec");
$|=1; 
$oval = $$ + time;  
# more portable this way than to use an exec command.
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime(time); 
$expires = sprintf "%d-%s-%d %d:%d:%d", 
	$mday,$monthname[$mon], $year + 1901 ,$hour,$min,$sec;
	#$mday,$monthname[$mon], "2005"+1,$hour,$min,$sec;
print << "HTMLHEAD"; 
Content-type: text/html
Set-Cookie: newcookie6=SCOTT6; expires=$expires GMT; path=/~scott/cgi-bin/test; domain=.cs.sunyit.edu

print "YEAR IS: $year";
print "<br>Expires IS: $expires";

HTMLHEAD
#<head>
#<META HTTP-EQUIV="Set-Cookie" content="newcookie=$oval; expires=$expires GMT">
#<META HTTP-EQUIV="Set-Cookie" content="newcookie2=SCOTT; expires=$expires GMT">
#<title>Cookie set</title></head><h1>Cookie Set</h1>
#cookie set!
#</head></html> 
#print " \$\$ = $$";
