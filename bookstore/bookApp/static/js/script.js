// per butonin tek cards
const cards = document.querySelectorAll('.card');
cards.forEach(card => {
  const button = card.querySelector('.btn');
  
  button.style.transform = 'translateY(100%)';
  button.style.opacity = '0';
  
  card.addEventListener('mouseenter', () => {
    button.style.transform = 'translateY(0)';
    button.style.opacity = '1';
  });
  
  card.addEventListener('mouseleave', () => {
    button.style.transform = 'translateY(100%)';
    button.style.opacity = '0';
  });
});

// per shkrimin tek fotoja ne home page 
const textElement = document.getElementById('typing-text');
const texts = [
  'Welcome to our bookstore!',
  'Discover a wide range of books...',
  'Find your next great read...'
];
let textIndex = 0;
let charIndex = 0;

function typeText() {
  if (charIndex < texts[textIndex].length) {
    textElement.textContent += texts[textIndex].charAt(charIndex);
    charIndex++;
    setTimeout(typeText, 100); 
  } else {
    setTimeout(eraseText, 2000); 
  }
}

function eraseText() {
  if (charIndex > 0) {
    textElement.textContent = texts[textIndex].substring(0, charIndex - 1);
    charIndex--;
    setTimeout(eraseText, 50); 
  } else {
    textIndex = (textIndex + 1) % texts.length;
    setTimeout(typeText, 1000); 
  }
}

typeText();
