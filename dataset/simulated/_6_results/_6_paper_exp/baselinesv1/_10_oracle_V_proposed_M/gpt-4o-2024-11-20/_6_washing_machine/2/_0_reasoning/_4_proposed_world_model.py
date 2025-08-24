class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'turn_power_on_off': [{'step': 1, 'actions': ['press_on_off_button'], 'variable': 'variable_power_on_off'}],
                'set_program': [{'step': 1, 'actions': ['press_program_button'], 'variable': 'variable_program'}],
                'set_load_size': [{'step': 1, 'actions': ['press_load_size_button'], 'variable': 'variable_load_size'}],
                'adjust_wash_time': [{'step': 1, 'actions': ['press_wash_button'], 'variable': 'variable_wash_time'}],
                'adjust_rinse_times': [{'step': 1, 'actions': ['press_rinse_button'], 'variable': 'variable_rinse_times'}],
                'adjust_spin_time': [{'step': 1, 'actions': ['press_spin_button'], 'variable': 'variable_spin_time'}],
                'start_pause_operation': [{'step': 1, 'actions': ['press_start_pause_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = variable_power_on_off
        self.variable_program = variable_program
        self.variable_load_size = variable_load_size
        self.variable_start_running = variable_start_running
        self.variable_wash_time = variable_wash_time
        self.variable_rinse_times = variable_rinse_times
        self.variable_spin_time = variable_spin_time

    # Action: press_on_off_button
    # Effect: Toggles the power state between "on" and "off".
    def press_on_off_button(self):
        self.feature.update_progress("press_on_off_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "turn_power_on_off":
            self.execute_action_and_set_next("press_on_off_button")

    # Action: press_program_button
    # Effect: Cycles through the washing programs (Heavy, Gentle, Normal, Rapid, Soak).
    def press_program_button(self):
        self.feature.update_progress("press_program_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_program":
            self.execute_action_and_set_next("press_program_button")

    # Action: press_load_size_button
    # Effect: Cycles through the load sizes (1---small, 2---medium, 3---large).
    def press_load_size_button(self):
        self.feature.update_progress("press_load_size_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_load_size":
            self.execute_action_and_set_next("press_load_size_button")

    # Action: press_wash_button
    # Effect: Adjusts the washing time (1-20 minutes or no wash process).
    def press_wash_button(self):
        self.feature.update_progress("press_wash_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_wash_time":
            self.execute_action_and_set_next("press_wash_button")

    # Action: press_rinse_button
    # Effect: Adjusts the rinse times (1-3 times or no rinse process).
    def press_rinse_button(self):
        self.feature.update_progress("press_rinse_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_rinse_times":
            self.execute_action_and_set_next("press_rinse_button")

    # Action: press_spin_button
    # Effect: Adjusts the spin time (3-9 minutes or no spin process).
    def press_spin_button(self):
        self.feature.update_progress("press_spin_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_spin_time":
            self.execute_action_and_set_next("press_spin_button")

    # Action: press_start_pause_button
    # Effect: Starts the washing cycle or pauses/resumes it. Always sets variable_start_running to "on".
    def press_start_pause_button(self):
        self.feature.update_progress("press_start_pause_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_pause_operation":
            self.variable_start_running.set_current_value("on")

    # Wrapper function to handle global conditions and execute actions
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        action = getattr(self, action_name, None)
        if callable(action):
            for _ in range(execution_times):
                action(**kwargs)

        # Update the display after action execution
        self.update_display()
        return self.display