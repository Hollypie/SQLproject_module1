from schema import create_tables
from seed import seed_data
from repository import (
    get_leaderboard,
    scores_in_date_range,
    add_player, 
    add_score,
    add_game_session,
    show_leaderboard,
    show_scores_by_date,
    add_new_session,
    delete_player_by_name,
    update_player_name,
    update_score
    
)

def main():
    print("Initializing database...")
    create_tables()

    answer = input("Seed database with sample data? (y/n): ").lower()
    if answer == "y":
        seed_data()
    else:
        print("Skipping seed data.")

    # MAIN MENU LOOP
    while True:
        print("=== MENU ===")
        print("1. View leaderboard")
        print("2. View scores in date range")
        print("3. Add new game session")
        print("4. Delete Player")
        print("5. Edit Player Name")
        print("6. Update Player Score")
        print("7. Exit")

        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            show_leaderboard()
        elif choice == "2":
            show_scores_by_date()
        elif choice == "3":
            add_new_session()
        elif choice == "4":
                player = input("What is the player you want to delete? ").title()
                deleted = delete_player_by_name(player)

                if deleted:
                    print(f"{player} was deleted.\n")
                else:
                    print(f"No player named {player} found.\n")
        elif choice == "5":
            update_player_name()
        elif choice == "6":
            update_score()
        elif choice == "7":
            print("Program complete.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
