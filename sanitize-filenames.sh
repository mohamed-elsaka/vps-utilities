#!/bin/bash 
eval "renamer --regex --find '[^a-zA-Z0-9\\.\\-\+]' --replace '_' '**'";
eval "renamer --regex --find '[_]{1,}' --replace '_' '**'";
