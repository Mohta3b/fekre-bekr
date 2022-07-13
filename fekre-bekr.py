import os


class Players:
    def __init__(self, id, solution_set, guesses=None, Win=0):
        if guesses is None:
            guesses = []
        self.Win = Win
        self.guesses = guesses
        self.solution_set = solution_set
        self.id = id

    def is_done(self):
        if self.Win != 0:
            print("Player(" + str(self.id + 1) + ") already have completed the game at round ", str(self.Win), "!")
            return True

    def print_guess(self, this_round_guess, round):
        if self.Win != 0:
            print("You already have completed the game at round ", str(self.Win), "!")
        else:
            if round > 0:
                print("last guesses for player " + str(self.id + 1) + ":")
                for guess in range(round):
                    print(*self.guesses[guess], sep=" ")
                print()
            self.guesses.append(this_round_guess)
            answer = ["None" for _ in range(4)]
            check_used_place = [False for _ in range(4)]
            winning_status = 0
            for i in range(4):
                if this_round_guess[i] == self.solution_set[i]:
                    winning_status += 1
                    answer[i] = "BLACK"
                    check_used_place[i] = True
            if winning_status == 4:
                self.Win = round + 1
                print("You Won!!!")
                return True
            for i in range(4):
                if answer[i] == "None":
                    for j in range(4):
                        if check_used_place[j] == False and this_round_guess[j] == self.solution_set[i]:
                            answer[j] = "WHITE"
                            check_used_place[j] = True
            print(*answer, sep=" ")
            return False


if __name__ == '__main__':
    n = int(input("Number of Players: "))
    number_of_rounds = int(input("Number of Rounds: "))
    answer_set = list(
        map(int, input("Enter the 4-set: \n0: Abi \n1: Sabz \n2: Zard \n3: Firoze-e \n4: Banafsh \n5: Narenji "
                       "\n6: Sorati \n7: Sefid \n8: Ghermez \n9: Meshki\n ").split()))
    # print(answer_set)
    Players_List = []
    for i in range(n):
        this_player = Players(i, answer_set)
        Players_List.append(this_player)
    # done = True
    for rounds in range(number_of_rounds):
        print("\nRound " + str(rounds + 1) + ":")
        done = True
        for player in range(n):
            if Players_List[player].is_done():
                continue
            guess_set = list(map(int, input("Guess(player " + str(player + 1) + "):\n").split()))
            don = Players_List[player].print_guess(guess_set, rounds)
            print("press enter to continue...")
            input()
            # os.system('cls')
            if not don:
                done = False
        if done:
            print("\n*******\nTHE END\n*******")
            break
