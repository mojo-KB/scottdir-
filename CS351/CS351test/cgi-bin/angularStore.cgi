#!/usr/bin/env perl 

use strict;
use warnings;
use lib '/home/f/csci/scott/www/cgi-bin/PMS/Class-Accessor-0.34/blib/lib';
use base 'Class::Accessor::Fast';
use Class::Accessor;
use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-Ajax-0.697/blib/lib';
use CGI::Ajax;
use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-4.35/lib';
use CGI qw(:standard);


my $num;
my $selection;
my @selection;
my $line;
my $item;
my $type;
my %type;
my @productinfo;
my $orderstatus = "good";

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
open(my $userfile, '<', 'data.txt')
    or die "Unable to open file, $!";

# References modified product list file
open(my $modifieduserfile, '>', 'temp.txt')
    or die "Unable to open file, $!";

# Displays items of selected product type
if($num eq "2") {
    print "<h2>Select which item you would like:</h2>";
    print "<form id=\"checkbox_form\">";
    while (<$userfile>) {
	$line = "$_";
	@productinfo = split(',' , $line);
	chomp @productinfo;
	if(lc $productinfo[0] eq lc "$selection") {
	    print '<input id="elementID" type="checkbox" name="$productinfo[0]" value="$productinfo[1]" ng-model="mySwitch"> $productinfo[1] -- $productinfo[2] <br>';
	}
        
   }

   print "</form>";
   print '<button onclick="submit_3()" ng-disabled="mySwitch">Submit</button>';
   
}

# performed after user selects items
if($num eq "3") {
   print "<h2>Items you selected:</h2>";
   while(<$userfile>) {
	$line = "$_";
	@productinfo = split(',' , $line);
        foreach $item (@selection) {
           chomp @productinfo;
           #print "Item is " + $item + "<br>";
           if(($productinfo[1] eq $item) && ($productinfo[2] == 0)){
                print "$productinfo[1] is out of stock.<br>";
                $orderstatus = "bad";
            }
           elsif($productinfo[1] eq $item) {
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
        print "<br>Thank you for your order!<br>";
   }
   # reset orderstatus
   $orderstatus = "good";
   # overwrites data.txt with the modifed data
   `cp temp.txt data.txt`;
   print "<input type=\"Button\" onclick=\"submit_1()\" value=\"Submit\">";
}


close($userfile)
   or warn "unable to close the file: $!";
close($modifieduserfile)
   or warn "unable to close the file: $!";
