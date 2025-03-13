# 📂 src/ingest_csv_json_parquet.py - Carga de datos en Azure Data Lake

from azure.storage.blob import BlobServiceClient

def upload_file(container_name, file_path, blob_name):
    connect_str = "DefaultEndpointsProtocol=https;AccountName=tu_cuenta;AccountKey=tu_clave"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"Archivo {blob_name} cargado exitosamente.")

if __name__ == "__main__":
    upload_file("data-lake-container", "./data/datos.csv", "datos.csv")