# Zhang Yanbo - Personal Portfolio Website

A beautiful, modern personal portfolio website built with Django showcasing Zhang Yanbo's academic background, experience, and skills.

## Features

- Modern, responsive design with gradient backgrounds
- Mobile-friendly layout
- Smooth animations and hover effects
- Education section with GPA highlights
- Professional experience showcase
- Technical skills display
- Contact information with clickable phone and email

## Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5.3.0, Custom CSS
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Inter (Google Fonts)

## Project Structure

```
MyWebPage/
??? personal_website/          # Django project settings
?   ??? __init__.py
?   ??? settings.py
?   ??? urls.py
?   ??? wsgi.py
?   ??? asgi.py
??? portfolio/                 # Portfolio app
?   ??? __init__.py
?   ??? apps.py
?   ??? urls.py
?   ??? views.py
??? templates/                 # HTML templates
?   ??? portfolio/
?       ??? home.html
??? manage.py                  # Django management script
??? requirements.txt           # Python dependencies
??? README.md                 # This file
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download the Project

```bash
# If you have git installed
git clone <repository-url>
cd MyWebPage

# Or simply download and extract the project files
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations

```bash
python manage.py migrate
```

### Step 5: Start the Development Server

```bash
python manage.py runserver
```

The website will be available at: **http://127.0.0.1:8000/**

## Customization

### Personal Information

To update personal information, edit the `portfolio/views.py` file and modify the context data in the `home` function.

### Styling

The website uses custom CSS variables defined in the `templates/portfolio/home.html` file. You can modify:

- `--primary-color`: Main brand color
- `--secondary-color`: Secondary brand color  
- `--accent-color`: Accent color for highlights
- `--text-primary`: Main text color
- `--text-secondary`: Secondary text color

### Skills

To add or modify technical skills, edit the skills section in the HTML template.

## Features in Detail

### Hero Section
- Profile image placeholder with graduation icon
- Name with gradient text effect
- Professional title
- Contact information with clickable links

### Education Section
- University details with school and location
- GPA badges with attractive styling
- Timeline indicators

### Experience Section
- Company and position information
- Department details
- Duration badges

### Skills Section
- Interactive skill tags with hover effects
- Responsive grid layout

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Deployment

For production deployment, consider:

1. Setting `DEBUG = False` in settings.py
2. Using a production database (PostgreSQL, MySQL)
3. Configuring static file serving
4. Setting up HTTPS
5. Using environment variables for sensitive data

## License

This project is created for personal use. Feel free to modify and use as needed.

---

**Note**: This is a single-page website as requested. No navigation or additional pages are implemented. 