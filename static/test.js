var socket = io.connect('http://127.0.0.1:5000');
var container;
var textbox;
function load(){
    container = document.getElementById("container");
    textbox = document.getElementById("text");
    join();
}
console.log(container);
socket.on('connect',function(){
    console.log('connected');
});
socket.on('msg',function(data){
    var a = document.createElement('p');
    a.innerText = data;
    container.appendChild(a);
    container.scrollTop = container.scrollHeight;
})
function c(){
    console.log('clicked');
    socket.emit('msg',{
        room : 'test',
        text : textbox.value
    });
    var a = document.createElement('p');
    //a.innerText = 'dick';
    container.appendChild(a);
    container.scrollTop = container.scrollHeight;
    
}
function join(){
    socket.emit('join','test');
}