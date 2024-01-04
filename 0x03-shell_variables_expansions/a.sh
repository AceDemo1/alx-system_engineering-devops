#!/bin/bash

# Script to add all changes, commit, and push to a Git repository

# Check if the Git repository is dirty (has changes)
if [[ -n $(git status -s) ]]; then
    # Add all changes
    git add .

    # Prompt for a commit message
    echo -n "Enter a commit message: "
    read commit_message

    # Commit changes with the provided message
    git commit -m "$commit_message"

    # Push changes to the default remote branch (e.g., 'main' or 'master')
    git push origin $(git symbolic-ref --short HEAD)
else
    echo "No changes to commit."
fi

