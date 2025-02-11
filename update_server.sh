#!/bin/bash

SERVER_IP="185.129.51.56"
PASSWORD="123qaz"


sshpass -p "$PASSWORD" ssh -tt -o StrictHostKeyChecking=no root@$SERVER_IP << EOF
cd /home/ges-api
echo "📥 Updating Git repository:"
git pull

echo ""
echo "🔄 Restarting project.service:"
sudo systemctl restart project.service

echo ""
echo "📊 Service status:"
sudo systemctl status project.service --no-pager
echo ""
echo "✅ Deployment completed successfully!"
exit
EOF
