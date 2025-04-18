'''This program has the user playing a game where they need to defeat three
different monsters to pass the trials.'''
import check_input
import hero
import beg_factory
import exp_factory

def main():
    kill_count = 0
    print("Monster Trials")
    player_name = input("What is your name? ")
    main_hero = hero.Hero(player_name)
    print(f"\nYou will face a series of 3\nmonsters, {player_name}.\nDefeat them all to win.")

    #create the factories and enemies
    b_factory = beg_factory.BeginnerFactory()
    ex_factory = exp_factory.ExpertFactory()
    monsters = [b_factory.create_random_enemy() for _ in range(2)]
    monsters.append(ex_factory.create_random_enemy())

    #Main Loop
    while main_hero.hp > 0 and monsters:
        print("\nChoose an enemy to attack:")
        for i, m in enumerate(monsters,1):
            print(f"{i}. {m.name} HP: {m.hp}")
        choice = check_input.get_int_range("Enter choice: ", 1, len(monsters))
        target_monster = monsters[choice - 1]
        print()
        print(main_hero)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        attack = check_input.get_int_range("Enter choice: ", 1, 2)

        #Hero attacks
        if attack == 1:
            result = main_hero.melee_attack(target_monster)
        else:
            result = main_hero.ranged_attack(target_monster)
        print(result)

        if target_monster.hp == 0:
            print(f"You have slain the {target_monster.name}")
            monsters.remove(target_monster)
            kill_count += 1
        #counterattack phase

        if target_monster.hp != 0:

            counter_attack = target_monster.melee_attack(main_hero)
            print(counter_attack)
        if main_hero.hp <= 0:
            print("\nYou lost........\nGame Over..")
            break
        elif kill_count == 3:
            print("\nCongratulations! You defeated all three monsters!\nGame Over!")
            break

main()
