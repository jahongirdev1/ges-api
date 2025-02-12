#!/bin/bash

SERVER_IP="185.129.51.56"
PASSWORD="123qaz"

# Prompt for commit message until a non-empty message is provided
while true; do
  read -p "Enter commit message: " COMMIT_MESSAGE
  if [ -n "$COMMIT_MESSAGE" ]; then
    break
  else
    echo "Commit message cannot be empty. Please try again."
  fi
done

# Commit and push local changes
echo "📤 Adding, committing, and pushing changes:"
git add .
git commit -m "$COMMIT_MESSAGE" || echo "No changes to commit."
git push

# Connect to the server and deploy changes
sshpass -p "$PASSWORD" ssh -tt -o StrictHostKeyChecking=no root@$SERVER_IP << EOF

# Pull the latest changes
echo "\n📥 Updating Git repository:"
cd /home/ges-api

# Stash local changes to prevent merge conflicts
git stash save "Auto-stashed before pull"

# Pull the latest changes
git pull

# Apply the stashed changes back if there are any
git stash pop || echo "No stashed changes to apply."

# Restart the service
echo "\n🔄 Restarting project.service:"
sudo systemctl restart project.service

# Check service status
echo "\n📊 Service status:"
sudo systemctl status project.service --no-pager

# Deployment completion message
echo "\n✅ Deployment completed successfully!"
exit
EOF
