# Video-Annotation-Pipeline


# Overview

This project provides a modularized pipeline for processing video annotations stored in CSV files. The pipeline loads annotation data, processes it, and outputs a DataFrame suitable in a way to divide the videos into specific phases.
How to Run

    Clone the repository:


git clone https://github.com/yourusername/video-annotation-pipeline.git
cd video-annotation-pipeline

    Install dependencies:


pip install -r requirements.txt

    Run the main script:


python3 main.py

# Code Structure

The code is organized into several modular functions to enhance readability and maintainability. Key functions include:

    load_csv_data:- Loads annotations from a CSV file into a DataFrame.
    process_row_data:- Processes a single row of the annotations DataFrame.
    process_annotations:- Processes the entire annotations DataFrame.
    process_all_annotation_data:- Processes all annotation files in a specified directory.
    main:- Orchestrates the entire pipeline.

# Design Decisions

1. Modularization

Each major functionality is encapsulated in a separate function. This promotes code reusability and makes it easier to maintain and extend the pipeline.

2. Iterative Processing

The code iterates through rows of the DataFrame using iterrows(). While not the most efficient for large DataFrames, it provides a straightforward solution for moderate-sized datasets, maintaining readability.

3. Pandas for Data Manipulation

The use of Pandas for handling DataFrames ensures efficient data manipulation and scalability. Concatenation with pd.concat is used for combining DataFrames.

# Tradeoffs

1. Iterative Processing vs. Vectorization

The use of iterrows() for DataFrame iteration can be less efficient than fully vectorized operations. This tradeoff was made for simplicity and readability. For extremely large datasets, exploring more efficient vectorized alternatives might be necessary.

2. Memory Usage

The code loads entire DataFrames into memory, which may become a limitation for very large datasets. For extremely large datasets, a more memory-efficient approach might involve reading and processing data in smaller chunks.

# Limitations

    Limited Error Handling: The code assumes well-formed CSV files and may not handle unexpected formats or errors robustly.

    Iterative Processing Overhead: For very large datasets, the iterative processing approach may result in slower execution times compared to fully vectorized solutions.

    Memory Usage: The code might face memory issues when dealing with very large datasets. For such cases, additional optimizations may be needed.

# Unit Tests

To run unit tests, use the following command:

python -m unittest discover tests
