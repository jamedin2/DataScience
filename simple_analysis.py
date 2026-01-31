"""
Simple HR Data Analysis - Starter Project
==========================================
This is a beginner-friendly script that demonstrates basic data analysis
using Python and pandas, with visualizations.

Run with: python simple_analysis.py
"""

import pandas as pd
import matplotlib.pyplot as plt


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


def create_visualizations(df):
    """Create and save visualizations of the HR data."""
    print("=" * 50)
    print("CREATING VISUALIZATIONS")
    print("=" * 50)

    # Create a figure with 4 subplots (2x2 grid)
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('HR Employee Analysis Dashboard', fontsize=16, fontweight='bold')

    # 1. Attrition Pie Chart (top-left)
    if 'Attrition' in df.columns:
        attrition_counts = df['Attrition'].value_counts()
        colors = ['#2ecc71', '#e74c3c']  # Green for No, Red for Yes
        axes[0, 0].pie(attrition_counts, labels=attrition_counts.index,
                       autopct='%1.1f%%', colors=colors, startangle=90)
        axes[0, 0].set_title('Employee Attrition')

    # 2. Department Bar Chart (top-right)
    if 'Department' in df.columns:
        dept_counts = df['Department'].value_counts()
        bars = axes[0, 1].bar(dept_counts.index, dept_counts.values, color='#3498db')
        axes[0, 1].set_title('Employees by Department')
        axes[0, 1].set_ylabel('Number of Employees')
        axes[0, 1].tick_params(axis='x', rotation=15)
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            axes[0, 1].text(bar.get_x() + bar.get_width()/2., height,
                           f'{int(height)}', ha='center', va='bottom')

    # 3. Salary Distribution Histogram (bottom-left)
    if 'MonthlyIncome' in df.columns:
        axes[1, 0].hist(df['MonthlyIncome'], bins=30, color='#9b59b6', edgecolor='white')
        axes[1, 0].set_title('Monthly Income Distribution')
        axes[1, 0].set_xlabel('Monthly Income ($)')
        axes[1, 0].set_ylabel('Number of Employees')
        axes[1, 0].axvline(df['MonthlyIncome'].mean(), color='red',
                          linestyle='--', label=f"Mean: ${df['MonthlyIncome'].mean():,.0f}")
        axes[1, 0].legend()

    # 4. Age Distribution (bottom-right)
    if 'Age' in df.columns:
        axes[1, 1].hist(df['Age'], bins=20, color='#f39c12', edgecolor='white')
        axes[1, 1].set_title('Age Distribution')
        axes[1, 1].set_xlabel('Age')
        axes[1, 1].set_ylabel('Number of Employees')
        axes[1, 1].axvline(df['Age'].mean(), color='red',
                          linestyle='--', label=f"Mean: {df['Age'].mean():.0f} years")
        axes[1, 1].legend()

    # Adjust layout and save
    plt.tight_layout()
    output_file = 'hr_analysis_dashboard.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nVisualization saved to: {output_file}")
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

    # Create visualizations
    create_visualizations(df)

    print("=" * 50)
    print("Analysis complete!")
    print("=" * 50)
    print("\nNext steps you can try:")
    print("  1. Add more analysis functions")
    print("  2. Build a predictive model")
    print("  3. Explore correlations between features")
    print()


if __name__ == "__main__":
    main()
