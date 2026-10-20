AssetOps SQL Practice Database

Files:
- assetops.db: populated SQLite database
- setup.sql: table schema reference (the database is already populated)

Tables and row counts:
- employees: 12
- technicians: 6
- assets: 40
- tickets: 180

Open assetops.db using DB Browser for SQLite, SQLiteStudio, or the sqlite3 command-line tool.

CLI example:
  sqlite3 assetops.db
  .tables
  SELECT COUNT(*) FROM tickets;
  .quit

Foreign keys are defined between assets/employees and tickets/assets/technicians.
