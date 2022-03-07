#!/usr/bin/perl -T

BEGIN {
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
   print "Content-type: text/html\n\n";
}
print "HELLO WORLD";
print "HELLO WORLD2";
