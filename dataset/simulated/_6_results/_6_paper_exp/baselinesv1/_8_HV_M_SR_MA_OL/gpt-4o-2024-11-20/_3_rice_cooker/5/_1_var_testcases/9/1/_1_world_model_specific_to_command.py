# The command is to turn on the rice cooker in quick cooking steam mode with a timer set to 20 minutes, and then start the machine.
# Let's validate the given code against the user manual to see if it's sufficient for this task.

# Checking required features and variables in the user manual:
# 1. A feature to select "quick_cooking_steam" cooking program.
# 2. A feature to adjust the "variable_timer" for 20 minutes.
# 3. A feature to start the appliance.

# The user manual mentions the following relevant raw texts:
# - **Cooking Programs**: Buttons to select cooking modes including "Quick Cooking/Steam".
# - **Timer Feature**: "Timer" can be adjusted for desired cooking time (e.g., 20 minutes).
# - **Starting/Stopping**: Appliance can be started with a "start" button and stopped with a "cancel" button.

# Relevant code features:
# - `feature_list["select_cooking_program"]`: This handles selecting a mode, including "quick_cooking_steam".
# - `feature_list["adjust_timer"]`: This manages timer adjustments.
# - `feature_list["start_appliance"]`: This starts the machine.

# The current code models these features adequately. For the given command:
# - Use "select_cooking_program" to select "quick_cooking_steam".
# - Use "adjust_timer" to set the timer to 20 minutes.
# - Use "start_appliance" to start.

# Feature sequence:
# - "select_cooking_program" => Select "quick_cooking_steam".
# - "adjust_timer" => Set timer to "20 minutes".
# - "start_appliance" => Start the appliance.

# Final goal variable values:
# - Set `variable_cooking_program` to "quick_cooking_steam".
# - Set `variable_timer` to 20 minutes.
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator):
    pass