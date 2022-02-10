import pandas as pd

def calculate_demographic_data(print_data = True):
    precision = 1
    # Read data from file
    df = pd.read_csv("./adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df\
        .groupby(by = "race", as_index = True, sort = False)\
        .count()["age"]\
        .round(decimals = precision)
    # What is the average age of men?
    average_age_men = df\
        .groupby("sex")\
        .get_group("Male")\
        .mean()["age"]\
        .round(decimals = precision)

    # What is the percentage of people who have a Bachelor's degree?
    have_bacharelor = df\
        .groupby("education")\
        .get_group("Bachelors")\
        .count()["age"]
    total = df.shape[0]
    percentage_bachelors = round(100 * have_bacharelor / total, precision)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    test_advanced = (
            (df["education"] == "Bachelors") |\
            (df["education"] == "Masters") |\
            (df["education"] == "Doctorate")
    )
    test_salary = (df["salary"] == ">50K")

    higher_education = df[test_advanced].shape[0]
    lower_education = df[-test_advanced].shape[0]

    # percentage with salary >50K
    higher_education_rich = round(100 * df[test_advanced & test_salary].shape[0] / higher_education, precision)
    lower_education_rich = round(100 * df[-test_advanced & test_salary].shape[0] / lower_education, precision)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    test_min_hours = (df["hours-per-week"] == min_work_hours)
    num_min_workers = df[test_min_hours].shape[0]

    rich_percentage = round(100 * df[test_min_hours & test_salary].shape[0] / num_min_workers, precision)

    # What country has the highest percentage of people that earn >50K?
    country_pop = df\
        .groupby("native-country")\
        .count()["salary"]
    rich_country_pop = df[test_salary]\
        .groupby("native-country")\
        .count()["salary"]
    country_rich_percent = rich_country_pop / country_pop

    highest_earning_country = country_rich_percent\
        .sort_values(ascending = False)\
        .index[0]
    highest_earning_country_percentage = round(100 * country_rich_percent\
        .sort_values(ascending = False)\
        .values[0], precision)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[test_salary & (df["native-country"] == "India")]\
        .groupby("occupation")\
        .count()["salary"]\
        .sort_values(ascending = False)\
        .index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_educaion_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

