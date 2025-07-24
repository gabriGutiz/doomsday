import datetime
import os
import random
import time
from rich import print
import questionary


DOOMSDAY = {1: 3, 2: 28, 3: 14, 4: 4, 5: 9, 6: 6, 7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}
DOOMSDAY_LEAP_YEAR = {1: 4, 2: 29, 3: 14, 4: 4, 5: 9, 6: 6, 7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}


def clear_screen():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (os.name is 'posix')
    else:
        _ = os.system('clear')


def get_doomsday(year):
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return DOOMSDAY_LEAP_YEAR if is_leap else DOOMSDAY


def get_random_date_by_difficulty(difficulty: str) -> datetime.date:
    """
    Generates a random date based on the selected difficulty level.
    """
    # "Super Hard" is the baseline: fully random within the whole range.
    if difficulty == "Super Hard":
        start_dt = datetime.date(1500, 1, 1)
        end_dt = datetime.date(2500, 12, 31)
        total_days = (end_dt - start_dt).days
        random_days = random.randrange(total_days)
        return start_dt + datetime.timedelta(days=random_days)

    # Define rules for other levels
    year_range = (1800, 2299) if difficulty in ["Easy", "Medium"] else (1500, 2500)
    
    # --- Year Generation ---
    # For Easy, Medium, and Hard, we generate years "close to" multiples of 12.
    # This makes calculating the year's "Doomsday" easier.
    target_last_digits = [0, 12, 24, 36, 48, 60, 72, 84, 96]
    base_year = random.choice(target_last_digits)
    offset = random.choice([0, 1, 2, 3])
    century = random.randrange(year_range[0], year_range[1] + 1, 100)
    year = century + base_year + offset
    
    # Ensure year stays within the intended range after offset
    year = max(year_range[0], min(year, year_range[1]))

    # --- Day and Month Generation ---
    if difficulty == "Easy":
        doomsdays = get_doomsday(year)
        
        month = random.choice(list(doomsdays.keys()))
        generate_day = lambda m: doomsdays[m] + random.choice([0, 1, 2, 3, 4, 5, 6]) # "close to"
        day = generate_day(month)
        
        # Ensure the generated date is valid, otherwise, regenerate.
        while True:
            try:
                return datetime.date(year, month, day)
            except ValueError: # Handles cases like Feb 30 or Nov 32
                day = generate_day(month)

    else: # For Medium and Hard, the day is fully random
        while True:
            try:
                # Pick a random day of the year and convert to a date
                day_of_year = random.randint(1, 366)
                return datetime.date(year, 1, 1) + datetime.timedelta(days=day_of_year - 1)
            except ValueError: # Handles day 366 on a non-leap year
                continue


def guess_the_weekday_game(date_to_guess: datetime.date):
    """
    Handles a single round of the game for a given date.
    """
    correct_weekday_index = (date_to_guess.weekday() + 1) % 7
    weekday_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    correct_weekday_name = weekday_names[correct_weekday_index]

    print(f"\nThe date is: [cyan]{date_to_guess.strftime('%Y-%m-%d')}[/cyan]")
    
    start_time = time.time()

    user_answer = questionary.select(
        "What day of the week is this?",
        choices=weekday_names,
        use_indicator=True
    ).ask()

    end_time = time.time()
    elapsed_time = end_time - start_time

    if user_answer is None:
        return None, None

    is_correct = (user_answer == correct_weekday_name)
    
    print("\n[bold]--- Result ---[/bold]")
    if is_correct:
        print(f"[green]🎉 Correct! It was indeed a {correct_weekday_name}.[/green]")
    else:
        print(f"[red]Sorry, that's not right. The correct day was {correct_weekday_name}.[/red]")
        
    print(f"You took {elapsed_time:.2f} seconds to answer.")
    
    return is_correct, elapsed_time


if __name__ == "__main__":
    all_results = []
    
    print("[bold]Welcome to the Weekday Guessing Game![/bold]")

    difficulty = questionary.select(
        "Choose a difficulty level:",
        choices=["Easy", "Medium", "Hard", "Super Hard"],
        use_indicator=True
    ).ask()

    if difficulty is not None:
        clear_screen()
        print(f"\n[bold]--- Chosen difficulty: {difficulty} ---[/bold]")
        while True:
            date_to_guess = get_random_date_by_difficulty(difficulty)
            
            success, time_taken = guess_the_weekday_game(date_to_guess)
            
            if success is None:
                break

            all_results.append({"success": success, "time": time_taken})
            
            play_again = questionary.confirm("Play another round?", default=True, auto_enter=True).ask()
            
            clear_screen()
            if not play_again:
                break
            
    if all_results:
        total_rounds = len(all_results)
        correct_guesses = sum(1 for r in all_results if r["success"])
        avg_time = sum(r["time"] for r in all_results) / total_rounds
        success_rate = (correct_guesses / total_rounds) * 100
        
        print("\n[bold]--- Game Over: Final Stats ---[/bold]")
        print(f"Difficulty played: {difficulty}")
        print(f"Total rounds played: [cyan]{total_rounds}[/cyan]")
        print(f"Correct guesses: [green]{correct_guesses}[/green] ({success_rate:.1f}%)")
        print(f"Average time to answer: [yellow]{avg_time:.2f} seconds[/yellow]")
        print("\nThanks for playing!")
    else:
        print("\nNo games were played. See you next time!")

