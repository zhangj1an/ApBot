[
    {
        "id": 1,
        "command": "Set the temperature to 98°C for boiling, then unlock the dispenser and pour some water.",
        "target_state": {
            "variable_temperature_setting": "98",
            "variable_cleaning_mode": "on",
            "variable_unlock_status": "unlocked",
            "variable_reduce_chlorine": "off",
            "variable_timer_setting": "off"
        },
        "important_target_states": {
            "variable_temperature_setting": "98",
            "variable_unlock_status": "unlocked"
        },
        "optimal_step_size": 5,
    },
    {
        "id": 2,
        "command": "Adjust the water temperature to 85°C for green tea.",
        "target_state": {
            "variable_temperature_setting": "85",
            "variable_cleaning_mode": "on",
            "variable_unlock_status": "locked",
            "variable_reduce_chlorine": "off",
            "variable_timer_setting": "off"
        },
        "important_target_states": {
            "variable_temperature_setting": "85"
        },
        "optimal_step_size": 4,
    },
    {
        "id": 3,
        "command": "Select 60°C to mix milk.",
        "target_state": {
            "variable_temperature_setting": "60",
            "variable_cleaning_mode": "on",
            "variable_unlock_status": "locked",
            "variable_reduce_chlorine": "off",
            "variable_timer_setting": "off"
        },
        "important_target_states": {
            "variable_temperature_setting": "60"
        },
        "optimal_step_size": 1,
    },
    {
        "id": 4,
        "command": "Set the dispenser to 60°C, then unlock the dispenser and pour some water.",
        "target_state": {
            "variable_temperature_setting": "60",
            "variable_cleaning_mode": "on",
            "variable_unlock_status": "unlocked",
            "variable_reduce_chlorine": "off",
            "variable_timer_setting": "off"
        },
        "important_target_states": {
            "variable_temperature_setting": "60",
            "variable_unlock_status": "unlocked"
        },
        "optimal_step_size": 3,
    },
    {
        "id": 5,
        "command": "Choose 98°C as the boiling temperature.",
        "target_state": {
            "variable_temperature_setting": "98",
            "variable_cleaning_mode": "on",
            "variable_unlock_status": "locked",
            "variable_reduce_chlorine": "off",
            "variable_timer_setting": "off"
        },
        "important_target_states": {
            "variable_temperature_setting": "98"
        },
        "optimal_step_size": 5,
    },
    {
        "id": 6,
        "command": "Set the temperature to 85°C, then unlock the dispenser and pour some water.",
        "target_state": {
            "variable_temperature_setting": "85",
            "variable_cleaning_mode": "on",
            "variable_unlock_status": "unlocked",
            "variable_reduce_chlorine": "off",
            "variable_timer_setting": "off"
        },
        "important_target_states": {
            "variable_temperature_setting": "85",
            "variable_unlock_status": "unlocked"
        },
        "optimal_step_size": 4,
    },
    {
        "id": 7,
        "command": "Set water to boil at 98°C, then unlock the dispenser and pour some water.",
        "target_state": {
            "variable_temperature_setting": "98",
            "variable_cleaning_mode": "on",
            "variable_unlock_status": "unlocked",
            "variable_reduce_chlorine": "off",
            "variable_timer_setting": "off"
        },
        "important_target_states": {
            "variable_temperature_setting": "98",
            "variable_unlock_status": "unlocked"
        },
        "optimal_step_size": 5,
    },
    {
        "id": 8,
        "command": "Select 60°C as the temperature, then unlock the dispenser and pour some water.",
        "target_state": {
            "variable_temperature_setting": "60",
            "variable_cleaning_mode": "on",
            "variable_unlock_status": "unlocked",
            "variable_reduce_chlorine": "off",
            "variable_timer_setting": "off"
        },
        "important_target_states": {
            "variable_temperature_setting": "60",
            "variable_unlock_status": "unlocked"
        },
        "optimal_step_size": 3,
    },
    {
        "id": 9,
        "command": "Enable the timer.",
        "target_state": {
            "variable_temperature_setting": "0",
            "variable_cleaning_mode": "on",
            "variable_unlock_status": "locked",
            "variable_reduce_chlorine": "off",
            "variable_timer_setting": "on"
        },
        "important_target_states": {
            "variable_reduce_chlorine": "timer"
        },
        "optimal_step_size": 1,
    },
    {
        "id": 10,
        "command": "Turn on the reduce chlorine feature.",
        "target_state": {
            "variable_temperature_setting": "0",
            "variable_cleaning_mode": "on",
            "variable_unlock_status": "locked",
            "variable_reduce_chlorine": "on",
            "variable_timer_setting": "off"
        },
        "important_target_states": {
            "variable_reduce_chlorine": "chlorine"
        },
        "optimal_step_size": 2,
    }
]