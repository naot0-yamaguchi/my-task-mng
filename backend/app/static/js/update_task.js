window.addEventListener('load', () => {
  document.querySelector('.contents_container').addEventListener('click', updateButtonClick);
});

async function updateButtonClick(event) {
  if (!event.target.classList.contains('update_button')) return;
  
  console.log('update_button has been clicked');

  const container = event.target.closest('.contents');
  // task_idを取得(task_idが存在しない場合は新規作成とする)
  const task_id = container.querySelector('.item-id');
  const [title, details, deadline, status] = [
    container.querySelector('.item-title').value,
    container.querySelector('.item-details').value,
    container.querySelector('.item-deadline').value,
    container.querySelector('.item-status').value
  ];

  const jwtToken = localStorage.getItem('jwtToken');

  if (!task_id) {
    // task_idが存在しないので新規作成
    // →タイトルの重複バリデーションを行う
    try {
      const checkResponse = await fetch('/check_existence', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${jwtToken}`
        },
        body: JSON.stringify({ title }),
      });
      const checkData = await checkResponse.json();
      if (checkData.task_id) {
        // すでに同名のタイトルのタスクが存在するため、エラーとする。
        alert('The title is duplicated. Please change.');
        return;
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  const method = task_id ? 'PATCH' : 'POST';
  const endpoint = task_id ? '/update_task' : '/new_task';
  const data = { title, details, deadline, status };
  
  if (task_id) {
    data.id = task_id.value;
  }
  
  console.log(data);

  try {
    const response = await fetch(endpoint, {
      method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${jwtToken}`
      },
      body: JSON.stringify(data)
    });
    const responseData = await response.json();
    console.log('Success:', responseData);
  } catch (error) {
    console.error('Error:', error);
  }
}
