# GCP IAM Security Insight Analyzer

This project identifies risky IAM role bindings and overly permissive access in a Google Cloud Platform (GCP) project.

## Features
- Uses Cloud Asset Inventory API to export IAM policies
- Analyzes roles to identify high-privilege assignments (e.g., Owner, Editor)
- Outputs recommendations to reduce excessive access

## Files
- `analyze_iam.py`: Main script for analyzing IAM bindings
- `sample_iam_policy.json`: Example IAM policy input
- `README.md`: Setup and usage instructions
