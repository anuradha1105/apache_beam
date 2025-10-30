# Apache Beam Data Engineering Demo

This repository contains Apache Beam assignment demonstrating the required Beam features in Google Colab using a virtual environment.

## Features Demonstrated

- **Map** – element-wise transformations  
- **Filter** – conditional filtering of PCollections  
- **ParDo** – custom `DoFn` for validation and enrichment  
- **Composite Transform** – reusable `PTransform` that chains multiple steps  
- **Partition** – splitting a PCollection into multiple branches  
- **Windowing** – fixed-time windows over timestamped events  
- **Pipeline I/O** – read from / write to text files

## Project Structure

```text
apache_beam/
├── apache_beam_demo.ipynb     # main Colab notebook
├── README.md                  # this file
├── data/
│   ├── sales_input.txt        # sample input data
│   └── sales_output-*.txt     # Beam output files (generated)
└── videos/                    # walkthrough videos (optional)
