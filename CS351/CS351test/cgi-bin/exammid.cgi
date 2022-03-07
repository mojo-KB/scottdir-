#!/usr/bin/perl

# input files for WebGL
# https://people.sc.fsu.edu/~jburkardt/data/tec/tec.html

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

  my %values;
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
  #my $q = new CGI;
  my $q = CGI->new ;
  my $myUser;

  print "Content-type: text/html\n\n";

  my $myFunc = $q->CGI::param('myfunc');
  
  if ($myFunc eq "getfriendmsgs") {
  	my $myFriends = $q->CGI::param('friends');
	my @friends = split(/:/,$myFriends);
print "FRIENDS = $myFriends  ";
	my $friend;
	foreach $friend (@friends) {
	   open FRIENDS, "<", "$friend" || die "bad friend" ;
	   my @msgs = <FRIENDS>;
	   print $msgs[$#msgs], "<br>\n";
	   close FRIENDS;
	}
  }
  if ($myFunc eq "post") {
  	$myUser = $q->CGI::param('user');
  	my $myPost = $q->CGI::param('mypost');
  	open MYFILE, ">>", "$myUser" || die "bad file" ;
  	my @tmpdat2 = <MYFILE>;
	print MYFILE $myPost, "\n";
	close MYFILE;
  }

  if ($myFunc eq "login") {
  $myUser = $q->CGI::param('user');

  open MYFILE, "<users.txt" || die "bad file" ;
  
  #my @tmpdat2 = readdir(DIR);
  my @tmpdat2 = <MYFILE>;

  my $inputName2;
  my @picknames3;
  my $mycnt4;
  foreach $inputName2 (@tmpdat2) {
        $picknames3[$mycnt4++] = $inputName2;
  }
  my $utf8_encoded_json_picknames = JSON::encode_json (\@picknames3);
  print $utf8_encoded_json_picknames;

  exit;
  }

  exit;
  my @tmpdat2;
  my $mycnt2;

  my $inputName2;

  #print $q->header('text/html'),
  #print "hello\n\n";
  #my @values  = $q->multi_param('QUERY_STRING');
   #$q->CGI::ReadParse(*values);

   my $myPickType = $q->CGI::param('mypicktype');

   $myFunc = $q->CGI::param('myfunc');
   $myUser = $q->CGI::param('myrunid');
   #print $values{'myFunc'};
   #print "<B>FUNC:<\B><br>";
   #print $myFunc;
   #print "<br><B>after FUNC:<\B><br>";

   #print "<br>AFTER MYFUNC<br>";
   #print "<br>VALUES<br>";
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

  BEGIN {
  #my $q = CGI::new() ;
  #my @values  = $q->multi_param('form_field');
  #print "Content-type: text/html\n\n";
   #open (STDERR, ">&STDOUT");
   #select(STDERR); $| = 1;
   #select(STDOUT); $| = 1;
   #my $buffer = $ENV{'QUERY_STRING'};
   #print "QS $buffer \n";
   #$q->CGI::ReadParse(*values);
   #my @values  = $q->multi_param('form_field');
   #print $q->header('text/html'),
   #print $CGI::q->header('application/json'),
   #$q->CGI::start_html(-title=>'CS351');
   #&CGI::ReadParse(*values);
   #print &PrintHeader, &PrintVariables(%values);
  #exit;
  }

#print <<ENDHEAD;
#ENDHEAD

if ($myFunc eq "getpicks") {
if ( ( $myPickType eq "run" ) || ( $myPickType eq "display" )) {
  chdir("RUN351");
  my @picknames;
  $picknames[0] = $myPickType; # handler will use first name in the array as type for Picker List
  $mycnt2 = 1;
  $inputName2 = "";
  my $somedir2 = ".";
  opendir(DIR, $somedir2) || die "Can't open directory $somedir2: $!";
  @tmpdat2 = readdir(DIR);

  foreach $inputName2 (@tmpdat2) {
#print "match $mycnt2 $inputName\n";
  #if ($inputName2 =~ m/\./ ) {
  if (!($inputName2 eq ".") && !($inputName2 eq "..") && !($inputName2 eq "files")){
        $picknames[$mycnt2++] = $inputName2;
  }
#print "found $inputName\n";
#print "\n";
  #
  }
  my $utf8_encoded_json_picknames = JSON::encode_json (\@picknames);
  print $utf8_encoded_json_picknames;
  exit;
}
}


if ( $myFunc eq "pickResults") {
}
if ( $myFunc eq "execexample") {

  #require File::Temp;
  #use File::Temp ();
  #$dir = File::Temp->newdir('tempXXXXX');

  # Make a temporary directory for this run
  my $myTestCase = $q->CGI::param('exampleTestCase');
  chomp $myTestCase;

  my $range = 100000;
  my $dirname = int(rand($range));
  #$dirname =  "CS351_tmp" . $dirname . int(rand($range));
  $dirname =  $myTestCase . "/CS351_tmp" . $dirname ;
  mkdir $dirname, 0755;
  #print $dirname . "\n";

  chdir $dirname;

  # Link the data files to this directory
  `ln -s /home/f/csci/scott/www/cgi-bin/DATA/mydata.dat .`;
  `ln -s /home/f/csci/scott/www/cgi-bin/DATA/mydata.dat mydata2.dat`;
  `ln -s /home/f/csci/scott/www/cgi-bin/DATA/mydata.dat mydata3.dat`;

   #`/home/f/csci/scott/www/cgi-bin/TEC360/prog TEC360_inputs.inp >& myOutput`;

  my @dirnames;
  $dirnames[0] = $dirname;
  #$dirnames[1] = "SCOTT";
  my $mycnt1 = 1;
  my $inputName = "";
my $somedir = ".";
opendir(DIR, $somedir) || die "Can't open directory $somedir: $!";
my @tmpdats = readdir(DIR);

foreach $inputName (@tmpdats) {
#print "match $mycnt1 $inputName\n";
if ($inputName =~ m/.*dat$/ ) {
	$dirnames[$mycnt1++] = $inputName;
#print "found $inputName\n";
#print "\n";
}
}


  #my @myNames = exec("ls *.dat");
  #foreach $inputName (@myNames) {
  #foreach $inputName (`ls *.dat`) {
	#chomp $inputName;
 	#$dirnames[0] += "++" + $inputName;
	#$dirnames[$mycnt1++] = $inputName;
  #}
  #print @dirnames;
  #exit;

  my $utf8_encoded_json_dirname = JSON::encode_json (\@dirnames);
  #my $utf8_encoded_json_dirname = JSON::encode_json (\@myNames);
  print $utf8_encoded_json_dirname;
  #my $json_text   = $JSON::json->encode( $dirname );
  #print $json_text ;
  exit;
}


# Encode Vertices and Faces to JSON
# imports encode_json, decode_json, to_json and from_json.
# imports encode_json, decode_json, to_json and from_json.
# simple and fast interfaces (expect/generate UTF-8)


 use constant { true => 1, false => 0 };

 use lib '/home/f/csci/scott/www/cgi-bin/JSON-2.90';
 use lib '/home/f/csci/scott/www/cgi-bin/JSON-2.90/lib';
 use lib::JSON; 
 use JSON::backportPP; 

my @jsonFaces;
my @jsonVertices;

sub doMyParse {

 
#print "HELLO1 \n";

open(tec360, "<mydata.dat") || die "Can't open tec360 dat: $!\n";

#print "HELLO2 \n";

my @newarray = <tec360>;
##print "NEWARRAY $newarray[0] \n";
##print "NEWARRAY $newarray[1] \n";
##print "NEWARRAY $newarray[2] \n";
##print "NEWARRAY $newarray[3] \n";
close (tec360);

my $foundtriangle = false;
my $foundvertex = false;

my $filename="myData";
my $fcnt = 0;
#foreach $line (@newarray) {
#
my $faceCnt = 0;
my $vertexCnt = 0;
my $line = 0;
my $filename2 = 0;
my @vals;

my $cnt = 0;
while ($cnt < $#newarray) {

        $line = $newarray[$cnt];
        if ( $line =~ /TITLE/ ) {
                $foundtriangle = false;
                #$line = <tec360>;
                #print "c360_surf $cnt  $newarray[$cnt++]; \n";
                $cnt++;
                #print "c360_surf $cnt  $newarray[$cnt++]; \n";
                $cnt++;
                #print "c360_surf $cnt  $newarray[$cnt++]; \n";
                $cnt++;
                $line = $newarray[$cnt++];
                #$line = <tec360>;
                #print "c360_surf $cnt  $line \n";
                #$line = <tec360>;
                #print "c360_surf $cnt  $line \n";
                if ($fcnt > 0) {
                        close($filename2);
                }
                $fcnt++;
                $filename2 = "$filename" . "$fcnt";

                open(myOutfile, ">$filename2") || die "Can't open $filename2 : $!\n";
        }
        else {
                $cnt++;
        }

        chomp $line;
        #@vals = split(/ .+/, $line);
        $vals[4] = "ScottSpetka";
        @vals = split(/ {1,}/, $line);
        #if ($vals[4] == "") {}
        #if ($vals[4] eq "") {}
        if ( defined $vals[5] ) {
                if ($foundtriangle eq false) {
                        $foundtriangle = true;
                        print myOutfile "TRIANGLES\n";
                }
#geom.vertices.push( new THREE.Vector3( 10, -10, 0 ) );
#geom.faces.push( new THREE.Face3( 0, 1, 2 ) );

                print myOutfile " geom.vertices.push( new THREE.Vector3( $vals[1], $vals[2], $vals[3] ));\n";
		$jsonVertices[$vertexCnt++] = $vals[1] . ";" . $vals[2] . ";" . $vals[3];
        }
        else {
                print myOutfile " geom.faces.push( new THREE.Face3( $vals[1], $vals[2], $vals[3] ));\n";
		$jsonFaces[$faceCnt++] = $vals[1] . ";" . $vals[2] . ";" . $vals[3];
		if (defined $vals[4] ) {
                print myOutfile " geom.faces.push( new THREE.Face3( $vals[2], $vals[3], $vals[4] ));\n";
		$jsonFaces[$faceCnt++] = $vals[2] . ";" . $vals[3] . ";" . $vals[4];
		}
        }
}

}  # end of sub doMyParse

if ( $myFunc eq "faces") {
 #chdir $myRunid;
 chdir "/home/f/csci/scott/www/cgi-bin/DATA";
 doMyParse();
 #print "FACES: ";
 #print @jsonFaces;
 #exit;
 my $utf8_encoded_json_faces = JSON::encode_json (\@jsonFaces);
 print $utf8_encoded_json_faces;
}

if ( $myFunc eq "vertices") {
 #chdir $myRunid;
 chdir "/home/f/csci/scott/www/cgi-bin/DATA";
 doMyParse();
 my $utf8_encoded_json_vertices = JSON::encode_json (\@jsonVertices);
 #$perl_hash_or_arrayref  = decode_json $utf8_encoded_json_text;
 #print "FACES: ", $utf8_encoded_json_faces;
 #print "<br>\n";
 #print "VERTICES ", $utf8_encoded_json_vertices;
 #print "<br>\n";
 print $utf8_encoded_json_vertices;
}