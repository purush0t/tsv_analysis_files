import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import time

d_spec = {"chr" : object,"strand" :object,"gene_ID" : object,
"transcript_ID": object,"intron_ID": int,"sj5start" : int,
"sj5end" : int,"sj5_cov_nonsplit" : int,
"sj5_cov_split" : int,"sj3start" : int,"sj3end" : int,"sj3_cov_nonsplit" : int,
"sj3_cov_split" : int,"score" : float}

"""tsv_p = "C:/Users/BIRYANI_31/Desktop/b31_results"
for s in range(43,53):
    
    df1 = pd.read_csv(f"output{s}_1.tsv",sep="\t",dtype=d_spec)
    df1["sample"] = s
    p_df = df1[["score","sample"]]
# print(p_df)"""

# Directory containing the CSV files
directory = "C:/Users/BIRYANI_31/Desktop/b31_results"

# Initialize an empty dictionary to store data frames
dfs = {}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".tsv"):
        print(f"processing -> {filename}")
        # Extract the filename without extension
        name = os.path.splitext(filename)[0]
        print(f"saving data_frame -> dictionary")
        # Read the CSV file and store it in the dictionary with the key as the filename
        dfs[name] = pd.read_csv(os.path.join(directory,filename),sep="\t",dtype=d_spec)

print("converted tsv_files-> data_frames")
# Now you can access each data frame using dfs[name] where name is the filename without extension

# Example:
# If you have a file named "data1.csv", you can access its data frame using dfs["data1"]

print("plotting voilin graphs")
ccat_df = pd.DataFrame()

for df_name in dfs.keys():
    if df_name in ["output48_1","output49_1","output50_1","output51_1","output52_1"] :
        temp_df = dfs[df_name]
        temp_df["sample"] = df_name
        p_df = temp_df[["score","sample"]]
        ccat_df = pd.concat([ccat_df, p_df], ignore_index=True)
    else:
        continue
    # plt.figure(figsize=(10, 6))
    # # sns.violinplot(x="sample", y="score", data=p_df)
    # # plt.xlabel("sample")
    # # plt.ylabel("score")
    # # plt.show()
print(ccat_df)
plt.figure(figsize=(10, 6))
sns.violinplot(x="sample", y="score", data=ccat_df,color="gray")
plt.xlabel("sample")
plt.ylabel("score")
plt.show()

print("|completed|")


