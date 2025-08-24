class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_sleep_mode = variable_sleep_mode
        self.variable_mode_selection = variable_mode_selection
        self.variable_timer = variable_timer
        self.variable_humidity_level = variable_humidity_level
        self.variable_internal_drying = variable_internal_drying
        self.variable_anion_function = variable_anion_function
        self.variable_air_swing = variable_air_swing
        self.variable_child_lock = variable_child_lock

    # Action: press_power_button
    # Effect: Toggles the power state of the appliance between "on" and "off".
    def press_power_button(self):
        self.feature.update_progress("press_power_button")
        self.variable_power_on_off.set_current_value("on" if self.variable_power_on_off.get_current_value() == "off" else "off")

    # Action: press_mode_button
    # Effect: Cycles through the available modes of the appliance.
    def press_mode_button(self):
        self.feature.update_progress("press_mode_button")
        self.execute_action_and_set_next("press_mode_button")

    # Action: press_and_hold_mode_button
    # Effect: Activates the child lock feature if held for 3 seconds or more.
    def press_and_hold_mode_button(self, duration=3):
        self.feature.update_progress("press_and_hold_mode_button")
        if duration >= 3:
            self.variable_child_lock.set_current_value("on")

    # Action: press_sleep_button
    # Effect: Toggles the sleep mode (ultra-silent air speed) on or off.
    def press_sleep_button(self):
        self.feature.update_progress("press_sleep_button")
        self.execute_action_and_set_next("press_sleep_button")

    # Action: press_timer_button
    # Effect: Adjusts the timer value in hours.
    def press_timer_button(self):
        self.feature.update_progress("press_timer_button")
        self.execute_action_and_set_next("press_timer_button")

    # Action: press_and_hold_timer_button
    # Effect: No explicit variable adjustment, but can be used for extended timer settings.
    def press_and_hold_timer_button(self, duration=3):
        self.feature.update_progress("press_and_hold_timer_button")
        if duration >= 3:
            pass  # No explicit variable adjustment

    # Action: press_humidity_button
    # Effect: Adjusts the humidity level in auto mode.
    def press_humidity_button(self):
        self.feature.update_progress("press_humidity_button")
        self.execute_action_and_set_next("press_humidity_button")

    # Action: press_and_hold_humidity_button_and_timer_button
    # Effect: Toggles between °C and °F temperature units.
    def press_and_hold_humidity_button_and_timer_button(self, duration=3):
        self.feature.update_progress("press_and_hold_humidity_button_and_timer_button")
        if duration >= 3:
            pass  # No explicit variable adjustment

    # Action: press_drying_button
    # Effect: No explicit variable adjustment, but starts the drying mode.
    def press_drying_button(self):
        self.feature.update_progress("press_drying_button")
        pass  # No explicit variable adjustment

    # Action: press_and_hold_drying_button
    # Effect: Activates the internal drying function if held for 2 seconds or more.
    def press_and_hold_drying_button(self, duration=2):
        self.feature.update_progress("press_and_hold_drying_button")
        if duration >= 2:
            self.variable_internal_drying.set_current_value("on")

    # Action: press_anion_button
    # Effect: Toggles the anion function on or off.
    def press_anion_button(self):
        self.feature.update_progress("press_anion_button")
        self.execute_action_and_set_next("press_anion_button")

    # Action: press_swing_button
    # Effect: Toggles the air swing function on or off.
    def press_swing_button(self):
        self.feature.update_progress("press_swing_button")
        self.execute_action_and_set_next("press_swing_button")