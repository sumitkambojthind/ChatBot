'use strict'
const chatBot = document.querySelector('.chat-section')
const message = document.querySelector('.input')
const btn = document.querySelector('.send')
const new_message = document.querySelector('.message')
const chatBox = document.querySelector('.middle-container')
const mic = document.querySelector('.mic')
const chat_opener = document.querySelector('.chater')
const fair_list = document.querySelector('.fair')
const contact_us = document.querySelector('.contact')
// send.addEventListener('click', function(e){
//     e.preventDefault()
//     alert('message sended')
// })





let messages = []
btn.classList.add('hidden')
// chatBot.classList.add('hidden')

btn.addEventListener('click', function(e){
    e.preventDefault()
    messages.push(message.value)
    console.log(messages)
    messages.forEach(el=>{

        const html = `
        
            <p class="message">${el}</p>
        
        `
        new_message.insertAdjacentHTML('beforebegin', html)

    })

    messages = [];
    mic.classList.remove('hidden')
    btn.classList.add('hidden')

    message.value = ''
});

message.addEventListener('click', function(e){
    e.preventDefault()
    mic.classList.add('hidden')
    
    btn.classList.remove('hidden')

})

chat_opener.addEventListener('click', function(e){
    e.preventDefault()
    chatBot.classList.remove('hidden')
})

/************************************adding elements while clicking */
fair_list.addEventListener('click', function(e){
    e.preventDefault()
    const fairEle = document.createElement('div')
    fairEle.innerHTML = `
        <div class='fair-container'>
            <ul class='fair-list grid grid-2-col gap08'>
                <li >NITJ &rarr; Railway station</li>
                <li class='li-name'>55/-</li>
                <li>NITJ &rarr; Bus stand</li>
                <li class='li-name'>55/-</li>
                <li>NITJ &rarr; jalandhar</li>
                <li class='li-name'>55/-</li>
                <li>NITJ &rarr; kartarpur</li>
                <li class='li-name'>30/-</li>
                <li>NITJ &rarr; maqsuda</li>
                <li class='li-name'>20/-</li>
            </ul>
            
        </div>
    
    `

    chatBox.append(fairEle)
})

contact_us.addEventListener('click', function(e){
    e.preventDefault()
    const contactList = document.createElement('div')
    contactList.innerHTML = `
        <div class='contact-container flex-3 flex-dir gap08'>
            <div class='call-facality flex-1 gap16'>
                <p class='number'>Call at &mdash;</p> 
                <p class='number-value'>94177-86265</p>   
            </div>
            <div class='live-chat flex-1 gap16'>
                <button class='liveBtn'>Live chat</button>
            </div>
        
        </div>
    `
    chatBox.append(contactList)


})