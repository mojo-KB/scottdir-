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
    open (STDERR, ">&STDOUT");
    select(STDERR); $| = 1;
    select(STDOUT); $| = 1;
    print "Content-type: text/html; charset=UTF-8\n\n";
}

my @inventory;
my $data = '';
#my (%food, %beverage, %clothing, %shoes);

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

#$num = param('num') || 'Nothing.';

my $q = CGI->new;
my $value = $q->param('num');
my $r = CGI->new;
my $value2 = $r->param('selection');

print "ENV QSTRING= $ENV{'QUERY_STRING'}";

$num = $value;

if($num eq "2") {
    $selection = $value2;
}
elsif($num eq "3") {
    $selection = $value2;
    @selection = split(',' , $selection);
}


# References product list file
open(my $userfile, '<', 'week10/test/data.txt')
    or die "Unable to open file, $!";

my $modifieduserfile;

# References modified product list file
open($modifieduserfile, '>', 'week10/test/temp.txt')
    or die "Unable to open file, $!";

#my @tmpsss = <$userfile>;
#print @tmpsss;

#if($num eq "2") {
#print "NUM WAS 2";
#}

	#print "MYSELECTION: $selection";
# Displays items of selected product type
if($num eq "2") {
    print "<h2>Select which item you would like:</h2>";
    print "<form id=\"checkbox_form\">";
    while (<$userfile>) {
	$line = "$_";
	@productinfo = split(',' , $line);
	#print "VALUEIS: @productinfo";
	chomp @productinfo;
          #print "$productinfo[0] -- $selection -- $productinfo[1] -- $productinfo[2]\n";
	if((lc $productinfo[0]) eq (lc "$selection")) {
	#print "FOUNDIT: @productinfo";
	    print "<input id=elementID type=checkbox name=$productinfo[0] value=$productinfo[1]> $productinfo[1] -- $productinfo[2] <br>";
	    #print "<input id=\"elementID\" type=\"checkbox\" name=\"$productinfo[0]\" value=\"$productinfo[1]\"> $productinfo[1] -- $productinfo[2] <br>";
	}
        
   }

   print "</form>";
   print "<input type=\"Button\" onclick=\"submit_3()\" value=\"Submit\">";
   
}


# performed after user selects items
if($num eq "3") {
   print "<h2>Items you selected:</h2>";
   while(<$userfile>) {
	$line = "$_";
	@productinfo = split(',' , $line);
        foreach $item (@selection) {
           chomp @productinfo;
           print "Selection is $selection";
           if("$productinfo[2]" eq "0" && "$productinfo[1]" eq lc "$item") {
               print "$productinfo[1] is out of stock<br>";
               $orderstatus = "bad";
           }
	   if("$productinfo[2]" ne "0" && "$productinfo[1]" eq lc "$item") {
		print "$productinfo[1]<br>";
                # decrements item inventory by 1
                $productinfo[2] = $productinfo[2] - 1;
	   }
        }
        # writes modified data to temp.txt
        print $modifieduserfile "$productinfo[0],$productinfo[1],$productinfo[2]";
   }
   print "Orderstatus is $orderstatus";
   # only thanks user if they did not select items out of stock
   if($orderstatus eq "good"){
        print "<br>Thank you for your order<br>";
   }
   $orderstatus = "good";
   # overwrites data.txt with the modifed data
   `cp temp.txt data.txt`;
   print "<input type=\"Button\" onclick=\"submit_2()\" value=\"Continue Shopping\">";
}


close($userfile)
   or warn "unable to close the file: $!";
close($modifieduserfile)
   or warn "unable to close the file: $!";
