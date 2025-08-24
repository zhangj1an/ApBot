# After reviewing the provided code and the user manual, the current code seems to correctly model the necessary features to achieve the user command.
# Below is the sequence of features needed to achieve the command, relevant user manual text, and goal variable values.

# 1. Sequence of features:
# - "select_cooking_program": Select the quick cooking steam mode by pressing the relevant program button.
# - "adjust_timer": Adjust the timer to 20 minutes if required.
# - "start_running": Start the appliance by pressing the start button.

# 2. Relevant user manual text:
# - To select a specific cooking program: "Press the button corresponding to the desired program, such as 'Quick Cooking/Steam'."
# - To adjust the timer: "Press the 'Timer' button to set the desired cooking time."
# - To start the appliance: "Press the 'Start' button to begin the selected program."

# 3. Goal variable values to achieve the command:
# - Set `variable_cooking_program` to "quick_cooking_steam".
# - Set `variable_timer` to 20 minutes.
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator):
    pass