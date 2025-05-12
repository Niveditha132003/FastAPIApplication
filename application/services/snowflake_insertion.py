import snowflake.connector
import random

def get_connection():
    return snowflake.connector.connect(
        user='NIVEDITHA',
        password='90351@Revanthsai',
        account='frtcizk-rr68458',
        warehouse='COMPUTE_WH',
        database='MYDB',
        schema='MYSCHEMA'
    )


def setup_table():
    conn = get_connection()
    cur = conn.cursor() 
    try:
        cur.execute("""
            CREATE OR REPLACE TABLE playertable (
                player_id INT,
                Player STRING,
                Team STRING,
                MatchNo INT,
                Vs_Team STRING,
                Score INT,
                Balls INT
            )
        """)
        data = [
            (1,'Virat', 'RCB', 1, 'KKR', (60, 100), (40, 60)),
            (2,'Rohit', 'MI', 2, 'CSK', (20, 40), (10, 30)),
            (3,'Dhoni', 'CSK', 3, 'GT', (25, 34), (7, 23)),
            (4,'Patidar', 'RCB', 5, 'GT', (25, 67), (21, 60)),
            (5,'Padikkal', 'RCB', 7, 'PBKS', (67, 100), (40, 80)),
            (6,'Hazelwood', 'RCB', 10, 'DC', (23, 78), (17, 69)),
            (7,'Salt', 'RCB', 6, 'CSK', (56, 101), (40, 70)),
            (8,'Hardik', 'MI', 9, 'SRH', (45, 100), (31, 60)),
            (9,'Abhisek', 'SRH', 11, 'DC', (8, 28), (2, 12)),
            (10,'Klaseen', 'SRH', 17, 'GT', (0, 18), (0, 24)),
            (11,'Nitish reddy', 'SRH', 4, 'RR', (5, 67), (3, 45)),
            (12,'KL Rahul', 'DC', 12, 'RCB', (5, 46), (6, 48)),
            (13,'Rishab pant', 'LSG', 13, 'RCB', (56, 100), (40, 60)),
            (14,'Russel', 'KKR', 1, 'RCB', (3, 49), (2, 34)),
            (15,'Shreyas', 'PBKS', 14, 'CSK', (45, 63), (40, 60)),
            (16,'Shubman Gill', 'GT', 3, 'CSK', (89, 100), (40, 68)),
            (17,'Sudharsan', 'GT', 16, 'MI', (67, 81), (40, 60)),
            (18,'Hasranga', 'RR', 15, 'MI', (64, 67), (60, 80)),
            (19,'Shivam Dubey', 'RR', 4, 'SRH', (24, 78), (21, 46)),

]
        
        
        insert_values = []
        for player_id,player, team, match_no, vs_team, score_range, balls_range in data:
            score = random.randint(score_range[0], score_range[1])
            balls = random.randint(balls_range[0], balls_range[1])
            insert_values.append(f"({player_id},'{player}', '{team}', {match_no}, '{vs_team}', {score}, {balls})")
        
        insert_query = "INSERT INTO playertable (Player_id, Player, Team, MatchNo, Vs_Team, Score, Balls) VALUES "
        insert_query += ", ".join(insert_values)

        cur.execute(insert_query)
        conn.commit()
        cur.execute("SELECT * FROM playertable")
        for row in cur:
            print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]},{row[6]}")

    except Exception as e:
        print("Error occurred while setting up table:", e)
    finally:
        cur.close()  
        conn.close()
get_connection()
setup_table()