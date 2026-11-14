import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Superstore Dashboard", layout="wide")
st.title("📊 Dashboard de Ventas - Superstore (Kaggle)")

@st.cache_data
def load_data():
    df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Mes_Num'] = df['Order Date'].dt.month
    df['Mes'] = df['Order Date'].dt.strftime('%b')
    return df

df = load_data()

# Sidebar para filtros
st.sidebar.header("Filtros de Exploración")
regiones = st.sidebar.multiselect(
    "Selecciona Regiones:",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)
df_filt = df[df['Region'].isin(regiones)]

# --- FILA 1: Barras y Líneas ---
col1, col2 = st.columns(2)
with col1:
    st.subheader("1. Ventas Totales por Categoría")
    ventas_cat = df_filt.groupby('Category')['Sales'].sum()
    st.bar_chart(ventas_cat, color="#4C72B0")

with col2:
    st.subheader("2. Venta Promedio Mensual")
    ventas_mes = df_filt.groupby(['Mes_Num', 'Mes'])['Sales'].mean().reset_index().sort_values('Mes_Num')
    st.line_chart(ventas_mes.set_index('Mes')['Sales'], color="#DD8452")

st.divider()

# --- FILA 2: Dispersión e Histograma ---
col3, col4 = st.columns(2)
with col3:
    st.subheader("3. Dispersión: Ventas vs Beneficio")
    st.scatter_chart(data=df_filt, x='Sales', y='Profit', color='Category')

with col4:
    st.subheader("4. Histograma: Ventas (< $1,000)")
    fig_hist, ax_hist = plt.subplots(figsize=(8, 4.5))
    sns.histplot(data=df_filt[df_filt['Sales'] < 1000], x='Sales', bins=25, kde=True, color='#55A868', ax=ax_hist)
    ax_hist.set_xlabel("Monto de Venta ($)")
    st.pyplot(fig_hist)

st.divider()

# --- FILA 3: Boxplot ---
st.subheader("5. Boxplot: Descuentos por Región")
fig_box, ax_box = plt.subplots(figsize=(12, 4))
sns.boxplot(data=df_filt, x='Region', y='Discount', palette='pastel', ax=ax_box)
ax_box.set_ylabel("Descuento (%)")
st.pyplot(fig_box)
