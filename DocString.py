
# For FSN Analysis

"""
A class for cleaning data before analysis.

Attributes:
-----------
data pool: PO
    data selection: G/L account data, MB51 data
    aditional data: Mara data, Exchange Rate
        The data to be cleaned.

Methods:
--------
__init__(data: G/L account data, MB51 data, PO, Mara data, Exchange Rate)
    Initializes the Clean object with the provided data.

remove_duplicates()
    Removes duplicate rows from the data.

remove_missing_values()
    Removes rows with missing values from the data.

remove_outliers(columns: List[str])
    Removes outliers from specified columns of the data.

normalize_data()
    Normalizes the data.

"""





"""
Initializes the Clean object with the provided data.

        Parameters:
        -----------
        path of the files
        data pool: PO
        data selection: G/L account data, MB51 data
        aditional data: Mara data, Exchange Rate
            The data to be cleaned.
"""





"""
A class for analyzing cleaned data.

Attributes:
-----------
cleaned_data : Master object
    The cleaned data to be analyzed.

Methods:
--------
__init__(cleaned_data: Master object)
    Initializes the Analysis object with the cleaned data.

descriptive_statistics()
    Computes descriptive statistics of the data.

correlation_analysis()
    Performs correlation analysis on the data.

visualize_data()
    Visualizes the data for analysis.

"""

"""
Initializes the Analysis object with the cleaned data.

Parameters:
-----------
cleaned_data : Master object
    The cleaned data to be analyzed.
"""





# for PO Analysis

"""
A class for cleaning data before analysis.

Attributes:
-----------
data pool: PO
    data selection: G/L account data, MB51 data
    aditional data: Mara data, Exchange Rate
        The data to be cleaned.

Methods:
--------
__init__(data: G/L account data, MB51 data, PO, Mara data, Exchange Rate)
    Initializes the Clean object with the provided data.

remove_duplicates()
    Removes duplicate rows from the data.

remove_missing_values()
    Removes rows with missing values from the data.

remove_outliers(columns: List[str])
    Removes outliers from specified columns of the data.

normalize_data()
    Normalizes the data.

"""





"""

Initializes the Clean object with the provided data.

        Parameters:
        -----------
        Excel files
        data: PO, Mara data, Exchange Rate
            The data to be cleaned.
"""





"""
A class for analyzing cleaned data.

Attributes:
-----------
cleaned_data : Master object
    The cleaned data to be analyzed.

Methods:
--------
__init__(cleaned_data: Master object)
    Initializes the Analysis object with the cleaned data.

descriptive_statistics()
    Computes descriptive statistics of the data.

correlation_analysis()
    Performs correlation analysis on the data.

visualize_data()
    Visualizes the data for analysis.

"""

"""
Initializes the Analysis object with the cleaned data.

Parameters:
-----------
cleaned_data : Master object
    The cleaned data to be analyzed.
"""


