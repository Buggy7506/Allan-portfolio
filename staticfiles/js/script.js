  // --------------------------- // SKILL BAR ANIMATION // --------------------------- function animateSkills() { const bars = document.querySelectorAll('.skill-fill'); bars.forEach(bar => { const targetWidth = bar.getAttribute('data-width') || '100%'; bar.style.width = '0'; setTimeout(() => { bar.style.width = targetWidth; }, 100); }); }

// --------------------------- // DARK MODE TOGGLE // --------------------------- function toggleTheme() { document.body.classList.toggle('dark-mode'); }

// --------------------------- // TYPING TEXT EFFECT // --------------------------- const text = "I specialize in: Python, Java, Excel, Word, JavaScript, HTML, Access..."; let i = 0;

function typeWriter() { if (i < text.length) { document.getElementById("typed-text").innerHTML += text.charAt(i); i++; setTimeout(typeWriter, 60); } }

// --------------------------- // DYNAMIC BACKGROUND IMAGES // --------------------------- const images = [ "/static/img/bg1.jpg", "/static/img/bg2.jpg", "/static/img/bg3.jpg" ];

let index = 0;

function changeBackground() { document.body.style.backgroundImage = url('${images[index]}'); index = (index + 1) % images.length; }

function rotateBackground() { changeBackground(); setInterval(changeBackground, 10000); }

// --------------------------- // MOBILE MENU TOGGLE // --------------------------- function toggleMenu() { const menu = document.getElementById("menu-links"); if (menu.style.display === "block") { menu.style.display = "none"; } else { menu.style.display = "block"; } }

// --------------------------- // ON PAGE LOAD // --------------------------- window.onload = function() { animateSkills(); typeWriter(); rotateBackground(); };
