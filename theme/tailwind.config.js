/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',   // ← tem que ser exatamente 'class' (string minúscula)
  content: [
    '../../templates/**/*.html',           // ajuste se necessário
    '../../blog/templates/**/*.html',
    '../../**/templates/**/*.html',        // mais seguro
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}