import pandas as pd

df = pd.read_csv("final_college_student_placement_dataset.csv")

'''1. Categorize placed students into salary bands:
    Low: < 300,000
    Medium: 300,000 – 600,000
    High: > 600,000'''
    
df['salary_band'] = df.apply(lambda x: 'Low' if x['Placement'] == 'Yes' and x['Salary'] < 300000 else (
    'Medium' if x['Placement'] == 'Yes' and x['Salary'] <= 600000 else (
    'High' if x['Placement'] == 'Yes' and x['Salary'] > 600000 else None)), axis=1)

print(df[['Placement', 'Salary', 'salary_band']].head(10))


'''2. For each gender and specialization, calculate:
    Placement rate
    Average salary (only placed)
    Avg MBA score'''
    
print(df.groupby(['Gender','Specialization']).agg(Placement_rate=('Placement',lambda x:(x=='yes').mean()),
                                                  Average_salary=('Salary',lambda x: x[df['Placement']=='Yes'].mean()),
                                                  Avg_MBA_score=('MBA_Percentage', lambda x: x.mean())
                                                  ))   

        
        
'''3.Find how many students have missing values in any column.'''
print(df.isnull().sum())
print(df[df.isnull().any(axis=1)])
print(df.isnull().any(axis=1).sum())

'''4. Display all rows where salary is missing.'''
print(df[df['Salary'].isnull()])

'''5. Filter only students with complete records (no missing values).'''
print(df.dropna())

'''6. Identify if there are any duplicate student entries'''
print(df.duplicated().any())

'''7. Drop the duplicate records and keep only the first occurrence.'''
df_no_duplicates = df.drop_duplicates(keep='first')
print(df_no_duplicates)

'''8. Check for duplicates based only on student_id.'''
print(df[df.duplicated(subset='College_ID', keep=False)])

'''9.Find all unique specializations offered to students.'''
print(df['Specialization'].unique())

'''10. How many unique MBA scores are there?'''
print(df['MBA_Percentage'].nunique())

'''11. Count of unique combinations of gender, specialization, and status.'''
print(df[['Gender', 'Specialization', 'Placement']].drop_duplicates().shape[0])

'''12. What is the average salary of all placed students?'''
print(df[df['Placement'] == 'Yes']['Salary'].mean())

'''13. What is the maximum and minimum degree percentage in the dataset?'''
print(df['CGPA'].max(), df['CGPA'].min())

'''14. Get total number of placed and unplaced students.'''
print(df['Placement'].value_counts())

'''15.For each specialization, calculate:
    Average SSC
    Average MBA
    Placement count'''
print(df.groupby('Academic_Performance').agg(avg_ssc=('SSC_Percentage', 'mean'),avg_mba=('MBA_Percentage', 'mean'),placed_count=('Placement', lambda x: (x == 'Yes').sum())))    
    

'''16. Create a summary table with:
    Column name
    Count of nulls
    Count of unique values
    Duplicated value count (if applicable)'''
summary_table = pd.DataFrame({
    'Column': df.columns,
    'Null_Count': df.isnull().sum().values,
    'Unique_Count': df.nunique().values,
    'Duplicate_Count': [df.duplicated(subset=col).sum() if df[col].duplicated().any() else 0 for col in df.columns]
})
print(summary_table)


#==================================================================================================================================================================================



import pandas as pd

df = pd.read_csv("updated_college_student_placement_dataset.csv")

#1. How many students are in the dataset?
#print(len(df))
#print(len(df['College_ID']))
#print(df.shape[0])
 
 
#2.Display the number of male and female students.
#gender_count = df['Gender'].value_counts()
#print(gender_count)

#3.What is the average percentage in MBA?
#print(df['MBA_Percentage'].mean())

#4.Show students who scored more than 80% in both SSC and HSC.
#print((df['SSC_Percentage']>80) & (df['HSC_Percentage']))

#5.Filter only students who have prior work experience.

#6. Average MBA score per specialization.

#7. Count of placed vs not placed students.

#8.Placement ratio per specialization.

#9. Create a new column placement_success with:

#    "High" if placed and salary > ₹950,000

#    "Average" if placed and salary <= ₹400,000

#    "Unplaced" if not placed

#10. Among placed students, which degree percentage range leads to highest average salary?
 
