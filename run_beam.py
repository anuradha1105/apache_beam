
import apache_beam as beam

output_path = "/content/data/sales_output"

with beam.Pipeline() as p:
    (
        p
        | "Create lines" >> beam.Create(["ok-1", "ok-2", "ok-3"])
        | "Write to text" >> beam.io.WriteToText(output_path)
    )
