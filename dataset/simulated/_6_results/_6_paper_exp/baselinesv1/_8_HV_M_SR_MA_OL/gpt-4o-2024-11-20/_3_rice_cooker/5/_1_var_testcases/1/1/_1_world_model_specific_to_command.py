# The task is described in the user command: turn on the rice cooker, set it to cook jasmine rice for 4 hours using the preset option, and start the machine.

# After reviewing the user manual and quoted code:
# - The feature "adjust_preset_time" already includes setting the preset option.
# - The "start_appliance" feature models starting the machine correctly.
# - The "select_cooking_program" feature is sufficient to set the program to jasmine rice.
# - The duration of 4 hours (240 minutes) can be set using the variable `variable_preset_time`.

# Sequence of features to achieve the task:
# 1. "start_appliance" -> Turn on the rice cooker by setting `variable_start_running` to "on".
# 2. "select_cooking_program" -> Set cooking program to "jasmine rice" by setting `variable_cooking_program` to "jasmine_rice".
# 3. "adjust_preset_time" -> Use the preset option to set total cooking time to 4 hours (240 minutes) by setting `variable_preset_time` to 240.
# 4. "start_appliance" -> Start the machine by setting `variable_start_running` to "on" again via pressing the start button.

# Based on the provided user manual text:
# - Raw text: "When the cooking program is chosen (not available on 'Clay Pot', Reheat, and 'Keep Warm'), press the 'Preset' button to set the time for finishing cooking. Press 'Start' button when the time is set."
# - Raw text: "Pressing 'Start' button will begin operation. Pressing 'Cancel' button will halt operation."

# Goal variable values:
# 1. Set `variable_start_running` to "on".
# 2. Set `variable_cooking_program` to "jasmine_rice".
# 3. Set `variable_preset_time` to 240 (4 hours).
# 4. Set `variable_start_running` to "on" (start cooking).

class ExtendedSimulator(Simulator):
    pass