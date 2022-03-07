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

if($num eq "1" || $num eq "2") {
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

# Displays product types in a form that contains radio buttons
if($selection eq "all" && $num eq "1") {
    print "<h2>Select a category:</h2>";
    while (<$userfile>) {
    	$line = "$_";
	@array = split(',' , $line);
	push @productTypes, $array[0];
    }

    # array uniq_list is assigned productTypes with no duplicates
    my @uniq_list = uniq(@productTypes);

    print "<form id=\"getSelected\">";
    # loops through array of products and assigns them to radio buttons
    foreach $type (@uniq_list) {
	chomp $type;
	print "<input type=\"radio\" name=\"itemType\" value=\"$type\">\u$type<br>";
    }
    print "</form>";
    # creates submit button that performs function submit_2 when it is clicked
    print "<input type=\"Button\" onclick=\"submit_2()\" value=\"Submit\">";
}

# Displays items of selected product type
if($num eq "2") {
    print "<h2>Select which item you would like:</h2>";
    print "<form id=\"checkbox_form\">";
    while (<$userfile>) {
	$line = "$_";
        # splits line and assigns product type, item name, and item quantity to productinfo array
	@productinfo = split(',' , $line);
	chomp @productinfo;
        # displays items of particular product type in a form that contains check boxes
        # productinfo[0] is the product type (example: food)
        # productinfo[1] is the item name (example: tofu)
        # productinfo[2] is the quantity of that particular item
	if($productinfo[0] eq "$selection") {
	    print "<input id=\"elementID\" type=\"checkbox\" name=\"$productinfo[0]\" value=\"$productinfo[1]\"> $productinfo[1] -- $productinfo[2] <br>";
	}
        
   }
   print "</form>";
   # creates submit button that performs function submit_3 when it is clicked
   print "<input type=\"Button\" onclick=\"submit_3()\" value=\"Submit\">";
   
}

# performed after user selects items
if($num eq "3") {
   print "<h2>Items you selected:</h2>";
   while(<$userfile>) {
	$line = "$_";
        # splits line and assigns product type, item name, and item quantity to productinfo array
	@productinfo = split(',' , $line);
        # loops through each item selected and adjusts inventory
	foreach $item (@selection) {
	   chomp @productinfo;
           # performed if item quantity is zero
           if("$productinfo[2]" eq "0" && "$productinfo[1]" eq "$item") {
               print "$productinfo[1] is out of stock<br>";
               $orderstatus = "bad";
           }
           # performed if there are still items of selection in inventory
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
   # resets orderstatus back to good for the next order
   $orderstatus = "good";
   # overwrites data.txt with the modifed data
   `cp temp.txt data.txt`;
   # creates submit button that performs function submit_1 when it is clicked
   print "<input type=\"Button\" onclick=\"submit_1()\" value=\"Continue Shopping\">";
}


close($userfile)
   or warn "unable to close the file: $!";
close($modifieduserfile)
   or warn "unable to close the file: $!";
