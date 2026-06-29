-- Create employees table
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary NUMERIC
);

-- Create index used for testing query performance
CREATE INDEX idx_department
ON employees(department);

-- Create query history table
CREATE TABLE query_history (
    id SERIAL PRIMARY KEY,
    query_text TEXT,
    execution_time_ms NUMERIC,
    scan_type VARCHAR(50),
    analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);