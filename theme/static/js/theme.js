
// Função de toggle
function toggleTheme() {
  if (document.documentElement.classList.contains('dark')) {
    document.documentElement.classList.remove('dark');
    localStorage.theme = 'light';
  } else {
    document.documentElement.classList.add('dark');
    localStorage.theme = 'dark';
  }
}

// Aplicar tema inicial (evita flicker)
(function() {
  const saved = localStorage.getItem('theme');
  
  if (saved === 'dark') {
    document.documentElement.classList.add('dark');
  } else if (saved === 'light') {
    document.documentElement.classList.remove('dark');
  } else {
    // Se não salvo → segue preferência do sistema
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.documentElement.classList.add('dark');
    }
  }
})();
