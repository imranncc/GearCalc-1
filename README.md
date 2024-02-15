
This project contains Python functions for calculating gear ratios, pitch diameters, and center distances for gearing mechanisms. It provides tools to verify gear ratios and center distances based on input parameters. The main function orchestrates the execution of these functions to demonstrate their usage and functionality.

### Functions:

#### `calc_GR(gear_list1, gear_list2):`
This function calculates the gear ratio of a gearing mechanism based on the input gear lists. It utilizes the gear ratios of individual gears to compute the overall gear ratio.

#### `calc_PD(gear_list, module):`
Given a list of gears and a module (gear parameter), this function calculates the pitch diameter for each gear in the list and returns a list of pitch diameters.

#### `calc_CD(pitch_diameter_list):`
This function computes the center distance between input and output gears for a set of gears. It takes a list of pitch diameters as input and calculates the center distance based on their arrangement.

#### `verify_gear_ratio(GR, gear_listFL, gear_listSL1, gear_list_SL2):`
This function verifies the gear ratio by comparing it with the calculated gear ratios for forefinger and thumb gears. It returns a list of Boolean values indicating whether the gear ratios match.

#### `verify_center_distance(module, first_lvl, forefinger, thumb):`
Given the module and gear lists for the first level, forefinger, and thumb gears, this function calculates the center distances for each set of gears and verifies them against predefined values. It returns a list of Boolean values indicating whether the center distances match.

#### `main():`
The main function orchestrates the execution of other functions to demonstrate their functionality. It initializes input parameters, calls verification functions, and prints the results.

### Usage:
To use this project:
1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the Python script.
4. Run the script using `python script_name.py`.
5. View the output to see the verification results.

### Contributors:
- Aditya Diwan
- Maaz Ghazi
- Imran Chowdhury
