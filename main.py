import game
import game_stats

menu_itens = {
    1: game.play,
    2: game_stats.show,
}

def main() -> None:
    while True:
        option = menu_itens.get(main_menu())
        if option == "exit":
            break
        elif option:
            option()
        else:
            "Invalid option. Please, try again."
        

def main_menu() -> int:
    return 0

if __name__ == "__main__":
    main()
