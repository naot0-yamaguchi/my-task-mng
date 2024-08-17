window.addEventListener('load', () => {
  document.querySelector('.contents_container').addEventListener('click', deleteButtonClick);
});

async function deleteButtonClick(event) {
  if (!event.target.classList.contains('delete_button')) return;
  
  console.log('delete_button has been clicked');

  const container = event.target.closest('.contents');
  // task_idを取得(task_idが存在しない場合は入力フォームのみの削除とする)
  const task_id = container.querySelector('.item-id');
  
  // フォームを削除する
  delete_form(container);
  
  if (!task_id) {
    return;
  }
  
  const jwtToken = localStorage.getItem('jwtToken');
  
  try {
    const response = await fetch('/delete_task', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${jwtToken}`
      },
      body: JSON.stringify({id: task_id.value})
    });
    const responseData = await response.json();
    console.log('Success:', responseData);
  } catch (error) {
    console.error('Error:', error);
  }
}

function delete_form(container) {
  container.remove();
}
