#!/usr/bin/perl -T
#!/usr/bin/perl

BEGIN {
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
   print "Content-type: text/html\n\n";
}

## Turns off buffering
# $| = 1;
# print "Content-type: text/html\n\n";

open(grades, "<grades") || die "Can't open grades: $!\n";
#open(GRADES, "grades") || { $openfailed = TRUE };
#if ($openfailed) {
	#print("openfailed\n");
	#exit;
#}
@newarray = <grades>;
print "NEWARRAY @newarray";
close (grades);
# $newarray[100000] =1;
$NEWARRString =@newarray;

print "\n**************************\n";
print "NEWARRAY STRING $NEWARRString Number in array $#newarray\n";
# NEWARRAY STRING 9 Number in array 8
print "\n**************************\n";
open(GRADES, "grades") || die "Can't open grades: $!\n";
$i=0;
while ($i<11) {
	$i++;
	print "LINE $i= $newarray[$i]";

	print "Value EXISTS, but may be undefined.\n"  if exists  $newarray[ $i ];
	print "Value is DEFINED, but may be false.\n"  if defined $newarray[ $i ];
	print "Value at array index $i is TRUE.\n" if         $newarray[ $i ];

}
print "\n**************************\n";

$LINECNT=0;

#while ($line = <GRADES>) { # works
#while (<GRADES>) { #works
foreach $line (<GRADES>) { # doesn't work unless use also $_ = $line;
 #foreach $line (@newarray) { # doesn't work unless use also $_ = $line;
    chomp $line;
    $_ = $line;
    if(/scott/){
	print "IT WAS SCOTT\n <br>";
    }
    $line = $_;
    print("my $_ hello\n");
    $LINECNT++;
    ($student, $grade) = split(/ /, $line);
    chomp $grade;
print "STUDENT $student GRADE $grade \n<BR>";
    $grades{$student} .= $grade . " ";
    $grades[$LINECNT] .= $student . " " . $grade . "\n";
print "***** $student GRADES: $grades{$student} <br>";

}

print "The whole ARRAY file:\n @grades";
print "AFTER The whole ARRAY file:\n";
print "The whole HASH file:\n %grades";
$myGrades=%grades;
print "The whole HASH file:\n $myGrades";
print "AFTER The whole HASH file:\n";
print "THERE ARE $LINECNT LINES IN THE FILE\n";

foreach $student (sort keys %ENV) {
print "ENV IS: $student $ENV{$student}<BR>\n";
}

$grades=17;
foreach $student (sort keys %grades) {
    $scores = 0;
    $total = 0;    
    @grades = split(/ /, $grades{$student});
print "Index of last GRADE ARRAY element $#grades  \n<BR>";
$size = @grades;
print "GRADE ARRAY SIZE1 (number of elements) $size  \n<BR>";
$size = scalar @grades;
print "GRADE ARRAY SIZE2 (number of elements) $size  \n<BR>";
print "GRADE ARRAY SIZE3 (number of elements)" . @grades ."\n<BR>";
print "GRADE ARRAY SIZE4 (number of elements) $grades  \n<BR>";
print "GRADE ARRAY First 2 elements: $grades[0] $grades[1] \n<BR>";
print "ENTIRE GRADE ARRAY @grades\n<BR>";
    foreach $grade (@grades) {
        $total += $grade;
        $scores++;
    }
    $average = $total / $scores;
    print "$student: $grades{$student}\tAverage: $average\n<BR>";

if ("0" eq 00){
print "IT WAS EQUAL (0)\n<BR>";
}
else {
print "IT WAS NOT EQUAL (0)\n<BR>";
}
if ("xyz" == 0){
print "IT WAS EQUAL\n<BR>";
}
else {
print "IT WAS NOT EQUAL\n<BR>";
}


}


=pod

=begin comment

my $object = NotGonnaHappen->new();


ignored_sub();

$wont_be_assigned = 37;

=end comment


=cut

#dwefwef ;


#print "HELLO\n<BR>";

#prin "HELLO\n<BR>";

#fqwefq




