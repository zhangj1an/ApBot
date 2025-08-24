class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'power_on_off': [{'step': 1, 'actions': ['press_on_off_button'], 'variable': 'variable_power_on_off'}],
                'select_program': [{'step': 1, 'actions': ['press_program_button'], 'variable': 'variable_program'}],
                'adjust_load_size': [{'step': 1, 'actions': ['press_load_size_button'], 'variable': 'variable_load_size'}],
                'adjust_wash_time': [{'step': 1, 'actions': ['press_wash_button'], 'variable': 'variable_wash_time'}],
                'adjust_rinse_times': [{'step': 1, 'actions': ['press_rinse_button'], 'variable': 'variable_rinse_times'}],
                'adjust_spin_time': [{'step': 1, 'actions': ['press_spin_button'], 'variable': 'variable_spin_time'}],
                'start_pause_cycle': [{'step': 1, 'actions': ['press_start_pause_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}],
                'null': [{'step': 1, 'actions': ['press_and_hold_start_pause_button', 'press_and_hold_on_off_button'], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_program = DiscreteVariable(value_range=["Heavy", "Gentle", "Normal", "Rapid", "Soak"], current_value="Heavy")
        self.variable_load_size = DiscreteVariable(value_range=["1---small", "2---medium", "3---large"], current_value="1---small")
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_wash_time = ContinuousVariable(value_ranges_steps=[(0, 20, 1)], current_value=0)
        self.variable_rinse_times = ContinuousVariable(value_ranges_steps=[(0, 3, 1)], current_value=0)
        self.variable_spin_time = ContinuousVariable(value_ranges_steps=[(0, 9, 1)], current_value=0)

    # Action: press_on_off_button
    # Effect: Toggles the power state between "on" and "off".
    def press_on_off_button(self):
        self.feature.update_progress("press_on_off_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "power_on_off":
            self.execute_action_and_set_next("press_on_off_button")

    # Action: press_program_button
    # Effect: Cycles through the washing programs (Heavy, Gentle, Normal, Rapid, Soak).
    def press_program_button(self):
        self.feature.update_progress("press_program_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_program":
            self.execute_action_and_set_next("press_program_button")

    # Action: press_load_size_button
    # Effect: Cycles through the load sizes (1---small, 2---medium, 3---large).
    def press_load_size_button(self):
        self.feature.update_progress("press_load_size_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_load_size":
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
    # Effect: Starts the washing cycle and sets the variable_start_running to "on".
    def press_start_pause_button(self):
        self.feature.update_progress("press_start_pause_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_pause_cycle":
            self.variable_start_running.set_current_value("on")

    # Wrapper function to handle global conditions and execute actions.
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Check if the appliance is powered on before executing any action.
        if self.variable_power_on_off.get_current_value() == "off" and action_name != "press_on_off_button":
            self.display = {"error": "Appliance is powered off. Please turn it on first."}
            return self.display

        # Execute the action and update the display.
        return super().run_action(action_name, execution_times, **kwargs)