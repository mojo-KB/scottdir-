#!/bin/sh

echo "Content-type: text/html"
echo ""
echo "<FORM METHOD=post ACTION=http://localhost:55555/cgi-bin/prtenv.cgi>"
echo "<input type=submit name=sss value=222>"
echo "</form>"
