#!/usr/bin/python3
"""Database connection and schema."""

import mysql.connector
from contextlib import contextmanager

class DBBase:
    def __init__(self):
        self.cfg = {
            'host': 'mysql-7b01a60-alustudent-792a.f.aivencloud.com',
            'port': 22910,
            'user': 'avnadmin',
            'password': 'AVNS_-xpmCGsjePsn2OMW3H3',
            'database': 'defaultdb',
            'ssl_ca': '/home/jefie369/Documents/coding lab/ca.pem'  # ✅ Replace with your actual path
        }
        self.init_schema()

    @contextmanager
    def conn(self):
        conn = mysql.connector.connect(**self.cfg)
        try:
            yield conn
        finally:
            conn.close()

    def init_schema(self):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username VARCHAR(50) PRIMARY KEY,
                    points INT NOT NULL DEFAULT 0
                )""")
            cur.execute("""
                CREATE TABLE IF NOT EXISTS centers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    location VARCHAR(100),
                    status VARCHAR(10),
                    distance FLOAT
                )""")
            cur.execute("""
                CREATE TABLE IF NOT EXISTS tips (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    tip TEXT
                )""")
            cur.execute("""
                CREATE TABLE IF NOT EXISTS rewards (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    description VARCHAR(100),
                    cost INT
                )""")
            conn.commit()
