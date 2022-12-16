import time
import pandas as pd
import numpy as np
import json


#here is the city data you can add another city here if you have the data
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("which city do you want to explore").lower()
        if city in CITY_DATA.keys():
            break

     # TO DO: get user input for month (all, january, february, ... , june)
    month =input("what is the month name and you can write all for all month").lower()
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =input("what is the day name and you can write all for all days").lower()


    print('-' * 40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month = month.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].value_counts().idxmax()
    print(f"The most common month is :{most_month}")
    # TO DO: display the most common day of week
    most_day_of_week = df['day_of_week'].value_counts().idxmax()
    print(f"The most common day of week is :{most_day_of_week}")
    # TO DO: display the most common start hour
    most_start_hour = df['hour'].value_counts().idxmax()
    print(f"The most common start hour is :{most_start_hour}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_statinon = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_start_statinon)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print(f"The most commonly used start station and end station : {most_start_end_station[0]}, {most_start_end_station[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print(f"Total travel time :{travel_time}")

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print(f"Mean travel time :{mean}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("number of user types:\n")
    user_typeNum = df['User Type'].value_counts()
    for index, user_typeNum in enumerate(user_typeNum):
        print(f"  {user_typeNum.index[index]}: {user_typeNum}")

    # TO DO: Display counts of gender
    print("number of gender:\n")
    gender_number = df['Gender'].value_counts()
    # iteratively print out the total numbers of genders
    for index, gender_count in enumerate(gender_number):
        print(f"  {gender_number.index[index]}: {gender_count}")

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    # the most common birth year
    common_year = birth_year.value_counts().idxmax()
    print("The most hcommon birth year:", common_year)
    #     # the most recent birt year
    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)
    # the most earliest birth year
    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    #the main function to test the functions in the project.
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        start_loc = 0
        bol=True
        while (True):
            print(df.iloc[:5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            if view_display.lower()!='yes':
                bol=False

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
