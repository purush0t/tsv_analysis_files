import pandas as pd
import os
cc_unq_df = pd.DataFrame()

# this script is to all output together a give a final list of unique list of genes
#43,44,45,46,47,48,49,50,51,52

k= 44

for m in [51]:
    if k==m:
        print("same_sample check m and k values")
        exit()
    else:
        
        #use -> one( to concat output from script 1)
        r_dir = f"C:/Users/BIRYANI_31/Desktop/tsv_analysis/script_result_0.8_1/{k}_{m}/{k}_{m}_unq.tsv"
        
        #use -> two (to concat output from this script)
        # r_dir = f"C:/Users/BIRYANI_31/Desktop/tsv_analysis/unq_gene_0.8_1/uni_gt{m}.tsv"
        
        df1 = pd.read_csv(r_dir, sep="\t")
        print(f"reading file:{r_dir}")
        print(f"df:{df1.shape}")
        #stacking gene and trans id from all files
        cc_unq_df = pd.concat([df1,cc_unq_df],ignore_index=True)
        print(f"cc_unq:{cc_unq_df.shape}")

c_dir = os.getcwd().replace("\\","/")
#only taking gene ID ,if needed you can use the commented line to store trans_ID
#removing duplicate using set()
# gene_id_list = set(cc_unq_df["g_ID"].tolist())
trans_id_list = set(cc_unq_df["t_ID"].tolist())

# data frame for unique transcripts
g_t = pd.DataFrame(list(trans_id_list),columns =["t_ID"])
print(f"final_df_shape:{g_t.shape}")
print(f"saving result file:{c_dir}")



# # data frame for unique genes 
# g_t = pd.DataFrame(list(gene_id_list),columns =["g_ID"])
# print(f"final_df_shape:{g_t.shape}")
# print(f"saving result file:{c_dir}")

#transcripts final file
g_t.to_csv(f"uni_trans{k}.tsv",sep="\t", index=False)


#use ->1
# g_t.to_csv(f"uni_gt{k}.tsv", sep="\t", index=False)

#use -> 2
# g_t.to_csv(f"final_unqgenes_{k}.tsv", sep="\t", index=False)

print("completed")
