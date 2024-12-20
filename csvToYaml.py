import pandas as pd
import yaml
import re

def csv_to_yaml_converter(csv_file):
    """Convert formulas from CSV file to YAML format"""
    # Read the CSV file
    try:
        df = pd.read_csv(csv_file, encoding='utf-8')
    except UnicodeDecodeError:
        # Try with a different encoding if utf-8 fails
        df = pd.read_csv(csv_file, encoding='latin-1')
    
    # Initialize the YAML structure
    yaml_data = {
        'formulas': {}
    }
    
    # Process each row
    for _, row in df.iterrows():
        column = row['Intitulé de Range']  # Assuming this is the column name in your CSV
        formula = row['Formule']  # Assuming this is the column name in your CSV
        
        # Skip if either column or formula is missing
        if pd.isna(column) or pd.isna(formula):
            continue
            
        # Clean up the formula
        formula = str(formula).strip()
        formula = formula.strip('"')  # Remove outer quotes
        formula = formula.replace('""', '"')  # Convert double quotes to single quotes
        
        # Add to YAML structure
        yaml_data['formulas'][column] = {
            'formula': formula,
            'description': f'Formula for column {column}'  # You can update descriptions later
        }
    
    return yaml_data

def convert_and_save_formulas(csv_file='sortie.csv', output_file='formulas.yaml'):
    """Convert CSV formulas and save to YAML file"""
    # Convert CSV to YAML structure
    yaml_data = csv_to_yaml_converter(csv_file)
    
    # Save to YAML file
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, sort_keys=False, allow_unicode=True, width=1000)
    
    # Also return the YAML content as a string
    return yaml.dump(yaml_data, sort_keys=False, allow_unicode=True, width=1000)

# Example usage
if __name__ == "__main__":
    try:
        # Convert CSV to YAML
        yaml_content = convert_and_save_formulas('sortie.csv', 'formulas.yaml')
        print("Conversion successful! YAML content preview:")
        print("\nFirst few formulas:")
        print("\n".join(yaml_content.split("\n")[:10]))
        print("\n... (more formulas)")
        print("\nYAML file has been saved as 'formulas.yaml'")
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        print("\nPlease check that:")
        print("1. 'sortie.csv' exists in the current directory")
        print("2. The CSV file has columns 'Intitulé de Range' and 'Formule'")
        print("3. You have write permissions in the current directory")

