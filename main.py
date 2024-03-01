import pandas as pd
import os


# - Loading annotations from CSV files to return DataFrame
def load_csv_data(csv_file):

    """
    Load annotations from a CSV file into a DataFrame

    Parameters:-
                csv_file: Path to the CSV file
    Returns:-
                DataFrame containing annotations
    """

    annotations_df = pd.read_csv(csv_file)
    return annotations_df


# - Dataframe containing specific columns
def process_row_data(row):

    """
    Processing single row of annotations DataFrame

    Parameters:-
                row: A row from the annotations DataFrame
    Returns:-
                DataFrame with columns: video,frame,phase,tag
    """

    video = row['video']
    start_frame = row['start_frame']
    end_frame = row['end_frame']
    phase = row['phase']
    tag = row['tag']

    frames = list(range(start_frame, end_frame + 1))

    data = {'video': [video] * len(frames),
            'frame': frames,
            'phase': [phase] * len(frames),
            'tag': [tag] * len(frames)}

    return pd.DataFrame(data)


# - Processing frame annotations iterating rows
def process_annotations(annotations_df):
    """
    Processing the annotations DataFrame

    Parameters:-
                annotations_df: DataFrame containing annotations
    Returns:-
                DataFrame with columns: video,frame,phase,tag
    """

    processed_dfs = [process_row_data(row) for _, row in annotations_df.iterrows()]
    return pd.concat(processed_dfs, ignore_index=True)



def process_all_annotation_data(directory_path):

    """
    Process all annotation files in the specified directory

    Parameters:-
                directory_path: Path to the directory containing annotation files.
    Returns:-
                DataFrame with columns: video, frame, phase, tag.
    """

    all_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
    all_dfs = []

    for file in all_files:
        file_path = os.path.join(directory_path, file)
        annotations_df = load_csv_data(file_path)
        processed_df = process_annotations(annotations_df)
        all_dfs.append(processed_df)

    return pd.concat(all_dfs, ignore_index=True)



def main():
    # - Path to the directory containing annotation files
    directory_path = "/home/fatima/Downloads/Archive_ML/"
    
    # - Processing annotation files to get the result DataFrame
    result_df = process_all_annotation_data(directory_path)
    
    # - Displaying the result DataFrame
    print(result_df)



if __name__ == "__main__":
    main()
