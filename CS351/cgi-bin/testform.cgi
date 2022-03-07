#!/bin/sh

echo "Content-type: text/html"
echo ""
#echo "<FORM METHOD=post ACTION=/cgi-bin/prtenv.cgi>"
echo "<FORM METHOD=get ACTION=/cgi-bin/ptest.cgi>"
echo "<input type=text name=testcase value=333>"
echo "<input type=submit name=myfunc value=222>"
echo "</form>"
