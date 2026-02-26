files = ["seq1", "seq2", "seq3", "seq4"]
date = "20/09/2007"

for name in files:

   new_name = name + date + ".fasta"

   print(f"{new_name}")
