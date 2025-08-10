# Standard Platform

This is the official monorepo for the **Standard** web application, a full-stack platform designed to empower creators by providing an intuitive, real-time visual editor for building beautiful, high-performance websites.

This project is a non-profit endeavor founded by two teenagers with a singular mission: to eliminate the friction between a brilliant idea and its digital reality.

---

## The Stack

This repository contains two primary projects:

1.  **`/backend`**: A **Django** application built with Python. It serves as a headless API using the Django REST Framework to manage user accounts, projects, and website generation.
2.  **`/frontend`**: A **Vue.js** Single-Page Application (SPA) built with TypeScript and Vite. This is the client-facing visual editor where creators build and customize their websites.

---

## Core Philosophy

*   **Radical Ownership:** Creators have full ownership of their final product. The platform generates clean, dependency-free source code that can be downloaded and hosted anywhere.
*   **Power in Simplicity:** The editor is designed to be powerful, not complicated. We prioritize a clean, intuitive user experience over a bloated feature set.
*   **Design as a Statement:** We believe a website is an identity. Our tools are crafted to help creators build digital presences that are bold, intentional, and unforgettable.

---

## Getting Started

### Prerequisites

*   Python 3.10+
*   Node.js 18+ and npm
*   A running instance of the backend server.

### Backend Setup (`/backend`)

1.  **Navigate into the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: We will create this `requirements.txt` file in a later step.)*

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```
    The backend API will be running at `http://127.0.0.1:8000/`.

### Frontend Setup (`/frontend`)

1.  **Navigate into the frontend directory in a new terminal:**
    ```bash
    cd frontend
    ```

2.  **Install Node dependencies:**
    ```bash
    npm install
    ```

3.  **Start the Vite development server:**
    ```bash
    npm run dev
    ```
    The frontend editor will be running at `http://localhost:5173/` (or a similar port). The editor connects to the Django server for its data.

---

This README establishes the project's purpose and provides a clear, professional guide for anyone who interacts with the code.

### **Next Action: Commit the README**

Now that you've created the file, let's add it to your repository.

**Action:** In your terminal (inside the `Standard-Platform` folder), run these commands:

```bash
