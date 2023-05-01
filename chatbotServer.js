const {PythonShell}=require("python-shell");
const input_types = document.querySelector('.input-types').value
const language = document.querySelector('.lang').value
const mic = document.querySelector('.mic').value
const play = document.querySelector('.play').value
const message = document.querySelector('.message')
alert('attached')
let options={
    scriptPath:"F:/chatbot/Final Chatbot (ttstravel)",
    args:[input_types,language,mic],

}

PythonShell.run('./badWord.py',options,(err,res)=>{
        if(err){
            console.log(err);
        }
        if(res){
            console.log(res);
        }
        let options2={
            scriptPath:"F:/chatbot/Final Chatbot (ttstravel)",
            args:[res[1],play,res[2]]
        
        }
        message.textContent = options2.args[0]
        alert(options2.args[0])
        PythonShell.run('./replyResponse.py',options2,(err,res2)=>{
                if(err){
                    console.log(err);
                }
                if(res2){
                    console.log(res2);
                }
        });

        
});

