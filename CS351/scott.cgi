#!/usr/bin/perl -T
##
## Turns off buffering
$| = 1;

print "Content-type: text/html\n\n";

{
my @A;
$A[1][1] = 3;
$A[1][2] = 4;
$A[2][3] = 5;
print "@A \n";
print "$A[2][3]  \n";
}


$X="hello";
print "YYY${X}world <br>\n";
print "now print it again $Xworld <br>\n";

#print<<END;
#    <HEAD>


#<META HTTP-EQUIV="Refresh" CONTENT="5;URL=http://www.cs.sunyit.edu/~scott/cgi-bin/scott.cgi">
#       <TITLE> Pragma No-cache </TITLE>

#    </HEAD>
#    <HEAD>
#
#       <META HTTP-EQUIV="PRAGMA" CONTENT="NO-CACHE">

#    </HEAD>
#END
#
if (defined($ENV{'CONTENT_LENGTH'})) {
	print " CONTENT_LENGTH WAS DEFINED -> METHOD POST\n\n<BR>";
}

print " CONTENT_LENGTH ### $ENV{'CONTENT_LENGTH'} XXX\n";

if (( $ENV{'CONTENT_LENGTH'}==0)&&($ENV{'QUERY_STRING'}eq""))
{
	&sendform;
	exit;
}




print "<H1>351test</H1>";
print<<EOF;
        <a href=\"imagemap.cgi/351test\">
        <img src=\"ch12/scott.gif\" ISMAP>
        </a>
EOF

print "<BR>";
print " STARTED IN SCOTT.cgi <br>";
print " STARTED \"IN\" SCOTT.cgi <br>";

## Get the input and put it into the $contents array
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
print " BUFFER (QS)  $ENV{'QUERY_STRING'}\n";

print "<BR>";
print "<BR>";

#$ENV{'CONTENT_LENGTH'} = "00";
# setenv QUERY_STRING "hello" - done in shell to run this at command line

print " CONTENT_LENGTH $ENV{'CONTENT_LENGTH'}\n<br>";
if ( $ENV{'CONTENT_LENGTH'} eq "") {
print " CONTENT_LENGTH (string compare) was NULL<BR>\n";
}
if ( $ENV{'CONTENT_LENGTH'} == 0) {
print " CONTENT_LENGTH (arithmetic compare) was NULL<BR>\n";
}
if ( $ENV{'CONTENT_LENGTH'} eq 0) {
print " CONTENT_LENGTH (string eq compare) was equal<BR>\n";
}
if ( "0" eq 0) {
print " CONTENT_LENGTH (\"0\" eq 0) was equal<BR>\n";
}
print "<BR>";
print " QUERY_STRING $ENV{'QUERY_STRING'}";
print "<BR>";
print "PATH_INFO is $ENV{'PATH_INFO'}\n";
($tmp,$init,$incr,$num) = split(/\//, $ENV{'PATH_INFO'});
print "tmp=$tmp, init=$init, incr=$incr, num=$num<br>";

print "<BR>";
print "<BR>";
if ($buffer eq ""){
	$buffer = $ENV{'QUERY_STRING'};
}

print "BUFFER=$buffer";




@pairs = split(/&/, $buffer);
print "<BR>";
print "<BR>";
 print "PAIRS: @pairs";
 print "END OF PAIRS";
print "<BR>";
print "<BR>";

#################
# infinite loop #
#################
#for($i=0;;$1 <10) {
#	$j++;
#}

$i=0;
foreach $pair (@pairs)
{
    ($name, $value) = split(/=/, $pair);
    $value =~ tr/+/ /;
    #$value =~ s/\+/&nbsp;/g;
    #$value =~ s/%([a-fA-F0-9])([a-fA-F0-9])/pack("C", hex($1.$2))/eg;
    #$value =~ s/%([a-fA-F0-9])([a-fA-F0-9])/pack("C", hex($1.$2))/eg;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    # $value =~ s/~!/ ~!/g;  # Security fix for mailx
    if ( $contents{$name} eq "" ) {
    $contents{$name} = $value;
    }
    else {
    $contents{$name} .= ";$value";
    }
    $i=$i+$value;

#if ($value =~ /</ || $name =~ /</) {
#  printf("Nice Try!<br>\n");
#  exit;
#}

# if ($value =~ /^[\w]+$/) {
  # printf("OK OK OK<br>\n");
# }
# else {
#}

#if (!($value =~ /\w/) || !($value =~ /[0-9]/)) 
#if (!($value =~ /\w/) || !($value =~ /[0-9]/)) {
  # printf("Nice found non-w Try!<br>\n");
  # exit;
# }

if ($buffer =~ /realname=/) {
	print "<br>REALNAME1 is $contents{'realname'} "; 
}

$_ = $buffer;
if (/realname=/) {
	print "<br>REALNAME2 is $contents{'realname'} "; 
}
print "<BR>\n";

if (defined($contents{'Iclickedsubmit2'})) {
print "<br>NEW Iclickedsubmit2 was $contents{'Iclickedsubmit2'}<br>";
}


print "Input Values Sum =: $i";
print "<BR>";
print "CONTENTS for $name =: $contents{$name}";
print "<BR>";
print "Input Values: $name $value";
print "<BR>";
}


## Loop to print contents
foreach $student (sort keys %contents) {
	print "<br>$student ::::  $contents{$student}";
}
print "<BR>";

print "Input Values FINAL Sum =: $i";
print "<BR>";
  print "Input Values2: username = $contents{'username'} ";
print "<BR>";
 print "Input Values2: realname = $contents{'realname'} ";
print "<BR>";
 print "Input Values2: flavor = $contents{'flavor'} ";
print "<BR>";
 print "Input Values2: flavor = $contents{'formnum'} ";


print "<form>";
	$ss = 0;
	while ( $ss < $contents{'realname'} ) {
		$ss++;
		$tmpx= "INVAL".$ss;
print "HELLO WORLD&nbsp;<input name=\"INVAL\"><BR>";
		#print "HELLO WORLD&nbsp;<input name=$tmpx><BR>";
print "<input type=submit value=\"INVAL\"><BR>";
	}
print "</form>";

	$form7 = FALSE;

if ( $contents{'formnum'} == 7  ) {
	print "IT IS LUCKY 7!!!";
	$form7 = TRUE;
	
}

# COMPARE IN LEXICOGRAPHIC ORDER

$testval = 4;
print "TESTVAL is $testval\n<BR>";
if ($testval eq "4") {
print "TESTVAL is (eg) $testval\n<BR>";
}
if ($testval > "100") {
print "TESTVAL is (>) $testval\n<BR>";
}
if ($testval gt "100") {
print "TESTVAL is (gt) $testval\n<BR>";
}
if (4 gt "100") {
print "TESTVAL 4 is (gt) $testval\n<BR>";
}

print "PATH_INFO is $ENV{'PATH_INFO'}";

if ( $ENV{'PATH_INFO'} eq "/form11" ) {
	print "IT IS LUCKY FORM 11!!!";
}

if (!$contents{'username'} && !$contents{'realname'}) {
        ## If all the fields are blank then send the comment form
	$Mydate = `date`;
        &sendform;
} elsif (($contents{'username'} eq "") || ($contents{'realname'} eq "")) {
        ## If any of the fields are blank then ask to them to retry 
        &needmore;
} else {
open(GRADES, ">>/tmp/CSC351") || die "Can't open grades: $!\n";
print GRADES "$buffer\n" ;
	print "<BR><BR>";
        print "<B>OUTPUT PROCESSED</B><BR>";
        if ( $contents{'flavor'} eq "b" ) {
	print "$contents{'username'} $contents{'realname'} Strawberries <BR><BR>";
}

if ($form7)  {
	print "HURRAY 77777777777";
}

        print "<I>$contents{'username'} ($contents{'realname'})</I><BR>";
        print "<B>", scalar localtime, "</B><BR><BR>";
        print "Remote host: $ENV{'REMOTE_HOST'}  IP: $ENV{'REMOTE_ADDR'}<BR>";
        print "SERVER is: ",  `hostname` , "<BR>";
        print "-" x 60, "\n";   # Print 60 dashes and a newline

        &thanks;
}

## Thank them for sending a comment
sub thanks
{
print <<"EOF";
<HTML><HEAD>
<TITLE>Thank you for running this program!</TITLE></HEAD>
<BODY><H1>Thank you for running this program!</H1><P>
Return to the <A HREF="/">Home Page</A><P>
</BODY></HTML>
EOF
}

## Not all blanks were filled when the user sent the form
sub needmore
{
print <<EOF;
<HTML><HEAD><TITLE>Need more info</TITLE></HEAD>
<BODY><H1>Please enter your email address and full name.</H1><P>
<i>Please click the Back button on your browser and fill in the missing
fields</i></BODY>
</HTML>
EOF
}    

#<FORM METHOD=POST ACTION="scott.cgi/form11">
## Send the HTML form (no fields filled in)
sub sendform
{
#<FORM METHOD=POST ACTION="http://arf.cs.sunyit.edu/surprise/surprise">
#Please enter your e-mail address: <INPUT ID="username"><P>
print <<EOF;
<HTML><HEAD><TITLE>TEST STUFF</TITLE></HEAD>
<BODY><H1>Please enter your name and email address below</H1>
EOF
print " <BR><font color=\"#CC33CC\"> DATE IS: $Mydate <BR>";
#@LS=`ls -l`;
#foreach $ls (@LS) {
#print " <BR>LS IS: $ls<BR>";
#}
#print " <BR></font>";
#print " <BR>LS IS: @LS<BR>";
#$HOST=`hostname`;

# $HOST =~ '^([\w]+\.+)$';
# $HOST =~ '^([\w]+\.+)';
# The \w is shorthand for [A-Za-z0-9_]
$HOST =~ '^([\w]+)(\.+)';
print " <BR>HOSTNAME2 IS: X $1 Y $2<BR>";
print " <BR>HOSTNAME IS: $HOST<BR>";


%flavorlist = ( 'a' => 'vanilla',
		'b' => 'Strawberry',
		'c' => 'Rum and Rasin',
		'd' => 'Peach and Orange',
		'e' => 'Chocolate',
		'f' => 'Raspberry',
		'h' => '----------------------------------------------------------',
		'g' => '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;');

print "Flavors: $contents{'flavor'} <BR><BR><BR>";

@flavors = split(/;/,$contents{'flavor'});

$j=0;
foreach $flav (@flavors) {
	print "Flavor $j: $flav: $flavorlist{$flav} <BR>";
	$j++;
}

print "<BR><BR>";

print <<EOF;
$Mydate

<!-- 
<FORM METHOD=get ACTION="http://www.cs.sunyit.edu/~scott/cgi-bin/scott.cgi?scotttest">
<FORM METHOD=get ACTION="http://www.cs.sunyit.edu/~scott/cgi-bin/scott.cgi">
<FORM METHOD=get ACTION="http://www.cs.sunyit.edu/~scott/cgi-bin/scott.cgi?JUNK/somepathinfo">
<FORM METHOD=post ACTION="http://web.cs.sunyit.edu/~scott/cgi-bin/prtenv.cgi">
<FORM METHOD=post ACTION="http://web.cs.sunyit.edu/~scott/cgi-bin/scott.cgi">
<FORM METHOD=post ACTION="http://web.cs.sunyit.edu/~scott/cgi-bin/scott.cgi/w/x/y/z?somejunk">
<FORM METHOD=get ACTION="scott.cgi/w/x/y/z?somejunk">
-->
<FORM METHOD=post ACTION="scott.cgi/w/x/y/z?somejunk">

scalar localtime
Please enter your name: <INPUT size=50 NAME="realname" value=scott><P>
<br>
Please enter your name: <INPUT NAME="username"> <P>
<!-- Please enter your name: <INPUT type=text value=hello> <P> --> 
<br>
orange: <INPUT name=cb type=checkbox value=orange><P>
<br>
yellow: <INPUT name=cb type=checkbox value=yellow><P>
<br>
red: <INPUT name=cb type=checkbox value=red><P>
<br>
blue: <INPUT name=cb type=checkbox value=blue checked><P>
<P>
<!-- 
<SELECT NAME="flavor" > 
<SELECT NAME="flavor" size=4> 
-->
<SELECT NAME="flavor" MULTIPLE size=6 width=40>

EOF
	
foreach $option (sort keys %flavorlist) {
    if($option eq "a") { $select = "SELECTED"; } else { $select=""; }
    print "<OPTION $select VALUE=$option>$flavorlist{$option}\n";
}
$option = "b";
print <<EOF;
    </SELECT>
PRINT A HASH VALUE$flavorlist{$option}
<P>
        <a href=\"scott.cgi?TEST\">
        <img src=\"ch12/scott.gif\" ISMAP>
        </a>



<INPUT TYPE="submit" NAME="Iclickedsubmit1" VALUE="Send0">
<INPUT TYPE="submit" NAME="Iclickedsubmit1" VALUE="Send1">
<INPUT TYPE="submit" NAME="Iclickedsubmit2" VALUE="">
<INPUT TYPE="hidden" NAME="formnum" VALUE="7">
<INPUT TYPE="reset" VALUE="Clear"><P>
</FORM>
</BODY></HTML>
EOF
}
