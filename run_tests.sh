#!/bin/bash

echo "====================================="
echo "Running all tests using python -m pytest"
echo "====================================="

python -m pytest

if [ $? -eq 0 ]; then
    echo "====================================="
    echo "All tests passed successfully!"
    echo "====================================="
else
    echo "====================================="
    echo "Some tests failed."
    echo "====================================="
fi