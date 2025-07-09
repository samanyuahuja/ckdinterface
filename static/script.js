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

document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.getElementById("toggleDiet");
  const foodEatList = document.getElementById("foodEatList");
  const downloadBtn = document.getElementById("downloadPdfBtn");

  function updateFoodList() {
    const list = toggle.checked ? nonvegList : vegList;
    foodEatList.innerHTML = "";
    list.forEach(item => {
      const li = document.createElement("li");
      li.classList.add("list-group-item");
      li.textContent = item;
      foodEatList.appendChild(li);
    });
  }

  updateFoodList();

  toggle.addEventListener("change", updateFoodList);

  downloadBtn.addEventListener("click", () => {
    const type = toggle.checked ? "nonveg" : "veg";
    const url = new URL("/download-diet", window.location.origin);
    const eatList = toggle.checked ? nonvegList : vegList;
    eatList.forEach(val => url.searchParams.append("eat", val));
    avoidList.forEach(val => url.searchParams.append("avoid", val));
    top3.forEach(val => url.searchParams.append("top3", val));
    url.searchParams.append("type", type);
    window.location.href = url.toString();
  });
});
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
document.addEventListener('DOMContentLoaded', () => {
  const scrollContainer = document.querySelector('.carousel-wrapper');
  const scrollLeftBtn = document.getElementById('scrollLeft');
  const scrollRightBtn = document.getElementById('scrollRight');

  if (scrollContainer && scrollLeftBtn && scrollRightBtn) {
    scrollLeftBtn.addEventListener('click', () => {
      scrollContainer.scrollBy({ left: -320, behavior: 'smooth' });
    });

    scrollRightBtn.addEventListener('click', () => {
      scrollContainer.scrollBy({ left: 320, behavior: 'smooth' });
    });
  }
});
