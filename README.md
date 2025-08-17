# Risk Register
#### Video Demo:
https://youtu.be/Bb6nJ7ovXTU
#### Description:

A command-line tool to track project risks with auto-incrementing IDs (RSK001, RSK002, …). Create risks, set probability/severity/status, list them, edit status, and remove by ID.

## Features

- Includes a main menu prompting user for command
- Automatically generates unique IDs for each risk
- Has customizable status and ratings parameters.


## Usage

1. Download or clone this repository.
2. Run `risk_register.py`
3. Follow the on-screen prompts

## Configuration

- **Statuses**: Open, Closed Avoided, Closed Accepted
- **Ratings**: High, Medium, Low

(You can change these in risk_register.py.)
## Commands

| Command | What it Does | Example |
| -------- | ------- | ------- |
| insert | create a new risk with guided prompts | insert |
| view | Lists all risks | view |
| edit | Update a risk's status | edit RSK001 |
| remove | Delete one or more risks by ID | remove RSK001 RSK002 |
| exit | Quit the program | exit |

## Key Functions
`main()`
- Responsible for creating an items list that risks will be added to, Initiates main menu with that list.

`add_risk(items: dict[str, Risk])`
- Inititates a new Risk object, asking the user for the name, probability, severity, and status. Everything but name has a default value if none provided.

`input_helper(label: str, default: str, allowed: list[str])`
- A short helper function that validates probability, severity, and statuses entered are in the `STATUSES` and `RATINGS` lists.

`name_input_helper(label: str)`
- Ensures the given risk name is not blank

`edit_risk(items: dict[str, Risk], id_str: str)`
- Allows the user to update the status of the given risk

`view_risks(items: dict[str, Risk])`
- Prints a list of all risks and a count with all of their details.

`delete_risk(items, rest: str)`
- Deletes risks either given in main menu command. If none provided, will prompt the user to enter IDs to delete.

## Project Structure

I ultimately decided it was best to manage risks using a Risk class that gets initiated every time one is created. This way, default values can automatically be assigned, there is clear structure, and easier code to read. I created Risk as a subclass of ProjectItem to be forward thinking, allowing room for more ProjectItems to be added in the future. Things like Change Orders and Issues could be created using the same parent class easily.

## Example Usage
`insert`

Enter name: `Server outage`

Probability (High, Medium, Low) [Low]: `High`

Severity (High, Medium, Low) [Low]: `High`

Status (Open, Closed Avoided, Closed Accepted) [Open]:

Added risk RSK001

`view`

Total risks: 1

RSK001: Server outage (Open) | Probability: High | Severity: High


## test_risk_register.py
- Ensures that a risk can be initialized with the default values.
- Ensures that parameters cannot be outside of given list.
- Ensures that calling a risk shows the correct output when called as a string.
- Ensures name input helper allows for normal input.

## Libraries Used
`sys`
- Used in order to exit the program when the user prompts to exit on the main menu
