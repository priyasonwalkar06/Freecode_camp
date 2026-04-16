import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = df[higher_edu & (df['salary'] == '>50K')]
    higher_education_rich = round(
        (len(higher_edu_rich) / len(df[higher_edu])) * 100, 1
    )

    lower_edu = ~higher_edu
    lower_edu_rich = df[lower_edu & (df['salary'] == '>50K')]
    lower_education_rich = round(
        (len(lower_edu_rich) / len(df[lower_edu])) * 100, 1
    )

    min_work_hours = df['hours-per-week'].min()

    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = round(
        (len(rich_min_workers) / len(min_workers)) * 100, 1
    )

    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()

    country_percent = (country_salary / country_total) * 100
    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(country_percent.max(), 1)

    india_rich = df[
        (df['native-country'] == 'India') &
        (df['salary'] == '>50K')
    ]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("% with Bachelors:", percentage_bachelors)
        print("% with higher education earning >50K:", higher_education_rich)
        print("% without higher education earning >50K:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("% rich among min workers:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()