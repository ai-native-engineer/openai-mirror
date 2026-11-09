<!-- source: https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt -->

# Uploading files and audio to ChatGPT

Upload documents, spreadsheets, presentations, images, and audio to ask questions and work with their contents.

Updated: 9 hours ago

ChatGPT can work with documents, spreadsheets, presentations, images, and audio files you attach to a conversation. You can ask it to summarize a document, compare information, analyze a spreadsheet, or transcribe and discuss an audio recording.

Audio understanding and transcription performance may vary across languages.

## Availability

Document, spreadsheet, presentation, text, and image uploads are available on Free and paid ChatGPT plans, subject to plan-specific limits and account settings, on the web and in supported mobile apps.

Audio uploads are available with paid ChatGPT subscriptions and workspaces, including Enterprise. Audio uploads are not available on the Free plan at this time.

Availability may vary by workspace settings, region, client version, and selected model.

The API has separate file-upload requirements, supported purposes, and limits.

# Use files in a conversation

1. Attach a supported file to your ChatGPT conversation.
2. Describe what you want ChatGPT to do with it, such as summarize a document, compare two files, or transcribe an audio recording.
3. Review the response and ask follow-up questions or request changes.

# Common file formats

Examples include the formats below. What ChatGPT can do with a file depends on its contents, the model you select, and the tools available in your chat.

| **File type** | **Example formats** | **Notes** |
| --- | --- | --- |
| Documents and text | DOCX, PDF, TXT, Markdown (.md), HTML (.html), XML (.xml), JSON (.json), YAML (.yaml), Python (.py), RTF (.rtf), OpenDocument Text (.odt), email (.eml) | You can’t upload a .gdoc file directly. Export it as PDF or DOCX, then upload the exported file. |
| Spreadsheets | XLSX, XLS, CSV, TSV, OpenDocument Spreadsheet (.ods) |  |
| Presentations | PPTX, OpenDocument Presentation (.odp) |  |
| Audio | WAV, MP3/MPEG, OGG/OGA, audio-only WebM, PCM, FLAC, AAC, M4A, audio-only MP4 | WebM and MP4 files identified as video are not supported by audio uploads.  The file must contain a valid, decodable audio stream.  Audio understanding and transcription performance may vary across languages. |

# Work with uploaded files

Transcripts may contain errors, and speaker identification may be unreliable. Review important details against the original recording.

## Summarize, compare, and analyze

* Summarize a research paper or another document in simpler terms.
* Upload a spreadsheet with qualitative and quantitative information to explore trends or create visualizations.
* Compare two documents or apply a framework from one document to another.
* Analyze the sentiment or tone of a document.
* Get feedback on a presentation’s content.
* Summarize a meeting recording, highlighting decisions, open questions, and next steps.

## Find specific information

* Find references to a topic or extract relevant quotes.
* Extract document metadata, such as an author or creation date.
* Count spreadsheet rows that have a particular attribute.
* Extract sections, headings, or lists from a document.
* Ask questions about a recording—for example, “What did they say about the launch deadline?”
* Extract key details from an interview or lecture, such as requirements, examples, or main takeaways.

## Transform content

* Rewrite a short document in a different style.
* Turn a presentation into a document.
* Ask for a transcript of an audio recording, then ask follow-up questions about its contents.
* Turn a recording into structured notes, a meeting recap, or a follow-up email draft.

**Data Analysis**: When Data Analysis is available, ChatGPT may use tools to open a ZIP archive and work with files inside it. What it can read depends on the files in the archive and the tools available in your chat.

For help analyzing data and creating charts, see: [Data analysis with ChatGPT](https://help.openai.com/articles/8437071).

# Audio upload and processing limits

Audio files can be up to 512 MB.

Longer recordings may be processed in smaller sections when Data Analysis is available. Processing is best-effort, and very long recordings may time out.

# Document and image upload limits

This section covers documents, spreadsheets, presentations, text files, and images.

## File size

* Documents and presentations have a maximum size of 512 MB per file.
* Text and document files are capped at 2 million tokens per file. This token limit does not apply to spreadsheets.
* CSV files and spreadsheets have a size limit of approximately 50 MB, depending on the size of each row.
* Images have a limit of 20 MB per image.

## Upload rate and storage

You can upload up to 80 files every 3 hours. Free users are limited to 3 file uploads per day. OpenAI may lower these limits during peak hours.

Shared upload storage is capped at 25 GB per user and 100 GB per organization. ChatGPT displays an error when a user or organization reaches a cap.

You can check saved-file storage usage in **Settings > Storage**. ChatGPT does not currently show how much of your rolling upload-rate quota has been used or remains. For saved-file storage information, see: [Using Library to manage files in ChatGPT](https://help.openai.com/articles/20001052). For help finding saved files in Space, see: [Getting started with Space in ChatGPT](https://help.openai.com/articles/20001549).

## Projects and GPT knowledge

Project file limits depend on your plan:

* Free: up to 5 files per project.
* Go and Plus: up to 25 files per project.
* Edu, Pro, Business, and Enterprise: up to 40 files per project.

You can attach up to 20 files to a GPT as knowledge. For details, see [Creating and editing GPTs](https://help.openai.com/articles/8554397). File-size restrictions and user or organization usage caps also apply.

# Troubleshoot an upload

If you see an “upload limit reached” message despite few or no recent uploads:

1. Confirm that you’re signed in to the correct account and subscription plan.
2. If the error message shows a retry time, wait until that time before uploading again. Failed upload attempts can sometimes count toward the upload-rate limit.
3. On web, open **Settings > Storage** to check saved-file storage usage. Saved-file storage is separate from upload-rate limits. For help managing saved files, see: [Using Library to manage files in ChatGPT](https://help.openai.com/articles/20001052). For help finding saved files in Space, see: [Getting started with Space in ChatGPT](https://help.openai.com/articles/20001549).
4. Check [OpenAI Status](https://status.openai.com) for incidents that may affect uploads.
5. If the issue continues, [contact OpenAI Support](https://help.openai.com/articles/6614161) with the details listed below.

If an audio upload fails, check that the file uses a supported audio format and contains a valid, decodable audio stream. WebM and MP4 files identified as video are not supported by audio uploads.

If a recording uploads but won’t transcribe, try converting it to WAV and uploading it again.

If you contact OpenAI Support, include your account email, a screenshot of the issue, the timestamp and time zone, the platform or browser you used, and the request ID if available.

# Manage uploaded documents and images

## Delete a saved file

Deleting a chat does not delete a file saved separately in Library or Space. Delete that saved copy separately if you also want to remove it.

If your account shows **Space**, you can find your saved files there.

If your account shows **Library**:

1. Open **Library** and select the file.
2. Select **Delete** or the trash icon next to the file.

If your Library includes **Recently deleted**, you can restore the file there until it is permanently deleted. You can also select **Delete forever** or **Delete all** to remove it sooner.

If you added a file to a custom GPT’s knowledge, remove it in the GPT builder. For instructions and details about managing saved files, see: [Using Library to manage files in ChatGPT](https://help.openai.com/articles/20001052). For help finding saved files in Space, see: [Getting started with Space in ChatGPT](https://help.openai.com/articles/20001549).

## Understand retention

Retention depends on where the file is stored and any workspace retention policy that applies. Saved files available through Library or Space can be retained separately from the conversation that used them. In Enterprise, Edu, and Healthcare workspaces, these saved files follow the workspace retention policy.

Content from a file that was brought into a conversation can remain in that conversation. Deleting a saved file and deleting a conversation are separate actions.

For chat deletion, files in GPTs and projects, temporary chats, transient files, and security or legal exceptions, see: [Chat and file retention in ChatGPT](https://help.openai.com/articles/8983778).

## Understand data use

How uploaded documents and images may be used to improve models depends on the service you use and your data settings. For information about consumer services, see: [Data Usage for Consumer Services FAQ](https://help.openai.com/articles/7039943), [How your data is used to improve model performance](https://help.openai.com/articles/5722486), and [Data Controls FAQ](https://help.openai.com/articles/7730893).

OpenAI does not use content submitted by customers to business offerings, such as the API and ChatGPT Enterprise, to improve model performance. For more information, see the [Enterprise Privacy page](https://openai.com/enterprise-privacy).

# Read images in documents

ChatGPT can analyze both text and images in PDFs, including charts and diagrams. To upload a PDF, select **+** in the prompt area, then **Add photos & files**. Ask questions about its contents. This also works when you attach the PDF directly in a chat with a GPT or in a project chat.

Files saved as GPT knowledge or project files are handled differently from direct chat attachments. Embedded images may not be included automatically. To ask about a specific chart or image, attach the PDF directly to the chat or upload the image separately.

If embedded images aren’t supported for your file, upload the images separately as PNG, JPEG, or non-animated GIF files. Select **+** in the prompt area, then **Add photos & files**. For supported image formats and limits, see: [ChatGPT Image Inputs FAQ](https://help.openai.com/articles/8400551).
