document.getElementById('add_button_container').addEventListener('click', add_new_form);

function add_new_form() {
    taskIndex = document.querySelectorAll('.item-index').length;
    today = new Date().toLocaleDateString('sv-SE');

    // 新しいタスクのHTMLテンプレートを作成
    const newTask = document.createElement('div');
    newTask.classList.add('contents');
    newTask.innerHTML = `
        <div class="task-item item-index">${taskIndex + 1}</div>
        <input type="text" class="task-item item-title" value="">
        <input type="text" class="task-item item-details" value="">
        <input type="date" class="task-item item-deadline" value="${today}">
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

    // コンテンツコンテナに新しいタスクを追加
    document.getElementsByClassName('contents_container')[0].appendChild(newTask);
}

// 画面初期表示時にタスクが存在しない場合、新規フォームを追加
document.addEventListener('load', () => {
    if (document.querySelectorAll('.contents').length === 0) {
        add_new_form();
    }
});
