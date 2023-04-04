/* script.js */
const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const transportation = parseInt(document.querySelector('#transportation').value);
  const energy = parseInt(document.querySelector('#energy').value);
  const waste = parseInt(document.querySelector('#waste').value);

  // TODO: calculate and display personalized recommendations based on user input
});
