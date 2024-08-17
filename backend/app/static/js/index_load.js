document.addEventListener('DOMContentLoaded', async () => {
  const jwtToken = localStorage.getItem('jwtToken');
  
  // トークンが存在しない場合はログインページにリダイレクト
  if (!jwtToken) {
    alert('Please Login to continue.');
    window.location.href = '/login';
  }
  
  // トークンが存在する場合は、認証付きリクエストを送る
  try {
    const response = await fetch('http://localhost/fecth_index_data', {
      method: 'GET',
      headers: {
        'Authorization': 'Bearer ' + jwtToken
      }
    });
    
    if (response.ok) {
      const data = await response.json();
      console.log('Protected data : ', data);
      if (data) {
        // データを詰めていく
        data.tasks.forEach(e => {
          console.log(e);
          taskIndex = document.querySelectorAll('.item-index').length;
          today = new Date().toLocaleDateString('sv-SE');

          // 新しいタスクのHTMLテンプレートを作成
          const newTask = document.createElement('div');
          newTask.classList.add('contents');
          newTask.innerHTML = `
              <input type="hidden" class="task-item item-id" value="${e.id}">
              <div class="task-item item-index">${taskIndex + 1}</div>
              <input type="text" class="task-item item-title" value="${e.title}">
              <input type="text" class="task-item item-details" value="${e.details}">
              <input type="date" class="task-item item-deadline" value="${new Date(e.deadline).toLocaleDateString('sv-SE')}">
              <select class="task-item item-status status">
                  <option value="未着手" selected>未着手</option>
                  <option value="進行中">進行中</option>
                  <option value="完了">完了</option>
              </select>
              <div class="task-item item-action">
                  <button class="update_button">更新</button>
                  <button class="delete_button">削除</button>
              </div>
          `;
          
          // 追加した後にselectの値を設定
          const statusSelectBox = newTask.querySelector('.item-status');
          statusSelectBox.value = e.status; // これで該当するオプションが選択される

          // コンテンツコンテナに新しいタスクを追加
          document.getElementsByClassName('contents_container')[0].appendChild(newTask);
        });
      }
    } else {
      console.log(response);
      console.log('Failed to load protected data.');
      // alert('Session has expired, please login again.');
      // localStorage.removeItem('jwtToken');
      // window.location.href = '/login';
    }
  } catch (error) {
    console.error('Error:', error);
    alert('An Error occured. Please try again.');
  }
});