import pandas as pd
import seaborn as naman
import matplotlib.pyplot as plt
import numpy as np
# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

#3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['id','age','sex','height', 'weight','ap_hi','ap_lo','cardio'],var_name='variable', value_name='Value')

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'Value']).size().reset_index(name='total')   #reset index to convert to df

    # 7,8

    fig=naman.catplot(data=df_cat,hue='Value',y='total',x='variable',kind="bar",col='cardio')

    # 9
    plt.savefig('catplot.png')
    plt.close()
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))&(df['weight'] >= df['weight'].quantile(0.025))& (df['weight'] <= df['weight'].quantile(0.975))]
    
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14,15
    plt.figure(figsize=(12, 10))
    fig = naman.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt=".1f")


    # 16
    plt.savefig('heatmap.png')
    plt.close()
    return fig.get_figure()

