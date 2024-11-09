import pandas as pd
import time
import os
import shutil
#data type of the column is specified to avoid warning
d_spec = {"chr" : object,"strand" :object,"gene_ID" : object,
"transcript_ID": object,"intron_ID": int,"sj5start" : int,
"sj5end" : int,"sj5_cov_nonsplit" : int,
"sj5_cov_split" : int,"sj3start" : int,"sj3end" : int,"sj3_cov_nonsplit" : int,
"sj3_cov_split" : int,"score" : float}
#result folder identifier
folder_ident = "range"  
# threshold range to filter genes from result
threshold_lower = 0.85
threshold_upper = 1

# getting current working directory and creating new result dir
c_dir = os.getcwd().replace("\\","/")
c_dir = c_dir+f"/script_result_{folder_ident}"

print("checking if path exist!..")
if os.path.exists(c_dir):
  print(f"{c_dir}->please delete existing folder:")
  exit()
else:
  print("making result directory...")
  os.makedirs(c_dir)
#my tsv result files are name ,output(sample identifier)_(filter level)
# my sample identifier range from 43-52, which used to loop through them
for i in [43,44,45,46,47]:
    for j in [48,49,50,51,52]:
      if i==j:
        continue
      else:
        start_time=time.time()
        #gettin output tsv file path
        file_n1 = f"C:/Users/BIRYANI_31/Desktop/b31_results/output{i}_1.tsv"
        file_n2 = f"C:/Users/BIRYANI_31/Desktop/b31_results/output{j}_1.tsv"

        # file -> data frames
        df1 = pd.read_csv(file_n1, sep="\t",dtype=d_spec)
        df2 = pd.read_csv(file_n2, sep="\t",dtype=d_spec)
        
        print("merging two data_frames on [transcript_ID, gene_ID]")
        merged_df = pd.merge(df1, df2, on=["transcript_ID","gene_ID"], how="inner")

        print("calculating score_ difference...")
        # utilizing panda vector operation to caluclate diff -> col[score_difference]
        merged_df["score_difference"] = merged_df["score_x"] - merged_df["score_y"]
        print("--|difference calculated!|--")

        #filtering rows based on threshold and storing in new df
        if threshold_lower and threshold_upper:
          filtered_df = merged_df[ (abs(merged_df["score_difference"]) >= threshold_lower) & 
                                  (abs(merged_df["score_difference"]) <= threshold_upper) ]
          # filtered_df = merged_df[abs(merged_df["score_difference"]) >= threshold]
        else:
          print("|please enter a threshold value|")
          filtered_df = merged_df.copy()  # Keep all transcripts
        # storing required column in new df
        p_df = filtered_df[[ "gene_ID","transcript_ID","score_x","score_y","score_difference"]]
        # removing duplicate gene and transcript id
        gene_id_list = set(filtered_df["gene_ID"].tolist())
        trans_id_list = set(filtered_df["transcript_ID"].tolist())
        # data frame with unique genes and transcript ID
        unq_gt = pd.DataFrame(list(zip(list(gene_id_list),list(trans_id_list))),columns =["g_ID","t_ID"])
        
        #saving to output files
        print("saving >> output.tsv")
        
        # geneid transid score-x score-y score-diff
        p_df.to_csv(f"{c_dir}/{i}_{j}_diff.tsv", sep="\t", index=False)
        # file with unique g_id and t_id
        unq_gt.to_csv(f"{c_dir}/{i}_{j}_unq.tsv", sep="\t", index=False)
        
        # time delay (to make folders)
        for p in range(3):
          time.sleep(1)
          print(f"time delay(mkdir):{p}",end="\r")
        print("\nmaking dir...")
        
        #2 out files for each run , stored to dir with sample 1&2
        if os.path.exists(f"{c_dir}/{i}_{j}"):
          print(f"file_name:{i}_{j} already exists,please change or delete them.\t breaking loop... ")
          break
        else:
          os.makedirs(f"{c_dir}/{i}_{j}")
          
        #time delay before moving them
        for k in range(3):
          time.sleep(1)
          print(f"time delay(mov):{p}",end="\r")
        # moving result files to repective directory
        print("\nmoving files...")
        shutil.move(f"{c_dir}/{i}_{j}_diff.tsv",f"{c_dir}/{i}_{j}")
        shutil.move(f"{c_dir}/{i}_{j}_unq.tsv",f"{c_dir}/{i}_{j}")
        end_time = time.time()
        time_elapsed = end_time - start_time
        print(f"Time taken: {time_elapsed:.2f} seconds")

print(f"|COMPLETED|\n result -> {c_dir}")

      



