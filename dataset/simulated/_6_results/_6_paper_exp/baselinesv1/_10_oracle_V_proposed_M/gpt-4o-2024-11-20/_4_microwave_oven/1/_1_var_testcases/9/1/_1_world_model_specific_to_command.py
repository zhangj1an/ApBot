# Python comments for code verification:
# Based on the requested user command to defrost 20 oz of chicken using weight defrost, then start the appliance and activate child lock:
# The given code already accurately models the appliance features and variables required to fulfill the command:
# 1. Weight Defrost Feature:
#    - User manual text: "Press 'WEIGHT DEFROST', screen will display 'dEF1'. Press numerical buttons to input weight to be defrosted. Input the weight ranged between 4~100 Oz. Press 'START/+30SEC.' to start defrosting and the cooking time remained will be displayed."
#    - Feature modeled in: `feature_list["set_weight_defrost"]`.
# 2. Starting the appliance:
#    - The "start" functionality is accurately modeled through the `feature_list["set_weight_defrost"]` as well as the action `press_start_plus_30sec_button`.
# 3. Activating child lock:
#    - User manual text: "Lock: In waiting state, press 'STOP/CANCEL' for 3 seconds, there will be a long 'beep' denoting the entering into the children-lock state. Lock quitting: In locked state, press 'STOP/CANCEL' for 3 seconds."
#    - Feature modeled in: `feature_list["toggle_child_lock"]`.

# Features involved:
# `feature_list["set_weight_defrost"]` for defrosting chicken.
# `press_start_plus_30sec_button` for starting the appliance.
# `feature_list["toggle_child_lock"]` to activate child lock.

# Goal Variable Values:
# - Set `variable_weight_defrost` to "20".
# - Set `variable_start_running` to "on".
# - Set `variable_child_lock` to "locked".

class ExtendedSimulator(Simulator): 
    pass