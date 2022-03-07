#!/usr/bin/perl
##
## Turns off buffering
$| = 1;

print "Content-type: text/html\n\n";

## Get the input and put it into the $contents array
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

#print " BUFFER  $ENV{'QUERY_STRING'}";
#print "<BR>";
if ($buffer eq ""){
	$buffer = $ENV{'QUERY_STRING'};
}
print "BUFFER=$buffer";

@pairs = split(/&/, $buffer);
#print "<BR>";
#print "<BR>";
 #print "PAIRS: @pairs";
 #print "END OF PAIRS";
#print "<BR>";
#print "<BR>";

foreach $pair (@pairs)
{
    ($name, $value) = split(/=/, $pair);
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9])([a-fA-F0-9])/pack("C", hex($1.$2))/eg;
    #$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    # $value =~ s/~!/ ~!/g;  # Security fix for mailx
    if ( $contents{$name} eq "" ) {
    $contents{$name} = $value;
    }
    else {
    $contents{$name} .= ";$value";
    }
}

        &sendform;
	exit;

## Send the HTML form (no fields filled in)
sub sendform
{
print <<EOF;
<HTML><HEAD><TITLE>TEST STUFF</TITLE></HEAD>
<BODY><H1>Please enter value to add to the list</H1>
EOF

$NewElem="";

print <<EOF;

<!-- 
<FORM METHOD=post ACTION="http://www.cs.sunyit.edu/~scott/cgi-bin/addtext.cgi">
-->

<FORM METHOD=post ACTION="addtext.cgi">

Please enter some text: <INPUT size=50 NAME="newelem" value=$contents{'newelem'}>
<P>
EOF
    if ( $contents{'hide'} eq "HIDE" ) {
	$contents{'display'}="no";
    }
    if ( $contents{'hide'} eq "NOHIDE" ) {
	$contents{'display'}="yes";
    }

    print "<input type=hidden name=display value=$contents{'display'}>";
    
    if ($contents{'display'} eq "yes") {
    print "Hide Output <input type=checkbox name=hide value=\"HIDE\">";
    }
    else {
    print "Display Output <input type=checkbox name=hide value=\"NOHIDE\"  >";
    	@sflv=split(/;/,$contents{'elems'});
    	foreach $option (@sflv) {
		print "<input type=hidden name=elems value=$option>";
    	}
    }
	
    # loop on thehidden variables and print the select
    if ($contents{'display'} eq "yes") {
    print "<SELECT NAME=\"elems\" size=4 MULTIPLE>";
    @sflv=split(/;/,$contents{'hidelems'});
    @selems=split(/;/,$contents{'elems'});
    foreach $option (@sflv) {
    	$select="";
    	foreach $s (@selems) {
    		if($option eq $s) { $select = "SELECTED"; } 
    	}
    print "<OPTION $select>$option </option>";
    }

    print "<OPTION> $contents{'newelem'} </option>";
    print "</SELECT>";
    }
print <<EOF;

<P>
EOF
    @sflv=split(/;/,$contents{'hidelems'});
    foreach $option (@sflv) {
	print "<input type=hidden name=hidelems value=$option>";
    }
    print "<input type=hidden name=hidelems value=$contents{'newelem'}>";

    	#$value =~ tr/+/ /;
	$try = $contents{'cnt'};
	$try =~ s/try//;
	$try++;
	#$contents{'cnt'}++;

print "<INPUT TYPE=\"submit\" NAME=\"cnt\" VALUE=\"try$try\">";

print <<EOF;
<INPUT TYPE="hidden" NAME="formnum" VALUE="7">
<INPUT TYPE="reset" VALUE="Clear"><P>
</FORM>
</BODY></HTML>
EOF
}
