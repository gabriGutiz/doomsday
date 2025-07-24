
# Doomsday: The Weekday Guessing Game

A fun and challenging command-line game to test and improve your mental date-calculation skills. This script presents you with a random date, and you have to guess the correct day of the week.

### Features

*   **Beautiful & Interactive UI**: Built with `rich` and `questionary` for a modern command-line experience with colors and interactive lists.
*   **Multiple Difficulty Levels**: From "Easy" mode (which helps you practice with specific anchor dates) to "Super Hard" (which uses a 1000-year date range).
*   **Performance Tracking**: At the end of your session, see your overall accuracy and average response time.
*   **Clean Interface**: The screen clears between rounds to keep you focused on the current challenge.
*   **Cross-Platform**: Works on Windows, macOS, and Linux.

## How to Run It

To get the game running on your local machine, follow these simple steps.

### Prerequisites

Make sure you have **Python 3.13+** installed on your system.

### Step 1: Get the Code

Clone this repository to your local machine using git:

```bash
git clone <your-repository-url>
cd <repository-folder>
```

*...or simply download the Python script (`main.py`) to a folder on your computer.*

### Step 2: Set Up a Virtual Environment (Recommended)

It's best practice to create a virtual environment to manage the project's dependencies.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

The game relies on two external libraries. You can install them using pip.

```bash
pip install rich questionary --quiet
```

### Step 4: Run the Game!

You're all set. Run the script from your terminal to start playing:

```bash
python game.py
```

## How to Get Good: Learn the "Doomsday" Method

This game isn't just about random guessing! There is a powerful mental algorithm you can learn to calculate the day of the week for any given date. The "Easy" and "Medium" difficulty levels are specifically designed to help you practice the core components of this method.

The most famous technique is the **Doomsday algorithm**, devised by mathematician John Horton Conway. It relies on knowing the "Doomsday" for each century and then using a few simple rules to find the day for any date.

To learn this amazing skill, check out the link below:

➡️ **Learn the method: [Wikipedia - Doomsday Rule](https://en.wikipedia.org/wiki/Doomsday_rule)**

For visual learners, searching for "Doomsday algorithm" on YouTube will also yield many excellent video tutorials.

Happy training

