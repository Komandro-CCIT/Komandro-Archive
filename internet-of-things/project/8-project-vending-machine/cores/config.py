from dotenv import load_dotenv
import os


class Config:
    load_dotenv()
    MIDTRANS_CLIENT_KEY = os.getenv('MIDTRANS_CLIENT_KEY') or ""
    MIDTRANS_SERVER_KEY = os.getenv('MIDTRANS_SERVER_KEY') or ""