<h1 align="center">🛒 Phimart</h1>


Phimart is a robust e-commerce backend API built with Django and Django REST Framework. It provides a solid foundation for an online marketplace, featuring product management, order processing, user authentication, and image handling, with a production-ready configuration for deployment.


<div align="center">
 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.x-red.svg)](https://www.django-rest-framework.org/)
</div>

<br />


<hr />

## 📑 Table of Contents

- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 📖 About the Project

**Phimart** is designed to simplify the complexities of online retail and mart management. Whether it's tracking inventory, processing user orders, or managing administrative tasks, Phimart provides a clean interface and a powerful backend to handle day-to-day e-commerce operations efficiently.

## ✨ Key Features

* **User Authentication:** Secure login and registration using JWT/OAuth.
* **Product Management:** Add, update, delete, and categorize products effortlessly.
* **Shopping Cart & Checkout:** Seamless cart management and secure checkout process.
* **Order Tracking:** Real-time status updates for customer orders.
* **Admin Dashboard:** Centralized hub for managing users, products, and sales analytics.
* **Responsive UI:** Fully optimized for desktop, tablet, and mobile devices.

## 💻 Tech Stack

| Category | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | React / Next.js | UI Framework (Update as needed) |
| **Backend** | Node.js / Express | Server environment and framework |
| **Database** | MongoDB / PostgreSQL | Primary data storage |
| **Styling** | Tailwind CSS | Utility-first CSS framework |
| **Deployment** | Vercel / Render | Cloud hosting platforms |

## 🚀 Getting Started

Follow these instructions to set up the project locally on your machine.

### Prerequisites

Ensure you have the following installed on your local development environment:
* [Node.js](https://nodejs.org/) (v16.x or higher)
* [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)
* Database (e.g., MongoDB local instance or URI)

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Athaher-Sayem/Phimart.git](https://github.com/Athaher-Sayem/Phimart.git)
   ```

2. **Navigate into the project directory:**
   ```bash
   cd Phimart
   ```

3. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your configuration details:
   ```env
   PORT=5000
   DATABASE_URI=your_database_connection_string
   JWT_SECRET=your_jwt_secret_key
   ```

5. **Run the application:**
   ```bash
   npm run dev
   # or
   yarn dev
   ```
   The app will typically be running at `http://localhost:3000` or `http://localhost:5000`.

## 🛠 Usage

Once the application is running, you can navigate to the local host address in your browser. 
* **Customers** can browse products, add them to the cart, and proceed to checkout.
* **Administrators** can access the `/admin` route (ensure you have an admin account set up in your DB) to manage inventory and view sales metrics.

## 🔌 API Reference

If you are integrating the backend with a different client, here are some of the core endpoints:

| Endpoint | Method | Auth Required | Description |
| :--- | :---: | :---: | :--- |
| `/api/users/login` | `POST` | No | Authenticates a user and returns a token |
| `/api/products` | `GET` | No | Fetches all available products |
| `/api/products/:id` | `GET` | No | Fetches a single product by ID |
| `/api/orders` | `POST` | Yes | Creates a new customer order |
| `/api/admin/stats` | `GET` | Yes (Admin) | Retrieves sales and user statistics |

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📫 Contact

**Athaher Sayem** * GitHub: [@Athaher-Sayem](https://github.com/Athaher-Sayem)
* Project Link: [https://github.com/Athaher-Sayem/Phimart](https://github.com/Athaher-Sayem/Phimart)

---
<p align="center">Made with ❤️ by Athaher Sayem</p>