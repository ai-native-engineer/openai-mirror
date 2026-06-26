<!-- source: https://developers.openai.com/cookbook/examples/vector_databases/kusto/readme/ -->

## Search the cookbook

May 10, 2023

# Kusto as a vector database

This recipe is archived and may reference outdated models or APIs.

[AS](https://github.com/Anshul Sharma)

[Anshul Sharma](https://github.com/Anshul Sharma)

[View on GitHub](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/kusto/README.md) [Download raw](https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/vector_databases/kusto/README.md)

[Azure Data Explorer aka Kusto](https://azure.microsoft.com/en-us/products/data-explorer) is a cloud-based data analytics service that enables users to perform advanced analytics on large datasets in real-time. It is particularly well-suited for handling large volumes of data, making it an excellent choice for storing and searching vectors.

Kusto supports a special data type called dynamic, which can store unstructured data such as arrays and properties bag. [Dynamic data type](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/scalar-data-types/dynamic) is perfect for storing vector values. You can further augment the vector value by storing metadata related to the original object as separate columns in your table.  
Kusto also supports in-built function [series\_cosine\_similarity\_fl](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/functions-library/series-cosine-similarity-fl) to perform vector similarity searches.

[Get started](https://aka.ms/kustofree) with Kusto for free.

![Kusto_Vector](/cookbook/assets/examples/vector_databases/kusto/images/kusto_vector_db.png)

## Getting started with Kusto and Open AI embedding

### Demo Scenario

![Wiki_embeddings](/cookbook/assets/examples/vector_databases/kusto/images/wiki_embeddings.png)

![semantic_search_flow](/cookbook/assets/examples/vector_databases/kusto/images/semantic_search_user_flow.png)

If you’d like to try this demo, please follow the instructions in the [Notebook](Getting_started_with_kusto_and_openai_embeddings.ipynb).

It will allow you to -

1. Use precomputed embeddings created by OpenAI API.
2. Store the embeddings in Kusto.
3. Convert raw text query to an embedding with OpenAI API.
4. Use Kusto to perform cosine similarity search in the stored embeddings.
