import sqlite3

characteristics = ["cores","threads","speed","brand","socket","model"]

class processors:
    
    def __init__(self,cores,threads,speed,brand,socket,model):
        self.cores = cores
        self.threads = threads
        self.speed = speed
        self.brand = brand
        self.socket = socket
        self.model = model
        

def show_object_from_dataBase():
    
    conn  = sqlite3.connect("dataBase.db")
    cur = conn.cursor()
    
    shows = cur.execute(f"""SELECT ID_processor FROM Processors""")
    
    ids = []
    for show in shows:
        ids.append(show)
    
    print(ids)
    
    id = input("Processor ID: ")
    
    filas = cur.execute(f"""SELECT * FROM Processors WHERE ID_processor = {id}""")
    
    
    for fila in filas:
        print(f"Cores: {fila[1]}")
        print(f"Threads: {fila[2]}")
        print(f"Speed: {fila[3]}")
        print(f"Brand: {fila[4]}")
        print(f"Socket: {fila[5]}")
        print(f"Model: {fila[6]}")
    conn.commit()
    conn.close()
    
def add_object_to_dataBase(self):
    conn  = sqlite3.connect("dataBase.db")
    cur = conn.cursor()
    
    cur.execute(f"""INSERT INTO Processors (Cores,Threads,Speed,Brand,Socket,Model)
                Values ({self.cores},{self.threads},{self.speed},"{self.brand}","{self.socket}","{self.model}")""")
    conn.commit()
    conn.close()
    print("object created")
    
def delete_object_from_dataBase():
    id = input("Processor ID: ")
    conn  = sqlite3.connect("dataBase.db")
    cur = conn.cursor()
    
    cur.execute(f"""DELETE FROM Processors WHERE ID_processor == {id}""")
    conn.commit()
    conn.close()
    print("object eliminated")

def update_object_from_dataBase():
    
    conn  = sqlite3.connect("dataBase.db")
    cur = conn.cursor()
    
    shows = cur.execute(f"""SELECT ID_processor FROM Processors""")
    
    ids = []
    for show in shows:
        ids.append(show)
    
    print(ids)
    
    id = input("Processor ID: ")
    
    filas = cur.execute(f"""SELECT * FROM Processors WHERE ID_processor = {id}""")
    
    for fila in filas:
        print(f"Cores: {fila[1]}")
        print(f"Threads: {fila[2]}")
        print(f"Speed: {fila[3]}")
        print(f"Brand: {fila[4]}")
        print(f"Socket: {fila[5]}")
        print(f"Model: {fila[6]}")
        
    typeChange = str(input("What do you wanna change?: "))
    
    for character in characteristics:
        if typeChange.lower() == character.lower():
            change = input("Replace: ")
        
            cur.execute(f"""UPDATE Processors
                        SET "{typeChange.capitalize()}" == '{change}'
                        WHERE ID_processor == {id}
                        """)
            print("object updated")
                 
    conn.commit()
    conn.close()
    



















