import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Analytics")

# Load sample dataset
df = pd.read_csv("notebook/data/stud.csv")

st.write("Sample of the Data:")
st.dataframe(df.head())

fig, ax = plt.subplots()
sns.histplot(df["math_score"], kde=True, ax=ax)
st.pyplot(fig)
