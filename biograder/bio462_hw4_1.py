from .Homework import Homework
import os
import pandas as pd


class bio462_hw4_1(Homework):

    def __init__(self, student_id="", version="latest", no_internet=False):

        valid_versions = ["1.0.0"]

        data_files = {
            
            "1.0.0": [
                "bio462_hw4_1_ans.txt",
                "bio462_hw4_1_hint.txt",
                "gene_locations.tsv.gz"
            ],
        }

        super().__init__(hw_number="bio462_hw4_1", student_id=student_id, version=version, valid_versions=valid_versions, data_files=data_files, no_internet=no_internet)
        # need to reference file of answer key and hints
        for file_path in self._data_files_paths:
            path_elements = file_path.split(os.sep)  # Get a list of the levels of the path
            file_name = path_elements[-1]

            if file_name == "bio462_hw4_1_ans.txt":
                self.ansArray = self.parseAnswers(file_path)
            elif file_name == "bio462_hw4_1_hint.txt":
                self.hintDict = self.parseHints(file_path)
            elif file_name == "gene_locations.tsv.gz":
                self._data["gene_locations"] = pd.read_csv(file_path, sep='\t', dtype={"chromosome": "O"}, index_col=[0], usecols=['Name', 'Database_ID', 'chromosome', 'start_bp', 'end_bp'])

        for question in range(1, len(self.ansArray) + 1):
            self._student_answers[question] = "?"
            self._student_attempts[question] = 0
            self._student_correct[question] = "No"
