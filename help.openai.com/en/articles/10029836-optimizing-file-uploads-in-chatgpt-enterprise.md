<!-- source: https://help.openai.com/en/articles/10029836-optimizing-file-uploads-in-chatgpt-enterprise -->

# Optimizing File Uploads in ChatGPT Enterprise

Understand how ChatGPT Enterprise features handle files based on their type, number, and size. Improve outputs based on file requirements.

Updated: 15 days ago

**ChatGPT Enterprise** now supports reading and understanding visuals (images, graphs, diagrams, etc.) embedded in **PDF** files included in prompts. Users can upload a PDF, and ChatGPT can interpret the text *and* any visual elements within that file.

For details see [**Visual Retrieval with PDFs FAQ**](/en/articles/10416312-visual-retrieval-with-pdfs-faq)**.**

ChatGPT Enterprise allows you to upload files in several ways:

* Directly from your computer
* From [Google Drive / SharePoint / OneDrive](/en/articles/9309188-connected-apps-on-chatgpt)
* As [GPT Knowledge](/en/articles/8843948-knowledge-in-gpts)
* As a [Project File](/en/articles/10169521-using-projects-in-chatgpt#h_b7966fa381)
* From a [GPT Action](https://platform.openai.com/docs/actions/sending-files/returning-files)

This guide explains how ChatGPT Enterprise features handles files based on their type, number, and size, and discusses strategies for improving outputs based on file requirements.

# Summary

ChatGPT Enterprise treats different file types very differently: extracting text from text documents like PDFs, Presentations, and Word files, analyzing structured data from spreadsheets using Python code, and describing image files through GPT-Vision. Understanding which file type triggers which workflow is key to getting the expected result.  
  
For text-based documents, ChatGPT Enterprise includes as much relevant text as possible directly alongside the prompt and uses a search system to access additional information. This works well for answering specific questions. However, this approach can struggle with complex tasks like summarizing very large documents or comparing multiple large files. Read on to understand stratgies for improving your results.

# Handling files based on type

ChatGPT Enterprise processes files in three main ways: text extraction, code analysis, and image interpretation. The **file type** determines which workflow ChatGPT Enterprise follows.

|  | **Text-Based Retrieval** | **Code Interpreter** | **Image Processing** | **Visual Retrieval** |
| --- | --- | --- | --- | --- |
| **File Type Examples** | pptx, docx, txt, md, json, xml, pdf\* \* PDFs uploaded as   [GPT Knowledge](/en/articles/8843948-knowledge-in-gpts)  or   [Project Files](/en/articles/10169521-using-projects-in-chatgpt#h_b7966fa381) | csv, xls, xlsx\* \*Note: Code Interpreter can operate on any file type, but ChatGPT Enterprise most commonly defaults to CI for spreadsheets | jpg, png | pdf\* \* PDFs included in user prompts |
| **Behavior** | Extracts the text from the file – some of the text is pasted (“stuffed”) directly into the context window; some text is stored for search | Code Interpreter passes the file to Python for processing | Images are interpreted natively by multi-modal models, subject to   [known limitations](https://platform.openai.com/docs/guides/images?api-mode=responses#limitations) . | A hybrid of text retrieval and image processing. Text is digitally extracted, and visual content is interpreted natively by multi-modal models. |

For text-only files, image files, or clearly structured data files (e.g., an Excel table of transactions), these divisions represent the best possible behavior.  
  
There are some gray areas that are less obvious, for example:

* Images embedded in files other than PDFs are not processed. To include them, convert the file to a PDF prior to uploading.
* ChatGPT Enterprise will always use Code Interpreter to interact with spreadsheets, even if the document contains a large amount of text. For example, if you ask ChatGPT Enterprise to translate a CSV file with 10 rows of text, it will attempt to translate the file using a Python library, which is less accurate than allowing the model to generate a translation directly. To mitigate this, try exporting the spreadsheet to a text-based format (PDF, for example).
* Similarly, if you upload a structured transactional table described contained in a JSON file, ChatGPT Enterprise will interpret this file as plain text. If you want to analyze the data contained in a JSON file, instruct the model to use Code Interpreter in your prompt.

# Handling files based on size

ChatGPT Enterprise uses models with a maximum context window of 128k tokens (roughly 200 pages of text). However, not all tokens are used to incorporate the text from uploaded files. The number of “stuffed” tokens varies by usage type.  
  
ChatGPT Enterprise "stuffs" some amount of text, and the remaining text is sent to a private search index (a "vector store", which is a type of database designed to efficiently store and retrieve large amounts of text). When you ask a question, ChatGPT Enterprise brings in the included text along with relevant chunks retrieved from a private search index.  
  
If you upload a single document, ChatGPT Enterprise includes text starting from the beginning until it reaches its limit. If you upload multiple documents, ChatGPT Enterprise includes some or all of each document. All text from the documents is also sent to a private search index.

## Context stuffing for text documents

This feature is under active development. As such, the following details are subject to change without notice.

ChatGPT Enterprise can process up to **110k tokens** from uploaded documents in the context window. If you upload one or more documents with a combined total of less than 110k tokens, the full content will be included.  
  
For a single document exceeding 110k tokens, only the first 110k tokens will be included, starting from the beginning. The remainder will only be sent to the private search index.  
  
If multiple documents are uploaded and their combined total exceeds 110k tokens, ChatGPT Enterprise uses a two-step process to balance document representation:

1. Extract up to 55k tokens, divided *evenly* among the uploaded documents.

1. For documents not fully represented in the first step, allocate the remaining 55k tokens *proportionally* based on the tokens left in each document.

1. Any remaining tokens are only sent to the private search index.

You can estimate the number of tokens in a text document by copying the document's text into the [OpenAI Tokenizer](https://platform.openai.com/tokenizer).

## Context stuffing for multimedia PDFs

When users upload PDFs containing both text and images, [Visual Retrieval](/en/articles/10416312-visual-retrieval-with-pdfs-faq) enables ChatGPT to process these images natively alongside digitally extracted text. The following steps supplement our standard context-handling procedures for multimedia PDFs:

* **Image Extraction and Embedding**: Images are extracted and embedded along with their associated digital text.
* **Intelligent Scaling**: Images are automatically scaled to maintain a balance between information quality and efficient usage of the available context window.

When uploaded PDFs exceed the 110k token limit, both images and text are embedded in the private search index. Text embeddings reference relevant images, allowing ChatGPT to retrieve the appropriate text-image pairs based on user queries. Retrieved images are then processed using ChatGPT's native multimodal capabilities.  
  
Accurately estimating token requirements for multimedia PDFs is challenging. Testing suggests that approximately 350 pages of mixed text and images will fully utilize the 110k token context window.

# Search strategies based on model type

Both GPT-series and o-series models support file uploads and utilize identical context stuffing and search embedding logic. All models execute hybrid searches against a private search index, combining keyword and semantic methods. In a hybrid search, the model generates a search phrase based on the user's prompt, and the private search index retrieves relevant text and images accordingly.  
  
However, these models differ in how they search through large documents that exceed the context window:

## GPT-series models

* **Single search per prompt:** GPT-series models perform one search per user prompt.
* **Effective use cases:** Ideal for answering straightforward questions embedded in extensive documentation.

**Example queries:**

* "What is the HR policy for early retirement?"
* "What does the `process_order` function do?"

## o-series models

* **Multiple searches per prompt:** Can execute multiple searches (typically 2-3) per user prompt, each with a unique search phrase. Searches are executed sequentially, and the model can update its approach based on information retrieved in prior searches.
* **Effective use cases:** More suitable for complex questions requiring multiple targeted searches across extensive documentation.

**Example queries:**

* "What are the HR policies for early retirement, parental leave, and overseas transfer?"
* "Explain what the `process_order` function does, list all methods invoked by this function, and briefly describe each invoked method."

Despite their strengths, o-series models may struggle when a query requires more than three searches.

# Tips for improving file search results

* Try using an o-series model for complex questions requiring multiple searches.
* Remember that responses may vary depending on the type, number, and size of documents you upload.
* Generally, loading in fewer, focused documents will lead to higher accuracy.
* Turn multi-question topics into single questions:

  + If you need to know every state’s HR policies, ask them one-by-one.
  + If you need to summarize many documents, ask for one document at a time. If that document is many hundreds of pages, consider breaking it down into smaller components.

    - You could ask ChatGPT Enterprise to write a “summary of summaries” if you fed it multiple summaries rather than entire documents.
  + If you have a CSV of an RFP (each line is a different question), ask those questions one-by-one instead of just loading the CSV and requesting a single response.
* Find ways to audit the model’s responses. Example GPT instructions are below:

```
# Context   
  
You are an expert at understanding documents. The user is going to attach a document and ask a question. They need to be able to connect your answer back to the exact part of the text where you grabbed your answer from.  
  
# Instructions  
  
1. Answer the user's question based on their attached document using the exact format provided below  
  
# Format   
  
- Question: { repeat user's question }  
- Answer: { provide an answer to user's question }  
Source:   
- - Section Number: { provide section number where you pulled in the answer }  
- - Section Title: { provide section title where you pulled in the answer }  
- - Exact Text: { provide the exact text where you pulled the answer from }  
  
# Rules  
  
- Give answers that are clear and concise  
- Only provide information provided in the document  
- If you cannot find the answer in the document, simply reply "No information found."
```
