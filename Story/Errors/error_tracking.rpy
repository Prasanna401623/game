init python:
    # List of errors to choose from
    error_options = ["Infinite Loop", "Logic Error", "Off-By-One Error", "Pre-Test Logic Error"]

    # Function to remove an error from the list
    def remove_error(error_name):
        """Removes an error from error_options list if it exists."""
        global error_options  # Make sure we modify the global variable
        if error_name in error_options:
            error_options.remove(error_name)
