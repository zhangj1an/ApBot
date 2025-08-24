class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'adjust_water_level': [{'step': 1, 'actions': ['press_water_level_button'], 'variable': 'variable_water_level'}],
                'adjust_preset_timer': [{'step': 1, 'actions': ['press_preset_button'], 'variable': 'variable_preset_timer'}],
                'adjust_process_setting': [{'step': 1, 'actions': ['press_process_button'], 'variable': 'variable_process_setting'}],
                'select_program': [{'step': 1, 'actions': ['press_program_button'], 'variable': 'variable_program_selection'}],
                'start_operation': [{'step': 1, 'actions': ['press_start_pause_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}],
                'toggle_power': [{'step': 1, 'actions': ['press_power_button', 'press_and_hold_power_button'], 'variable': 'variable_power_on_off'}],
                'set_child_lock': [{'step': 1, 'actions': ['press_and_hold_program_button'], 'variable': 'variable_child_lock'}],
                'manual_rotate_tub': [{'step': 1, 'actions': ['turn_tub_dial_clockwise']}],
                'hold_start_pause': [{'step': 1, 'actions': ['press_and_hold_start_pause_button']}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = variable_power_on_off
        self.variable_start_running = variable_start_running
        self.variable_child_lock = variable_child_lock
        self.variable_water_level = variable_water_level
        self.variable_preset_timer = variable_preset_timer
        self.variable_process_setting = variable_process_setting
        self.variable_program_selection = variable_program_selection

    # Action: press_power_button
    def press_power_button(self):
        # Toggles the power on/off
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "toggle_power":
            self.execute_action_and_set_next("press_power_button")

    # Action: press_and_hold_power_button
    def press_and_hold_power_button(self, duration=3):
        # Toggles the power on/off with a press-and-hold action
        self.feature.update_progress("press_and_hold_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "toggle_power" and duration >= 3:
            self.execute_action_and_set_next("press_and_hold_power_button")

    # Action: press_start_pause_button
    def press_start_pause_button(self):
        # Starts the operation and sets the variable_start_running to "on"
        self.feature.update_progress("press_start_pause_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_operation":
            self.variable_start_running.set_current_value("on")

    # Action: press_and_hold_start_pause_button
    def press_and_hold_start_pause_button(self, duration=3):
        # Placeholder for any specific behavior for holding the start/pause button
        self.feature.update_progress("press_and_hold_start_pause_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "hold_start_pause" and duration >= 3:
            self.execute_action_and_set_next("press_and_hold_start_pause_button")

    # Action: press_program_button
    def press_program_button(self):
        # Adjusts the program selection
        self.feature.update_progress("press_program_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_program":
            self.execute_action_and_set_next("press_program_button")

    # Action: press_process_button
    def press_process_button(self):
        # Adjusts the process setting (wash, rinse, spin)
        self.feature.update_progress("press_process_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_process_setting":
            self.execute_action_and_set_next("press_process_button")

    # Action: press_water_level_button
    def press_water_level_button(self):
        # Adjusts the water level
        self.feature.update_progress("press_water_level_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_water_level":
            self.execute_action_and_set_next("press_water_level_button")

    # Action: press_preset_button
    def press_preset_button(self):
        # Adjusts the preset timer
        self.feature.update_progress("press_preset_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_preset_timer":
            self.execute_action_and_set_next("press_preset_button")

    # Action: press_and_hold_program_button
    def press_and_hold_program_button(self, duration=5):
        # Sets the child lock if held for 5 seconds
        self.feature.update_progress("press_and_hold_program_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_child_lock" and duration >= 5:
            self.execute_action_and_set_next("press_and_hold_program_button")

    # Action: turn_tub_dial_clockwise
    def turn_tub_dial_clockwise(self):
        # Manually rotates the tub
        self.feature.update_progress("turn_tub_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "manual_rotate_tub":
            self.execute_action_and_set_next("turn_tub_dial_clockwise")