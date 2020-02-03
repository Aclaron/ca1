#!/bin/bash
##
## Initialize college pc's for use with git
##

git config user.name "Aclaron"
git config user.email "aaron.cleary28@mail.dcu.ie"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
git pull

echo
echo ~~~~~~~
echo "Done!"
echo ~~~~~~~
echo