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

   
