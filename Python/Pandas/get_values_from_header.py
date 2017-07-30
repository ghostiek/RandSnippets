"""Goes through a dataframe (df) and checks if any of its headers contain a certain substring. Returns a list"""
def get_values_from_header(df, str_contained):
    headers = []
    for header in list(df):
        if str_contained in header:
            headers.append(header)
    return headers