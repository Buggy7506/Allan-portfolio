 // ---------------------------
// SKILL BAR ANIMATION
// ---------------------------
function animateSkills() {
  const bars = document.querySelectorAll('.skill-fill');
  bars.forEach(bar => {
    const targetWidth = bar.getAttribute('data-width') || '100%';
    bar.style.width = '0';
    setTimeout(() => {
      bar.style.width = targetWidth;
    }, 100);
  });
}

// ---------------------------
// DARK MODE TOGGLE
// ---------------------------
function toggleTheme() {
  document.body.classList.toggle('dark-mode');
}

// ---------------------------
// TYPING TEXT EFFECT
// ---------------------------
const text = "I specialize in: Python, Java, Excel, Word, JavaScript, HTML, Access...";
let i = 0;

function typeWriter() {
  const typedText = document.getElementById("typed-text");
  if (!typedText) return;

  if (i < text.length) {
    typedText.innerHTML += text.charAt(i);
    i++;
    setTimeout(typeWriter, 60);
  }
}

// ---------------------------
// DYNAMIC BACKGROUND IMAGES
// ---------------------------
const images = [
  "/static/img/bg1.jpg",
  "/static/img/bg2.jpg",
  "/static/img/bg3.jpg"
];
let index = 0;

function changeBackground() {
  document.body.style.backgroundImage = `url('${images[index]}')`;
  index = (index + 1) % images.length;
}

// ---------------------------
// RUN AFTER HTML LOADS
// ---------------------------
document.addEventListener("DOMContentLoaded", function () {
  animateSkills();
  typeWriter();
  changeBackground();
  setInterval(changeBackground, 10000); // Every 10 seconds

  // Debug: Confirm JS loaded
  console.log("✅ JavaScript Loaded & Running!");
});
