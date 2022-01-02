import time
import pandas as pd
import numpy as np
import calendar 

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
        cities= ['chicago','new york city','washington']
        city= input('\nPlease choose the following cities: Chicago, New york city, Washington \n').lower()
        if city in cities:
            break
        else:
            print("\n Invalid city name. Please choose a valid city name") 


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months= ['january','february','march','april','may','june','all'] 
        month= input('\nPlease select the month between January to June or type all if you want to select all months \n').lower()
        if month in months:
            break
        else:
            print("\n Invalid month selected. Please select the correct month or type all if you want select all months") 
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
         days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
         day= input("\nPlease select the day of week you want to display or type all if you want to select all days \n").lower()
         if day in days:
            break
         else:
            print("\n Invalid day of week selected. Please select the correct day or type all if you want select all days of week") 


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
    #Load city data file into data frame
    df = pd.read_csv(CITY_DATA[city])
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
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
    common_month = df['month'].mode()[0]
    print('The most common month is',calendar.month_name[common_month]) 

    # TO DO: display the most common day of week
    common_dow = df['day_of_week'].mode()[0]
    print('The most common day of week is', common_dow)

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour #extract hour from the start time column 
    common_sh = df['Start Hour'].mode()[0]
    print('The most common start hour is', common_sh)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_ss = df['Start Station'].mode()[0]
    print('The most common start station is', common_ss)

    # TO DO: display most commonly used end station
    common_es = df['End Station'].mode()[0]
    print('The most common end station is', common_es)

    # TO DO: display most frequent combination of start station and end station trip
    combination_stations = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('The most frequent combination start and end stations is from', combination_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute,second=divmod(total_travel_time,60)
    hour,minute=divmod(minute,60)

    print ('The total travel time is {} hours {} minutes {} seconds'.format(hour,minute,second))

    # TO DO: display mean travel time
    mean_time = round(df['Trip Duration'].mean())
    minute,second = divmod(mean_time, 60)
    if minute>60:
        hour,minute = divmod(minute, 60)
        print('The average travel time is {} hours {} minutes {} seconds'.format(hour,minute,second))
    else:
        print ('The average travel time is {} minutes {} seconds'.format(minute,second))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('The total type of users are\n',count_user_type)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('\nUser by gender are\n',gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        oldest = int(df['Birth Year'].min())
        print('\nThe oldest year of birth is', oldest)
        
        youngest = int(df['Birth Year'].max())
        print('The youngest year of birth is', youngest)
        
        most_common = df['Birth Year'].mode()[0]
        print('Most users are born in', most_common)
           
    else:
        print('\n User gender and year of birth are not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    a=0
    answer = input('Please type "Yes" if you would like to view the first 5 lists of data\n').lower()
    while True:
        if answer == 'no':
            break
        print(df[a:a+5])
        answer = input('Please type "Yes"if you would like to view the next 5 entries of data\n').lower()
        a=+5
                
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
