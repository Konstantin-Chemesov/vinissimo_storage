from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import psycopg2

def get_connection():
    conn = psycopg2.connect(dbname="vinissulita", user="ks_chemesov", password="Gohome", host="0.0.0.0", port="5433")
    cur = conn.cursor()
    cur.execute("INSERT INTO vine.v_vine (vine_name) VALUES ('Мысхако');")
    conn.commit()
    cur.close()
    print("Подключение установлено")
    conn.close()

@api_view(['GET'])
def just_try(request):
    return Response({"message": "Hello, world!"})

if __name__ == '__main__':
    get_connection()