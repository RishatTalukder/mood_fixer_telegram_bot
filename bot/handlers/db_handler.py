# bot/handlers/db_handler.py

from bot.database.db_setup import init_db,SessionLocal
from bot.database.functions import add_placeholders,get_jokes

def setup_database():
    """
    Initializes the database and adds placeholder data.
    """
    init_db()  # This function initializes the database and binds it to SessionLocal
    print("Database initialized successfully.")

    Session = SessionLocal()

    if get_jokes(Session):
        print("Database already contains data.")
        Session.close()
        return

    # Add placeholder data
    add_placeholders()
    Session.close()

def register():
    """
    This function registers database initialization and setup.
    """
    setup_database()
