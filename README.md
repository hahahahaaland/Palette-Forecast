# 🎨 Palette Forecast
### *Where Art Meets Intelligence.*

Palette Forecast is a full-stack **Art Commerce Intelligence Platform** that transforms an art store into a data-driven business. Beyond simply managing artists, artworks, and customer orders, the platform uncovers valuable insights into customer preferences, popular artistic styles, revenue trends, and sales performance.

Designed with a modern React frontend and a Flask-powered REST API, Palette Forecast demonstrates how business intelligence can be integrated into creative industries.

---

# Project Highlights

 Manage talented artists and their portfolios.

 Maintain an inventory of artworks across multiple styles and mediums.

 Record customized customer orders with premium options.

 Generate meaningful analytics using **Pandas**.

 Experience a responsive modern interface built with **React + Tailwind CSS**.

---

# Features

## Dashboard

The dashboard provides a quick snapshot of the business.

- Total Artists
- Total Artworks
- Total Orders
- Total Revenue
- Available Artworks
- Sold Artworks

---

## Artist Management

Manage every artist connected with the brand.

✔ View Artists

✔ Add Artist

✔ Edit Artist

✔ Delete Artist

Each artist stores:

- Name
- Specialization
- Experience
- Country

---

## Artwork Management

Maintain an organized artwork inventory.

Each artwork stores:

- Title
- Artist
- Style
- Medium
- Base Price
- Availability Status

Supported operations:

- View Artwork
- Add Artwork
- Edit Artwork
- Delete Artwork

---

##  Order Management

Customers can personalize their purchases.

Order details include:

- Customer Name
- Artwork
- Size
- Frame Type
- Canvas Finish
- Customization
- Commission Order
- Gift Wrap
- Final Price
- Order Date

---

# Business Analytics

Instead of simply storing data, Palette Forecast analyzes it.

Using **Pandas**, the application generates insights such as:

Total Revenue

Most Popular Artist

Most Popular Style

 Most Popular Medium

 Artwork Status Distribution

Gift Wrap Statistics

Commission Order Statistics

These insights help understand customer preferences and business performance.

---

# Technology Stack

## Backend

- Python
- Flask
- SQLite
- Pandas
- Flask-CORS

---

## Frontend

- React
- Vite
- Tailwind CSS
- Axios

---

# Project Structure

```
Palette Forecast
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── services/
│
├── static/
├── templates/
├── app.py
├── analytics.py
├── config.py
├── db.py
├── models.py
├── seed.py
├── requirements.txt
└── README.md
```

---

# Getting Started

## Clone the Repository

```bash
git clone <repository-url>
cd Palette-Forecast
```

---

## Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Flask

```bash
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

---

## Start React Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# API Endpoints

## Artists

- GET /artists
- POST /artists
- PUT /artists/{id}
- DELETE /artists/{id}

---

## Artworks

- GET /artworks
- POST /artworks
- PUT /artworks/{id}
- DELETE /artworks/{id}

---

## Orders

- GET /orders
- POST /orders

---

## Analytics

- /analytics/revenue
- /analytics/top-artist
- /analytics/top-style
- /analytics/top-medium
- /analytics/status
- /analytics/gift-wrap
- /analytics/commissions

---

# Learning Outcomes

This project demonstrates practical experience with:

- REST API Development
- CRUD Operations
- Relational Database Design
- SQL Joins
- React State Management
- Axios API Integration
- Tailwind CSS
- Data Analysis using Pandas
- Full-Stack Application Development

---

# Future Improvements

- Image upload for artworks
- Artist profile pages
- Search & filtering
- Authentication & authorization
- Sales forecasting
- Interactive charts using Chart.js or Recharts
- Export analytics reports to PDF/Excel

---

# Author

**Nandani**

*"Creativity is an art. Intelligence is the masterpiece."* 