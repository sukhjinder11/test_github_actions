#!/bin/bash
echo "Hello World"

# y=($(gh release list --limit 1))
# z=(($y)[1:3])
# echo $z

# y=($(gh pr list --limit 1))
# z=($(gh pr view $y --json labels))
# # gh pr view $y --json labels

# case "bug" in $z:
#     echo "there is a bug"

latest=($(gh pr list --limit 1))
echo 'latest:' $latest

b=($(gh pr list --label bug --limit 1))
echo 'b:' $b

e=($(gh pr list --label enhancement --limit 1))
echo 'e:' $e

m=($(gh pr list --label major --limit 1))
echo 'm:' $m

case $latest in 
    $b )
        echo "Its a bug" ;;
    $m )
        echo "Its a major" ;;
    $e )
        echo "Its an enhancement" ;;
esac
