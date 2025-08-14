# model_template
This is a template repository for (groundwater) models created with ZLFLO.

## Repository Description

This repository provides a starting point for building groundwater models using the zeelandflow framework. It includes example configurations, documentation, and scripts to help users set up, run, and analyze groundwater simulations efficiently.

### What to do yourself when using this template
- Fill the pyproject.toml with your projecct dependencies.
- Change `run_model.py` file in the .github/workflows directory such that it runs all the model files in the `src` directory.
- Change the defaults (`extent`, `model_name` etc.) in the settings.py in the scripts (`src`) directory.


#### Workflows and GitHub actions
This repository includes several GitHub Actions workflows:

- **Model Run Workflow:** Automatically runs the model when changes are pushed to the main branch or when a pull request is opened. You can customize this workflow to fit your model's requirements.
- **Linting and Testing Workflow:** Checks code quality and runs tests to ensure reliability and maintainability of your scripts.
- **Files Workflow** Tests if the files extensions are allowed and if the file size is not larger than 5MB.
