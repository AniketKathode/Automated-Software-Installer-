#!/bin/bash

LOG_FILE="install_log.txt"
exec > >(tee -a "$LOG_FILE") 2>&1  # Redirect output to log file

echo "----- Script Execution: $(date) -----"

SOFTWARE_LIST=("git" "curl" "vim")

if [ "$1" == "1" ]; then
    echo "Running option 1..."
    for software in "${SOFTWARE_LIST[@]}"; do
        if dpkg -l | grep -q "$software"; then
            echo "$software is already installed."
        else
            echo "Installing $software..."
            sudo apt install -y "$software" && echo "$software installed successfully."
        fi
    done
    echo "Installation completed."

elif [ "$1" == "2" ]; then
    echo "Running option 2..."
    for software in "${SOFTWARE_LIST[@]}"; do
        if dpkg -l | grep -q "$software"; then
            echo "Removing $software..."
            sudo apt remove -y "$software" && echo "$software removed successfully."
        else
            echo "$software is not installed."
        fi
    done
    echo "Uninstallation completed."

else
    echo "Invalid option. Use 1 for install or 2 for uninstall."
    exit 1
fi
