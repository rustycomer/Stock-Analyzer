USER_CHOICE = """
Enter:
-  '1' for XLC (Communication Services)
-  '2' for XLY (Consumer Discretionary)
-  '3' for XLP (Consumer Staples)
-  '4' for XLE (Energy)
-  '5' for XLF (Financials)
-  '6' for XLV (Health Care)
-  '7' for XLI (Industrials)
-  '8' for XLB (Materials)
-  '9' for XLRE (Real Estate)
- '10' for XLK (Technology)
- '11' for XLU (Utilities)
- 'q' to quit


Please choose one: """


def main_menu():
    user_choice = input(USER_CHOICE)
    while user_choice != 'q':
        if user_choice == '1':
            pass
        elif user_choice == '2':
            pass
        elif user_choice == '3':
            pass
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            pass
        elif user_choice == '6':
            pass
        elif user_choice == '7':
            pass
        elif user_choice == '8':
            pass
        elif user_choice == '9':
            pass
        elif user_choice == '10':
            pass
        elif user_choice == '11':
            pass
        else:
            print("Not a valid option")
        user_choice = input(USER_CHOICE)
