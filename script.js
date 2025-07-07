function askChatbot() {
  const input = document.getElementById('chatInput').value;
  const responseBox = document.getElementById('chatbotResponse');
  if (input.trim() === "") {
    responseBox.innerText = "Please enter a question.";
  } else {
    // Placeholder response — integrate AI later
    responseBox.innerText = `You asked: "${input}". Our assistant will reply soon.`;
  }
}

function generateDietPlan() {
  const dietBox = document.getElementById('dietPlanOutput');
  // Placeholder diet plan — integrate AI logic later
  dietBox.innerText = "Your CKD-friendly diet plan will appear here.";
}
