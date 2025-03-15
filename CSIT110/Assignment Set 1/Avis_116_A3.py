# Full Name: Avis Oh Xin Wan
# Tutorial Group: 1 (116)
# Objective: This is assignment 3.
# File name: Avis_116_A3.py
#
# Declarations: This is my own program. I gave not passed my program to anyone in this class. If I do so, I accept any penalty of mark.
import random

# Define class Diverinfo
class Diverinfo:
    # Instance methods
    def __init__(self, country, name, age):
        self.country = country
        self.name = name
        self.age = age

    # Accessor methods
    def get_Country(self):
        return self.country

    def get_Name(self):
        return self.name

    def get_Age(self):
        return self.age

    # Mutator methods
    def set_Country(self, country):
        self.country = country

    def set_Name(self, name):
        self.name = name

    def set_Age(self, age):
        self.age = age

    # str function
    def __str__(self):
        s = "country is {0}, diver name is called {1} and his/her is {2}".format(self.country, self.name, self.age)
        return s

# Define class Diving
class Diving:
    # Instance methods
    def __init__(self, diver, score, difficulty, cf, fs):
        self.diver = diver
        self.score = score
        self.difficulty = difficulty
        self.cf = cf
        self.fs = fs

    # Accessor methods
    def get_Diver(self):
        return self.diver

    def get_Score(self):
        return self.score

    def get_Difficulty(self):
        return self.difficulty

    def get_Cf(self):
        return self.cf

    def get_Fs(self):
        return self.fs

    # Mutator methods
    def set_Diver(self, diver):
        self.diver = diver

    def set_Score(self, score):
        self.score = score

    def set_Difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_Cf(self, cf):
        self.cf = cf

    def set_Fs(self, fs):
        self.fs = fs
        
    # Method to display game info
    @staticmethod
    def display_game_info(round_num, divers, df_list):
        print("\nRound {0}\n".format(round_num + 1))
        print("Starting Position\n")
        print("{0:>2}.\t{1:<9} {2:<10}{3:>2}".format("No", "Country", "Name", "DF"))
        for i, diver in enumerate(divers):
            df = generate_difficulty()
            rounded_df = round(df, 1)
            df_list.append(rounded_df)
            print("{0:>2}.\t{1:<9} {2:<10}{3:>2.1f}".format(i + 1, diver.get_Country(), diver.get_Name(), df))

    # Method to display results
    @staticmethod
    def display_result(round_num, cf, df_list, divers):
        print("\n{0:<10} {1:<9} {2:>3}  {3:<4} {4:<4} {5:<4} {6:<4} {7:<4} {8:<4} {9:<4} {10:<4} {11:<10} {12:<10}\t {13:<10}".format(
            "Country", "Name", "Age", "DF", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "c/f", "Total", "Final"))

        final_list = []

        # Loop for divers
        for i, diver in enumerate(divers):
            judges_scores = [generate_Scores() for _ in range(7)]
            total = get_total_score(judges_scores) * df_list[i]
            carried_forward = cf[i]
            final = carried_forward + total
            cf[i] = final

            final_list.append({"country": diver.get_Country(), "name": diver.get_Name(), "final": final})

            print("{0:<10} {1:<9} {2:>3}  {3:<4.1f} {4:<4.1f} {5:<4.1f} {6:<4.1f} {7:<4.1f} {8:<4.1f} {9:<4.1f} {10:<4.1f} {11:<10.2f} {12:<10.2f}\t {13:<10.2f}".format(
                diver.get_Country(), diver.get_Name(), diver.get_Age(), df_list[i],
                judges_scores[0], judges_scores[1], judges_scores[2],
                judges_scores[3], judges_scores[4], judges_scores[5],
                judges_scores[6], carried_forward, total, final))

        Diving.display_ranking(final_list, round_num)

    # Method to display ranking
    @staticmethod
    def display_ranking(final_list, round_num):
        print(f"\nRank after Round {round_num + 1}\n")
        print("{0:<6}{1:<10}{2:<10}{3}".format("Rank", "Country", "Name", "Score"))

        # Sort the divers with their point in descending order
        final_list.sort(key=lambda x: x["final"], reverse=True)

        for i, diver in enumerate(final_list):
            print("{0:>2}{1:<4}{2:<10}{3:<10}{4:<.2f}".format(i + 1, ".", diver["country"], diver["name"], diver["final"]))

# This function generates age for those divers
def generate_Ages():
    return random.randint(15, 30)

# This function generates scores between 0 to 10
def generate_Scores():
    score_base = random.randint(0, 10)
    if score_base == 10:
        score_fraction = 0.0
        score = score_base + score_fraction
    else:
        score_fraction = random.choice([0.0, 0.5])
        score = score_base + score_fraction
    return score

# This function removes two highest and two lowest scores and get the sum of the remaining scores.
def get_total_score(judges_scores):
    sorted_scores = sorted(judges_scores)
    trimmed_scores = sorted_scores[2:-2]
    return sum(trimmed_scores)

# This function generates the difficulty to be display and calculate the total scores.
def generate_difficulty():
    return random.uniform(2.0, 5.0)

def main():
    country = ["Singapore", "China", "France", "China", "U S A", "Spain", "Brazil", "Malaysia", "Thailand", "Japan"]
    name = ["Diver 1", "Diver 2", "Diver 3", "Diver 4", "Diver 5", "Diver 6", "Diver 7", "Diver 8", "Diver 9", "Diver 10"]
    divers = [Diverinfo(country[i], name[i], generate_Ages()) for i in range(10)]
    cf = [0.0] * 10

    # Have 5 rounds
    for round_num in range(5):
        df_list = []
        Diving.display_game_info(round_num, divers, df_list)
        Diving.display_result(round_num, cf, df_list, divers)

    # The last statement
    input("\nEnter any character to end")

if __name__ == '__main__':
    main()
