class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                'power_control': [{'step': 1, 'actions': ['press_and_hold_power_button'], 'variable': 'variable_power_on_off'}],
                'start_cycle': [{'step': 1, 'actions': ['press_start_pause_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}],
                'choose_wash_mode': [{'step': 1, 'actions': ['press_wash_mode_button'], 'variable': 'variable_wash_mode'}],
                'choose_sterilize_dry_mode': [{'step': 1, 'actions': ['press_sterilize_dry_button'], 'variable': 'variable_sterilize_dry_mode'}],
                'trigger_drain_water': [{'step': 1, 'actions': ['press_and_hold_wash_mode_button_and_sterilize_dry_button']}],
                'clear_descale_reminder': [{'step': 1, 'actions': ['press_and_hold_wash_mode_button']}],
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
        self.display = {}

    # Action: press_and_hold_power_button
    def press_and_hold_power_button(self, duration=3):
        # Update feature progress
        self.feature.update_progress("press_and_hold_power_button")
        current_feature = self.feature.current_value[0]
        # If the duration is sufficient, toggle power on/off
        if current_feature == "power_control" and duration >= 3:
            if self.variable_power_on_off.get_current_value() == "off":
                self.variable_power_on_off.set_current_value("on")
            else:
                self.variable_power_on_off.set_current_value("off")

    # Action: press_start_pause_button
    def press_start_pause_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_pause_button")
        current_feature = self.feature.current_value[0]
        # Start the cycle if in the start_cycle feature
        if current_feature == "start_cycle":
            self.variable_start_running.set_current_value("on")

    # Action: press_wash_mode_button
    def press_wash_mode_button(self):
        # Update feature progress
        self.feature.update_progress("press_wash_mode_button")
        current_feature = self.feature.current_value[0]
        # Cycle through wash modes if in the choose_wash_mode feature
        if current_feature == "choose_wash_mode":
            self.execute_action_and_set_next("press_wash_mode_button")

    # Action: press_sterilize_dry_button
    def press_sterilize_dry_button(self):
        # Update feature progress
        self.feature.update_progress("press_sterilize_dry_button")
        current_feature = self.feature.current_value[0]
        # Cycle through sterilize and dry modes if in the choose_sterilize_dry_mode feature
        if current_feature == "choose_sterilize_dry_mode":
            self.execute_action_and_set_next("press_sterilize_dry_button")

    # Action: press_and_hold_wash_mode_button_and_sterilize_dry_button
    def press_and_hold_wash_mode_button_and_sterilize_dry_button(self, duration=3):
        # Update feature progress
        self.feature.update_progress("press_and_hold_wash_mode_button_and_sterilize_dry_button")
        current_feature = self.feature.current_value[0]
        # Trigger water drainage if in the trigger_drain_water feature
        if current_feature == "trigger_drain_water" and duration >= 3:
            pass  # No variable to update, just a feature action

    # Action: press_and_hold_wash_mode_button
    def press_and_hold_wash_mode_button(self, duration=5):
        # Update feature progress
        self.feature.update_progress("press_and_hold_wash_mode_button")
        current_feature = self.feature.current_value[0]
        # Clear descale reminder if in the clear_descale_reminder feature
        if current_feature == "clear_descale_reminder" and duration >= 5:
            pass  # No variable to update, just a feature action

    # Wrapper function to execute actions with global condition checks
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Check if the appliance is powered on
        if self.variable_power_on_off.get_current_value() == "off" and action_name != "press_and_hold_power_button":
            self.display = {"error": "Appliance is powered off"}
            return self.display

        # Execute the action
        action = getattr(self, action_name, None)
        if callable(action):
            for _ in range(execution_times):
                action(**kwargs)

        # Update the display
        self.update_display()
        return self.display