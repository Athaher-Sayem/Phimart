# Phimart

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.x-red.svg)](https://www.django-rest-framework.org/)

Phimart is a robust e-commerce backend API built with Django and Django REST Framework. It provides a solid foundation for an online marketplace, featuring product management, order processing, user authentication, and image handling, with a production-ready configuration for deployment.

## ✨ Features

*   **Product Management**: Complete CRUD operations for products, categories, and inventory.
*   **Order Processing**: Handle customer orders, cart management, and order status tracking.
*   **User Authentication**: Secure user registration, login, and profile management (using Django's built-in auth system, potentially extended in the `users` app).
*   **Image Management**: Dedicated `Image` model with serializers and viewsets for flexible product image handling, integrated with Cloudinary for cloud storage.
*   **RESTful API**: Well-structured API endpoints built with Django REST Framework, using `ViewSets` and `Routers` for clean and efficient URL routing.
*   **Production Ready**: Configured for deployment with:
    *   **PostgreSQL**: Robust database backend.
    *   **Cloudinary**: Cloud-based media management for scalability.
    *   **WhiteNoise**: Efficient serving of static files.
    *   **python-decouple**: Environment variable management for sensitive settings.
    *   **Vercel**: Includes `vercel.json` for easy deployment on the Vercel platform.

## 🛠️ Technology Stack

*   **Backend**: Python, Django, Django REST Framework
*   **Database**: PostgreSQL (production), SQLite (development default)
*   **Image Storage**: Cloudinary
*   **Deployment Ready**: Vercel, Gunicorn, WhiteNoise
*   **Environment**: python-decouple, dj-database-url

## 🚀 Getting Started

### Prerequisites

*   Python (3.8+ recommended)
*   pip and virtualenv (or venv)
*   Git
*   (Optional) PostgreSQL for local production simulation
*   (Optional) A Cloudinary account for image uploads

### Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Athaher-Sayem/Phimart.git
    cd Phimart