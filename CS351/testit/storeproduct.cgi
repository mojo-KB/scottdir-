#!/usr/bin/env perl 

use strict;
use warnings;
use lib '/home/f/csci/scott/www/cgi-bin/PMS/Class-Accessor-0.34/blib/lib';
use base 'Class::Accessor::Fast';
use Class::Accessor;
use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-Ajax-0.697/blib/lib';
use CGI::Ajax;
use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-4.35/lib';
use CGI;

BEGIN {
    open (STDERR, ">%STDOUT");
    select(STDERR); $| = 1;
    select(STDOUT); $| = 1;
    print "Content:type: text/html; charset=UTF-8\n\n";
}

my @inventory;
my $data = '';
my (%food, %beverage, %clothing, %shoes);

my $num;
my $selection;
my @selection;
my $line;
my @array;
my $item;
my @productTypes;
my $type;
my %type;
my @productinfo;
my $orderstatus = "good";

# removes duplicate items from array -- http://blog.danmassey.net/?p=136
sub uniq{
    my %temp_hash = map { $_, 0 } @_;
    return keys %temp_hash;
}

$num = param('num') || 'Nothing.';

if($num eq "2") {
    $selection = param('selection') || 'Nothing.';
}
elsif($num eq "3") {
    $selection = param('selection') || 'Nothing.';
    @selection = split(',' , $selection);
}

print "Content-type: text/html\n\n";

# References product list file
open(my $userfile, '<', 'Homework5/store.txt')
    or die "Unable to open file, $!";

# References modified product list file
open(my $modifieduserfile, '>', 'Homework5/temp.txt')
    or die "Unable to open file, $!";

# Displays items of selected product type
if($num eq "2") {
    print "<h2>Select which item you would like:</h2>";
    print "<form id=\"checkbox_form\">";
    while (<$userfile>) {
	$line = "$_";
	@productinfo = split(',' , $line);
	chomp @productinfo;
	if($productinfo[0] eq "$selection") {
	    print "<input id=\"elementID\" type=\"checkbox\" name=\"$productinfo[0]\" value=\"$productinfo[1]\"> $productinfo[1] -- $productinfo[2] <br>";
	}
        
   }
   print "</form>";
   print "<input type=\"Button\" onclick=\"submit2()\" value=\"Submit\">";
   
}

# performed after user selects items
if($num eq "3") {
   print "<h2>Items you selected:</h2>";
   while(<$userfile>) {
	$line = "$_";
	@productinfo = split(',' , $line);
	foreach $item (@selection) {
	   chomp @productinfo;
           if("$productinfo[2]" eq "0" && "$productinfo[1]" eq "$item") {
               print "$productinfo[1] is out of stock<br>";
               $orderstatus = "bad";
           }
	   if("$productinfo[2]" ne "0" && "$productinfo[1]" eq "$item") {
		print "$productinfo[1]<br>";
                # decrements item inventory by 1
                $productinfo[2] = $productinfo[2] - 1;
	   }
	}
        # writes modified data to temp.txt
        print $modifieduserfile "$productinfo[0],$productinfo[1],$productinfo[2]\n";
   }
   # only thanks user if they did not select items out of stock
   if($orderstatus eq "good"){
        print "<br>Thank you for your order<br>";
   }
   $orderstatus = "good";
   # overwrites store.txt with the modifed data
   `cp Homework5/temp.txt Homework5/store.txt`;
   print "<input type=\"Button\" onclick=\"getProductType()\" value=\"Continue Shopping\">";
}


close($userfile)
   or warn "unable to close the file: $!";
close($modifieduserfile)
   or warn "unable to close the file: $!";
