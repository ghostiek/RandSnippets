"""Goes through a dataframe (df) and checks if any of its headers contain a certain substring. Returns a list
Example use case: df.loc[index, get_values_from_header(df, str_contained)].plot(kind="bar")
"""
def get_values_from_header(df, str_contained, case_sensitive = False):
    col_names = []
    headers = list(df)
    
    if not case_sensitive:
        str_contained = str_contained.lower()
        headers = set(map(str.lower, headers))
       
    for header in list(df):
        if str_contained in header:
            col_names.append(header)
    return col_names
