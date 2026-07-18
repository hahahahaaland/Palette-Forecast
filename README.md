# Palette-Forecast
Art Commerce Intelligence Platform.

# Palette Forecast

## Art Commerce Intelligence Platform

Palette Forecast is a backend REST API built using Flask and SQLite for managing an art marketplace. The platform allows users to manage artists, artworks, styles, mediums, and customer orders while providing business analytics to help identify sales trends and customer preferences.

The project goes beyond basic CRUD operations by combining inventory management with analytics that can support business decision-making.

---

# Features

## Artist Management

- Add new artists
- View artist details
- Update artist information
- Delete artists

## Artwork Management

- Manage artworks
- Track artwork availability
- Store artwork pricing
- Associate artworks with artists, styles, and mediums

## Order Management

- Create customer orders
- Gift wrap support
- Commission order support
- Canvas finish selection
- Frame selection
- Custom artwork requests

## Analytics

- Revenue Summary
- Top Selling Artist
- Most Popular Style
- Most Popular Medium
- Artwork Status Summary
- Gift Wrap Statistics
- Commission Order Statistics
- Dashboard Summary

---

# Database Design

The application uses SQLite with the following relational tables:

- Artists
- Styles
- Mediums
- Artworks
- Orders

Relationship Overview

```
Artist
   │
   ├──< Artworks >── Style
   │          │
   │          └── Medium
   │
   └──────── Orders
```

---

# Technology Stack

- Python
- Flask
- SQLite
- REST API
- Postman
- Git
- GitHub

---

# Project Structure

```
Palette Forecast/
│
├── app.py
├── config.py
├── db.py
├── models.py
├── seed.py
├── requirements.txt
├── README.md
│
├── database/
│   └── palette_forecast.db
│
└── .venv/
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/hahahahaaland/Palette-Forecast.git
```

Navigate to the project directory

```bash
cd Palette-Forecast
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

# API Endpoints

## Artists

- GET /artists
- GET /artists/{id}
- POST /artists
- PUT /artists/{id}
- DELETE /artists/{id}

## Artworks

- GET /artworks
- POST /artworks
- PUT /artworks/{id}
- DELETE /artworks/{id}

## Orders

- GET /orders
- POST /orders
- PUT /orders/{id}
- DELETE /orders/{id}

## Styles

- GET /styles
- GET /styles/{id}
- POST /styles
- PUT /styles/{id}
- DELETE /styles/{id}

## Mediums

- GET /mediums
- GET /mediums/{id}
- POST /mediums
- PUT /mediums/{id}
- DELETE /mediums/{id}

---

# Analytics Endpoints

- GET /analytics/revenue
- GET /analytics/top-artist
- GET /analytics/top-style
- GET /analytics/top-medium
- GET /analytics/artwork-status
- GET /analytics/gift-wrap
- GET /analytics/commissions
- GET /dashboard

---

# Future Enhancements

- JWT Authentication
- User Accounts
- Artwork Image Upload
- Admin Dashboard
- Sales Forecasting
- Interactive Charts
- Payment Gateway Integration
- Email Notifications

---

# Project Objective

Palette Forecast demonstrates how backend systems can extend beyond basic CRUD operations by integrating inventory management with business analytics.

The project showcases relational database design, RESTful API development, SQL analytics, and clean backend architecture using Flask and SQLite.

---

# Author

**Nandani**

Capstone Project developed using Flask, SQLite, REST APIs, and SQL Analytics.
