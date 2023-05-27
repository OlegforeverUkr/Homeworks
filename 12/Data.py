import psycopg2
from settings import host, user, password, db, port

new_database = 'new'
new_table = 'users'
new_columns = False

try:
    connect = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db
    )

    connect.set_session(autocommit=True)

    with connect.cursor() as cursor:
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{new_database}'")
        db_exists = cursor.fetchone()[0]

        if not db_exists:
            cursor.execute(f'CREATE DATABASE {new_database};')
            print(f'Create Database!')

    connect = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=new_database
    )

    connect.set_session(autocommit=True)

    with connect.cursor() as cursor:
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{new_table}')")
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            cursor.execute(f'''CREATE TABLE {new_table} (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        email VARCHAR(50) NOT NULL);''')

        if new_columns:
            col_1 = input('Insert name and parameters of new column (phone varchar(100) not null) - ')
            options = [i for i in col_1.split()]
            if len(options) > 2:
                cursor.execute(
                    f"ALTER TABLE {new_table} ADD COLUMN {options[0]} {options[1]} DEFAULT '---' {options[2]} {options[3]};")
            else:
                cursor.execute(
                    f"ALTER TABLE {new_table} ADD COLUMN {options[0]} {options[1]} DEFAULT '---' NOT NULL;")

            cursor.execute(
                f"SELECT column_name FROM information_schema.columns WHERE table_name = '{new_table}' ORDER BY ordinal_position DESC LIMIT 1")
            last_column_name = cursor.fetchone()[0]

            if last_column_name == options[0]:
                name = input('Insert name user - ')
                email = input('Insert email user - ')
                new_column_value = input(f"Insert value for the new column '{options[0]}' - ")

                cursor.execute(f"INSERT INTO {new_table} (name, email, {options[0]}) VALUES (%s, %s, %s);",
                               (name, email, new_column_value))
        else:
            name = input('Insert name user - ')
            email = input('Insert email user - ')

            cursor.execute(f"INSERT INTO {new_table} (name, email) VALUES (%s, %s);", (name, email))

        print("Data is updated!")

except Exception as e:
    print('Error:', e)

finally:
    if connect:
        connect.close()
        print('Connection end!')
