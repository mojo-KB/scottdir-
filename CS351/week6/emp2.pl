#!/usr/bin/perl
#
#use strict;
use warnings;

use lib '/home/f/csci/scott/www/cgi-bin/JSON-2.90';
use lib '/home/f/csci/scott/www/cgi-bin/JSON-2.90/lib';

 use lib::JSON; 
 use JSON::backportPP; 

 
binmode STDOUT, ":utf8";
#use utf8;
 
use JSON;
 
my $json;
{
  local $/; #Enable 'slurp' mode
  open my $fh, "<", "emp.json";
  $json = <$fh>;
  close $fh;
}

#print $json;

my $data = decode_json($json);
# Output to screen one of the values read
print "Boss' hobbies: " .
      $data->{'boss'}->{'Hobbies'}->[0] . "n";
# Modify the value, and write the output file as json
$data->{'boss'}->{'Hobbies'}->[0] = "Swimming";
open my $fh, ">", "emp_out.json";
print $fh encode_json($data);
close $fh;

print "\n########\n";
print $data->{'employees'}[0]{'Name'};

print "\n########\n";

for ( @{$data->{'employees'}} ) {
   print $_->{'Name'}."\n";
}
print "\n########\n";

#for ( %{$data->{}} ) {
   #print $_ "\n";
   #print $_->{'Name'}."\n";
#}

print "\n########\n";

use Data::Dumper;
print Dumper $data;


exit;

  open $fh, "<", "emp_out.json";
  $json = <$fh>;
  close $fh;

print "########\n";

$data = decode_json($json);
# Output to screen one of the values read
print "Boss' hobbies: " .
      $data->{'boss'}->{'Hobbies'}->[0] . "ses";
# Modify the value, and write the output file as json
$data->{'boss'}->{'Hobbies'}->[0] = "Swimming";

#my $i;
#foreach $i (sort keys %data) {
    #print "Key is: $i \n";
#}

