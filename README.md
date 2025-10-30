# Apache Beam Data Engineering Exercise

A comprehensive demonstration of **Apache Beam** features for data engineering and stream processing, implemented in **Google Colab** using a dedicated virtual environment.

---

## 📋 Overview

This project presents an end-to-end implementation of an Apache Beam data pipeline using synthetic e-commerce sales data.  
It demonstrates how Beam’s unified batch and stream processing model can be used to perform transformations, filtering, partitioning, and time-based windowing — all within a single scalable pipeline.

The notebook serves as a practical exercise for learning and applying Beam concepts in a reproducible environment.

---

## 🎯 Features Demonstrated

- **ParDo** – Parallel element processing using custom `DoFn` classes  
- **Map** – Element-wise transformations and calculations  
- **Filter** – Conditional record filtering  
- **Partition** – Splitting data into multiple logical outputs  
- **Composite Transforms** – Building reusable multi-step transform components  
- **Windowing** – Time-based data aggregation with fixed windows  
- **Pipeline I/O** – Reading and writing datasets from external files  

---

## 🧱 Project Structure

```text
apache_beam/
├── apache_beam_demo.ipynb         # main Colab notebook
│── sales_input.txt            # sample input data
│── sales_output-00000-of-00001.txt   # generated output file
├── videos/                        # walkthrough recordings
└── README.md                      # this file
---

## 🚀 Environment & Versions

This project was developed and executed in **Google Colab** with the following setup:

| Component | Version / Tool |
|:--|:--|
| Python | **3.12.12** |
| Apache Beam | **2.58.0** |
| Virtual Environment | **virtualenv** |
| Operating System | Ubuntu (Colab runtime) |
| Notebook Interface | Jupyter / Colab |
| Date of Execution | October 2025 |

---

## 🧱 Implementation Summary

The notebook walks through each required Beam concept using a practical example of e-commerce sales data processing.

| Section | Description |
|:--|:--|
| **1. Environment Setup** | Creates and configures a clean Beam environment using `virtualenv`. |
| **2. Map** | Demonstrates element-wise transformations such as calculating total sales amount. |
| **3. Filter** | Shows conditional filtering, e.g., selecting sales from a specific store. |
| **4. ParDo** | Implements custom `DoFn` for validation and computation of derived metrics. |
| **5. Composite Transform** | Combines multiple transforms (cleaning + grouping + summation) into one reusable component. |
| **6. Partition** | Splits PCollections into multiple outputs based on store or category. |
| **7. Windowing** | Groups timestamped events into fixed windows for time-based aggregation. |
| **8. Pipeline I/O** | Reads data from input files and writes processed results to output files. |
| **9. Full Pipeline** | Integrates all the above features in a complete data engineering workflow. |

Each code cell demonstrates the relevant Beam concept, executes independently, and prints structured outputs for clarity.

---

## 💡 Key Concepts

- **PCollection:** Immutable distributed dataset that flows through the pipeline.  
- **Transform:** Operation applied to a PCollection (e.g., Map, Filter, ParDo).  
- **Pipeline:** Logical container for all transforms and data flow execution.  
- **DoFn:** Custom user-defined function used within `ParDo` for flexible data processing.  
- **Window:** Mechanism to group data into time intervals for streaming aggregation.  

---

## 🎓 Learning Objectives

By completing this exercise, you will learn:

- How to design and execute Apache Beam pipelines in Python  
- How to apply core Beam transforms for data processing  
- How to develop custom `DoFn` classes for advanced logic  
- How to organize multiple transformations using composite patterns  
- How to implement windowing for time-based aggregation  
- How to perform file-based input and output operations  

---

## 🧩 Example Snippets

**Basic Beam Pipeline**

```python
import apache_beam as beam

with beam.Pipeline() as pipeline:
    (
        pipeline
        | 'Create' >> beam.Create([1, 2, 3, 4, 5])
        | 'Multiply by 2' >> beam.Map(lambda x: x * 2)
        | 'Print results' >> beam.Map(print)
    )
```

**ParDo**

```python
class ComputeTotal(beam.DoFn):
    def process(self, element):
        element['total'] = element['quantity'] * element['price']
        yield element
```

**Windowing**

```python
from apache_beam.transforms import window

pipeline | beam.WindowInto(window.FixedWindows(60))  # 60-second windows
```

---

## 🔗 Resources

- [Apache Beam Official Documentation](https://beam.apache.org/documentation/)  
- [Beam Python SDK](https://beam.apache.org/documentation/sdks/python/)  
- [Interactive Beam Playground](https://beam.apache.org/get-started/try-beam-playground/)  
- [Beam Transform Catalog](https://beam.apache.org/documentation/transforms/python/overview/)  

---

## 🎬 Video Walkthrough (Optional)

Suggested video structure for presentation:

1. **Introduction (1–2 min)** – Project overview, goals, and dataset  
2. **Code Walkthrough (8–10 min)** – Demonstrate each Beam feature sequentially  
3. **Execution Demo (2–3 min)** – Run cells in Colab, show output and file generation  
4. **Conclusion (1 min)** – Summarize key takeaways and real-world relevance  

---

## 🤝 Contributing

This project is part of an academic exercise. You are encouraged to experiment by:

- Extending the dataset  
- Modifying the transforms  
- Exploring advanced windowing and triggers  
- Integrating Beam ML components  


