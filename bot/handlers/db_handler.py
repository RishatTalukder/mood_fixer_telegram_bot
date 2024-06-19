from bot.database.db_setup import init_db, SessionLocal
from bot.database.functions import add_placeholders, get_jokes

def setup_database():
    """
    Initializes the database and adds placeholder data.
    """
    try:
        init_db()  # This function initializes the database and binds it to SessionLocal
        print("Database initialized successfully.")

        session = SessionLocal()

        if get_jokes(session):
            print("Database already contains data.")
            session.close()
            return

        # Add placeholder data
        add_placeholders()
    except Exception as e:
        print(f"Error setting up database: {e}")
    finally:
        session.close()

def register():
    """
    This function registers database initialization and setup.
    """
    setup_database()
