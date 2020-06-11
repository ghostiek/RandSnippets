"""Goes through a dataframe (df) and checks if any of its headers contain a certain substring. Returns a list
Example use case: df.loc[index, get_values_from_header(df, str_contained)].plot(kind="bar")
"""
import re
def get_values_from_header(df, regex_match):
    col_names = []
    headers = list(df)
    
    for header in headers:
        if re.search(regex_match, header):
            col_names.append(header)
    return col_names
