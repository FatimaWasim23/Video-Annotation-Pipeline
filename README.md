# Video-Annotation-Pipeline


# Overview

This project provides a modularized pipeline for processing video annotations stored in CSV files. The pipeline loads annotation data, processes it, and outputs a DataFrame suitable in a way to divide the videos into specific phases.The project processes video annotations stored in CSV files and transforms them into a structured DataFrame. The resulting DataFrame contains information about each (video, frame) tuple, including video,frame,phase and specified tag.

How to Run

    Clone the repository:
    git clone https://github.com/yourusername/video-annotation-pipeline.git
    cd video-annotation-pipeline

    Install dependencies:
    pip install -r requirements.txt

    Run the main script:
    python3 video_annotation_pipeline.py

# Code Structure

The code is organized into several modular functions to enhance readability and maintainability. Key functions include:

    load_csv_data:- Loads annotations from a CSV file into a DataFrame.This function takes a CSV file path as input and uses Pandas to read the CSV into a DataFrame(annotations_df).
    process_row_data:- Processes a single row of the annotations DataFrame.
    process_annotations:- Processes the entire annotations DataFrame.It iterates through each row of the DataFrame, extracts relevant information (video, start_frame, end_frame, phase, tag).It then generates a new DataFrame (processed_df) where each row corresponds to a (video, frame) tuple, with columns video, frame, phase, and tag.The frames between start_frame and end_frame (inclusive) are expanded into separate rows in the processed_df.
    process_all_annotation_data:- Processes all annotation files in a specified directory.It retrieves a list of all CSV files in the directory.For each file it loads the annotations, processes them using process_annotations, and appends the result to a list (all_dfs) and then it concatenates all DataFrames in the list into a single DataFrame (result_df) using pd.concat and the result DataFrame is returned.
    main:- Orchestrates the entire pipeline.


1. Efficiency Considerations:
   
The code uses Pandas, a powerful library for handling large datasets efficiently.It iterates through the rows of the DataFrame using iterrows(), which is not the most efficient for large DataFrames but is reasonable for moderate-sized datasets. The use of pd.concat is efficient for combining DataFrames, and it uses ignore_index=True to reset the index in the final concatenated DataFrame.

2. Scalability:
   
The code is designed to handle multiple CSV files efficiently and concatenate the results into a single DataFrame, making it scalable for thousands of video annotation files.


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

1. Limited Error Handling: The code assumes well-formed CSV files and may not handle unexpected formats or errors robustly.

2. Iterative Processing Overhead: For very large datasets, the iterative processing approach may result in slower execution times compared to fully vectorized solutions.

3. Memory Usage: The code might face memory issues when dealing with very large datasets. For such cases, additional optimizations may be needed.

4. Parallel Processing: The code currently does not utilize parallel processing, which could be a consideration for further optimization.

# Unit Tests

To run unit tests, use the following command:

    python3 -m unittest discover tests
