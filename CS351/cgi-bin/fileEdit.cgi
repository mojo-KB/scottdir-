#!/usr/bin/perl

  use strict;
  use warnings;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS2/Class-Accessor-0.34/blib/lib';
  use base 'Class::Accessor::Fast';
  use Class::Accessor::Fast;
  use Class::Accessor;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-Ajax-0.697/blib/lib';
  use CGI::Ajax;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-4.35/lib';
  use CGI;

BEGIN{
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
}


   open (MYOUT, ">MYOUT");
   print MYOUT $ENV{'QUERY_STRING'};

  print "Content-type: text/html\n\n";
   #print "<br>NEW STUFF<br>";
        # create a CGI object (query) for use
    my $q = CGI->new;
    my $value   = $q->param('myfunc');
   #print $value;
   #print "<br>AFTER NEW STUFF<br>";
    #my @values  = $q->multi_param('testcase');
    #my @values  = $q->param('testcase');
   #print @values;
   #print "<br>AFTER NEW STUFF2<br>";

   my $somedir = "FNAMES";
   my $newline ="";
   if($value eq "getfilenames") {
	opendir(DIR, $somedir) || die "Can't open directory $somedir: $!";
	my @tmpdat2 = readdir(DIR);
 	my $line ="";
        foreach $line ( @tmpdat2 ) {
		if(( $line ne '.') && ($line ne '..')) {
		  $newline .= $line . ";";
		}
        }
	print $newline;
   }
   if($value eq "getContents") {
	my $filez;
	my $values  = $q->param('getTheList');
	my @fnames = split(/;/,$values);
	my $out="";
	my $myfile;
	foreach $myfile ( @fnames ) {
	  $filez= "FNAMES/" . $myfile; 
	  open (INFILE, "$filez") || die "Can't open file $filez: $!";;
	  my @filein = <INFILE>;
	  my $allstr = "";
	  my $inline;
	  foreach $inline ( @filein ) {
		$allstr .= $inline;
	  }
	  #my $allstr = @filein;
	  if ($out eq "") {
	  	$out = $myfile . "=" . $allstr;
	  } else {
	  	$out = $out . "&" . $myfile . "=" . $allstr;
	  }
	}
	print MYOUT $out;
	print $out;
   }
   if($value eq "saveContents") {
	my $filez;
	my $pair;
	my $contentz;
	my $values  = $q->param('getTheList');
	print MYOUT $values;

	my @pairs = split(/&/,$values);
	foreach $pair ( @pairs ) {
	    my ($filez,$contentz) = split(/=/,$pair);
	    # Transform ascii hex codes back to characters
    	    $contentz =~ tr/+/ /;
    	    $contentz =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	    # Disallow any non-alphanumeric file names
	    if ($filez =~ m/[^a-zA-Z0-9]/){
    		print "The string contains non-alphanumeric characters";
		die "Sorry about that!";
	    }	
	    # Remember to add the directory name
	    open (OUTFILE, ">FNAMES/$filez") || die "Can't open file $filez: $!";;
	    print OUTFILE $contentz;
	    close (OUTFILE);
        }
	print("SUCCESS");
   }
 

   
