import unittest
import os
import shutil
import pandas as pd
from main import load_csv_data, process_row_data, process_annotations, process_all_annotation_data


class TestVideoAnnotationsPipeline(unittest.TestCase):

    def setUp(self):

        # - Temporary CSV file for testing
        csv_content = "video,start_frame,end_frame,phase,tag\n1,0,10,TestPhase,0\n"
        with open('test_annotations.csv', 'w') as temp_csv:
            temp_csv.write(csv_content)


    def tearDown(self):

        # - Removing temporary CSV file after testing
        os.remove('test_annotations.csv')


    def test_load_annotations_csv(self):

        # - Test loading annotations from the temporary CSV
        result_df = load_csv_data('test_annotations.csv')
        expected_df = pd.DataFrame({'video': [1], 'start_frame': [0], 'end_frame': [10], 'phase': ['TestPhase'], 'tag': [0]})
        pd.testing.assert_frame_equal(result_df, expected_df)


    def test_process_annotations_row(self):

        # - Test processing a single row
        row = {'video': 1, 'start_frame': 0, 'end_frame': 5, 'phase': 'TestPhase', 'tag': 0}
        result_df = process_row_data(row)
        expected_df = pd.DataFrame({'video': [1] * 6, 'frame': list(range(0, 6)), 'phase': ['TestPhase'] * 6, 'tag': [0] * 6})
        pd.testing.assert_frame_equal(result_df, expected_df)


    def test_process_annotations(self):

        # - Create a DataFrame for testing
        input_df = pd.DataFrame({'video': [1], 'start_frame': [0], 'end_frame': [5], 'phase': ['TestPhase'], 'tag': [0]})

        # - Test processing the entire DataFrame
        result_df = process_annotations(input_df)
        expected_df = pd.DataFrame({'video': [1] * 6, 'frame': list(range(0, 6)), 'phase': ['TestPhase'] * 6, 'tag': [0] * 6})
        pd.testing.assert_frame_equal(result_df, expected_df)


    def test_process_all_annotation_files(self):

        # - Create a temporary directory with multiple CSV files for testing
        os.makedirs('test_directory', exist_ok=True)
        with open('test_directory/file1.csv', 'w') as temp_csv:
            temp_csv.write("video,start_frame,end_frame,phase,tag\n1,0,5,TestPhase1,0\n")
        with open('test_directory/file2.csv', 'w') as temp_csv:
            temp_csv.write("video,start_frame,end_frame,phase,tag\n2,3,8,TestPhase2,1\n")


        # - Test processing all annotation files in the temporary directory
        result_df = process_all_annotation_data('test_directory')
        expected_df = pd.DataFrame({
            'video': [1] * 6 + [2] * 6,
            'frame': list(range(0, 6)) + list(range(3, 9)),
            'phase': ['TestPhase1'] * 6 + ['TestPhase2'] * 6,
            'tag': [0] * 6 + [1] * 6
        })


        # - Sort both DataFrames by the 'video' column before assertion
        result_df = result_df.sort_values(by='video').reset_index(drop=True)
        expected_df = expected_df.sort_values(by='video').reset_index(drop=True)

        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()
