# Load CSV (using python)
import csv
import numpy as np
import pandas as pnd
import seaborn as sns
import json as jsn

def Full_time_job_after_bootcamp(dataFrame):
    g = sns.countplot(dataFrame[dataFrame.AttendedBootcamp == 1]['BootcampFullJobAfter'])
    g = g.set_xticklabels(["No","Yes"])
    sns.plt.title("Full-time job after Bootcamp?")
    sns.plt.show()

def Gender_Employment_Field(dataFrame):
    sns.countplot(x='Gender', hue='EmploymentField', data=dataFrame)
    sns.plt.show()

def Gender_School_Degree(dataFrame):
    sns.countplot(x='Gender', hue='SchoolDegree', data=dataFrame)
    sns.plt.show()

def Salary_Increase_After_bootcamp(dataFrame):

    name_sal_income_set = dataFrame[['BootcampName', 'BootcampPostSalary', 'Income']].dropna()

    name_sal_income_set = name_sal_income_set.groupby('BootcampName').sum()[['BootcampPostSalary', 'Income']]

    name_sal_income_set = pnd.DataFrame(
         ((name_sal_income_set['BootcampPostSalary'] - name_sal_income_set['Income']) / name_sal_income_set['Income']) * 100)


    name_sal_income_set.columns = ['Percentage_change_in_salary']

    name_sal_income_set = name_sal_income_set[name_sal_income_set.Percentage_change_in_salary > 0].sort_values(by='Percentage_change_in_salary',
                                                                                                        ascending=False)
    j = name_sal_income_set.to_json()

    print(j)

# plotting code starts
#     g = name_sal_income_set.plot.bar()
#     sns.plt.ylabel("Percentage change in salary")
#     sns.plt.title("Percentage change in salary after attending particular bootcamp")
#     g = g.set_xticklabels(g.get_xticklabels(), rotation=90)
#     sns.plt.show()

def Job_Preference(dataFrame):
    job_prefs_set = dataFrame[['JobPref', 'Gender']]
    sns.countplot(x='JobPref', hue='Gender', data=job_prefs_set)
    sns.plt.show()

def ResourceUsage(dataFrame):
    # Interesting to see what resources are popular among the successful developers?
    # Successful developers are those who got job after bootcamp :)

    tmp_set = dataFrame[dataFrame.BootcampFullJobAfter == 1][
        ['ResourceUdemy', 'ResourceUdacity', 'ResourceYouTube', 'ResourceW3Schools', 'ResourceStackOverflow',
         'ResourceTreehouse', 'ResourceReddit', 'ResourceKhanAcademy', 'ResourceLynda', 'ResourceCodeWars',
         'ResourceBlogs','ResourceBooks', 'ResourceCodecademy', 'ResourceCoursera', 'ResourceDevTips', 'ResourceEdX',
         'ResourceEggHead', 'ResourceFCC', 'ResourceGoogle', 'ResourceHackerRank', 'ResourceMDN', 'ResourceOdinProj',
         'ResourceOther', 'ResourcePluralSight', 'ResourceSkillCrush', 'ResourceSoloLearn']].dropna(how='all')

    tmp_set = tmp_set.count() # counts non-NA values in each column in the given set
    tmp_set.columns = ['Resource', 'Count'] # name the columns in tmp set
    tmp_set = tmp_set.sort_values(ascending=False) #sort in the decreasing order of count for a nice graph

    j = tmp_set.to_json()
    print(j)

    # plot
    tmp_set.plot.bar(x='Resource', y='Count')
    sns.plt.show()

def Age_PostCamp_Salary_Relation(dataFrame):
    tmp_set = dataFrame[['Age', 'BootcampPostSalary']].dropna()
    g = tmp_set.plot(kind='scatter', x='Age', y='BootcampPostSalary')
    sns.plt.show()

def Experience_PostCamp_Salary_Relation(dataFrame):
    experience_postCamp_salary_set = dataFrame[['MonthsProgramming', 'BootcampPostSalary']].dropna()
    g = experience_postCamp_salary_set.plot(kind='scatter', x='MonthsProgramming', y='BootcampPostSalary')
    sns.plt.show()

def Main():
    filename = "G:\\Subhash\\Madhuri\\Kaggle\\2016-new-coder-survey-\\2016-FCC-New-Coders-Survey-Data.csv"

    dataFrame = pnd.read_csv(filename, quotechar='"', dtype=None, delimiter=',', skipinitialspace=True, thousands=',',  low_memory=False )

    #import matplotlib.pyplot as pltLib
    #pltLib.scatter(dataFrame['Age'], dataFrame['BootcampPostSalary'])
    #pltLib.scatter(dataFrame['CodeEventBootcamp'], dataFrame['BootcampPostSalary'])
    #pltLib.scatter(dataFrame['MonthsProgramming'], dataFrame['BootcampPostSalary'])
    #pltLib.show()


    #Gender_Employment_Field(dataFrame)

    #Gender_School_Degree(dataFrame)

    #Full_time_job_after_bootcamp(dataFrame)

    #Salary_Increase_After_bootcamp(dataFrame)

    #Job_Interest(dataFrame)

    # Job_Preference(dataFrame)

    #Age_PostCamp_Salary_Relation(dataFrame)
#   #Experience_PostCamp_Salary_Relation(dataFrame)

    #ResourceUsage(dataFrame);


    #sns.plt.show()

# Execute main function
Main()