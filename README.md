# Interpolation and Numerical Methods

This repository contains Python code for various interpolation and numerical methods implemented as part of an assignment.

## How to Run

To run the program, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Navigate to the root directory of the project.
3. Install the required dependencies by running the following command:
pip3 install -r requirements.txt
4. Once the dependencies are installed, you can execute the program by running the following command:
python3 -m src.test.test_assignment_2

This command runs the test script `test_assignment_2.py` located in the `src/test` directory.

## Description

This codebase provides implementations for the following numerical methods:

- Neville's Algorithm for polynomial interpolation.
- Newton's Forward Difference Method for polynomial interpolation.
- Hermite Divided Difference Method for polynomial interpolation with derivatives.
- Cubic Spline Interpolation.

Each method is implemented as a separate module under the `src/main` directory. The test cases for these methods can be found in the `src/test` directory.

## File Structure

- `src/main`: Contains the implementations of the numerical methods.
- `src/test`: Contains the test cases for the implemented methods.
- `requirements.txt`: Lists the dependencies required to run the code.
- `README.md`: This file, providing an overview of the project and instructions for running the code.