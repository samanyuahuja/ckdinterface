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
// Wait for DOM to load
document.addEventListener("DOMContentLoaded", function () {
  // Animate all cards
  const cards = document.querySelectorAll('.card');
  cards.forEach((card, index) => {
    card.style.opacity = 0;
    card.style.transition = 'opacity 0.6s ease-in-out, transform 0.6s ease';
    card.style.transform = 'translateY(20px)';

    setTimeout(() => {
      card.style.opacity = 1;
      card.style.transform = 'translateY(0)';
    }, 200 * index); // stagger animation
  });

  // Animate images when scrolled into view
  const revealOnScroll = document.querySelectorAll('.img-fluid');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
      }
    });
  }, {
    threshold: 0.3
  });

  revealOnScroll.forEach(img => {
    img.classList.add('hidden-before-scroll');
    observer.observe(img);
  });

  // Smooth scroll to graph explanation (if link used)
  const howToLink = document.querySelector('a[href="#interpretationGuide"]');
  if (howToLink) {
    howToLink.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector('#interpretationGuide');
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
        target.classList.add('show');
      }
    });
  }
});
