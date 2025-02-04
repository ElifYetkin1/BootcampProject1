# -*- coding: utf-8 -*-
"""AygazBootcamp1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w5TpCDBjsYW9EYxbOPYB_as2gNzQgwzI
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype
import plotly.express as px
url = 'https://raw.githubusercontent.com/ElifYetkin1/BootcampProject1/main/AB_NYC_2019.csv?token=GHSAT0AAAAAACFNWRYFWFU6N64PLVJUGYXCZF6MO6Q'
df_abnb = pd.read_csv(url)

df_abnb.info()

df_abnb.head()

# veriyi biraz düzenleyeceğim. Last review ve rewievs per month sütunlarındaki NaN değerlerini 0 ile değiştiriyorum
df_abnb['last_review'].fillna(0)
df_abnb['rewievs_per_month'].fillna(0)

#mahalleye göre verilerin dağılımına bakalım

df_abnb['neighbourhood'].value_counts()

#  şehire göre dağılıma bakalım

df_abnb['neighbourhood_group'].value_counts()

#dağılımı grafikle göstereceğim
df_abnb['neighbourhood_group'].value_counts().plot.bar(color = "pink").set_title("Şehirlere göre dağılım")

#airbnb'lerin bulunduğu şehir ile fiyatları arasındaki ilişkiye bakalım

means_of_price = []
cities = ["Manhattan","Brooklyn","Queens","Bronx","Staten Island"]

Manhattan= df_abnb.where(df_abnb['neighbourhood_group']=="Manhattan")
Manmean= int(Manhattan["price"].mean())
means_of_price.append(Manmean)


Brooklyn= df_abnb.where(df_abnb['neighbourhood_group']=="Brooklyn")
Brookmean= int(Brooklyn["price"].mean())
means_of_price.append(Brookmean)


Queens = df_abnb.where(df_abnb['neighbourhood_group']=="Queens")
Queensmean= int(Queens["price"].mean())
means_of_price.append(Queensmean)


Bronx = df_abnb.where(df_abnb['neighbourhood_group']=="Bronx")
Bronxmean= int(Bronx["price"].mean())
means_of_price.append(Bronxmean)


Staten = df_abnb.where(df_abnb['neighbourhood_group']=="Staten Island")
Statenmean= int(Staten["price"].mean())
means_of_price.append(Statenmean)



sns.barplot(data=df_abnb,x=cities, y=means_of_price, palette = ['coral','pink', 'mediumpurple', 'wheat','paleturquoise'])
plt.title("Şehre Göre Ortalama Fiyat Değişimi")

sns.barplot(x="neighbourhood_group", y="price", hue="room_type", data=df_abnb,palette = ['coral','pink', 'mediumpurple'])
plt.title("City - Room Type - Price")

df_abnb.groupby("neighbourhood_group").sum().plot.pie(y='number_of_reviews',  autopct="%.1f%%", ylabel="", legend=False, figsize=(5,5),
                                                      title = "Şehirlere Göre Yorum Dağılışı",colors = ['red', 'pink', 'mediumpurple','lightcoral','firebrick'])