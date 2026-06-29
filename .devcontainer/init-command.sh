#!/bin/sh

# This script is run when the dev container is started.
# And will run specific commands based on the operating system.

# Detect the HOST operating system
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

echo "Working on: $machine"

# For Mac and Linux: add SSH keys found under ~/.ssh
if [ "$machine" = "Mac" ] || [ "$machine" = "Linux" ]; then
    find ~/.ssh/ -type f -exec grep -l 'PRIVATE' {} \; | xargs -I{} ssh-add "{}"
fi
