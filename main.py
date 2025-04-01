def main():
    while True:
        option = main_menu()
        if option == "play game":
            play_game()
        if option == "show stats":
            show_statistics()
        if option == "exit":
            break;


if __name__ == "__main__":
    main()