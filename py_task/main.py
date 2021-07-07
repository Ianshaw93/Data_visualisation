import pandas as pd
import json
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import seaborn as sns
plt.interactive(False)

#step 1: create a function which reads a csv and transforms into a dataframe
def create_dataframe(data_csv):
    df_all = pd.read_csv(data_csv)
    return df_all

def manipulate_dataframe(df_all):
    # cut columns not needed for json data
    df = df_all.drop(columns = ['user_id', 'log_id', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8'])
    # create dictionary for emotion occurence within dataframe
    emotion_occurence = df['emotion'].value_counts()
    # remove duplicate rows
    df.drop_duplicates(inplace=True)
    # add in occurence column 'log_count' into dataframe -
    # mapping key of dictionary to emotion column of dataframe
    df['log_count'] = df['emotion'].map(emotion_occurence)
    return df

def remove_outliers_inter_quantile_range(df):
    # as noted in read_me file this was not used for the final figures
    # arrange dataset in increasing order #*later pass in log_count
    df = df.sort_values(by=['log_count'], ascending=True)
    # print(sorted_df)
    # Calculate first and third quantiles
    quantile1, quantile3 = np.percentile(df['log_count'], [25, 75])
    # Find interquantile range
    iqr_value = quantile3 - quantile1
    # Find lower bound q1*1.5
    lower_bound_val = quantile1 - (1.5 * iqr_value)
    # Find upper bound q3*1.5
    upper_bound_val = quantile3 + (1.5 * iqr_value)
    # df = df.drop(df[(df.log_count < lower_bound_val) and (df.log_count > upper_bound_val)].index)
    df2 = df.drop(df[(df.log_count > upper_bound_val)].index) # not sure why line above does not work
    # print(df)
    return df2

def csv_to_json(df):
    # convert data to json format (using 'record' that removes index)
    df_json = (df.to_json(orient="records"))
    return df_json

def scatter_plot(df):
    circle_area = df['log_count']
    plt.scatter((df['X']), (df['Y']),
                c='green', edgecolor='black',
                s = 10*circle_area , linewidth=1,
                alpha= 0.5
                )
    plt.show()

def scatter_plot2(df):
    # sort into different occurrences i.e. log_count
    fig, ax = plt.subplots(figsize=(12, 8))
    df = df.sort_values(by=['log_count'], ascending=True)
    log_count_unique_values = set(df['log_count'])
    # split into dictionaries per occurrence
    log_count_dict = dict(tuple(df.groupby('log_count')))
    print(log_count_dict)
    x_mean = []
    y_mean = []
    num_emotions = []
    for i in log_count_unique_values:
        # log_count_unique_values as above
        x_mean.append(np.mean(log_count_dict[i]['X']))
        y_mean.append(np.mean(log_count_dict[i]['Y']))
        num_emotions.append(len((log_count_dict[i]['X'])))


    circle_area = np.array(num_emotions)
    color = 'green'
    # # cmap = mpl.cm.cool
    cmap = cm.get_cmap('Greens', 128)
    # lightness used for opacity
    lightness = [ value/162 for value in log_count_unique_values]
    log_count_value = [value for value in log_count_unique_values]
    rgb = sns.set_hls_values(color=color, h=None, l=lightness, s=0)


    # first scatter used for outline with alpha=1 of circles;
    # second scatter for fill with alpha depending on number of emotions
    scatter1 = plt.scatter((x_mean), (y_mean),
                c='white', edgecolor='black',
                s=10*circle_area, linewidth=1,
                alpha=0.25
                )

    scatter2 = plt.scatter((x_mean), (y_mean),
                c=color, edgecolor='black',
                s = 10*circle_area, linewidth=1,
                alpha= 10000*lightness, label=num_emotions
                )

    plt.title("Mean Co-ordinate Bubble Chart")
    plt.xlabel("x-mean")
    plt.ylabel("y-mean")
    handles, labels = scatter1.legend_elements(prop='sizes', alpha=0.2, num=len(num_emotions_set))
    plt.legend(handles, labels, loc=(.7, 0.1), title='Number of emotions Times 10');
    plt.show()

def histrogram(df):
    fig, ax = plt.subplots()
    ax.bar(df['X'], df['log_count'], width=0.1, edgecolor='black', label='x')
    ax.bar(df['Y'], df['log_count'], width=0.1, alpha=0.3, edgecolor='black', label='y')
    ax.set_ylabel("Frequency", fontsize=16)
    plt.legend(title="Emotion Co-ordinates")
    plt.show()


all_data_csv = 'anonoymous_data.csv'

df_all = create_dataframe(all_data_csv)
df = manipulate_dataframe(df_all)

# final graphs
scatter_plot2(df)
histrogram(df)

# Original Scatter plot
# scatter_plot(df)
