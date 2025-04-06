from src import data_cleaning, analysis, visualization
import os

def main():
    # Path to the raw data Excel file
    raw_data_path = os.path.join('data', 'raw', 'Litholink.xlsx')
    
    # Load the Excel file (all sheets)
    sheets = data_cleaning.load_excel_data(raw_data_path)
    
    # Clean the individual sheets
    litholink_df = data_cleaning.clean_litholink_main(sheets['Litholink_main'])
    variability_df = data_cleaning.clean_variability_study(sheets['Variability Study'])
    
    # Save the processed data as CSV files
    data_cleaning.save_processed_data(litholink_df, 'litholink_clean.csv')
    data_cleaning.save_processed_data(variability_df, 'variability_clean.csv')
    
    # Run analyses
    impact_results = analysis.analyze_stone_and_ph_impact(litholink_df)
    variability_results = analysis.analyze_variability(variability_df)
    
    print("Impact Analysis Results:")
    print(impact_results)
    print("\nVariability Analysis Results:")
    print(variability_results)
    
    # Generate plots (ensure the 'plots' directory exists)
    os.makedirs('plots', exist_ok=True)
    visualization.plot_variable_distribution(litholink_df, 'Ca24')
    visualization.plot_variability(variability_df, 'pH')
    
if __name__ == '__main__':
    main()
