const prevBtn = document.querySelector('.menu-items-wrapper .prev');
const nextBtn = document.querySelector('.menu-items-wrapper .next');
const menuItems = document.querySelector('.menu-items');

const scrollAmount = 270; // sa px të lëvizë me klik

nextBtn.addEventListener('click', () => {
  menuItems.scrollBy({ left: scrollAmount, behavior: 'smooth' });
});

prevBtn.addEventListener('click', () => {
  menuItems.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
});





