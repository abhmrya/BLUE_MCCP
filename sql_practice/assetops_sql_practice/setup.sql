-- AssetOps SQL Practice Database (SQLite)
PRAGMA foreign_keys = ON;

CREATE TABLE employees (
 employee_id INTEGER PRIMARY KEY,
 employee_name TEXT NOT NULL,
 department TEXT NOT NULL
);
CREATE TABLE technicians (
 technician_id INTEGER PRIMARY KEY,
 technician_name TEXT NOT NULL,
 team TEXT NOT NULL
);
CREATE TABLE assets (
 asset_id INTEGER PRIMARY KEY,
 hostname TEXT NOT NULL UNIQUE,
 category TEXT NOT NULL,
 purchase_date TEXT NOT NULL,
 warranty_months INTEGER NOT NULL CHECK(warranty_months >= 0),
 cost REAL NOT NULL CHECK(cost >= 0),
 status TEXT NOT NULL,
 employee_id INTEGER REFERENCES employees(employee_id)
);
CREATE TABLE tickets (
 ticket_id INTEGER PRIMARY KEY,
 asset_id INTEGER NOT NULL REFERENCES assets(asset_id),
 technician_id INTEGER NOT NULL REFERENCES technicians(technician_id),
 category TEXT NOT NULL,
 priority TEXT NOT NULL,
 status TEXT NOT NULL,
 created_at TEXT NOT NULL,
 closed_at TEXT,
 hours_spent REAL NOT NULL CHECK(hours_spent >= 0)
);
-- See the accompanying assetops.db for the populated practice dataset.
