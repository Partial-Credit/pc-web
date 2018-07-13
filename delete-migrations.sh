#!/usr/bin/env bash

read -p "Are you sure you want to delete all migrations? (y/n) " -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Deleting migrations!"
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete
fi
