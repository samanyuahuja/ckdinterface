/**
* Template Name: Medilab
* Template URL: https://bootstrapmade.com/medilab-free-medical-bootstrap-theme/
* Updated: Aug 07 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function(e) {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);

})();

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
document.querySelector("#sendChatBtn").addEventListener("click", async () => {
  const input = document.querySelector("#chatInput");
  const message = input.value.trim();
  if (!message) return;

  const chatBox = document.querySelector("#chatBox");
  chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
  input.value = "";

  try {
    const res = await fetch("/chatbot", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    if (data.reply) {
      chatBox.innerHTML += `<p><strong>AI:</strong> ${data.reply}</p>`;
    } else {
      chatBox.innerHTML += `<p><strong>AI:</strong> Failed to get response.</p>`;
    }
  } catch (err) {
    chatBox.innerHTML += `<p><strong>AI:</strong> Failed to connect.</p>`;
  }

  chatBox.scrollTop = chatBox.scrollHeight;
});
