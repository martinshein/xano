#!/bin/bash

# GitHub Deployment Script for Xano Documentation
# Run this script locally with your GitHub credentials

echo "🚀 Deploying Xano Documentation to GitHub..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
fi

# Add GitHub remote if not exists
if ! git remote | grep -q "origin"; then
    echo "Adding GitHub remote..."
    git remote add origin https://github.com/martinshein/xano.git
else
    echo "GitHub remote already configured"
fi

# Add all files
echo "Adding all files..."
git add -A

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "No changes to commit"
else
    echo "Committing changes..."
    git commit -m "Update Xano documentation - optimized for no-code users

- Comprehensive API documentation updates
- Enhanced guides for n8n, WeWeb, and Make integrations
- Improved readability and structure
- Added practical examples and use cases
- Removed HTML artifacts and navigation elements"
fi

# Push to GitHub
echo "Pushing to GitHub..."
echo "You may be prompted for your GitHub credentials..."
git push origin main --force

echo "✅ Deployment complete!"
echo "View your documentation at: https://github.com/martinshein/xano"