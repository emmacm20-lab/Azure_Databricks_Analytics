# 📂 docs/README.md - Documentación del Proyecto
"""
# ☁️ Análisis de Datos en Azure con Databricks y SQL Server

## 📌 Descripción del Proyecto

Este proyecto implementa una **infraestructura de datos en Azure** utilizando **Databricks, SQL Server y almacenamiento en formato Parquet y JSON**. Se centra en la **automatización de ingestión, transformación y análisis de datos** con capacidades de análisis avanzado. Incluye:

- **Carga de archivos CSV, JSON y Parquet en Azure Data Lake.**
- **Procesamiento de datos con Spark en Databricks.**
- **Filtrado dinámico de fechas basado en fecha proceso.**
- **Modelado y consultas en SQL Server con datos transformados.**
- **Análisis estadístico y modelos predictivos aplicados en PySpark.**

## 📂 Estructura del Proyecto
```
📁 Azure_Databricks_Analytics
│── 📂 src/
│   │── ingest_csv_json_parquet.py  # Carga de datos en Azure Data Lake
│   │── transform_data_databricks.py  # Transformaciones con Spark en Databricks
│   │── filter_by_date.py  # Filtrado de datos por fecha proceso
│   │── analytics_pyspark.py  # Modelos analíticos en PySpark
│── 📂 tests/
│   │── test_ingest.py  # Pruebas de carga de datos
│   │── test_filter.py  # Pruebas de filtrado de datos
│   │── test_transform.py  # Pruebas de transformación de datos en Databricks
│   │── test_analytics.py  # Pruebas de análisis en PySpark
│── 📂 docs/
│   │── README.md  # Documentación del proyecto
```

## 🚀 Instalación y Configuración

1. **Clona este repositorio:**
   ```sh
   git clone https://github.com/emmacm20-lab/Azure_Databricks_Analytics.git
   ```
2. **Carga los archivos en Azure Data Lake:**
   ```sh
   python src/ingest_csv_json_parquet.py
   ```
3. **Ejecuta la transformación de datos en Databricks:**
   ```sh
   python src/transform_data_databricks.py
   ```
4. **Realiza el análisis de datos con PySpark:**
   ```sh
   python src/analytics_pyspark.py
   ```

## 📩 Flujo de Trabajo
1. **Ingestión de Datos**: Se cargan archivos CSV, JSON y Parquet en Azure Data Lake.
2. **Procesamiento en Databricks**: Transformación y limpieza con Spark.
3. **Filtrado Dinámico**: Selección de datos basada en fecha proceso.
4. **Almacenamiento y Consulta**: Datos cargados en SQL Server y analizados en Databricks.
5. **Análisis Predictivo**: Modelos estadísticos en PySpark para generación de insights.

## 🛠 Tecnologías Utilizadas
- **Azure Databricks**: Procesamiento y análisis de datos con Spark.
- **Azure Data Lake**: Almacenamiento de archivos estructurados y semiestructurados.
- **SQL Server**: Consolidación de datos y consultas analíticas.
- **PySpark**: Modelos analíticos y filtrado dinámico.
- **Linux & Bash**: Automatización de procesos en entornos cloud.

## 📈 Resultados Esperados
- 📌 **Automatización de ingestión y procesamiento de datos en Azure.**
- 📌 **Optimización de consultas y modelos predictivos en Databricks.**
- 📌 **Integración fluida entre datos estructurados y no estructurados.**
- 📌 **Mayor eficiencia en análisis de datos para toma de decisiones.**

## 🧪 Pruebas
El proyecto incluye pruebas en Python para validar la carga, filtrado y procesamiento de datos.
1. **Ejecución de pruebas:**
   ```sh
   python -m unittest discover tests/
   ```

## 📬 Contacto
Para consultas o sugerencias, contáctame en [emmanuel.cmora20@gmail.com](mailto:emmanuel.cmora20@gmail.com).
"""

# 📂 src/ingest_csv_json_parquet.py - Carga de datos en Azure Data Lake
```python
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
```

# 📂 src/transform_data_databricks.py - Transformaciones con Spark en Databricks
```python
from pyspark.sql import SparkSession

def transform_data():
    spark = SparkSession.builder.appName("Data Transformation").getOrCreate()
    df = spark.read.parquet("dbfs:/mnt/data/datos.parquet")
    df_transformed = df.withColumnRenamed("old_column", "new_column")
    df_transformed.write.mode("overwrite").parquet("dbfs:/mnt/data/datos_limpiados.parquet")
    print("Transformación completada.")

if __name__ == "__main__":
    transform_data()
```

# 📂 src/filter_by_date.py - Filtrado dinámico por fecha proceso
```python
import pandas as pd

def filter_by_date(df, fecha_proceso):
    df_filtered = df[df['fecha'] == fecha_proceso]
    return df_filtered

if __name__ == "__main__":
    df = pd.read_csv("data/datos.csv")
    fecha_proceso = "2024-05-01"
    df_filtrado = filter_by_date(df, fecha_proceso)
    print(df_filtrado.head())
```

# 📂 tests/test_ingest.py - Pruebas de carga de datos en Azure Data Lake
```python
import unittest
from src.ingest_csv_json_parquet import upload_file

class TestIngestData(unittest.TestCase):
    def test_upload(self):
        try:
            upload_file("data-lake-container", "./data/dummy.csv", "dummy.csv")
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
```

# 📂 tests/test_filter.py - Pruebas de filtrado de datos
```python
import unittest
import pandas as pd
from src.filter_by_date import filter_by_date

class TestFilterData(unittest.TestCase):
    def test_filter(self):
        df = pd.DataFrame({"fecha": ["2024-05-01", "2024-06-01"], "valor": [100, 200]})
        df_filtered = filter_by_date(df, "2024-05-01")
        self.assertEqual(len(df_filtered), 1)

if __name__ == "__main__":
    unittest.main()
```

# 📂 tests/test_transform.py - Pruebas de transformación de datos en Databricks
```python
import unittest
from src.transform_data_databricks import transform_data

class TestTransformData(unittest.TestCase):
    def test_transform(self):
        try:
            transform_data()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
```

# 📂 tests/test_analytics.py - Pruebas de análisis en PySpark
```python
import unittest
from src.analytics_pyspark import run_analytics

class TestAnalytics(unittest.TestCase):
    def test_analytics(self):
        try:
            run_analytics()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
```