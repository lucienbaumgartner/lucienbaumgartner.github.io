#!/bin/bash
now="$(date)"

git add _site/.
git commit -m 'new deployment: $now'
git push -f origin dev:master
