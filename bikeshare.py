import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('enter the city that you want to analays : chicago, new york city or washington? \n> ').lower()
        if city in cities:
            break

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = input('enter the month that you want to analays \n> {} \n> '.format( months )).lower()


    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = input('enter the day that you want to analays \n> {} \n> '.format( days )).lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    df['hour'] = df['Start Time'].dt.hour


    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print("The most common month is :", common_month)

    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most  common day of week is :", common_day_of_week)

    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is :", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station :", common_start_station)

    common_end_station = df['End Station'].mode()[0]
    
    print("The most common end station :", common_end_station)

    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most frequent combination of start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print(df['User Type'].value_counts())

    if city != 'washington':
        print(df['Gender'].value_counts())
        print(df['Birth Year'].min())
        print(df['Birth Year'].max())
        print(df['Birth Year'].mode()[0])
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    row = 0
    while True:
        viewdata = input("Would you like to see the raw data? Type 'yes' or 'no'.").lower()
        if viewdata == 'yes': 
            row += 1
            print(df.iloc[(row-1)*5:row*5])
        elif viewdata == 'no':
            return
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)



        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()