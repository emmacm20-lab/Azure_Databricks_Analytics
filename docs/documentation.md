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
