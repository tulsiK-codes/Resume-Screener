document.addEventListener('DOMContentLoaded', () => {
    const resumeFileInput = document.getElementById('file-input');
    const jobDesc = document.getElementById('jd-tarea');
    const analyseResumeBtn = document.getElementById('analyse-btn');
    const resultShowcase = document.getElementById('result-showcase');

    /* Version 1 - Check for the input type file and text area for the uploaded resume and job description and if present, grab them and show them in the console*/

    //files property - returns an array-like FileList object

    analyseResumeBtn.addEventListener('click', (e) => {
        e.preventDefault();
        // console.log("Analyze button clicked");

        const chosenFile = resumeFileInput.files[0];
        const jd = jobDesc.value;

        // if(chosenFile) {
        //     console.log(chosenFile);            
        //     console.log("File Name:", chosenFile.name);
        //     console.log("File Size (bytes):", chosenFile.size);
        //     console.log("File Type:", chosenFile.type);
        // } else {
        //     console.log("No file selected.");
        // }



        // if(jd.trim() === ""){
        //     console.log("Paste a Job Description");
        // }else {
        //     console.log("The job description -", jd);

        // }

        if (!chosenFile) {
            console.log("Please select a resume.");
            return;
        }

        if (jd.trim() === "") {
            console.log("Please paste a job description.");
            return;
        }

        console.log("Resume:", chosenFile.name);
        console.log("Job Description:", jd);


        resumeFileInput.value = "";
        jobDesc.value = "";
    })

// Sprint 1 completed













    /* Listening to change event so as to capture the file as soon as the user selects it
       
   const fileInput = document.getElementById('myFileInput'); -> this is the file input
   
   fileInput.addEventListener('change', (event) => {
     // Access the selected file
     const selectedFile = event.target.files[0]; 
   
     if (selectedFile) {
       console.log("File Name:", selectedFile.name);
       console.log("File Size (bytes):", selectedFile.size);
       console.log("File Type:", selectedFile.type);
       } else {
           console.log("No file selected.");
       }
   });
   */

    /* Handling multiple files
     const fileInput = document.getElementById('myFileInput');
    
    fileInput.addEventListener('change', (event) => {
      // Convert FileList to a true JavaScript Array
      const selectedFiles = Array.from(event.target.files); 
      
      selectedFiles.forEach((file) => {
        console.log(`Selected: ${file.name}`);
      });
    });
     */

    /*Check for file type
    if (selectedFile && selectedFile.type !== "application/pdf" || ".pdf") {
      alert("Error: Only PDF files are allowed!");
      fileInput.value = ""; // Clear the invalid selection
    }*/




})