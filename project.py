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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input(
            "Can you please select the city you want to see statistics for ? Valid options (chicago,new york city,washington) : ")
        if city not in ('chicago','new york city','washington'):
            print("that was not a correct soultion")
            continue
        else:
            print('i see you choose :',city.title())
            break
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Which month would you like to see? : Valid Options (january,february,....) or all : ")
        if month not in ('january','february','march','april','may','june','july','august','september','october','november','december','all'):
            print("Sorry not sure what month is that")
            continue
        else:
            print('Great Choice :' ,month.title())
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("which day would you like to see? : Valid Options (monday,sunday,tuesday,wednesda',thursday,friday,saturday) or all : ")
        if day not in ('monday','sunday','tuesday','wednesday','thursday','friday','saturday','all'):
            print("are you sure its the correct day")
            continue
        else:
            print('Ok you choose that day :',day.title())
            break
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
    df['hour'] = df['Start Time'].dt.hour
    df['Month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    print(df.head(1))
    if month != 'all':
        df = df[df['Month'] == month.title()]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    print('most common month is',popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('most common day is', popular_day)
    # TO DO: display the most common start hour
    popular_start = df['hour'].mode()[0]
    print('most common Start Time is', popular_start)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('most common Start station is', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('most common End station is', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end = df[['Start Station', 'End Station']].mode().loc[0]
    print('most common station is\n', popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Duration Time is : %s seconds" % (sum(df['Trip Duration'])))

    # TO DO: display mean travel time
    print("Average Trip Duration Time is :" , df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Types Are\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('Genders Breakdown\n',df['Gender'].value_counts())
    except:
        print('Gender Column not found in sheet')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('Earliest Birth Year would be:',df['Birth Year'].min())
    except:
        print('Birth YearColumn not found in sheet')
    try:
        print('Most Recent Birth Year would be:',df['Birth Year'].max())
    except:
        print('Birth YearColumn not found in sheet')
    try:
        most_common_year = df['Birth Year'].mode()[0]
        print("Most Common Year is ",most_common_year)
    except:
        print('Birth Year column not found in sheet')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
