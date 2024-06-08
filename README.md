# PDF_RAG


<h1>Step 1:</h1>
Install all the dependencies using requirements.txt file. <br>

<h1>Step 2a(Running for the very first time):</h1>
If you have not added your PDF:<br>
1. Copy your PDF in data folder<br>
2. Update the file path in embeddings.py

```loader = PyPDFLoader("data/PDF_NAME.pdf")```<br>

3.Now run embeddings.py to generate embeddings and upload it to Pinecone

<h1>Step 2b(Already have embeddings generated and uploaded on Pinecone VectorDB):</h1>
You can proceed now to next step

<h1>Step 3:</h1>
Run main.py to start the action. You can change the question or make it take inputs too.