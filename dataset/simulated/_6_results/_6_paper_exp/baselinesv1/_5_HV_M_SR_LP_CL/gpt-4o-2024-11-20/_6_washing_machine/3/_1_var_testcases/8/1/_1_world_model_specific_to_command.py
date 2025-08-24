# The adjustments required based on analysis above.
updated_feature_list = feature_list

# No changes to existing features, but refining child lock and preset logic.

class ExtendedSimulator(Simulator):
    def reset(self):
        super().reset()
        # Initializing existing variables
        self.feature = Feature(feature_list=updated_feature_list, current_value=("empty", 1))
        self.variable_power_on_off = variable_power_on_off
        self.variable_start_running = variable_start_running
        self.variable_child_lock = variable_child_lock
        self.variable_water_level = variable_water_level
        self.variable_preset_timer = variable_preset_timer
        self.variable_process_setting = variable_process_setting
        self.variable_program_selection = variable_program_selection

    # Adjusting action: press_and_hold_program_button for child lock
    def press_and_hold_program_button(self, duration=5):
        """
        Handles child lock activation logic.
        """
        self.feature.update_progress("press_and_hold_program_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_child_lock" and duration >= 5:
            self.variable_child_lock.set_current_value("on")

    # Refining preset timer logic for setting specific hours
    def press_preset_button(self):
        """
        Adjusts the preset timer. Increases the timer based on defined steps.
        """
        self.feature.update_progress("press_preset_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_preset_timer":
            self.assign_variable_to_next(self.variable_preset_timer)

# Command Execution
# Sequence of features required for the given command:
#  1. Use "toggle_power" to turn the appliance on.
#  2. Use "select_program" to set the program to "8 Water Save".
#  3. Use "adjust_water_level" to set the water level to "42 L".
#  4. Use "adjust_preset_timer" to set the timer to "5 hours".
#  5. Use "start_operation" to start the appliance.
#  6. Use "set_child_lock" to enable the child lock.

# Features from the user manual that describe the relevant command:
# 1. Power on the machine:
#    - "Power On/Off" - The power turns off automatically if you do not press “Start/Pause” within 10 minutes after power-on.
#      Feature: toggle_power.
# 2. Choose Water Save program:
#    - "Variety of Programs" - Saving water -> Program 8 Water Save.
#      Feature: select_program.
# 3. Set water level to 42 L:
#    - "Change Water Level" - During the wash process, press “Water Level” to change the water level.
#      Feature: adjust_water_level.
# 4. Finish in 5 hours:
#    - "Preset" - Set the time to finish washing (in hours).
#      Feature: adjust_preset_timer.
# 5. Start the Appliance:
#    - "Start/Pause" - Start the operation.
#      Feature: start_operation.
# 6. Activate Child Lock:
#    - "Setting Child Lock" - To prevent children from falling into the tub and drowning, if the lid is opened while the washing machine is operating, this function sounds a buzzer until it is closed.
#      Feature: set_child_lock.

# Goal variable values for the command:
# 1. variable_power_on_off = "on" (Power turned on).
# 2. variable_program_selection = "8 Water Save" (Set the program to Water Save).
# 3. variable_water_level = "42 L" (Set water level).
# 4. variable_preset_timer = 5 (Set timer to 5 hours).
# 5. variable_start_running = "on" (Start the appliance).
# 6. variable_child_lock = "on" (Activate child lock).