class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'power': [{'step': 1, 'actions': ['press_power_button'], 'variable': 'variable_power_on_off'}],
                'start_operation': [{'step': 1, 'actions': ['press_start_pause_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}],
                'adjust_water_level': [{'step': 1, 'actions': ['press_water_level_button'], 'variable': 'variable_water_level'}],
                'child_lock': [{'step': 1, 'actions': ['press_and_hold_program_button'], 'variable': 'variable_child_lock'}],
                'set_preset_timer': [{'step': 1, 'actions': ['press_preset_button'], 'variable': 'variable_preset_timer'}],
                'change_process_setting': [{'step': 1, 'actions': ['press_process_button'], 'variable': 'variable_process_setting'}],
                'select_program': [{'step': 1, 'actions': ['press_program_button'], 'variable': 'variable_program_selection'}],
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
        # Update feature progress and set power to "on"
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "power":
            self.variable_power_on_off.set_current_value("on")

    # Action: press_start_pause_button
    def press_start_pause_button(self):
        # Update feature progress and set start_running to "on"
        self.feature.update_progress("press_start_pause_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_operation":
            self.variable_start_running.set_current_value("on")

    # Action: press_water_level_button
    def press_water_level_button(self):
        # Update feature progress and adjust water level to the next value
        self.feature.update_progress("press_water_level_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_water_level":
            self.execute_action_and_set_next("press_water_level_button")

    # Action: press_and_hold_program_button
    def press_and_hold_program_button(self, duration=3):
        # Update feature progress and set child lock to "on" if duration >= 3 seconds
        self.feature.update_progress("press_and_hold_program_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "child_lock" and duration >= 3:
            self.variable_child_lock.set_current_value("on")

    # Action: press_preset_button
    def press_preset_button(self):
        # Update feature progress and adjust preset timer to the next value
        self.feature.update_progress("press_preset_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_preset_timer":
            self.execute_action_and_set_next("press_preset_button")

    # Action: press_process_button
    def press_process_button(self):
        # Update feature progress and adjust process setting to the next value
        self.feature.update_progress("press_process_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "change_process_setting":
            self.execute_action_and_set_next("press_process_button")

    # Action: press_program_button
    def press_program_button(self):
        # Update feature progress and adjust program selection to the next value
        self.feature.update_progress("press_program_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_program":
            self.execute_action_and_set_next("press_program_button")

    # Override run_action to include global condition checks
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Check if child lock is on and restrict actions
        if self.variable_child_lock.get_current_value() == "on" and action_name not in ["press_power_button", "press_and_hold_program_button"]:
            self.display = "child lock: locked"
            return self.display

        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)