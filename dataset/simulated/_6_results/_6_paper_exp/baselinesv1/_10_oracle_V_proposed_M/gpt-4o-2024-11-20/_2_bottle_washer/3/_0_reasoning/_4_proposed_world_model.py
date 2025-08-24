class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                'power_on_off': [{'step': 1, 'actions': ['press_and_hold_power_button'], 'variable': 'variable_power_on_off'}],
                'set_wash_mode': [{'step': 1, 'actions': ['press_wash_mode_button'], 'variable': 'variable_wash_mode'}],
                'set_sterilize_dry_mode': [{'step': 1, 'actions': ['press_sterilize_dry_button'], 'variable': 'variable_sterilize_dry_mode'}],
                'start_appliance': [{'step': 1, 'actions': ['press_start_pause_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_wash_mode = DiscreteVariable(
            value_range=["Wash & Dry", "Wash, Sterilize, Dry", "Wash Only"],
            current_value="Wash & Dry"
        )
        self.variable_sterilize_dry_mode = DiscreteVariable(
            value_range=["Sterilize & Dry", "Dry Only", "Sterilize Only"],
            current_value="Sterilize & Dry"
        )

    # Action: press_and_hold_power_button
    def press_and_hold_power_button(self, duration=3):
        # Update feature progress
        self.feature.update_progress("press_and_hold_power_button")
        current_feature = self.feature.current_value[0]
        # If the duration is sufficient, toggle power on/off
        if current_feature == "power_on_off" and duration >= 3:
            if self.variable_power_on_off.get_current_value() == "off":
                self.variable_power_on_off.set_current_value("on")
            else:
                self.variable_power_on_off.set_current_value("off")

    # Action: press_wash_mode_button
    def press_wash_mode_button(self):
        # Update feature progress
        self.feature.update_progress("press_wash_mode_button")
        current_feature = self.feature.current_value[0]
        # Cycle through wash modes
        if current_feature == "set_wash_mode":
            self.execute_action_and_set_next("press_wash_mode_button")

    # Action: press_sterilize_dry_button
    def press_sterilize_dry_button(self):
        # Update feature progress
        self.feature.update_progress("press_sterilize_dry_button")
        current_feature = self.feature.current_value[0]
        # Cycle through sterilize and dry modes
        if current_feature == "set_sterilize_dry_mode":
            self.execute_action_and_set_next("press_sterilize_dry_button")

    # Action: press_start_pause_button
    def press_start_pause_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_pause_button")
        current_feature = self.feature.current_value[0]
        # Start the appliance
        if current_feature == "start_appliance":
            self.variable_start_running.set_current_value("on")

    # Override run_action to include global conditions
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Check if the appliance is powered on
        if self.variable_power_on_off.get_current_value() == "off" and action_name != "press_and_hold_power_button":
            self.display = "Appliance is off. Please turn it on first."
            return self.display

        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)