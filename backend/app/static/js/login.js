document.getElementById('submit_button').addEventListener('click', async (event) => {
  // デフォルト動作防止
  event.preventDefault();
  // データ成形
  const userName = document.getElementById('user_name').value;
  const userPw = document.getElementById('user_pw').value;
  const data = {
    user_name: userName,
    user_pw: userPw
  };
  
  // フェッチ
  try {
    const response = await fetch('http://localhost/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    
    if (response.ok) {
      console.log('Success');
      const responseData = await response.json();
      const jwtToken = responseData.jwt_token;
      
      localStorage.setItem('jwtToken', jwtToken);
      
      const indexResponse = await fetch('http://localhost/index', {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + jwtToken
        }
      });
      
      if (indexResponse.ok) {
        window.location.href = '/index';
      } else {
        console.log('Failed to load /index');
        alert('Failed to load index page');
      }
    } else {
      console.log('Failed');
      const errorData = await response.json();
      alert('Login failed: ' + (errorData.message || 'Unknown error'));
    }
  } catch (error) {
    console.log('Request failed', error);
  }
});
