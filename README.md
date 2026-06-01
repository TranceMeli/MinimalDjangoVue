![Django](https://img.shields.io/badge/Django-4.2-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.16-red?logo=django&logoColor=white)
![Vue](https://img.shields.io/badge/Vue-3-4FC08D?logo=vue.js&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-5-646CFF?logo=vite&logoColor=white)
![Axios](https://img.shields.io/badge/Axios-1.6-5A29E4?logo=axios&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Node](https://img.shields.io/badge/Node.js-20+-339933?logo=node.js&logoColor=white)

# DjangoVue

A minimal full-stack setup with a Django REST Framework backend and a Vue 3 frontend. Features a sticky navbar with four pages (Home, About, Projects, Contact), each connected to its own API endpoint.

## Project Structure

```
djangovue/
├── backend/              # Django
│   ├── config/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── api/
│   │   └── views.py
│   └── manage.py
└── frontend/             # Vue 3 + Vite
    ├── src/
    │   ├── components/
    │   │   └── Navbar.vue
    │   └── App.vue
    └── vite.config.js
```

## Prerequisites

- Python 3.10+
- Node.js 20+

## Getting Started

### Backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate

pip install django djangorestframework django-cors-headers
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The app is available at `http://localhost:5173`.

## How It Works

Clicking a nav link triggers an API call to the corresponding Django endpoint. The response message is displayed in the frontend with the page name highlighted in bold.

```
Vue (5173)  →  GET /api/home/     →  Django (8000)
            ←  { "message": "Hello from Home API" }

Vue (5173)  →  GET /api/about/    →  Django (8000)
            ←  { "message": "Hello from About" }
```

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/home/` | Home message |
| GET | `/api/about/` | About message |
| GET | `/api/projects/` | Projects message |
| GET | `/api/contact/` | Contact message |