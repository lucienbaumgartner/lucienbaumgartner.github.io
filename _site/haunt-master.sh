#!/bin/bash
now="$(date)"
echo "[commit message:] new deployment: $now"
git add _site/.
git commit -m 'new deployment: $now'
git show --name-only
git push -f origin dev:master
