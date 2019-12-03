# facebook-motif-analysis

This repository is a modification of Stanford's SNAP library to support Node-attribute-based motif identification. 

### Key points
1. Python scripts are used for pre-processing the data.
2. It works for the Facebook100 dataset
3. To run the C++ file:

```
cd snap-higher-order/examples/motifcluster
make
./motifclustermain -i:[edgelist_file] -m:M4 -n:[nodelist_file] (OR) python generate_motifs.py
```
