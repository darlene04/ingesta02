import mysql.connector
import pandas as pd
import boto3


conexion = mysql.connector.connect(
    host="host.docker.internal",
    port=3307,
    user="root",
    password="123456",
    database="prueba_ingesta"
)

cursor = conexion.cursor()


cursor.execute("SELECT * FROM alumnos")

datos = cursor.fetchall()


df = pd.DataFrame(
    datos,
    columns=["id", "nombre", "carrera"]
)

archivo = "alumnos.csv"

df.to_csv(archivo, index=False)

print("CSV generado correctamente")


nombreBucket = "ingesta-02"

s3 = boto3.client('s3')

s3.upload_file(
    archivo,
    nombreBucket,
    archivo
)

print("Archivo subido a S3")


cursor.close()
conexion.close()