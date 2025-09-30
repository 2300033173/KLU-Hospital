@echo off
echo Setting up GitHub repository for Hospital Management System...
echo.

echo Step 1: Initialize Git repository
git init

echo Step 2: Add all files
git add .

echo Step 3: Create initial commit
git commit -m "Initial commit: Hospital Management System with Docker support"

echo.
echo ========================================
echo MANUAL STEPS REQUIRED:
echo ========================================
echo 1. Go to GitHub.com and create a new repository
echo 2. Copy the repository URL
echo 3. Run these commands:
echo.
echo    git remote add origin YOUR_REPO_URL
echo    git branch -M main
echo    git push -u origin main
echo.
echo ========================================
echo DOCKER COMMANDS:
echo ========================================
echo To run with Docker:
echo    docker-compose up --build
echo.
echo To share with friends:
echo    Share the GitHub repo URL
echo    They can run: docker-compose up
echo ========================================

pause