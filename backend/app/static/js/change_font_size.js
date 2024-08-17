document.querySelectorAll('.task-item input[type="text"]').forEach(function(input) {
  input.addEventListener('input', function() {
    adjustFontSize(input);
  });
});

function adjustFontSize(input) {
  const length = input.value.length;
  if (length > 20) {
    input.style.fontSize = '14px';  // 文字数が多い場合
  } else if (length > 10) {
    input.style.fontSize = '18px';  // 文字数が中程度の場合
  } else {
    input.style.fontSize = '24px';  // 文字数が少ない場合
  }
}
