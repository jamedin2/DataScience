"""
Simple HR Data Analysis - Starter Project
==========================================
This is a beginner-friendly script that demonstrates basic data analysis
using Python and pandas.

Run with: python simple_analysis.py
"""

import pandas as pd


def load_data(filepath):
    """Load the HR dataset from a CSV file."""
    print("Loading data...")
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} employee records\n")
    return df


def show_basic_info(df):
    """Display basic information about the dataset."""
    print("=" * 50)
    print("DATASET OVERVIEW")
    print("=" * 50)
    print(f"Number of employees: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
    print(f"\nColumn names:")
    for col in df.columns:
        print(f"  - {col}")
    print()


def show_attrition_stats(df):
    """Show employee attrition statistics."""
    print("=" * 50)
    print("ATTRITION STATISTICS")
    print("=" * 50)

    if 'Attrition' in df.columns:
        attrition_counts = df['Attrition'].value_counts()
        total = len(df)

        print("\nAttrition breakdown:")
        for status, count in attrition_counts.items():
            percentage = (count / total) * 100
            print(f"  {status}: {count} employees ({percentage:.1f}%)")
    else:
        print("No 'Attrition' column found in dataset")
    print()


def show_salary_stats(df):
    """Show salary-related statistics."""
    print("=" * 50)
    print("SALARY STATISTICS")
    print("=" * 50)

    salary_col = None
    for col in ['MonthlyIncome', 'Salary', 'Income']:
        if col in df.columns:
            salary_col = col
            break

    if salary_col:
        print(f"\n{salary_col} Statistics:")
        print(f"  Average: ${df[salary_col].mean():,.2f}")
        print(f"  Minimum: ${df[salary_col].min():,.2f}")
        print(f"  Maximum: ${df[salary_col].max():,.2f}")
        print(f"  Median:  ${df[salary_col].median():,.2f}")
    else:
        print("No salary column found in dataset")
    print()


def show_department_breakdown(df):
    """Show breakdown by department."""
    print("=" * 50)
    print("DEPARTMENT BREAKDOWN")
    print("=" * 50)

    if 'Department' in df.columns:
        dept_counts = df['Department'].value_counts()
        print("\nEmployees by department:")
        for dept, count in dept_counts.items():
            print(f"  {dept}: {count}")
    else:
        print("No 'Department' column found in dataset")
    print()


def main():
    """Main function to run the analysis."""
    print("\n" + "=" * 50)
    print("  SIMPLE HR DATA ANALYSIS")
    print("  Your First Data Science Project!")
    print("=" * 50 + "\n")

    # Load the data
    df = load_data("HR Employee Attrition.csv")

    # Run analysis functions
    show_basic_info(df)
    show_attrition_stats(df)
    show_salary_stats(df)
    show_department_breakdown(df)

    print("=" * 50)
    print("Analysis complete!")
    print("=" * 50)
    print("\nNext steps you can try:")
    print("  1. Add more analysis functions")
    print("  2. Create visualizations with matplotlib")
    print("  3. Build a predictive model")
    print()


if __name__ == "__main__":
    main()
