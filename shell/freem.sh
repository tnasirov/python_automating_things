gb=$(free -m | awk 'NR==2{print $4}')
echo $gb