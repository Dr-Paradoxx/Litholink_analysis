import pandas as pd
import scipy.stats as stats

def analyze_stone_and_ph_impact(df: pd.DataFrame) -> dict:
    """
    Performs analysis to assess the impact of Stone Category and pH category
    on variables: Ca24, SSCaP, Ca24kg, Ca24Cr24, Cit24, and Serum_Ca.
    Returns a dictionary of statistical test results.
    """
    results = {}
    variables = ['Ca24', 'SSCaP', 'Ca24kg', 'Ca24Cr24', 'Cit24', 'Serum_Ca']
    for var in variables:
        groups = [group[var].values for name, group in df.groupby(['Stone_Category', 'pH_category'])]
        stat, pvalue = stats.kruskal(*groups)
        results[var] = {'statistic': stat, 'p-value': pvalue}
    return results

def analyze_variability(df: pd.DataFrame) -> dict:
    """
    Evaluates variability for same day sample pairs by stone category.
    Performs paired comparisons or computes variation metrics for variables:
    Ca24, SSCaP, Ca24kg, Ca24Cr24, Cit24, Serum_Ca, and pH.
    """
    variability_results = {}
    variables = ['Ca24', 'SSCaP', 'Ca24kg', 'Ca24Cr24', 'Cit24', 'Serum_Ca', 'pH']
    for var in variables:
        variability = df.groupby('Stone_Category')[var].std()
        variability_results[var] = variability.to_dict()
    return variability_results
