#!/usr/bin/perl

use DBI;

# Report on the tables about persons and operations
print "content-type: text/html\n\n";
print <<"HEADER";
<html>
<head><title>Patient Record Demonstration</title></head>
<body bgcolor=#FFFFDD text=#228822>
<h1>Patient Report from joined tables</h1>
All about this stuff ...<br>
<pre>
HEADER

# Run the database query
#$db_handle = DBI -> connect("DBI:mysql:test","scott","coco");
print "PATH IS:  $ENV{'PATH'}";
$ENV{'PATH'} = "/home/faculty/scott/bin/MySQL/bin:$ENV{'PATH'}";
print "\nbefore Which\n";
print `which mysql`;
print "\nafter Which\n";
#/home/faculty/scott/bin/MySQL/bin
my $db_handle = DBI->connect("DBI:mysql:database=test;host=localhost", "scott", "coco", {'RaiseError' => 1});
$db_handle = DBI->connect("DBI:/home/faculty/scott/bin/mysql:test:localhost", "scott", "coco");
#$getkey = $db_handle -> prepare("use test");
$getkey -> execute;
$getkey = $db_handle -> prepare("select employee.fname
        from employee");
$getkey -> execute;

# Get back and output the results
while (@row = $getkey->fetchrow)  {
        printf ("%-25s %3s %4d %-20s %4d %4d\n",@row);
        }

# Links to other parts of the application
print <<"FOOTER";
</pre>
<hr>
Copyright, contacts details, etc
</body></html>
FOOTER
