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

  print "Content-type: text/html\n\n";
   print "<br>NEW STUFF<br>";
        # create a CGI object (query) for use
    my $q = CGI->new;
    my $value   = $q->param('myfunc');
   print $value;
   print "<br>AFTER NEW STUFF<br>";
    my @values  = $q->multi_param('testcase');
   print @values;
   print "<br>AFTER NEW STUFF2<br>";

exit;

    # Process an HTTP request
    # my @values  = $q->multi_param('form_field');
    my $value   = $q->param('param_name');

    my $fh      = $q->upload('file_field');

    my $riddle  = $q->cookie('riddle_name');
    my %answers = $q->cookie('answers');

    # Prepare various HTTP responses
    print $q->header();
    print $q->header('application/json');

    my $cookie1 = $q->cookie(
        -name  => 'riddle_name',
        -value => "The Sphynx's Question"
    );

    my $cookie2 = $q->cookie(
        -name  => 'answers',
        -value => \%answers
    );

    print $q->header(
        -type    => 'image/gif',
        -expires => '+3d',
        -cookie  => [ $cookie1,$cookie2 ]
    );

    #print $q->redirect('http://somewhere.else/in/movie/land');

 # my %values;
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
  #my $q = new CGI;
  #my $q = CGI->new ;

   print "<br>NEW STUFF<br>";
  #print "Content-type: text/html\n\n";
   #print $myFunc;

   print "<br>AFTER MYFUNC<br>";
  #print $q->header('text/html'),
  print "hello\n\n";
  #my @values  = $q->multi_param('QUERY_STRING');
   #$q->CGI::ReadParse(*values);
   my $myFunc = $q->CGI::param('myfunc');
   #print $values{'myFunc'};
   print $myFunc;
    my $value   = $q->param('param_name');
   print "<br>AFTER MYFUNC<br>";
   print "<br>VALUES<br>";
   print $ENV{'QUERY_STRING'};
   print "<br>AFTER VALUES<br>";
   my @names = $q->CGI::param;
   print @names;
   print "<br>AFTER KEYWORDS<br>";
   my @keywords = $q->CGI::keywords;
   print @keywords;
   print "<br>AFTER KEYWORDS<br>";
   print $myFunc;
   print "<br>AFTER FUNC<br>";


