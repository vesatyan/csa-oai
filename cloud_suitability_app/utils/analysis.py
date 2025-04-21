
import pandas as pd
from .llm_logic import get_llm_reasoning
from .ml_logic import get_strategy_prediction, calculate_cost_score

def analyze_data(df):
    # ML-based strategy recommendation
    df['Migration Strategy'] = df.apply(get_strategy_prediction, axis=1)
    # Cost and OS compatibility analysis
    df['OS Cost Score'] = df.apply(calculate_cost_score, axis=1)
    # LLM-based reasoning
    df['LLM Reasoning'] = df.apply(get_llm_reasoning, axis=1)

    result_html = df.to_html()
    output_path = '/tmp/output.xlsx'
    df.to_excel(output_path, index=False)

    return result_html, output_path
