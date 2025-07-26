import sqlite3

conn = sqlite3.connect("nutrition.db")
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS retention_factors (
        Retn_Code TEXT,
        Desc TEXT,
        Nutr_No TEXT,
        NutrDesc TEXT,
        Retn_Factor REAL,
        N INTEGER,
        StdDev REAL
    )
''')

with open("retn5_dat.txt", "r", encoding="utf-8") as file:
    for line in file:
        fields = [f.strip("~") for f in line.strip().split("^")]
        if len(fields) != 7:
            continue  

        try:
            retn_code = fields[0]
            desc = fields[1]
            nutr_no = fields[2]
            nutr_desc = fields[3]
            retn_factor = float(fields[4]) if fields[4] else None
            n = int(fields[5]) if fields[5] else None
            stddev = float(fields[6]) if fields[6] else None

            cur.execute('''
                INSERT INTO retention_factors
                (Retn_Code, Desc, Nutr_No, NutrDesc, Retn_Factor, N, StdDev)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (retn_code, desc, nutr_no, nutr_desc, retn_factor, n, stddev))
        except Exception as e:
            print("Error parsing line:", line)
            print(e)


conn.commit()

print("Храни, съдържащи 'VEAL':")
for row in cur.execute("SELECT * FROM retention_factors WHERE Desc LIKE '%VEAL%'"):
    print(row)

conn.close()
