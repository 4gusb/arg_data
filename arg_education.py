import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CONNECTION
try:
    conn = mysql.connector.connect(user="", password="",
                                    host= "", 
                                    database="",
                                    port="")
    print("MySQL Database connection successful")
except:
    print("Error")


# -------PROCESSED VALUES--------

df_2016 = pd.read_sql("SELECT ldesemp, mdesemp, isocioa\
                        FROM aprender2016", conn)




#  GET AVG FROM SPANISH AND MATH GRADES AND SOCIOECONOMIC INDEX. 
# From column replace empty values, then convert all to integers to finally get their mean.


# 2016 VALUES

m_avg_2016 = ((df_2016['mdesemp'].replace(' ', 0)).astype(int)).mean() 
# print(m_avg_2016)

l_avg_2016 = ((df_2016['ldesemp'].replace(' ', 0)).astype(int)).mean() 
# print(l_avg_2016)

i_avg_2016 = ((df_2016['isocioa'].replace(' ', 0)).astype(int)).mean() 
# print(i_avg_2016)



# 2018 VALUES

df_2018 = pd.read_sql("select ldesemp, mdesemp, isocioa\
                       FROM aprender2018", conn)
# print(df_2018.head())

m_avg_2018 = ((df_2018['mdesemp'].replace(' ', 0)).astype(int)).mean() 
# print(m_avg_2018)

l_avg_2018 = ((df_2018['ldesemp'].replace(' ', 0)).astype(int)).mean() 
# print(l_avg_2018)

i_avg_2018 = ((df_2018['isocioa'].replace(' ', 0)).astype(int)).mean() 
# print(i_avg_2018)



# 2021 VALUES
df_2021 = pd.read_sql("select ldesemp, mdesemp, NSE_puntaje\
                       FROM aprender2021", conn)
# print(df_2021.head())

m_avg_2021 = ((df_2021['mdesemp'].replace(' ', 0)).astype(int)).mean() 
# print(m_avg_2021)

l_avg_2021 = ((df_2021['ldesemp'].replace(' ', 0)).astype(int)).mean() 
# print(l_avg_2021)

i_avg_2021 = (((df_2021['NSE_puntaje'].replace(' ', 0)).str.replace(',', '.')).astype(float)).mean() 
# print(i_avg_2021)




# PLOT PER VALUE YEARS

# ------PLOT INFO-------

categories = ["ldesemp", "mdesemp", "isocioa"]
values_2016 = [m_avg_2016, l_avg_2016, i_avg_2016]
values_2018 = [m_avg_2018, l_avg_2018, i_avg_2018]
values_2021 = [m_avg_2021, l_avg_2021, i_avg_2021]

width = 0.2
xpos = np.arange(len(categories))


# ------PLOT-------


plt.bar(xpos, values_2016, width, color="#11009E", label = '2016')
plt.bar(xpos + 0.2, values_2018, width, color="#3498DB", label = '2018')
plt.bar(xpos + 0.4, values_2021, width, color="#F1C40F", label = '2021')
plt.xticks(range(len(categories)), ['SPANISH LEVEL', 'MATHS LEVEL', 'SOCIOEC INDEX'])
plt.ylim(0, max((max(values_2016)),(max(values_2018)),(max(values_2021))) + 1)
plt.legend()
plt.show()



# PLOT PER VARIABLES

# ------PLOT INFO-------

categories = ["2016", "2018", "2021"]
values_mdesemp = [m_avg_2016, m_avg_2018, m_avg_2021]
values_ldesemp = [l_avg_2021, l_avg_2021, l_avg_2021]
values_isocioa = [i_avg_2016, i_avg_2018, i_avg_2021]

width = 0.2
xpos = np.arange(len(categories))


# ------PLOT-------


plt.bar(xpos, values_mdesemp, width, color="#11009E", label = 'MATHS LEVEL')
plt.bar(xpos + 0.2, values_ldesemp, width, color="#3498DB", label = 'SPANISH LEVEL')
plt.bar(xpos + 0.4, values_isocioa, width, color="#F1C40F", label = 'SOCIOEC INDEX')
plt.ylim(0, max((max(values_ldesemp)),(max(values_isocioa)),(max(values_mdesemp))) + 1)
plt.xticks(range(len(categories)), categories)
plt.legend()
plt.show()

--
