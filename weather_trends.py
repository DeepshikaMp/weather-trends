import pandas as pd

def load_data():
    '''Loading the temperate data to a data frame.
    Args:
        none.
    Returns:
        weather_data dataframe is returned.
    '''
    weather_data = pd.read_csv('Temperature.csv')
    print(weather_data)
    return weather_data

def main_stats():
    '''Exploring the weather trends by analysing local and global temperatures.
    Args:
        none.
    Returns:
        none.
    '''
    df = load_data()


if __name__ == "__main__":
	main_stats()
