[
    {
        "command": "Turn on the dehumidifier and set the humidity to 50%.",
        "id": 1,
        "important_target_states": {
            "variable_humidity": "50",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 4,
        "target_state": {
            "child_lock": "unlocked",
            "sleep": "off",
            "temperature_unit": "Celsius",
            "variable_anion": "off",
            "variable_humidity": "50",
            "variable_internal_drying": "off",
            "variable_mode": "auto dehumidification",
            "variable_power_on_off": "on",
            "variable_swing": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Switch on the dehumidifier and activate continuous dehumidification mode.",
        "id": 2,
        "important_target_states": {
            "variable_mode": "continuous dehumidification",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "child_lock": "unlocked",
            "sleep": "off",
            "temperature_unit": "Celsius",
            "variable_anion": "off",
            "variable_humidity": "0",
            "variable_internal_drying": "off",
            "variable_mode": "continuous dehumidification",
            "variable_power_on_off": "on",
            "variable_swing": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Enable the dehumidifier and initiate the internal drying function.",
        "id": 3,
        "important_target_states": {
            "variable_internal_drying": "on",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "child_lock": "unlocked",
            "sleep": "off",
            "temperature_unit": "Celsius",
            "variable_anion": "off",
            "variable_humidity": "0",
            "variable_internal_drying": "on",
            "variable_mode": "auto dehumidification",
            "variable_power_on_off": "on",
            "variable_swing": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Turn on the dehumidifier and engage the anion function.",
        "id": 4,
        "important_target_states": {
            "variable_anion": "on",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "child_lock": "unlocked",
            "sleep": "off",
            "temperature_unit": "Celsius",
            "variable_anion": "on",
            "variable_humidity": "0",
            "variable_internal_drying": "off",
            "variable_mode": "auto dehumidification",
            "variable_power_on_off": "on",
            "variable_swing": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Switch on the dehumidifier and start air swing.",
        "id": 5,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_swing": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "child_lock": "unlocked",
            "sleep": "off",
            "temperature_unit": "Celsius",
            "variable_anion": "off",
            "variable_humidity": "0",
            "variable_internal_drying": "off",
            "variable_mode": "auto dehumidification",
            "variable_power_on_off": "on",
            "variable_swing": "on",
            "variable_timer": "0"
        }
    },
    {
        "command": "Power on the dehumidifier and set a timer to operate for 8 hours.",
        "id": 6,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_timer": "8"
        },
        "optimal_step_size": 9,
        "target_state": {
            "child_lock": "unlocked",
            "sleep": "off",
            "temperature_unit": "Celsius",
            "variable_anion": "off",
            "variable_humidity": "0",
            "variable_internal_drying": "off",
            "variable_mode": "auto dehumidification",
            "variable_power_on_off": "on",
            "variable_swing": "off",
            "variable_timer": "8"
        }
    },
    {
        "command": "Start the dehumidifier and adjust the humidity setting to 60%.",
        "id": 7,
        "important_target_states": {
            "variable_humidity": "60",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 6,
        "target_state": {
            "child_lock": "unlocked",
            "sleep": "off",
            "temperature_unit": "Celsius",
            "variable_anion": "off",
            "variable_humidity": "60",
            "variable_internal_drying": "off",
            "variable_mode": "auto dehumidification",
            "variable_power_on_off": "on",
            "variable_swing": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Turn on the dehumidifier and set it to purification mode.",
        "id": 8,
        "important_target_states": {
            "variable_mode": "purification",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 4,
        "target_state": {
            "child_lock": "unlocked",
            "sleep": "off",
            "temperature_unit": "Celsius",
            "variable_anion": "off",
            "variable_humidity": "0",
            "variable_internal_drying": "off",
            "variable_mode": "purification",
            "variable_power_on_off": "on",
            "variable_swing": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Activate the dehumidifier and leave it in ventilation mode.",
        "id": 9,
        "important_target_states": {
            "variable_mode": "ventilation",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 5,
        "target_state": {
            "child_lock": "unlocked",
            "sleep": "off",
            "temperature_unit": "Celsius",
            "variable_anion": "off",
            "variable_humidity": "0",
            "variable_internal_drying": "off",
            "variable_mode": "ventilation",
            "variable_power_on_off": "on",
            "variable_swing": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Switch on the dehumidifier and configure the timer to shut down after 3 hours.",
        "id": 10,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_timer": "3"
        },
        "optimal_step_size": 4,
        "target_state": {
            "child_lock": "unlocked",
            "sleep": "off",
            "temperature_unit": "Celsius",
            "variable_anion": "off",
            "variable_humidity": "0",
            "variable_internal_drying": "off",
            "variable_mode": "auto dehumidification",
            "variable_power_on_off": "on",
            "variable_swing": "off",
            "variable_timer": "3"
        }
    }
]
