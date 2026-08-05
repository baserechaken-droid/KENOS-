RESPONSES = {

    "battery": {
        "prefix": "Battery status checked."
    },

    "time": {
        "prefix": "The current time is."
    },

    "torch_on": {
        "text": "Flashlight activated."
    },

    "torch_off": {
        "text": "Flashlight switched off."
    },

    "shutdown": {
        "text": "KenOS shutting down."
    }

}



def get_response(key, default=None):

    return RESPONSES.get(
        key,
        default
    )
