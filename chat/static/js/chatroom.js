date_time = new Date();
console.log('date time is:' + date_time);
const user_username = JSON.parse(document.getElementById('user_username').textContent);
const roomName = JSON.parse(document.getElementById('room-name').textContent);

document.querySelector('#submit').onsubmit = function (e) {
    e.preventDefault();
    const messageInputDom = document.querySelector('#input');
    const message = messageInputDom.value;
    if (message == '') {
        return
    }
    chatSocket.send(JSON.stringify({
        'message': message,
        'username': user_username,
        'room': roomName,
    }));
    messageInputDom.value = '';
};

const chatSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/chat/' +
    roomName +
    '/'
);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (user_username == data.username) {
        rightMessage(data.message);
    } else {
        leftMessage(data);
    }
    const element = document.getElementById('msg-box');
    element.scrollTop = element.scrollHeight;
}

function rightMessage(data_message) {
    const mesg_box = `<div class="chat-message-right pb-4 mx-3" id="mesgs">
                            <div class="mx-2">
                                <img src="https://bootdey.com/img/Content/avatar/avatar3.png" class="rounded-circle mr-1" width="30" height="30">
                            </div>
                            <div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3">
                                <div class="d-flex">
                                    <div class="font-weight-bold mb-1 text-success">You</div>
                                    <button style="padding: 0 3px; outline: None; border: 1px solid green; border-radius: 5px; margin: 0 3px;">Save</button>
                                </div>
                                ${data_message}
                            </div>
                        </div>`;
    let parent = document.getElementById('msg-box');
    parent.innerHTML += mesg_box;
}

function leftMessage(data) {
    const mesg_box = `<div class="chat-message-left pb-4 mx-3" id="mesgs">
                            <div class="mx-2">
                                <img src="https://bootdey.com/img/Content/avatar/avatar3.png" class="rounded-circle mr-1" width="30" height="30">
                            </div>
                            <div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3">
                                <div class="font-weight-bold mb-1 text-success">${data.username}</div>
                                ${data.message}
                            </div>
                        </div>`;
    let parent = document.getElementById('msg-box');
    parent.innerHTML += mesg_box;
}
