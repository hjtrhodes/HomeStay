from database_connection import DatabaseConnection

def seed_database():
    db_connection = DatabaseConnection()
    db_connection.connect()
    try:
        db_connection.seed('../seeds/homestay_bnb_seed.sql')
        print("Seed data inserted successfully.")
    except Exception as e:
        print(f"Error seeding database: {str(e)}")

if __name__ == "__main__":
    seed_database()