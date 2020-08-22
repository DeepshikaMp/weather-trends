import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    '''Loading the temperate data to a data frame.
    Args:
        none.
    Returns:
        dataframe is returned.
    '''
    df = pd.read_csv('Temperature.csv')
    
    return df

def seven_year_rolling_average(df):
    '''Calculates 7 year rolling average window for global and city temperature.
    Args:
        Temperature dataframe.
    Returns:
        returns dataframe with global_average_temp, city_average_temp columns.
    '''
    df['g_seven_average_temp'] = df.iloc[:,1].rolling(window = 7).mean()
    df['c_seven_average_temp'] = df.iloc[:,3].rolling(window = 7).mean()

    return df

def ten_year_rolling_average(df):
    '''Calculates 10 year rolling average window for global and city temperature.
    Args:
        Temperature dataframe.
    Returns:
        returns dataframe with g_seven_average_temp, c_seven_average_temp.
    '''
    df['g_ten_average_temp'] = df.iloc[:,1].rolling(window = 10).mean()
    df['c_ten_average_temp'] = df.iloc[:,3].rolling(window = 10).mean()

    return df


def seven_year_line_chart(df):
    '''Comparing 7-year Global and Sydney Average Temperatures using line chart.
    Args:
        Temperature dataframe.
    Returns:
        none.
    '''
    plt.title('Comparing 7-year Global and Sydney Average Temperatures', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Temperature', fontsize=14)
    plt.plot( df['year'], df['g_seven_average_temp'], marker='', color='green', linewidth=2, linestyle='dashed', label="Global")
    plt.plot( df['year'], df['c_seven_average_temp'], marker='', color='blue', linewidth=2, label="Sydney")
    plt.grid(True)
    plt.legend()
    plt.show()


def ten_year_line_chart(df):
    '''Comparing 10-year Global and Sydney Average Temperatures using line chart.
    Args:
        Temperature dataframe.
    Returns:
        none.
    '''
    plt.title('Comparing 10-year Global and Sydney Average Temperatures', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Temperature', fontsize=14)
    plt.plot( df['year'], df['g_ten_average_temp'], marker='', color='green', linewidth=2, linestyle='dashed', label="Global")
    plt.plot( df['year'], df['c_ten_average_temp'], marker='', color='blue', linewidth=2, label="Sydney")
    plt.grid(True)
    plt.legend()
    plt.show()


def main_stats():
    '''Exploring the weather trends by analysing local and global temperatures.
    Args:
        none.
    Returns:
        none.
    '''
    df = load_data()
    seven_year_rolling_average(df)
    ten_year_rolling_average(df)
    print(df)
    seven_year_line_chart(df)
    ten_year_line_chart(df)


if __name__ == "__main__":
    main_stats()
