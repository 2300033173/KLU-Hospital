# Hospital Management System - Deployment Guide

## Docker Setup

### Prerequisites
- Docker installed on your system
- Docker Compose installed

### Quick Start with Docker

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd hospitalmanagement-final
```

2. **Build and run with Docker Compose:**
```bash
docker-compose up --build
```

3. **Access the application:**
- Open browser: `http://localhost:8000`

### Manual Docker Commands

1. **Build the image:**
```bash
docker build -t hospital-management .
```

2. **Run the container:**
```bash
docker run -p 8000:8000 hospital-management
```

## Local Development Setup

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Create superuser (optional):**
```bash
python manage.py createsuperuser
```

4. **Run the server:**
```bash
python manage.py runserver
```

## GitHub Deployment Options

### 1. GitHub Pages (Static files only)
- Not suitable for Django apps

### 2. Heroku Deployment
- Add `Procfile` and configure for Heroku
- Use PostgreSQL addon

### 3. Railway/Render Deployment
- Connect GitHub repository
- Auto-deploy on push

### 4. AWS/DigitalOcean
- Use Docker image for deployment

## Environment Variables

Create `.env` file for production:
```
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=your-database-url
```

## Sharing with Friends

1. **Share Docker way:**
```bash
# Friend runs this command
docker-compose up
```

2. **Share GitHub repository:**
- Clone and run locally
- Or deploy to cloud platform

## Default Login Credentials

- **Admin**: Create via Django admin or signup
- **Doctor**: Requires admin approval after signup  
- **Patient**: Requires admin approval after signup