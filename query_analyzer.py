import os
from dotenv import load_dotenv

load_dotenv()

import psycopg2

def analyze_query(query):

    try:
        
    
    
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        cur = conn.cursor()



        cur.execute(f"EXPLAIN ANALYZE {query}") # This retrieves the query plan from PostgreSQL


        plan = [row[0] for row in cur.fetchall()]



        planning_time = None

        for line in plan:
            if "Planning Time" in line:
                planning_time = float(
                    line.split(":")[1]
                        .replace("ms", "") # we remove the "ms" from the string temporarily because Python cannot convert/store this value to do operations -> 
                        .strip()
                )

        execution_time = None

        for line in plan:
            if "Execution Time" in line:
                execution_time = float(
                    line.split(":")[1]
                        .replace("ms", "")
                        .strip()
                )



        scan_type = "Unknown"

        for line in plan:
            if "Seq Scan" in line:
                scan_type = "Sequential Scan"
                break

            if "Index Scan" in line:
                scan_type = "Index Scan"
                break


        recommendation = "No recommendation"

        if scan_type == "Sequential Scan":
            recommendation = (
                "Sequential scan detected. "
                "Consider adding an index."
            )

        if(scan_type == "Index Scan"):
            recommendation = (
                "Index is being used correctly"
            )


        if execution_time < 50:
            rating = "Good"
        elif execution_time < 200:
            rating = "Moderate"
        else:
            rating = "Poor"


        analysis = {
            "planning_time": planning_time,
            "execution_time": execution_time,
            "scan_type": scan_type,
            "rating": rating,
            "recommendation": recommendation
        }



        cur.execute( # Saves the results
            """
            INSERT INTO query_history
            (query_text, execution_time_ms, scan_type)
            VALUES (%s, %s, %s)
            """,
            (query, execution_time, scan_type)
        )

        conn.commit()

        cur.close()
        conn.close()
        return analysis

    except psycopg2.Error as e:
        return {"error": str(e)}

    finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()



def get_query_history():

    conn = psycopg2.connect(
            host="localhost",
            database="analyzer",
            user="postgres",
            password="graduate"
        )

    cur = conn.cursor()

    cur.execute("""
        SELECT
        id,
        query_text,
        execution_time_ms,
        scan_type,
        analyzed_at
        FROM query_history
        ORDER BY analyzed_at DESC;
    """)

    rows = cur.fetchall()

    history = []

    for row in rows:
        history.append({
            "id": row[0],
            "query": row[1],
            "execution_time": row[2],
            "scan_type": row[3],
            "analyzed_at": row[4]
        })

    cur.close()
    conn.close()

    return history