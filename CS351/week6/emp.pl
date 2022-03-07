#!/usr/bin/perl
#
#use strict;
use warnings;

 #use lib '/cygdrive/e/WEBGL/TEST/JSON-2.90';
 #use lib '/cygdrive/e/WEBGL/TEST/JSON-2.90/lib';
use lib '/home/f/csci/scott/www/cgi-bin/JSON-2.90';
use lib '/home/f/csci/scott/www/cgi-bin/JSON-2.90/lib';
 use lib::JSON; 
 #use JSON::backportPP; 

 
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

print $json;

my $data = decode_json($json);
# Output to screen one of the values read
print "Boss' hobbies: " .
      $data->{'boss'}->{'Hobbies'}->[0] . "n";
print "\n";
#print "This Boss: " .
      #$data->{'boss'} ;
print "This EMP1: " .  keys %$data;
print "This EMP2: " ;
      print keys %$data;
print "This EMP3: " ;
      #print keys %$data[0];
my $tmp;
foreach $tmp (keys %$data) {
      print $tmp . "\n";
      print keys $data->{'employees'} . "\n";
      #print keys $data->{$tmp} . "\n";
}
      #keys $data->{'employees'} ;
print "\n";
# Modify the value, and write the output file as json
$data->{'boss'}->{'Hobbies'}->[0] = "Swimming";
open my $fh, ">", "emp_out.json";
print $fh encode_json($data);
close $fh;

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

