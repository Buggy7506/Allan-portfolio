function animateSkills() {
    const bars = document.querySelectorAll('.skill-fill');
    bars.forEach(bar => {
      const targetWidth = bar.style.width;
      bar.style.width = '0';
      setTimeout(() => {
        bar.style.width = targetWidth;
      }, 100);
    });
  }
  
  function toggleTheme() {
    document.body.classList.toggle('dark-mode');
  }
  
  const text = "I specialize in: Python, Java, Excel, Word, JavaScript, HTML, Access...";
  let i = 0;
  
  function typeWriter() {
    if (i < text.length) {
      document.getElementById("typed-text").innerHTML += text.charAt(i);
      i++;
      setTimeout(typeWriter, 60);
    }
  }
  
  window.onload = function() {
    animateSkills();
    typeWriter();
  }
  