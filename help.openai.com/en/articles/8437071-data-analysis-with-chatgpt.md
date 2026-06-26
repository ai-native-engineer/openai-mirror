<!-- source: https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt -->

# Data analysis with ChatGPT

Use ChatGPT to inspect uploaded data, create tables and charts, and review code-backed analysis.

Updated: 10 days ago

# Overview

ChatGPT can analyze uploaded files, answer questions about the data, and create tables or charts when the output benefits from a structured view.  
  
For best results, upload structured data with clear column names and one record per row. Tell ChatGPT what you want to learn from the file, and specify any columns, calculations, groupings, or chart types you want it to use.

# Supported files and connected sources

ChatGPT supports common file types for data analysis, including:

* Spreadsheets, such as .xls, .xlsx, and .csv files
* PDFs
* Text and data files, such as .json, .xml, .yaml, .txt, and .md files

Available file types can vary by model, plan, workspace settings, and account capabilities.  
  
When connectors are available for your account or workspace, you can also attach files from connected sources such as Google Drive, OneDrive, and SharePoint.

# Preparing spreadsheets

Use:

* Descriptive column headers in the first row
* One row per record
* Plain-language column names

Avoid:

* Multiple unrelated tables in one sheet
* Empty rows or columns that split the data
* Images that contain values ChatGPT needs to analyze

# Analyzing data

ChatGPT can help with:

* Summarizing rows, columns, trends, and outliers
* Creating tables for row-by-row review
* Creating charts from uploaded data
* Running Python-based calculations, transformations, and statistical analysis
* Explaining assumptions, results, and possible next steps

For some data-analysis tasks, ChatGPT writes and runs Python code in a stateful Jupyter notebook environment. The environment can use files made available to the session and can display pandas DataFrames as interactive tables when that format is useful.

# Reviewing analysis details

When ChatGPT uses Python for analysis, review the generated code, outputs, and assumptions before relying on the result. If the answer depends on a specific method, ask ChatGPT to show or adjust that method.

# Using charts

ChatGPT can create static charts as image outputs. Some charts can also be shown as interactive charts.  
  
When an interactive chart is available, select **Switch to interactive chart**. To return to the image version, select **Switch to static chart**.  
  
Interactive charts are supported for bar, line, pie, and scatter charts. Other chart types may be returned as static images.

# File limits

The exact limit of files per conversation can vary by upload type, model, plan, workspace settings, and remaining file-upload allowance. For more information, see: [File uploads FAQ](https://help.openai.com/articles/8555545).  
  
Project and GPT knowledge-file limits are separate from conversation upload limits and may be configured differently.

# Privacy and uploaded files

For more information about how uploaded files are stored, retained, and deleted, see: [Chat and File Retention Policies in ChatGPT](https://help.openai.com/articles/8983778).  
  
To learn how your content may be used to improve model performance and how to manage your data settings, see: [How your data is used to improve model performance](https://help.openai.com/articles/5722486) and [Data Controls FAQ](https://help.openai.com/articles/7730893).

# Constraints

The Python environment used for data analysis cannot make external web requests or API calls. If analysis depends on external data, upload the data or connect an available source before asking ChatGPT to analyze it.  
  
ChatGPT may choose an analysis method or chart type that does not match your intent on the first try. Ask it to use a specific method, chart type, grouping, or column when you need a particular approach.

# FAQ

## Can ChatGPT analyze scanned PDFs or images that contain tables?

ChatGPT may not reliably extract exact values from image-based tables, scanned files, or files with complex visual layouts. When exact values matter, upload a spreadsheet or text-based file instead.

## Why might ChatGPT not analyze the full file?

A file may upload successfully but still be too large, complex, image-heavy, or poorly structured for complete analysis. If the result seems incomplete, ask ChatGPT to inspect specific sheets, rows, columns, or sections, or split the file into smaller files.

## Can ChatGPT access connected-source files I do not have permission to view?

When using connected apps, ChatGPT uses the connected account and app permissions. Workspace admins may also control which apps are available. For more information, see: [Apps in ChatGPT](https://help.openai.com/articles/11487775).
