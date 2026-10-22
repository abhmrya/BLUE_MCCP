PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS assets;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS technicians;

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL CHECK (salary > 0)
);
CREATE TABLE technicians (
    technician_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    team TEXT NOT NULL
);
CREATE TABLE assets (
    asset_id INTEGER PRIMARY KEY,
    asset_name TEXT NOT NULL,
    category TEXT NOT NULL,
    assigned_to INTEGER,
    purchase_cost REAL NOT NULL CHECK (purchase_cost >= 0),
    FOREIGN KEY (assigned_to) REFERENCES employees(employee_id)
);
CREATE TABLE tickets (
    ticket_id INTEGER PRIMARY KEY,
    asset_id INTEGER,
    employee_id INTEGER NOT NULL,
    technician_id INTEGER,
    status TEXT NOT NULL CHECK (status IN ('open', 'in_progress', 'closed')),
    priority TEXT NOT NULL CHECK (priority IN ('low', 'medium', 'high')),
    created_date TEXT NOT NULL,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (technician_id) REFERENCES technicians(technician_id)
);

INSERT INTO employees VALUES
(1, 'Rahul Sharma', 'IT', 30000),
(2, 'Priya Singh', 'IT', 50000),
(3, 'Amit Verma', 'HR', 40000),
(4, 'Neha Gupta', 'HR', 60000),
(5, 'Karan Patel', 'IT', 25000),
(6, 'Mei Chen', 'Finance', 55000),
(7, 'Rohan Das', 'Finance', 45000),
(8, 'Sara Khan', 'Operations', 35000);

INSERT INTO technicians VALUES
(1, 'Priya Singh', 'Infrastructure'),
(2, 'Rohan Das', 'Support'),
(3, 'Mei Chen', 'Applications');

INSERT INTO assets VALUES
(101, 'Rahul-Laptop', 'Laptop', 1, 75000),
(102, 'Priya-Laptop', 'Laptop', 2, 90000),
(103, 'Amit-Monitor', 'Monitor', 3, 18000),
(104, 'Neha-Laptop', 'Laptop', 4, 85000),
(105, 'Spare-Monitor', 'Monitor', NULL, 15000),
(106, 'Karan-Desktop', 'Desktop', 5, 60000),
(107, 'Finance-Laptop', 'Laptop', 6, 95000),
(108, 'Sara-Phone', 'Phone', 8, 30000);

INSERT INTO tickets VALUES
(1001, 101, 1, 1, 'open', 'high', '2026-01-03'),
(1002, 102, 2, 2, 'closed', 'low', '2026-01-04'),
(1003, 101, 1, 2, 'closed', 'medium', '2026-01-08'),
(1004, 103, 3, 3, 'open', 'medium', '2026-01-09'),
(1005, 104, 4, 1, 'in_progress', 'high', '2026-01-11'),
(1006, 106, 5, 2, 'open', 'high', '2026-01-12'),
(1007, 107, 6, 3, 'closed', 'low', '2026-01-13'),
(1008, 108, 8, 1, 'open', 'medium', '2026-01-14'),
(1009, NULL, 7, 2, 'closed', 'low', '2026-01-15'),
(1010, 105, 3, NULL, 'open', 'low', '2026-01-16'),
(1011, 106, 5, 1, 'in_progress', 'medium', '2026-01-18'),
(1012, 102, 2, 3, 'closed', 'high', '2026-01-20');
