document.addEventListener('DOMContentLoaded', () => {
    const resumeFileInput = document.getElementById('file-input');
    const jobDesc = document.getElementById('jd-tarea');
    const analyseResumeBtn = document.getElementById('analyse-btn');
    const resultShowcase = document.getElementById('result-showcase');

    /* Sprint 1 - Check for the input type file and text area for the uploaded resume and job description and if present, grab them and show them in the console*/

    //files property - returns an array-like FileList object

    // analyseResumeBtn.addEventListener('click', (e) => {
    //     e.preventDefault();
    //     // console.log("Analyze button clicked");

    //     const chosenFile = resumeFileInput.files[0];
    //     const jd = jobDesc.value;

    //     // if(chosenFile) {
    //     //     console.log(chosenFile);            
    //     //     console.log("File Name:", chosenFile.name);
    //     //     console.log("File Size (bytes):", chosenFile.size);
    //     //     console.log("File Type:", chosenFile.type);
    //     // } else {
    //     //     console.log("No file selected.");
    //     // }



    //     // if(jd.trim() === ""){
    //     //     console.log("Paste a Job Description");
    //     // }else {
    //     //     console.log("The job description -", jd);

    //     // }

    //     if (!chosenFile) {
    //         console.log("Please select a resume.");
    //         return;
    //     }

    //     if (jd.trim() === "") {
    //         console.log("Please paste a job description.");
    //         return;
    //     }

    //     console.log("Resume:", chosenFile.name);
    //     console.log("Job Description:", jd);


    //     resumeFileInput.value = "";
    //     jobDesc.value = "";
    // })


// SPRINT 2
/* Replacing console-only feedback with UI feedback.
Showing results in result-showcase */

    // analyseResumeBtn.addEventListener('click', (e) => {
    //     e.preventDefault();
    //     const resume = resumeFileInput.files[0];
    //     const jd = jobDesc.value;

    //     if(!resume){
    //         resultShowcase.textContent = "Please select a resume";
    //         return;
    //     }
    //     if(jd.trim() === ""){
    //         resultShowcase.textContent = "Please paste a job description";
    //         return;
    //     }
    //     // resultShowcase.textContent = `Resume selected: ${resume.name}\nJob description received successfully`;
    //     resultShowcase.innerHTML = `Resume selected: ${resume.name}<br>Job description received successfully`;

    //     /*Suppose the backend later fails with:
    //      "Unable to analyze resume" If you already cleared the inputs, the user must upload everything again. And thats a problem, so keep the fields intact until the analysis is completed.
    //     jobDesc.value = "";
    //     resumeFileInput.value = "";*/

    // })

    /* Real Sprint2:
    - Create an object containing the data
    - Display a temporary "Analyzing..." msg
    - Simulate a backend call using setTimeout() function
    - Then replace the msg with fake analysis result like:
    resultShowcase.innerHTML = `
    <h3>Analysis Complete</h3>
    <p><strong>Match Score:</strong> 72%</p>
    <p><strong>Matched Skills:</strong> Java, SQL, Git</p>
    <p><strong>Missing Skills:</strong> Spring Boot, Docker</p>
`;*/

    /* I came to know that files are stored in different way for different use cases i.e. 
    - For temporary client-side logic-> Direct Assignment to Object(myObj.file = file) 
    - For Uploading to a server database - FormData Object is used(formData.append())
    - Saving to localStorage or saving as a .json file - conversion to Base64 String via FileReader
    */

    analyseResumeBtn.addEventListener('click',(e) => {
        e.preventDefault();
        const resume = resumeFileInput.files[0];
        const jd = jobDesc.value;
        if(!resume) {
            resultShowcase.textContent = "Please select a resume";
            return;
        }
        if(jd.trim() === ''){
            resultShowcase.textContent = "Please paste a job description";
            return;
        }
        //Result
        const formData = new FormData();
        formData.append("resumeFile", resume);
        formData.append("jobDescription", jd);
        resultShowcase.textContent = 'Analysing Resume...';
        function showFakeResult() {
            resultShowcase.innerHTML = `
            <h3>Analysis Complete</h3>
            <p><strong>Match Score:</strong> 72%</p>
            <p>Matched Skills: Java, SQL, Git</p>
            <p>Missing Skills: Spring Boot, Docker</p>`;
        }
        setTimeout(showFakeResult, 3000);
        //Becoz we aren't using the id of setTimeout so we can directly write it 
    })

})

/* Notes on file input and accessing its properties */
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

/* Notes about FileReader and use case
 const fileInput = document.querySelector('input[type="file"]');
const file = fileInput.files[0];

const reader = new FileReader();

// Define what happens when the file finishes converting
reader.onload = function(event) {
  const base64String = event.target.result;

  // Store the Base64 string in your object
  const userProfile = {
    username: "alex_dev",
    avatarFile: base64String // Looks like "data:image/png;base64,iVBORw..."
  };

  // Now it can safely be saved to localStorage or stringified!
  localStorage.setItem("user", JSON.stringify(userProfile));
};

// Start the conversion process
reader.readAsDataURL(file);

Line (reader.onload = ...): You are planning what to do after the file is read. It does not actually read the file yet. It just registers a listener (like setting an alarm clock)

line (reader.readAsDataURL(file)): This is the actual execution. It kicks off the engine to start scanning the file data. Without this line, Line 1 will sit there forever and never run.
- FileReader is asynchronous (it runs in the background)
- reader.readAsDataURL(file) says the FileReader "Go open this file in the background right now. Let me know when you are done."
- event.target.result --->
        result is a built-in property belonging to the browser's native FileReader object

1. event: This is the information packet generated by the browser when the file finishes loading.

2. target: This points directly back to the object that triggered the event. In this case, event.target is literally just your reader instance.

3.result: This is a native, hardcoded property inside the browser's FileReader blueprint. The moment the file reading finishes successfully, the browser automatically dumps the converted Base64 string into reader.

Note: Because event.target is the reader, writing event.target.result is exactly the same as writing reader.result
*/