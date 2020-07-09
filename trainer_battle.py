from Actions import tap
import poke_characters


indev = "In Development"
invalid = "\nThat is not a valid section please try again."

"""
IDEA: create a script for trainer battle specific instead of creating a class create a battle script that will run
every time the a battle is initiated.
"""


class TrainerBattle:
    def __init__(self, opponent_name, opponent_poke, player_poke, move_set, move_names):
        self.opponent_name = opponent_name
        self.opponent_poke = opponent_poke
        self.player_poke = player_poke
        self.move_set = move_set
        self.move_names = move_names

    """NOTE: Link Pokemon moves with fight moves here!
    QUESTION what can be done for fight() so that we can accept 1,2,3 or 4 arguments w/o creating another seprate method
    """

    def current_hp(self):
        print(f"Opponent's {self.opponent_poke.name} has {self.opponent_poke.hp} remaining")
        print(f"Your {self.player_poke.name} has {self.player_poke.hp} remaining")
        tap()

    def win_loss(self):
        if self.player_poke.hp <= 0:
            print("GAME OVER")
            return self.player_poke
            # add function to reset game
        elif self.opponent_poke.hp <= 0:
            print("Victory!")
            return self.player_poke


    def opponent_turn(self):
        print("It is now opponent's " + self.opponent_poke.name + "'s turn!")
        damage = self.move_set["move1"](self.opponent_poke)
        self.player_poke.hp -= damage
        self.current_hp()
        self.win_loss()
        self.battle()

    # def items(self):
    #     print("Which item would you like to use?")
    #     print("[A] Potions x [{}] ".format(inventory.items["potion"]))
    #     print("[B] Super Potion x [{}]".format(inventory.items["super potion"]))
    #     print("[C] Cancel, Go back")
    #     ans = input("Choice:  ")
    #     if ans == "A":
    #         inventory.items["potion"] -= 1
    #         print("Potion used to regain 20HP")
    #     elif ans == "B":
    #         inventory.items["super potion"] -= 1
    #         print("Super Potion used 50 HP was regained")
    #     elif ans == "C":
    #         print(indev)
    #     else:
    #         print(invalid)
    #         self.items()
    #
    #     ans = input()

    # def pokeball(self):
    #     print(indev)
    #     pass

    def attack_moves(self):
        print(f"{self.player_poke.name} wants to fight! Which Move should they use?")
        print(f"[A] {self.move_names[0]}\n[B] {self.move_names[1]}\n[C] Go Back. ")
        ans = input("\nType answer here: ")

        if ans == "A":
            damage = self.move_set["move1"](self.player_poke)
            self.opponent_poke.hp -= damage
            self.current_hp()
            self.win_loss()
            self.opponent_turn()
            self.battle()

        elif ans == "B":
            def_down = self.move_set["move2"](self.player_poke)
            self.opponent_poke.defence *= def_down
            print(f"Opponent's {self.opponent_poke.name} went down to {self.opponent_poke.defence}")
            self.battle()

        elif ans == "C":
            self.battle()
        # Add elif for C and D and if Dictionary for move names are blank use Exceptions statement

        else:
            print(invalid)
            self.attack_moves()


    def battle(self):

        while self.opponent_poke.hp > 0 and self.player_poke.hp > 0:
            print("What will you do? \n[A] Fight \n[B] Items \n[C] Pokeball \n[D] Flee ")
            ans = input("\nType answer here: ")
            if ans == "A":
                self.attack_moves()

            elif ans == "B":
                # self.items()
                pass
            elif ans == "C":
                print(f"{self.opponent_name} says: What do you think you're doing you can't steal my pokemon!")
                self.battle()
            elif ans == "D":
                print("You can't flee from a trainer battle!\n")
                self.battle()
            else:
                print(invalid)
                self.battle()

        return self.player_poke


p_cyndiquil = poke_characters.cyndiquil_l5
cy_l5_move_names = ["scratch", "smokescreen"]

totodile1 = poke_characters.totodile_l5
cyndiquil1 = poke_characters.cyndiquil_l5
rival_poke = [totodile1, cyndiquil1]  # IDEA: use dictionary to create list of pokemon and use if-statement to switch

first_battle = TrainerBattle("Rival Gary", rival_poke[0], p_cyndiquil, poke_characters.cy_l5, cy_l5_move_names)
p_cyndiquil = first_battle.battle()
