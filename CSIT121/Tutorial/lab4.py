import logging

class TestResultException(Exception):
    pass

class TestResult:
    _lab4_log = "Lab_log.txt"

    def __init__(self, datafile: str):
        self.__name = ""
        self.__scores = {}
        self.load(datafile)

    def load(self, datafile: str):
        logger = logging.getLogger(self.__class__.__name__)
        
        # Configure logging once, outside the method
        logging.basicConfig(filename=self._lab4_log, filemode='w', level=logging.ERROR)
        
        try:
            with open(datafile, 'r') as infile:
                self.__name = infile.readline().strip()
                for line in infile:
                    id, mark = line.split(",")
                    try:
                        mark = float(mark)
                        if mark < 0 or mark > 100:
                            raise TestResultException("Mark must be between 0 and 100")
                        self.__scores[id.strip()] = mark
                    except (ValueError, TestResultException) as e:
                        logger.error("{}: {}".format(str(e), line.strip()))
        except FileNotFoundError:
            logger.error("Data file not found: {}".format(datafile))
            raise

    def update_score(self, candidate_id: str, new_mark: float):
        if new_mark < 0 or new_mark > 100:
            raise TestResultException("Mark must be between 0 and 100")
        self.__scores[candidate_id] = new_mark

    def get_basic_stats(self):
        if not self.__scores:
            return "No scores available."
        lowest = min(self.__scores.values())
        highest = max(self.__scores.values())
        average = sum(self.__scores.values()) / len(self.__scores)
        return f"Lowest: {lowest}, Highest: {highest}, Average: {average:.2f}"

    def get_retest_list(self):
        retest_candidates = {id: mark for id, mark in self.__scores.items() if mark < 50}
        with open("Retest_list.txt", 'w') as f:
            for id, mark in retest_candidates.items():
                f.write(f"{id} {mark}\n")
        return retest_candidates

    def get_name(self):
        return self.__name

    def __str__(self):
        passing_count = sum(1 for mark in self.__scores.values() if mark >= 50)
        return f"{self.__name} - Number of passing candidates: {passing_count}"

def main():
    # Initialize the TestResult with a sample data file
    try:
        test_result = TestResult("datafile.txt")
        print("Test Name:", test_result.get_name())  # Use get_name method
        print(test_result.get_basic_stats())  # Show lowest, highest, and average score
        
        # Print list of candidates needing a retest and generate "Retest_list.txt"
        retest_list = test_result.get_retest_list()
        print("Candidates for Retest:", retest_list)
        
        # Print the summary of test result with passing count
        print(test_result)
        
        # Update a candidate's score and reprint stats
        test_result.update_score("c15", 55)
        print("Updated Basic Stats after modifying score for c15:")
        print(test_result.get_basic_stats())

    except TestResultException as e:
        print(f"Error in processing test results: {e}")
    except FileNotFoundError:
        print("Error: The data file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
