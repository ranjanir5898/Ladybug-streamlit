{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "63097925",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv(\"RTA Dataset.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "413230f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Day_of_week</th>\n",
       "      <th>Age_band_of_driver</th>\n",
       "      <th>Sex_of_driver</th>\n",
       "      <th>Educational_level</th>\n",
       "      <th>Vehicle_driver_relation</th>\n",
       "      <th>Driving_experience</th>\n",
       "      <th>Type_of_vehicle</th>\n",
       "      <th>Owner_of_vehicle</th>\n",
       "      <th>Service_year_of_vehicle</th>\n",
       "      <th>Defect_of_vehicle</th>\n",
       "      <th>...</th>\n",
       "      <th>Casualty_class</th>\n",
       "      <th>Sex_of_casualty</th>\n",
       "      <th>Age_band_of_casualty</th>\n",
       "      <th>Casualty_severity</th>\n",
       "      <th>Work_of_casuality</th>\n",
       "      <th>Fitness_of_casuality</th>\n",
       "      <th>Pedestrian_movement</th>\n",
       "      <th>Cause_of_accident</th>\n",
       "      <th>Accident_severity</th>\n",
       "      <th>Hour_of_Day</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Monday</td>\n",
       "      <td>18-30</td>\n",
       "      <td>Male</td>\n",
       "      <td>Above high school</td>\n",
       "      <td>Employee</td>\n",
       "      <td>1-2yr</td>\n",
       "      <td>Automobile</td>\n",
       "      <td>Owner</td>\n",
       "      <td>Above 10yr</td>\n",
       "      <td>No defect</td>\n",
       "      <td>...</td>\n",
       "      <td>na</td>\n",
       "      <td>na</td>\n",
       "      <td>na</td>\n",
       "      <td>na</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Not a Pedestrian</td>\n",
       "      <td>Moving Backward</td>\n",
       "      <td>Slight Injury</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Monday</td>\n",
       "      <td>31-50</td>\n",
       "      <td>Male</td>\n",
       "      <td>Junior high school</td>\n",
       "      <td>Employee</td>\n",
       "      <td>Above 10yr</td>\n",
       "      <td>Public (&gt; 45 seats)</td>\n",
       "      <td>Owner</td>\n",
       "      <td>5-10yrs</td>\n",
       "      <td>No defect</td>\n",
       "      <td>...</td>\n",
       "      <td>na</td>\n",
       "      <td>na</td>\n",
       "      <td>na</td>\n",
       "      <td>na</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Not a Pedestrian</td>\n",
       "      <td>Overtaking</td>\n",
       "      <td>Slight Injury</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Monday</td>\n",
       "      <td>18-30</td>\n",
       "      <td>Male</td>\n",
       "      <td>Junior high school</td>\n",
       "      <td>Employee</td>\n",
       "      <td>1-2yr</td>\n",
       "      <td>Lorry (41?100Q)</td>\n",
       "      <td>Owner</td>\n",
       "      <td>NaN</td>\n",
       "      <td>No defect</td>\n",
       "      <td>...</td>\n",
       "      <td>Driver or rider</td>\n",
       "      <td>Male</td>\n",
       "      <td>31-50</td>\n",
       "      <td>3</td>\n",
       "      <td>Driver</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Not a Pedestrian</td>\n",
       "      <td>Changing lane to the left</td>\n",
       "      <td>Serious Injury</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Sunday</td>\n",
       "      <td>18-30</td>\n",
       "      <td>Male</td>\n",
       "      <td>Junior high school</td>\n",
       "      <td>Employee</td>\n",
       "      <td>5-10yr</td>\n",
       "      <td>Public (&gt; 45 seats)</td>\n",
       "      <td>Governmental</td>\n",
       "      <td>NaN</td>\n",
       "      <td>No defect</td>\n",
       "      <td>...</td>\n",
       "      <td>Pedestrian</td>\n",
       "      <td>Female</td>\n",
       "      <td>18-30</td>\n",
       "      <td>3</td>\n",
       "      <td>Driver</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Not a Pedestrian</td>\n",
       "      <td>Changing lane to the right</td>\n",
       "      <td>Slight Injury</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Sunday</td>\n",
       "      <td>18-30</td>\n",
       "      <td>Male</td>\n",
       "      <td>Junior high school</td>\n",
       "      <td>Employee</td>\n",
       "      <td>2-5yr</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Owner</td>\n",
       "      <td>5-10yrs</td>\n",
       "      <td>No defect</td>\n",
       "      <td>...</td>\n",
       "      <td>na</td>\n",
       "      <td>na</td>\n",
       "      <td>na</td>\n",
       "      <td>na</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Not a Pedestrian</td>\n",
       "      <td>Overtaking</td>\n",
       "      <td>Slight Injury</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 32 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "  Day_of_week Age_band_of_driver Sex_of_driver   Educational_level  \\\n",
       "0      Monday              18-30          Male   Above high school   \n",
       "1      Monday              31-50          Male  Junior high school   \n",
       "2      Monday              18-30          Male  Junior high school   \n",
       "3      Sunday              18-30          Male  Junior high school   \n",
       "4      Sunday              18-30          Male  Junior high school   \n",
       "\n",
       "  Vehicle_driver_relation Driving_experience      Type_of_vehicle  \\\n",
       "0                Employee              1-2yr           Automobile   \n",
       "1                Employee         Above 10yr  Public (> 45 seats)   \n",
       "2                Employee              1-2yr      Lorry (41?100Q)   \n",
       "3                Employee             5-10yr  Public (> 45 seats)   \n",
       "4                Employee              2-5yr                  NaN   \n",
       "\n",
       "  Owner_of_vehicle Service_year_of_vehicle Defect_of_vehicle  ...  \\\n",
       "0            Owner              Above 10yr         No defect  ...   \n",
       "1            Owner                 5-10yrs         No defect  ...   \n",
       "2            Owner                     NaN         No defect  ...   \n",
       "3     Governmental                     NaN         No defect  ...   \n",
       "4            Owner                 5-10yrs         No defect  ...   \n",
       "\n",
       "    Casualty_class Sex_of_casualty Age_band_of_casualty Casualty_severity  \\\n",
       "0               na              na                   na                na   \n",
       "1               na              na                   na                na   \n",
       "2  Driver or rider            Male                31-50                 3   \n",
       "3       Pedestrian          Female                18-30                 3   \n",
       "4               na              na                   na                na   \n",
       "\n",
       "  Work_of_casuality Fitness_of_casuality Pedestrian_movement  \\\n",
       "0               NaN                  NaN    Not a Pedestrian   \n",
       "1               NaN                  NaN    Not a Pedestrian   \n",
       "2            Driver                  NaN    Not a Pedestrian   \n",
       "3            Driver               Normal    Not a Pedestrian   \n",
       "4               NaN                  NaN    Not a Pedestrian   \n",
       "\n",
       "            Cause_of_accident Accident_severity  Hour_of_Day  \n",
       "0             Moving Backward     Slight Injury           17  \n",
       "1                  Overtaking     Slight Injury           17  \n",
       "2   Changing lane to the left    Serious Injury           17  \n",
       "3  Changing lane to the right     Slight Injury            1  \n",
       "4                  Overtaking     Slight Injury            1  \n",
       "\n",
       "[5 rows x 32 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# convert object type column into datetime datatype column\n",
    "df['Time'] = pd.to_datetime(df['Time'])\n",
    "\n",
    "# Extrating 'Hour_of_Day' feature from the Time column\n",
    "new_df = df.copy()\n",
    "new_df['Hour_of_Day'] = new_df['Time'].dt.hour\n",
    "n_df = new_df.drop('Time', axis=1)\n",
    "n_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5b7c6052",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "17"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# feature selection based on visualization (to_be_continue)\n",
    "features = ['Day_of_week','Number_of_vehicles_involved','Number_of_casualties','Area_accident_occured',\n",
    "      'Types_of_Junction','Age_band_of_driver','Sex_of_driver','Educational_level',\n",
    "      'Vehicle_driver_relation','Type_of_vehicle','Driving_experience','Service_year_of_vehicle','Type_of_collision',\n",
    "      'Sex_of_casualty','Age_band_of_casualty','Cause_of_accident','Hour_of_Day']\n",
    "len(features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "203e2a43",
   "metadata": {},
   "outputs": [],
   "source": [
    "# new dataframe generated\n",
    "featureset_df = n_df[features]\n",
    "target = n_df['Accident_severity']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5b7e2343",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 12316 entries, 0 to 12315\n",
      "Data columns (total 17 columns):\n",
      " #   Column                       Non-Null Count  Dtype \n",
      "---  ------                       --------------  ----- \n",
      " 0   Day_of_week                  12316 non-null  object\n",
      " 1   Number_of_vehicles_involved  12316 non-null  int64 \n",
      " 2   Number_of_casualties         12316 non-null  int64 \n",
      " 3   Area_accident_occured        12077 non-null  object\n",
      " 4   Types_of_Junction            11429 non-null  object\n",
      " 5   Age_band_of_driver           12316 non-null  object\n",
      " 6   Sex_of_driver                12316 non-null  object\n",
      " 7   Educational_level            11575 non-null  object\n",
      " 8   Vehicle_driver_relation      11737 non-null  object\n",
      " 9   Type_of_vehicle              11366 non-null  object\n",
      " 10  Driving_experience           11487 non-null  object\n",
      " 11  Service_year_of_vehicle      8388 non-null   object\n",
      " 12  Type_of_collision            12161 non-null  object\n",
      " 13  Sex_of_casualty              12316 non-null  object\n",
      " 14  Age_band_of_casualty         12316 non-null  object\n",
      " 15  Cause_of_accident            12316 non-null  object\n",
      " 16  Hour_of_Day                  12316 non-null  int64 \n",
      "dtypes: int64(3), object(14)\n",
      "memory usage: 1.6+ MB\n"
     ]
    }
   ],
   "source": [
    "# metadata of the new sub dataset\n",
    "featureset_df.info()\n",
    "feature_df = featureset_df.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "57abaa19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 12316 entries, 0 to 12315\n",
      "Data columns (total 17 columns):\n",
      " #   Column                       Non-Null Count  Dtype \n",
      "---  ------                       --------------  ----- \n",
      " 0   Day_of_week                  12316 non-null  object\n",
      " 1   Number_of_vehicles_involved  12316 non-null  int64 \n",
      " 2   Number_of_casualties         12316 non-null  int64 \n",
      " 3   Area_accident_occured        12316 non-null  object\n",
      " 4   Types_of_Junction            12316 non-null  object\n",
      " 5   Age_band_of_driver           12316 non-null  object\n",
      " 6   Sex_of_driver                12316 non-null  object\n",
      " 7   Educational_level            12316 non-null  object\n",
      " 8   Vehicle_driver_relation      12316 non-null  object\n",
      " 9   Type_of_vehicle              12316 non-null  object\n",
      " 10  Driving_experience           12316 non-null  object\n",
      " 11  Service_year_of_vehicle      12316 non-null  object\n",
      " 12  Type_of_collision            12316 non-null  object\n",
      " 13  Sex_of_casualty              12316 non-null  object\n",
      " 14  Age_band_of_casualty         12316 non-null  object\n",
      " 15  Cause_of_accident            12316 non-null  object\n",
      " 16  Hour_of_Day                  12316 non-null  int64 \n",
      "dtypes: int64(3), object(14)\n",
      "memory usage: 1.6+ MB\n"
     ]
    }
   ],
   "source": [
    "# NaN are missing because service info might not be available, we will fill as 'Unknown'\n",
    "feature_df['Service_year_of_vehicle'] = feature_df['Service_year_of_vehicle'].fillna('Unknown')\n",
    "feature_df['Types_of_Junction'] = feature_df['Types_of_Junction'].fillna('Unknown')\n",
    "feature_df['Area_accident_occured'] = feature_df['Area_accident_occured'].fillna('Unknown')\n",
    "feature_df['Driving_experience'] = feature_df['Driving_experience'].fillna('unknown')\n",
    "feature_df['Type_of_vehicle'] = feature_df['Type_of_vehicle'].fillna('Other')\n",
    "feature_df['Vehicle_driver_relation'] = feature_df['Vehicle_driver_relation'].fillna('Unknown')\n",
    "feature_df['Educational_level'] = feature_df['Educational_level'].fillna('Unknown')\n",
    "feature_df['Type_of_collision'] = feature_df['Type_of_collision'].fillna('Unknown')\n",
    "\n",
    "# features information\n",
    "feature_df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "424f50b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(12316, 106)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# setting input features X and target y \n",
    "X = feature_df[features] # here features are selected from 'object' datatype\n",
    "y = n_df['Accident_severity']\n",
    "\n",
    "# we will use pandas get_dummies method for on-hot encoding\n",
    "encoded_df = pd.get_dummies(X, drop_first=True)\n",
    "encoded_df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "83715779",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Encoded labels: ['Fatal injury' 'Serious Injury' 'Slight Injury']\n"
     ]
    }
   ],
   "source": [
    "# import labelencoder from sklearn.preprocessing\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "# create labelencoder object\n",
    "lb = LabelEncoder()\n",
    "lb.fit(y)\n",
    "y_encoded = lb.transform(y)\n",
    "print(\"Encoded labels:\",lb.classes_)\n",
    "y_en = pd.Series(y_encoded)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2ea444f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# feature selection method using chi2 for categorical output, categorical input\n",
    "from sklearn.feature_selection import SelectKBest, chi2\n",
    "fs = SelectKBest(chi2, k=50)\n",
    "X_new = fs.fit_transform(encoded_df, y_en)\n",
    "\n",
    "# Take the selected features\n",
    "cols = fs.get_feature_names_out()\n",
    "\n",
    "# convert selected features into dataframe\n",
    "fs_df = pd.DataFrame(X_new, columns=cols)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9e02951b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/kuttima/.local/lib/python3.11/site-packages/imblearn/over_sampling/_smote/base.py:572: FutureWarning: The parameter `n_jobs` has been deprecated in 0.10 and will be removed in 0.12. You can pass an nearest neighbors estimator where `n_jobs` is already set instead.\n",
      "  warnings.warn(\n",
      "/home/kuttima/.local/lib/python3.11/site-packages/imblearn/over_sampling/_smote/base.py:336: FutureWarning: The parameter `n_jobs` has been deprecated in 0.10 and will be removed in 0.12. You can pass an nearest neighbors estimator where `n_jobs` is already set instead.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "((31245, 50), (31245,))"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "# importing the SMOTENC object from imblearn library \n",
    "from imblearn.over_sampling import SMOTENC\n",
    "\n",
    "# categorical features for SMOTENC technique for categorical features\n",
    "n_cat_index = np.array(range(3,50))\n",
    "\n",
    "# creating smote object with SMOTENC class\n",
    "smote = SMOTENC(categorical_features=n_cat_index, random_state=42, n_jobs=True)\n",
    "X_n, y_n = smote.fit_resample(fs_df,y_en)\n",
    "\n",
    "# print the shape of new upsampled dataset\n",
    "X_n.shape, y_n.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "60236ec7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2    10415\n",
      "1    10415\n",
      "0    10415\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# print the target classes distribution\n",
    "print(y_n.value_counts())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "b558c29d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9425108017282765"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# import the necessary libraries\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import confusion_matrix, classification_report, f1_score\n",
    "\n",
    "# train and test split and building baseline model to predict target features\n",
    "X_trn, X_tst, y_trn, y_tst = train_test_split(X_n, y_n, test_size=0.2, random_state=42)\n",
    "\n",
    "# modelling using random forest baseline\n",
    "rf = RandomForestClassifier(n_estimators=800, max_depth=20, random_state=42)\n",
    "rf.fit(X_trn, y_trn)\n",
    "\n",
    "# predicting on test data\n",
    "predics = rf.predict(X_tst)\n",
    "\n",
    "# train score \n",
    "rf.score(X_trn, y_trn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "59484cb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Submission by: Ladybug\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.95      0.96      0.95      2085\n",
      "           1       0.84      0.83      0.84      2100\n",
      "           2       0.86      0.86      0.86      2064\n",
      "\n",
      "    accuracy                           0.88      6249\n",
      "   macro avg       0.88      0.88      0.88      6249\n",
      "weighted avg       0.88      0.88      0.88      6249\n",
      "\n"
     ]
    }
   ],
   "source": [
    "stackup_username = \"Ladybug\"\n",
    "print(\"Submission by:\", stackup_username)\n",
    "\n",
    "# classification report on test dataset\n",
    "classif_re = classification_report(y_tst,predics)\n",
    "print(classif_re)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "6cd2990e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8835332005395422\n"
     ]
    }
   ],
   "source": [
    "# f1_score of the model\n",
    "f1score = f1_score(y_tst,predics, average='weighted')\n",
    "print(f1score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "06454976",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['ordinal_encoder2.joblib']"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# selecting 7 categorical features from the dataframe\n",
    "import joblib\n",
    "from sklearn.preprocessing import OrdinalEncoder\n",
    "\n",
    "new_fea_df = feature_df[['Type_of_collision','Age_band_of_driver','Sex_of_driver',\n",
    "    'Educational_level','Service_year_of_vehicle','Day_of_week','Area_accident_occured']]\n",
    "\n",
    "oencoder2 = OrdinalEncoder()\n",
    "encoded_df3 = pd.DataFrame(oencoder2.fit_transform(new_fea_df))\n",
    "encoded_df3.columns = new_fea_df.columns\n",
    "\n",
    "# save the ordinal encoder object for inference pipeline\n",
    "joblib.dump(oencoder2, \"ordinal_encoder2.joblib\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "89f6a56f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['rta_model_deploy3.joblib']"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# final dataframe to be trained for model inference\n",
    "s_final_df = pd.concat([feature_df[['Number_of_vehicles_involved','Number_of_casualties','Hour_of_Day']],encoded_df3], axis=1)\n",
    "\n",
    "# train and test split and building baseline model to predict target features\n",
    "X_trn2, X_tst2, y_trn2, y_tst2 = train_test_split(s_final_df, y_en, test_size=0.2, random_state=42)\n",
    "\n",
    "# modelling using random forest baseline\n",
    "rf = RandomForestClassifier(n_estimators=700, max_depth=20, random_state=42)\n",
    "rf.fit(X_trn2, y_trn2)\n",
    "\n",
    "# save the model object\n",
    "joblib.dump(rf, \"rta_model_deploy3.joblib\", compress=9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "159036f4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "ed95dc85",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8c31c59",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b2261c8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90e61497",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa89ef63",
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
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
