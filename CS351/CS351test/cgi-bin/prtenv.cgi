#!/usr/bin/perl 
print "Content-type: text/html\n\n ENV IS:\n<p>ENV";

print " CONTENT_LENGTH ### $ENV{'CONTENT_LENGTH'} XXX\n<p>";

print "Machine OS is" . `uname` . "<p>";

foreach $x (keys %ENV){
 $_ = $x;
 if ( /.*REMOTE*/ ) {
 print "\n<BR>FIRST $x $ENV{$x}<BR>";
 }
}

foreach $x (keys %ENV){
 if ( $x =~ ".*REMOTE*" ) {
 print "\n<BR>SECOND $x $ENV{$x}<BR>";
 }
}

foreach $x (keys %ENV){
 print "\n<BR>THIRD $x $ENV{$x}<BR>";
}

#print "----------------------------------------------\n<BR>";
#print "----------------------------------------------\n<BR>";
#print "----------------------------------------------\n<BR>";
#print "----------------------------------------------\n<BR>";
#
print `/usr/bin/printenv`;
print "----------------------------------------------\n<BR>";
print "----------------------------------------------\n<BR>";
print "----------------------------------------------\n<BR>";
print "----------------------------------------------\n<BR>";
#
@prt = `/usr/bin/printenv`;
foreach $x (@prt){
	print "$x <br>";
}

