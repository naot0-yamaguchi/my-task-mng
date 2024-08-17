window.addEventListener('load', () => {
  // ログアウトボタンのクリックイベントリスナー
  document.getElementById('logoutButton').addEventListener('click', async function() {
    // ログアウト処理の例
    alert('You have been logged out.');
    jwtToken = localStorage.getItem('jwtToken');
    // バックエンド側にログアウト通知
    try {
      const response = await fetch('/logout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + jwtToken
        },
        body: JSON.stringify({jwtToken})
      });
      const result = await response.json();
      console.log(result);
      console.log('notified the backend that logged out."');
    } catch (error) {
      console.error('Error', error);
    }
    localStorage.removeItem('jwtToken'); // JWTトークンを削除
    document.cookie = 'refresh_token=; Max-Age=0; path=/;'; // refresh_tokenクッキーを削除
    window.location.href = '/login'; // ログインページにリダイレクト
  });
});
