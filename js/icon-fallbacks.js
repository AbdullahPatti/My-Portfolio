(function () {
  var marks = {
    'MS SQL Server': 'MS', 'ChromaDB': 'CH', 'Firebase': 'F', 'LLM APIs': 'AI',
    'Prompt Engineering': '✦', 'Whisper': 'W', 'REST APIs': '{}', 'SQLAlchemy': 'SA',
    'Ollama': 'O', 'LLM APIs': 'AI',
    'Qdrant': 'Q', 'RAG': 'R'
  };
  function addFallback(tile, name) {
    if (!marks[name] || tile.querySelector('.brand-fallback')) return;
    var mark = document.createElement('span');
    mark.className = 'brand-fallback brand-' + name.toLowerCase().replace(/[^a-z0-9]+/g, '-');
    mark.textContent = marks[name];
    var image = tile.querySelector('img');
    if (image) image.style.display = 'none';
    tile.insertBefore(mark, tile.firstChild);
  }
  document.querySelectorAll('.tool-tile').forEach(function (tile) {
    var label = tile.querySelector('span:not(.tool-caption)');
    var name = label && label.textContent.trim();
    if (!name) return;
    if (!tile.querySelector('img') && marks[name]) addFallback(tile, name);
    var image = tile.querySelector('img');
    if (image) image.addEventListener('error', function () { addFallback(tile, name); });
  });
  var linkedIn = document.querySelector('.social-row a:nth-child(2)');
  if (linkedIn) {
    var icon = linkedIn.querySelector('img');
    if (icon) icon.addEventListener('error', function () { icon.style.display = 'none'; linkedIn.classList.add('linkedin-fallback'); });
  }
})();
