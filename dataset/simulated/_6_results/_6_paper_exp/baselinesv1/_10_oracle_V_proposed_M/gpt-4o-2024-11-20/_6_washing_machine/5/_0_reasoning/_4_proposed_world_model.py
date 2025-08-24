class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(feature_list={
            'power_control': [{'step': 1, 'actions': ['press_on_off_button'], 'variable': 'variable_on_off'}],
            'start_pause': [{'step': 1, 'actions': ['press_start_pause_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}],
            'set_program': [{'step': 1, 'actions': ['press_program_buttons'], 'variable': 'variable_program'}],
            'adjust_water_level': [{'step': 1, 'actions': ['press_water_level_button'], 'variable': 'variable_water_level'}],
            'adjust_rinse_times': [{'step': 1, 'actions': ['press_rinse_button'], 'variable': 'variable_rinse_times'}],
            'adjust_spin_speed': [{'step': 1, 'actions': ['press_spin_button'], 'variable': 'variable_spin_speed'}],
            'adjust_time_manager': [{'step': 1, 'actions': ['press_time_manager_button'], 'variable': 'variable_time_manager'}],
            'toggle_clean_tub': [{'step': 1, 'actions': ['press_clean_tub_off_button'], 'variable': 'variable_clean_tub'}],
            'toggle_child_lock': [{'step': 1, 'actions': ['press_and_hold_water_level_button_and_time_manager_button'], 'variable': 'variable_child_lock'}],
            'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
        }, current_value=("empty", 1))

        # Initialize variables
        self.variable_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_program = DiscreteVariable(value_range=["Regular", "Delicates", "Mixed", "Wool", "Heavy Duty", "Bedding", "Quick Wash", "Clean Tub"], current_value="Regular")
        self.variable_water_level = DiscreteVariable(value_range=["1", "2", "3", "4", "5", "6"], current_value="1")
        self.variable_rinse_times = DiscreteVariable(value_range=["1 time", "2 times", "3 times", "4 times"], current_value="1 time")
        self.variable_spin_speed = DiscreteVariable(value_range=["Off", "Low", "Medium", "High"], current_value="Off")
        self.variable_time_manager = DiscreteVariable(value_range=["1", "2", "3", "4", "5", "6"], current_value="1")
        self.variable_clean_tub = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_child_lock = DiscreteVariable(value_range=["on", "off"], current_value="off")

    # Action: press_on_off_button
    def press_on_off_button(self):
        # Update feature progress
        self.feature.update_progress("press_on_off_button")
        # Toggle the on/off state
        if self.variable_on_off.get_current_value() == "off":
            self.variable_on_off.set_current_value("on")
        else:
            self.variable_on_off.set_current_value("off")

    # Action: press_start_pause_button
    def press_start_pause_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_pause_button")
        # Always set start_running to "on" when this button is pressed
        self.variable_start_running.set_current_value("on")

    # Action: press_program_buttons
    def press_program_buttons(self):
        # Update feature progress
        self.feature.update_progress("press_program_buttons")
        # Change the program to the next one in the list
        self.execute_action_and_set_next("press_program_buttons")

    # Action: press_water_level_button
    def press_water_level_button(self):
        # Update feature progress
        self.feature.update_progress("press_water_level_button")
        # Adjust the water level to the next value
        self.execute_action_and_set_next("press_water_level_button")

    # Action: press_rinse_button
    def press_rinse_button(self):
        # Update feature progress
        self.feature.update_progress("press_rinse_button")
        # Adjust the rinse times to the next value
        self.execute_action_and_set_next("press_rinse_button")

    # Action: press_spin_button
    def press_spin_button(self):
        # Update feature progress
        self.feature.update_progress("press_spin_button")
        # Adjust the spin speed to the next value
        self.execute_action_and_set_next("press_spin_button")

    # Action: press_time_manager_button
    def press_time_manager_button(self):
        # Update feature progress
        self.feature.update_progress("press_time_manager_button")
        # Adjust the time manager to the next value
        self.execute_action_and_set_next("press_time_manager_button")

    # Action: press_clean_tub_off_button
    def press_clean_tub_off_button(self):
        # Update feature progress
        self.feature.update_progress("press_clean_tub_off_button")
        # Toggle the clean tub function
        if self.variable_clean_tub.get_current_value() == "off":
            self.variable_clean_tub.set_current_value("on")
        else:
            self.variable_clean_tub.set_current_value("off")

    # Action: press_and_hold_water_level_button_and_time_manager_button
    def press_and_hold_water_level_button_and_time_manager_button(self, duration=3):
        # Update feature progress
        self.feature.update_progress("press_and_hold_water_level_button_and_time_manager_button")
        # Toggle child lock if the button is held for at least 3 seconds
        if duration >= 3:
            if self.variable_child_lock.get_current_value() == "off":
                self.variable_child_lock.set_current_value("on")
            else:
                self.variable_child_lock.set_current_value("off")