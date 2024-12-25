import requests
import pandas as pd
from db_connect import get_db_connection
import json

### EXTRACT
try:
    data = requests.get('https://russian-casualties.in.ua/api/v1/data/json/daily').json()

except Exception as e:
    print(f"An error occurred in EXTRACT phase: {e}")

### TRANSFORM
try:
    legend = data['legend']
    data = data['data']
    df = pd.DataFrame(data).transpose()
    df.reset_index(level=0, inplace=True)
    df.rename(columns={'index': 'Date'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
except Exception as e:
    print(f"An error occurred in TRANSFORM phase: {e}")


##LOAD
try:
    with open("credentials.json", "r") as file:
        credentials = json.load(file)

    TABLE_NAME = credentials['table']
    conn = get_db_connection()
    cursor = conn.cursor()
    latest_date = df['Date'].iloc[-1].strftime('%Y-%m-%d')

    try:
        cursor.execute(f"SELECT MAX(Date) as Date FROM {TABLE_NAME};")
        latest_db_date = cursor.fetchone()[0]
    except:
        print('Ziadne zaznami v tabulke , nemohli sme dostat latest_db_date')

    if latest_db_date is not None:
        latest_db_date = latest_db_date.strftime('%Y-%m-%d')
        df = df[df['Date'] > latest_db_date]

    #df.to_sql(TABLE_NAME,conn, if_exists='append', index=False)
    rows = [tuple(row) for _, row in df.iterrows()]

    # Prepare the insert query
    insert_query = """
    INSERT INTO military_stats (Date, tanks, apv, artillery, mlrs, aaws, aircraft, 
                            helicopters, uav, vehicles, boats, submarines, se, missiles, personnel)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    # Execute the insert query for all rows at once
    cursor.executemany(insert_query, rows)
    conn.commit()
    # Execute the insert query for all rows at once

    print(f"SUCCESSFULLY inserted {df.shape[0]} rows into table {TABLE_NAME}")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"An error occurred in LOAD phase: {e}")