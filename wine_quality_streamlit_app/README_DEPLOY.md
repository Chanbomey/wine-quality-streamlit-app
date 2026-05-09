# Streamlit Deployment Instructions

## Files needed in your GitHub repo
- `app.py`
- `requirements.txt`
- `winequality-red.csv`

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Push these files to a public GitHub repository.
2. Go to Streamlit Community Cloud.
3. Click **New app**.
4. Select your GitHub repo.
5. Set the main file path to `app.py`.
6. Click **Deploy**.

## Important
The app expects the dataset file to be named exactly:

```text
winequality-red.csv
```

Place it in the same folder as `app.py`.
