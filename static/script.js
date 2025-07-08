// Placeholder: You can add your AI logic, chatbot, or dynamic features here

// Example: Toggle mobile nav (if you implement a mobile nav toggle button)
function toggleNav() {
  const nav = document.getElementById('main-nav');
  if (nav.style.display === "block") {
    nav.style.display = "none";
  } else {
    nav.style.display = "block";
  }
}

// Example: Dummy chatbot response (replace with real AI later)
function chatbotReply(userInput) {
  const responses = [
    "I'm here to help! Can you tell me more about your symptoms?",
    "Our system suggests you consult a doctor for detailed advice.",
    "Based on your input, it is recommended to stay hydrated and monitor symptoms."
  ];
  const randomIndex = Math.floor(Math.random() * responses.length);
  return responses[randomIndex];
}

// Example: Dummy diet plan generator (replace with real logic later)
function generateDietPlan() {
  return `
    <ul>
      <li>🥗 Breakfast: Oatmeal with fresh berries</li>
      <li>🍗 Lunch: Grilled chicken with quinoa and steamed veggies</li>
      <li>🍎 Snack: Apple slices with almond butter</li>
      <li>🍲 Dinner: Baked salmon with brown rice and broccoli</li>
    </ul>
  `;
}
// === 🌙 Dark Mode Toggle ===
console.log("Dark mode script loaded");
document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("darkToggle");
  const body = document.body;

  // Load saved theme from localStorage
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    body.classList.add("dark-mode");
    toggleButton.textContent = "☀️ Light Mode";
  }

  toggleButton.addEventListener("click", function () {
    body.classList.toggle("dark-mode");

    const isDark = body.classList.contains("dark-mode");
    localStorage.setItem("theme", isDark ? "dark" : "light");
    toggleButton.textContent = isDark ? "☀️ Light Mode" : "🌙 Dark Mode";
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("diagnosisForm");
  const spinner = document.getElementById("loadingSpinner");

  if (form && spinner) {
    form.addEventListener("submit", function () {
      spinner.style.display = "block";
      form.style.display = "none";
    });
  }
});
