# ETL Project for Military Casualties Data

## Project Overview

This project implements an ETL (Extract, Transform, Load) process that fetches data from an API, processes it, and loads it into a PostgreSQL database.

### Steps

1. **Extract**:  
   - Fetches daily military casualties data from an external API (`https://russian-casualties.in.ua/api/v1/data/json/daily`).
   - Handles any exceptions during data extraction and logs errors if necessary.

2. **Transform**:
   - The fetched data is processed and transformed into a structured pandas DataFrame.
   - Columns are renamed for clarity, and the `Date` column is converted to a datetime format.

3. **Database Table Creation**:
   - The table `military_stats` is created in the table_setup.sql file.

4. **JSON File for Credentials**:
   - The `credentials.json` file stores sensitive information for connecting to the PostgreSQL database, including host, port, database, user, password, and the target table name.

5. **Database Connection**:
   - The `get_db_connection()` function uses credentials from a `credentials.json` file to establish a connection to the PostgreSQL database using `psycopg2`.

6. **Load**:
   - Establishes a connection to a PostgreSQL database using credentials stored in a `credentials.json` file.
   - Retrieves the latest entry from the database to determine which records should be inserted.
   - Inserts new records into the `military_stats` table in the database.
   

7. **Error Handling**:
   - Throughout the process, exceptions are caught and logged for troubleshooting.

### Files

- `ETL.py`: Contains the ETL process logic (Extract, Transform, Load).
- `db_connect.py`: Contains the database connection logic using `psycopg2`.
- `credentials.json`: Stores the database connection credentials.
- `table_setup.sql`: Stores the database connection credentials.

### How to Run

1. Set up the PostgreSQL database and ensure that the `military_stats` table exists.
2. Populate the `credentials.json` file with appropriate values for your database connection.
   I have provided `dummy_credentials.json` to show you how it's structure shoud look like.
3. Run the `ETL.py` script to fetch data from the API, transform it, and load it into the database.


### Possible changes

Instead of `psycopg2` library you can use `sqlalchemy library.


