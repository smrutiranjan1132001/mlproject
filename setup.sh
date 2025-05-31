#!/bin/bash

# Create the .streamlit directory in the home folder
mkdir -p ~/.streamlit/

# Write the credentials file
cat <<EOF > ~/.streamlit/credentials.toml
[general]
email = "your-email@example.com"
EOF

# Write the config file
cat <<EOF > ~/.streamlit/config.toml
[server]
headless = true
enableCORS = false
port = \$PORT
EOF
