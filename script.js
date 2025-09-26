function addHabit() {
  let input = document.getElementById("habitInput");
  let habitText = input.value.trim();

  if (habitText === "") return;

  let li = document.createElement("li");
  li.textContent = habitText;

  // Toggle completed
  li.addEventListener("click", () => {
    li.classList.toggle("completed");
  });

  // Delete button
  let deleteBtn = document.createElement("button");
  deleteBtn.textContent = "❌";
  deleteBtn.style.marginLeft = "10px";
  deleteBtn.onclick = () => li.remove();

  li.appendChild(deleteBtn);
  document.getElementById("habitList").appendChild(li);

  input.value = "";
}