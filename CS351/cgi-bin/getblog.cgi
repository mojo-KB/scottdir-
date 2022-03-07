#!/usr/bin/perl

  use strict;
  use warnings;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS/Class-Accessor-0.34/blib/lib';
  use base 'Class::Accessor::Fast';
  use Class::Accessor::Fast;
  use Class::Accessor;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-Ajax-0.697/blib/lib';
  use CGI::Ajax;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-4.35/lib';
  use CGI;

open (DEBUGOUT, ">>DEBUG");
print DEBUGOUT "START doMyParse vertices";
print DEBUGOUT "START QUERY_STRING=$ENV{'QUERY_STRING'}";

  my %values;
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
  #my $q = new CGI;
  #my $q = CGI->new ;

  print "Content-type: text/html\n\n";
  #print $q->header('text/html'),
  #print "hello\n\n";
  #my @values  = $q->multi_param('QUERY_STRING');
   #$q->CGI::ReadParse(*values);

   #my $q = CGI->new;
   #my $myNum = $q->param('num');
   my $myNum = 1;

   #print $values{'myFunc'};
   #print "<B>FUNC:<\B><br>";
   #print $myFunc;
   #print "<br><B>after FUNC:<\B><br>";
   my $line;
   open(myblogs, "<cgi-bin/blogs") || die "Can't open products: $!\n";
   my @bloglines=<myblogs>;
   print DEBUGOUT "BLOG " . $bloglines[$myNum];
   print $bloglines[$myNum];
   exit;

        open(myblogs, "<cgi-bin/blogs") || die "Can't open products: $!\n";
        #@newarray = <myprods>;
        #print "NEWARRAY @newarray";
        foreach $line (<myblogs>) {
                chomp $line;
                #($cat, $thelist) = split(/:/,$line);
                #if($cat eq $category){}
                print "$line";
                close (myprods);
                #exit;
        }


   #print "<br>AFTER MYFUNC<br>";
   #print $ENV{'QUERY_STRING'};
   #print "<br>AFTER VALUES<br>";
   #my @names = $q->CGI::param;
   #print @names;
   #print "<br>AFTER KEYWORDS<br>";
   #my @keywords = $q->CGI::keywords;
   #print @keywords;
   #print "<br>AFTER KEYWORDS<br>";
   #print $myFunc;
   #print "<br>AFTER FUNC<br>";
   # &CGI::ReadParse(*values);
   exit;


