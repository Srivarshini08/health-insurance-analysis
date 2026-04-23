{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0b51188d-42a1-4f5d-8fab-0a1fdaf1cc24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data cleaned and saved to:\n",
      "C:\\health-insurance-analysis\\data\\cleaned_insurance_data.csv\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "# File paths\n",
    "input_path = r\"C:\\health-insurance-analysis\\data\\health_insurance_cost_and_risk_dataset.csv\"\n",
    "output_path = r\"C:\\health-insurance-analysis\\data\\cleaned_insurance_data.csv\"\n",
    "\n",
    "# Load dataset\n",
    "df = pd.read_csv(input_path)\n",
    "\n",
    "# 1. Basic Cleaning\n",
    "\n",
    "# Normalize text columns\n",
    "df['sex'] = df['sex'].astype(str).str.lower().str.strip()\n",
    "df['smoker'] = df['smoker'].astype(str).str.lower().str.strip()\n",
    "df['exercise_frequency'] = df['exercise_frequency'].astype(str).str.strip().str.capitalize()\n",
    "df['occupation_risk'] = df['occupation_risk'].astype(str).str.lower().str.strip()\n",
    "\n",
    "# 2. Handle Missing Values\n",
    "\n",
    "df['age'] = df['age'].fillna(df['age'].mean())\n",
    "df['bmi'] = df['bmi'].fillna(df['bmi'].median())\n",
    "df['children'] = df['children'].fillna(df['children'].mode()[0])\n",
    "\n",
    "# 3. Encode Categorical Columns\n",
    "\n",
    "df['sex'] = df['sex'].map({'male': 0, 'female': 1})\n",
    "df['smoker'] = df['smoker'].map({'no': 0, 'yes': 1})\n",
    "\n",
    "df['exercise_frequency'] = df['exercise_frequency'].map({\n",
    "    'Never': 0,\n",
    "    'Rarely': 1,\n",
    "    'Weekly': 2\n",
    "})\n",
    "\n",
    "df['occupation_risk'] = df['occupation_risk'].map({\n",
    "    'low': 0,\n",
    "    'moderate': 1,\n",
    "    'high': 2\n",
    "})\n",
    "\n",
    "# Convert boolean to int\n",
    "df['pre_existing_condition'] = df['pre_existing_condition'].astype(int)\n",
    "\n",
    "# One-hot encoding for region\n",
    "df = pd.get_dummies(df, columns=['region'], drop_first=True)\n",
    "\n",
    "# 4. Final Cleaning\n",
    "\n",
    "df = df.drop_duplicates()\n",
    "df = df.fillna(0)\n",
    "df['children'] = df['children'].astype(int)\n",
    "\n",
    "# 5. Save Cleaned Data\n",
    "# Ensure directory exists\n",
    "os.makedirs(r\"C:\\health-insurance-analysis\\data\", exist_ok=True)\n",
    "\n",
    "df.to_csv(output_path, index=False)\n",
    "\n",
    "print(\"Data cleaned and saved to:\")\n",
    "print(output_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38f9b43e-d57a-46ae-ae54-aedcf6450163",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
