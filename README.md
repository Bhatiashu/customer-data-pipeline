# 🚀 Customer Data Pipeline

## 📌 Overview

This project implements a **data pipeline system** using a microservices architecture with **Flask, FastAPI, and PostgreSQL**, orchestrated via Docker.

The system simulates real-world data ingestion by:
- Serving mock customer data via a Flask API
- Ingesting and processing data using FastAPI
- Persisting structured data into PostgreSQL
- Providing APIs for querying stored data

---

## 🏗 Architecture

Flask Mock Server (Port 5000)
↓
FastAPI Pipeline Service (Port 8000)
↓
PostgreSQL Database (Port 5432)


### 🔄 Data Flow

1. Flask serves paginated customer data from a JSON file  
2. FastAPI fetches data from Flask (handles pagination)  
3. FastAPI performs **upsert** into PostgreSQL  
4. APIs expose stored data for querying  

---

## 📁 Project Structure


customer-data-pipeline/
│
├── docker-compose.yml
├── README.md
│
├── mock-server/
│ ├── app.py
│ ├── data/customers.json
│ ├── Dockerfile
│ └── requirements.txt
│
├── pipeline-service/
│ ├── main.py
│ ├── database.py
│ ├── models/customer.py
│ ├── services/ingestion.py
│ ├── Dockerfile
│ ├── requirements.txt
|

## ⚙️ Technologies Used

- Flask – Mock API server  
- FastAPI – High-performance ingestion service  
- PostgreSQL – Relational database  
- SQLAlchemy – ORM  
- Docker & Docker Compose – Containerization  
- Python 3.10+  

---

## 🧩 Features

### ✅ Flask Mock Server
- Loads customer data from JSON file  
- Supports pagination (`page`, `limit`)  
- Endpoints:
  - `GET /api/customers`
  - `GET /api/customers/{id}`
  - `GET /api/health`

---

### ✅ FastAPI Pipeline Service
- Fetches data from Flask API  
- Handles pagination automatically  
- Performs **upsert (insert/update)** into PostgreSQL  
- Endpoints:
  - `POST /api/ingest`
  - `GET /api/customers`
  - `GET /api/customers/{id}`

---

### ✅ PostgreSQL
- Stores structured customer data  
- Primary key: `customer_id`  
- Supports efficient querying  

---

## 🚀 Getting Started

### 🔹 Prerequisites

- Docker & Docker Compose installed  
- Python 3.10+ (optional for local testing)

---

## ▶️ Run the Project

```bash
docker-compose up --build

🌐 Services
Service	URL
Flask API	http://localhost:5000

FastAPI	http://localhost:8000

PostgreSQL	localhost:5432

🧪 API Testing
🔹 1. Test Flask API
curl "http://localhost:5000/api/customers?page=1&limit=5"
🔹 2. Ingest Data
curl -X POST http://localhost:8000/api/ingest

Response:

{
  "status": "success",
  "records_processed": 20
}
🔹 3. Get Customers from Database
curl "http://localhost:8000/api/customers?page=1&limit=5"

4. Get Single Customer
curl http://localhost:8000/api/customers/CUST001

Tested using Docker Compose with PostgreSQL health checks ensuring reliable service startup.

🧠 Key Design Decisions
🔹 Pagination Handling

FastAPI iterates through all pages from the Flask API to ensure complete data ingestion.

🔹 Upsert Strategy
Existing records are updated
New records are inserted
Ensures data consistency and avoids duplication.
🔹 Separation of Concerns
Flask → Data provider
FastAPI → Processing & ingestion
PostgreSQL → Storage

🔹 Containerized Setup

Docker ensures:

Easy setup
Consistent environment
No dependency conflicts

📊 Database Schema
Column	Type
customer_id	VARCHAR (Primary Key)
first_name	VARCHAR
last_name	VARCHAR
email	VARCHAR
phone	VARCHAR
address	TEXT
date_of_birth	DATE
account_balance	DECIMAL
created_at	TIMESTAMP

⚠️ Error Handling
404 for missing customers
Proper API error responses
Safe database transactions
🔍 Future Improvements
Add logging and monitoring
Implement retry mechanism for ingestion
Add async processing for scalability
Add indexing for large datasets
Add authentication layer

✅ Submission Checklist
✔ All services run with docker-compose
✔ Flask serves paginated data
✔ FastAPI ingests data correctly
✔ PostgreSQL stores data
✔ All endpoints working
🎯 Summary

This project demonstrates:

Microservices-based architecture
Data ingestion pipeline design
REST API development
Database integration
Docker-based deployment

The solution is scalable, modular, and aligned with real-world backend engineering practices.