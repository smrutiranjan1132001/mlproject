#!/bin/bash

echo "Setting up Streamlit config..."

mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"smruti1132001@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = \$PORT\n\
" > ~/.streamlit/config.toml

echo "Streamlit config setup done."
