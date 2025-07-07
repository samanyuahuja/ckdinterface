function askChatbot() {
  const input = document.getElementById("chatInput").value.trim();
  const response = document.getElementById("chatbotResponse");
  if (input === "") {
    response.innerText = "Please enter a question.";
  } else {
    response.innerText = `You asked: "${input}". Our AI will respond shortly.`;
  }
}

function generateDietPlan() {
  const diet = document.getElementById("dietPlanOutput");
  diet.innerText = "Your personalized CKD-friendly diet plan will appear here soon.";
}
