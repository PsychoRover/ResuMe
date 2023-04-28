// const form = document.querySelector("form");
// const pdfViewer = document.querySelector("#pdf");
// const skillList = document.querySelector("#skill-list");
//
// form.addEventListener("submit", (event) => {
//   event.preventDefault();
//   const file = event.target.elements["pdf-file"].files[0];
//   const fileReader = new FileReader();
//   fileReader.onload = function () {
//     const url = URL.createObjectURL(file);
//     pdfViewer.setAttribute("data", url);
//     showSkillExtractor();
//     extractSkillsFromPDF(file);
//   };
//   fileReader.readAsDataURL(file);
// });
//
// function extractSkillsFromPDF(pdfFile) {
//   // Code to extract skills from PDF goes here
//   const skills = ["Skill 1", "Skill 2", "Skill 3"];
//   displaySkills(skills);
// }
//
// function displaySkills(skills) {
//   skills.forEach((skill) => {
//     const skillDiv = document.createElement("div");
//     skillDiv.textContent = skill;
//     skillDiv.classList.add("skill");
//     skillList.appendChild(skillDiv);
//   });
// }
//
// function showSkillExtractor() {
//   const skillExtractor = document.querySelector("#skill-extractor");
//   skillExtractor.style.display = "block";
// }
const fileInput = document.querySelector("#file-js input[type=file]");
fileInput.onchange = () => {
  if (fileInput.files.length > 0) {
    const fileName = document.querySelector("#file-js .file-name");
    fileName.textContent = fileInput.files[0].name;
  }
};
