document.getElementById('submit_button').addEventListener('click', event => {
  console.log(1);
  // デフォルト動作防止
  event.preventDefault();
  console.log(2);
  // データ成形
  const userName = document.getElementById('user_name').value;
  const userPw = document.getElementById('user_pw').value;
  const data = {
    user_name: userName,
    user_pw: userPw
  };
  console.log(3);
  
  // XHRオブジェクト作成
  const xhr = new XMLHttpRequest();
  const url = 'http://localhost/register';
  xhr.open('POST', url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify(data));
  console.log(4);
  
  xhr.onreadystatechange = () => {
    if (xhr.readyState === 4 && xhr.status === 201) {
      console.log('Success');
      const location = xhr.getResponseHeader('Location');
      if (location) {
        window.location.href = location;
      } else {
        console.log('Error');
      }
    } else if (xhr.readyState === 4) {
      console.log('Failed');
    }
  }
  console.log(5);
});
