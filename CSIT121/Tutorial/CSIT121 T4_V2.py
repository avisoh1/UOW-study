class TestResultException(Exception):
    pass

class TestResult:
    _lab4_log = "Lab_log.txt"

    def __init__(self, datafile: str):
        self.__name = ""
        self.__scores = {}
        self.load(datafile)
    
    def load(self,datafile:str):
        with open(datafile, "r") as infile, open(type(self)._lab4_log, "w") as outfile:
            self.__name = infile.readline().strip()
            self.__scores = {}
            for line in infile:
                id,mark = line.split(",")
                try:
                    mark = float(mark)
                    if mark < 0 or mark > 100:
                        raise TestResultException("Mark must be chosen between 0 and 100.")
                    self.__scores[id] = mark
                except(ValueError,TestResultException) as e:
                    outfile.write(f"Error for {id}: {e}\n")

    def update_score(self, candidate_id: str, new_mark: float):
        """Update score for a specific candidate, checking mark validity."""
        if not (0 <= new_mark <= 100):
            raise TestResultException("Mark must be chosen between 0 and 100.")
        self.__scores[candidate_id] = new_mark
    
    def get_basic_stats(self):
        """
        To return lowest, highest & average mark in a string
        """
        if len(self.__scores) == 0:
            return "No score"
        data = self.__scores.values()
        lowest = min(data)
        highest = max(data)
        avg = sum(data)/len(data)
        return f"Test: {self.__name}\nLowest: {lowest:.1f},Highest: {highest:.1f},Average: {avg:.1f}"

    def get_retest_list(self,datafile):
        with open(datafile, "w") as outfile: # ensure it is automatically close
            for k,v in self.__scores.items():
                if v < 50:
                    print(f"{k},{v}",file = outfile)
            outfile.close()

    def get_name(self):
        return self.__name
    
    def __str__(self):
        """Return the test name and the number of candidates passing."""
        passing_count = sum(1 for mark in self.__scores.values() if mark >= 50)
        return f"Test: {self.__name}, Candidates Passed: {passing_count}"

def main():
    # Initialize the TestResult with a sample data file
    try:
        test_result = TestResult("datafile.txt")
        print("Test Name:", test_result.get_name())  # Use get_name method
        print(test_result.get_basic_stats())  # Show lowest, highest, and average score
        
        # Print list of candidates needing a retest and generate "Retest_list.txt"
        retest_list = test_result.get_retest_list("Lab_log.txt")
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