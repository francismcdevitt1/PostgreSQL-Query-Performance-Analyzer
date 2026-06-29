# PostgreSQL Query Performance Analyzer

# Overview

A RestAPI created with Python and FastAPI that manages SQL queries using EXPLAIN ANALYZE.
The application executes relevant metrics like execution time, detects scan strategies, stores analysis history and generates optimization recommendations.

## Features

- Analyze SQL queries
- Extract planning time
- Extract execution time
- Detect Index Scan vs Sequential Scan
- Performance rating
- Optimization recommendations
- Store analysis history
- REST API with FastAPI

## Technologies

- Python
- PostgreSQL
- FastAPI
- psycopg2
- pgAdmin

## Configuration

Create a `.env` file in the project root with the following variables:

DB_HOST=localhost
DB_NAME=analyzer
DB_USER=postgres
DB_PASSWORD=your_password

## Installation

1. Clone the repository

git clone ...

2. Install dependencies

pip install -r requirements.txt

3. Start the API

uvicorn app:app --reload

4. Open

http://127.0.0.1:8000/docs

## Run

1. Create a PostgreSQL database named analyzer.

2. Run:

sql/create_tables.sql

3. Run:

sql/sample_data.sql

4. Start the API:

uvicorn app:app --reload

## Example Queries

# Uses an Index Scan

SELECT \*
FROM employees
WHERE department = 'Engineering';

# Usually uses a Sequential Scan

SELECT \*
FROM employees
WHERE name = 'Alice';

# Retrieve all employees

SELECT \*
FROM employees;

# Retrieve a specific employee by ID

SELECT \*
FROM employees
WHERE id = 1;
