import yaml
import pandas as pd
import numpy as np
from datetime import datetime
import re



class ExcelFormulaEvaluator:
    def __init__(self, df):
        self.df = df
        self.current_row = 0
        
    def get_rc_value(self, col_offset):
        """Get value from relative column reference"""
        try:
            current_col = self.current_col_idx + col_offset
            if current_col >= 0 and current_col < len(self.df.columns):
                return self.df.iloc[self.current_row, current_col]
            return 0
        except:
            return 0
    
    def iferror(self, try_value, error_value):
        """Implement Excel's IFERROR function"""
        try:
            result = try_value() if callable(try_value) else try_value
            return result if pd.notna(result) else error_value
        except:
            return error_value

    def find(self, find_text, within_text, start_num=1):
        """Implement Excel's FIND function"""
        try:
            if pd.isna(within_text) or pd.isna(find_text):
                return 0
            within_text = str(within_text)
            find_text = str(find_text)
            return within_text.index(find_text, start_num - 1) + 1
        except:
            return 0

    def mid(self, text, start_num, num_chars):
        """Implement Excel's MID function"""
        try:
            if pd.isna(text) or pd.isna(start_num) or pd.isna(num_chars):
                return ""
            text = str(text)
            start_num = int(start_num)
            num_chars = int(num_chars)
            return text[start_num-1:start_num-1+num_chars]
        except:
            return ""

    def evaluate_formula_for_cell(self, formula, row_idx, col_idx):
        """Evaluate Excel formula for specific cell"""
        self.current_row = row_idx
        self.current_col_idx = col_idx
        
        # Replace relative cell references
        def replace_rc(match):
            offset = int(match.group(1)) if match.group(1) else 0
            return str(self.get_rc_value(offset))
        
        formula = re.sub(r'RC\[(-?\d+)\]', replace_rc, formula)
        
        # Clean up formula
        formula = formula.replace('""', '\"')
        formula = formula.replace('<>', '!=')
        
        # Create local variables for Excel functions
        iferror = self.iferror
        find = self.find
        mid = self.mid
        
        try:
            result = eval(formula)
            return result
        except Exception as e:
            print(f"Error evaluating formula in row {row_idx}, col {col_idx}: {str(e)}")
            return None

def process_formulas_yaml(yaml_content, data_df):
    """Process YAML containing formulas and apply them to dataframe"""
    # Parse YAML content
    formulas_data = yaml.safe_load(yaml_content)
    
    evaluator = ExcelFormulaEvaluator(data_df)
    results_df = data_df.copy()
    
    # Apply formulas
    for col, info in formulas_data['formulas'].items():
        formula = info['formula']
        try:
            col_idx = data_df.columns.get_loc(col)
            results_df[col] = [
                evaluator.evaluate_formula_for_cell(formula, row_idx, col_idx)
                for row_idx in range(len(data_df))
            ]
            print(f"Successfully processed column {col}")
        except Exception as e:
            print(f"Error processing column {col}: {str(e)}")
    
    return results_df

# Usage example:
"""
# Save the example_yaml content to a file named 'formulas.yaml'
with open('formulas.yaml', 'w') as f:
    f.write(example_yaml)

# Load your data
df = pd.read_excel('your_data.xlsx')

# Process formulas
with open('formulas.yaml', 'r') as f:
    yaml_content = f.read()
    
result_df = process_formulas_yaml(yaml_content, df)
"""


""""
pas testé; à voir les fonctions excell qui manque.
"""