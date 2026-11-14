# 📊 Análisis Exploratorio y Dashboard de Ventas (Superstore)

[![Abrir en Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dashboard-superstore-zotvgyxo6vdu9rxzafjhho.streamlit.app/)

Este proyecto presenta un flujo completo de análisis y visualización de datos utilizando el conjunto de datos público **Superstore Sales** de Kaggle. El objetivo es comparar la implementación de 5 visualizaciones estadísticas fundamentales en **Matplotlib** y **Seaborn**, y desplegar posteriormente una aplicación web interactiva mediante **Streamlit**.

---

## 🌐 Aplicación Web Interactiva

Puedes explorar los datos y filtrar las métricas en tiempo real a través de la aplicación desplegada en Streamlit Community Cloud:
👉 **[Ver Dashboard en Vivo](https://dashboard-superstore-zotvgyxo6vdu9rxzafjhho.streamlit.app/)**

---

## 📈 Visualizaciones Incluidas

El proyecto implementa los siguientes 5 tipos de gráficos tanto en el cuaderno de análisis como en la interfaz web:

1. **Gráfico de Barras (Bar Chart):** Comparación de ingresos totales generados por cada categoría de producto.
2. **Gráfico de Líneas (Line Chart):** Evolución temporal del promedio de ventas mensuales.
3. **Gráfico de Dispersión (Scatter Plot):** Relación entre el volumen de ventas y el beneficio neto (*Profit*), segmentado por categoría.
4. **Histograma (Histogram + KDE):** Distribución de frecuencia del importe de los pedidos.
5. **Diagrama de Caja (Boxplot):** Dispersión, mediana y valores atípicos (*outliers*) de los descuentos aplicados según la región geográfica.

---

## 📁 Estructura del Repositorio

* **`app.py`**: Código fuente de la aplicación web interactiva desarrollada con Streamlit.
* **`comparativa_graficos.ipynb`**: Cuaderno de Google Colab que contiene la descarga automatizada desde Kaggle, la limpieza de datos y la comparativa lado a lado de los 5 gráficos en **Matplotlib** y **Seaborn**.
* **`Sample - Superstore.csv`**: Conjunto de datos utilizado para el análisis y la visualización.
* **`requirements.txt`**: Lista de dependencias de Python necesarias para ejecutar el proyecto y desplegarlo en la nube.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Manipulación de datos:** Pandas, NumPy
* **Visualización estática:** Matplotlib, Seaborn
* **Despliegue Web:** Streamlit & Streamlit Community Cloud
* **Origen de datos:** Kaggle API (`vivek468/superstore-dataset-final`)

---

## 🚀 Ejecución en Local

Si deseas clonar este repositorio y ejecutar el dashboard en tu propio equipo:

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/Reysanx/dashboard-superstore.git](https://github.com/Reysanx/dashboard-superstore.git)
   cd dashboard-superstore
