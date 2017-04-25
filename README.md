RNA Editing

# Installation:

[Install Singularity](http://singularity.lbl.gov/)

[Download Executable](https://s3-us-west-1.amazonaws.com/rnaediting-0.0.2/rnaediting-0.0.2.img)

That's it!

### (Optional) Download Small Example Files
[Example BAM](https://github.com/YeoLab/rna_editing_pipeline/blob/master/example_data/example.bam)
[Example Reference](https://github.com/YeoLab/rna_editing_pipeline/blob/master/example_data/ce11.chrI.fa)
[Example Known SNPs](https://github.com/YeoLab/rna_editing_pipeline/blob/master/example_data/knownSNPs.bed)

[Example YAML](https://github.com/YeoLab/rna_editing_pipeline/blob/master/example_data/example-minimal.yml)
[Example YAML with optional arguments](https://github.com/YeoLab/rna_editing_pipeline/blob/master/example_data/example.yml)
# Running the Pipeline:
```
rnaediting example-minimal.yml
```

# Optional Arguments:
```
--junction_overhang (DEFAULT 10): filters reads that are split upon junctions that are not at least flanked by this number on either side
--edge_mutation (DEFAULT 5): filters reads that contain a mutation that lies on the 3' end of the read by this much
--non_ag (DEFAULT 1): filters reads that contains more than this number of non-AG (or TC depending on strand) mutations
--min_variant_coverage (DEFAULT 5): hard filter that removes variant sites supported by less than this number of reads
--alpha (DEFAULT 0): 'pseudocount' parameter. Use higher number for low coverage datasets (see: https://en.wikipedia.org/wiki/Beta_distribution)
--beta (DEFAULT 0): 'pseudocount' parameter. Use higher number for low coverage datasets (see: https://en.wikipedia.org/wiki/Beta_distribution)
--edit_fraction (DEFAULT 0.01): the minimum allowable edit fraction (higher fraction -> more stringent)
--dp (DEFAULT DP4): filters coverage based on either the "DP" flag or the "DP4" flag in a vcf file (see: https://www.biostars.org/p/46361/)
```