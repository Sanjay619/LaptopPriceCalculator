from django.shortcuts import render,HttpResponse
import random
import mysql.connector
from mysql.connector import Error
import MySQLdb
from datetime import datetime


def loginView(request):
    try:
     Con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="laptoppricingtooldb")
     Cursor = Con.cursor()
     sql = "SELECT * FROM laptoppricingtooldb.laptopinventory"

     print(Cursor.execute(sql))
    except MySQLdb.Error as e:
          print(f"Error while connecting to MySQL: {e}")
    finally:
         print("Debug: Checking connection status before closing")
         if 'connection' in locals() and connection.is_connected():
          MySQLdb.Connect.close()
          print("MySQL connection is closed")
    return render(request, 'login.html')




def SignUpView(request):
    # Handle GET request
    if request.method == 'GET':
        return render(request, "signup.html")

    # Handle POST request (form submission)
    if request.method == 'POST':
         
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        cpassword = request.POST.get('password2')

        print(name , email, password , cpassword)                
       # Establish a connection to the database

        Con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="laptoppricingtooldb")
        Cursor = Con.cursor()
        insert_query = """
        INSERT INTO user (name, email, password, createdts, isAdmin)
        VALUES (%s, %s, %s, %s, %s)"""
    

         # Execute the query
        Cursor.execute(insert_query, (name, email, password, '15-12-2024','0' ))

        # Commit the transaction
        Con.commit()
        return HttpResponse("User has been created successfully!!!")


      
        
          
    return render(request, "signup.html")
       
       
       
       

  

   


def DashboardView(request):
     laptops = [
        {
            "brand": "Dell",
            "model": "Inspiron 15",
            "price": random.randint(500, 1500),
            "processor": "Intel i5",
            "ram": 8,
            "storage": 512,
            "image_url": "https://images.unsplash.com/photo-1580894732444-44e20b49ae5e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=400"
        },
        {
            "brand": "HP",
            "model": "Pavilion 14",
            "price": random.randint(600, 1200),
            "processor": "Intel i7",
            "ram": 16,
            "storage": 256,
            "image_url": "https://images.unsplash.com/photo-1541807084-5c52b6bfc3f8?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=400"
        },
        {
            "brand": "Lenovo",
            "model": "ThinkPad X1",
            "price": random.randint(800, 2000),
            "processor": "Intel i3",
            "ram": 4,
            "storage": 128,
            "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=400"
        },
        {
            "brand": "Apple",
            "model": "MacBook Air",
            "price": random.randint(900, 2500),
            "processor": "M1",
            "ram": 8,
            "storage": 512,
            "image_url": "https://images.unsplash.com/photo-1517430816045-df4b7de01f55?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=400"
        },
        {
            "brand": "Asus",
            "model": "ZenBook 13",
            "price": random.randint(700, 1800),
            "processor": "AMD Ryzen 5",
            "ram": 16,
            "storage": 256,
            "image_url": "https://images.unsplash.com/photo-1571731956672-b24f2a8bba14?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=400"
        },
    ]
     return render(request, 'dashboard.html', {'laptops' : laptops})
    




