a=$1
b=$2
result=`expr "$a + $b" | bc`
echo $result