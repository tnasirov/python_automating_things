select opt in Addition Subtraction Multiplication Division Quit
do
  case $opt in
  Addition)
    read -p "Enter number 1: " num1
    read -p "Enter number 2: " num2
    echo "the addition of your $num1 and $num2 is: $((num1+num2))"
    ;;

  Subtraction)
    read -p "Enter number 1: " num1
    read -p "Enter number 2: " num2
    echo "the Subtraction of your $num1 and $num2 is: $((num1-num2))"
    ;;

  Multiplication)
    read -p "Enter number 1: " num1
    read -p "Enter number 2: " num2
    echo "the Multiplication of your $num1 and $num2 is: $((num1*num2))"
    ;;

  Division)
    read -p "Enter number 1: " num1
    read -p "Enter number 2: " num2
    echo "the Division of your $num1 and $num2 is: $((num1/num2))"
    ;;

  Quit)
    echo "You wanted to quit. Exiting..."
    sleep 1
    exit 0
    ;;
  *)
    echo "Invalid Option"
    ;;
  esac
done